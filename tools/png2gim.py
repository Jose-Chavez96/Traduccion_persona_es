#!/usr/bin/env python3
"""
png2gim.py — Re-inserta una imagen editada en un GIM existente, IN-PLACE.

Mantiene cabecera, formato, dims y paleta originales del GIM. Solo reescribe la
region de pixeles (re-indexando a la paleta original + re-swizzle). Como las
dimensiones/format/paleta no cambian, el tamano del blob es identico -> se puede
parchear el contenedor en el mismo offset (TOC intacto) y luego MD5 + xdelta.

API:
  reencode_blob(gim_bytes, rgba, w, h) -> nuevo gim_bytes (mismo tamano)
  round_trip_check(gim_bytes) -> True si decode->encode reproduce los bytes exactos

Uso CLI (test identidad):
  python3 tools/png2gim.py selftest <archivo.bin>
"""
import sys, os, struct
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gim2png import (u16, u32, parse_gim, split_container, pal_entry, palsize, unswizzle)

def swizzle(data, pitch, h):
    out=bytearray(pitch*h); bw=16; bh=8; wb=pitch//bw; dst=0
    for by in range(h//bh):
        for bx in range(wb):
            for r in range(bh):
                src=(by*bh+r)*pitch+bx*bw
                out[dst:dst+bw]=data[src:src+bw]; dst+=bw
    return out

def _blocks(g):
    img=None; pal=None; p=0x10
    while p+16<=len(g):
        typ=u16(g,p); blksize=u32(g,p+4); nextoff=u32(g,p+8)
        if typ in (0x04,0x05):
            dp=p+16; hsize=u32(g,dp); fmt=u16(g,dp+4); order=u16(g,dp+6)
            w=u16(g,dp+8); h=u16(g,dp+10); pix=dp+hsize
            blk={'fmt':fmt,'order':order,'w':w,'h':h,'pix':pix}
            if typ==0x04: img=blk
            else: pal=blk
        if nextoff==0 or p+nextoff<=p or p+nextoff>len(g): break
        p=p+nextoff
    return img,pal

def reencode_blob(g, rgba, w_in, h_in):
    img,pal=_blocks(g)
    fmt=img['fmt']; w=img['w']; h=img['h']; order=img['order']
    assert (w,h)==(w_in,h_in), "dims mismatch"
    bpp={4:4,5:8}.get(fmt)
    if bpp is None: raise ValueError('solo INDEX4/INDEX8 soportado para re-encode (fmt=%d)'%fmt)
    # paleta original -> dict color->index
    pf=pal['fmt']; ps=palsize(pf); ncol=16 if fmt==4 else 256
    pal_rgba=[pal_entry(pf,g,pal['pix']+i*ps) for i in range(ncol)]
    lut={}
    for i,c in enumerate(pal_rgba):
        lut.setdefault(c,i)
    def nearest(c):
        if c in lut: return lut[c]
        # match por distancia (por si el editor altero alfa/rgb levemente)
        best=0; bd=1<<30
        for i,p in enumerate(pal_rgba):
            d=(c[0]-p[0])**2+(c[1]-p[1])**2+(c[2]-p[2])**2+(c[3]-p[3])**2
            if d<bd: bd=d; best=i
        return best
    spitch=(((w*bpp)//8)+15)&~15; sh=(h+7)&~7
    # sembrar desde el buffer original (preserva bytes de padding pitch/altura)
    raw_orig=g[img['pix']:img['pix']+spitch*sh]
    lin=bytearray(unswizzle(raw_orig,spitch,sh) if order==1 else raw_orig)
    for y in range(h):
        for x in range(w):
            o=(y*w+x)*4; idx=nearest((rgba[o],rgba[o+1],rgba[o+2],rgba[o+3]))
            if fmt==5:
                lin[y*spitch+x]=idx
            else:
                bo=y*spitch+x//2
                if (x&1)==0: lin[bo]=(lin[bo]&0xF0)|(idx&0xF)
                else: lin[bo]=(lin[bo]&0x0F)|((idx&0xF)<<4)
    raw = swizzle(lin, spitch, sh) if order==1 else lin
    out=bytearray(g)
    out[img['pix']:img['pix']+len(raw)]=raw
    return bytes(out)

def round_trip_check(g):
    res=parse_gim(g)
    if not res or isinstance(res[0],str): return None
    w,h,rgba=res
    img,pal=_blocks(g)
    if img['fmt'] not in (4,5): return None
    ng=reencode_blob(g,rgba,w,h)
    # comparar solo region de pixeles
    bpp={4:4,5:8}[img['fmt']]
    spitch=(((w*bpp)//8)+15)&~15; sh=(h+7)&~7
    a=g[img['pix']:img['pix']+spitch*sh]; b=ng[img['pix']:img['pix']+spitch*sh]
    return a==b

if __name__=='__main__':
    if sys.argv[1]=='selftest':
        d=open(sys.argv[2],'rb').read()
        blobs=split_container(d)
        ok=fail=skip=0
        for i,g in enumerate(blobs):
            r=round_trip_check(g)
            if r is None: skip+=1; print('%02d skip (no-index/parse)'%i)
            elif r: ok+=1; print('%02d OK byte-identico'%i)
            else: fail+=1; print('%02d FAIL'%i)
        print('OK=%d FAIL=%d SKIP=%d'%(ok,fail,skip))
