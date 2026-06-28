#!/usr/bin/env python3
"""
gim2png.py — Decodificador GIM (PSP) -> PNG, sin dependencias (solo stdlib zlib).

Soporta:
  - contenedor Persona: u32 count + count*u32 sizes, blobs concatenados desde 0x50
    (o un .gim suelto que empiece en 'MIG.00.1PSP').
  - formatos imagen: INDEX4(4), INDEX8(5), RGBA8888(3), RGBA4444(2), RGBA5551(1), RGBA5650(0)
  - paletas: RGBA8888/4444/5551/5650
  - unswizzle PSP (pixelOrder=1), bloques 16x8 bytes.

Uso:
  python3 tools/gim2png.py <archivo.bin|.gim> <outdir>
Genera outdir/<base>_NN.png y un indice .txt con dims/formato por sub-textura.
"""
import sys, os, struct, zlib

def u16(b,o): return struct.unpack_from('<H',b,o)[0]
def u32(b,o): return struct.unpack_from('<I',b,o)[0]

def write_png(path, w, h, rgba):
    """rgba: bytes RGBA8888 length w*h*4."""
    raw=bytearray()
    stride=w*4
    for y in range(h):
        raw.append(0)                 # filter none
        raw += rgba[y*stride:(y+1)*stride]
    def chunk(typ,data):
        c=struct.pack('>I',len(data))+typ+data
        return c+struct.pack('>I',zlib.crc32(typ+data)&0xffffffff)
    sig=b'\x89PNG\r\n\x1a\n'
    ihdr=struct.pack('>IIBBBBB',w,h,8,6,0,0,0)
    idat=zlib.compress(bytes(raw),9)
    open(path,'wb').write(sig+chunk(b'IHDR',ihdr)+chunk(b'IDAT',idat)+chunk(b'IEND',b''))

def pal_entry(fmt, b, o):
    if fmt==3:  # RGBA8888
        return b[o],b[o+1],b[o+2],b[o+3]
    v=u16(b,o)
    if fmt==2:  # RGBA4444
        r=(v&0xF); g=(v>>4)&0xF; bb=(v>>8)&0xF; a=(v>>12)&0xF
        return r*17,g*17,bb*17,a*17
    if fmt==1:  # RGBA5551
        r=(v&0x1F); g=(v>>5)&0x1F; bb=(v>>10)&0x1F; a=(v>>15)&1
        return r*255//31,g*255//31,bb*255//31,a*255
    if fmt==0:  # RGBA5650
        r=(v&0x1F); g=(v>>5)&0x3F; bb=(v>>11)&0x1F
        return r*255//31,g*255//63,bb*255//31,255
    return 0,0,0,255

def palsize(fmt): return 4 if fmt==3 else 2

def unswizzle(data, pitch, h):
    out=bytearray(pitch*h)
    bw=16; bh=8
    wb=pitch//bw
    src=0
    for by in range(h//bh):
        for bx in range(wb):
            for r in range(bh):
                dst=(by*bh+r)*pitch+bx*bw
                out[dst:dst+bw]=data[src:src+bw]; src+=bw
    return out

def parse_gim(g):
    """Devuelve (w,h,rgba) o None."""
    img=None; pal=None
    p=0x10
    while p+16<=len(g):
        typ=u16(g,p); blksize=u32(g,p+4); nextoff=u32(g,p+8)
        if typ in (0x04,0x05):
            dp=p+16
            hsize=u32(g,dp); fmt=u16(g,dp+4); order=u16(g,dp+6)
            w=u16(g,dp+8); h=u16(g,dp+10)
            pix=dp+hsize
            blk={'fmt':fmt,'order':order,'w':w,'h':h,'pix':pix,'end':p+blksize}
            if typ==0x04: img=blk
            else: pal=blk
        if nextoff==0 or p+nextoff<=p or p+nextoff>len(g): break
        p=p+nextoff
    if not img: return None
    fmt=img['fmt']; w=img['w']; h=img['h']; order=img['order']
    bpp={0:16,1:16,2:16,3:32,4:4,5:8}.get(fmt)
    if bpp is None: return ('?fmt%d'%fmt,w,h,None)
    pitch=(w*bpp)//8
    # PSP swizzle pads pitch a multiplo de 16 y h a 8
    spitch=(pitch+15)&~15; sh=(h+7)&~7
    raw=g[img['pix']:img['pix']+spitch*sh]
    if order==1 and len(raw)>=spitch*sh:
        raw=unswizzle(raw, spitch, sh)
    # construir paleta
    palette=[]
    if fmt in (4,5) and pal:
        pf=pal['fmt']; ps=palsize(pf); ncol=16 if fmt==4 else 256
        po=pal['pix']
        for i in range(ncol):
            palette.append(pal_entry(pf,g,po+i*ps))
    out=bytearray(w*h*4)
    for y in range(h):
        for x in range(w):
            if fmt==4:
                byte=raw[y*spitch + x//2]
                idx=(byte&0xF) if (x&1)==0 else (byte>>4)
                r,gg,b,a=palette[idx] if idx<len(palette) else (0,0,0,255)
            elif fmt==5:
                idx=raw[y*spitch + x]
                r,gg,b,a=palette[idx] if idx<len(palette) else (0,0,0,255)
            elif fmt==3:
                o=y*spitch+x*4; r,gg,b,a=raw[o],raw[o+1],raw[o+2],raw[o+3]
            else:
                o=y*spitch+x*2; r,gg,b,a=pal_entry(fmt,raw,o)
            do=(y*w+x)*4
            out[do]=r; out[do+1]=gg; out[do+2]=b; out[do+3]=a
    return (w,h,out)

def split_container(d):
    if d[:11]==b'MIG.00.1PSP':
        return [d]
    cnt=u32(d,0)
    if cnt<=0 or cnt>4096: return [d]
    sizes=[u32(d,4+4*i) for i in range(cnt)]
    base=(4+4*cnt+15)&~15; o=base; blobs=[]
    for s in sizes:
        if s>=12 and d[o:o+11]==b'MIG.00.1PSP':
            blobs.append(d[o:o+s])
        o+=s
    return blobs

def main():
    fn=sys.argv[1]; outdir=sys.argv[2]
    os.makedirs(outdir,exist_ok=True)
    d=open(fn,'rb').read()
    base=os.path.splitext(os.path.basename(fn))[0]
    blobs=split_container(d)
    idx=open(os.path.join(outdir,base+'_index.txt'),'w')
    for i,g in enumerate(blobs):
        res=parse_gim(g)
        if not res:
            idx.write('%02d: parse-fail\n'%i); continue
        if res[0]=='?' or (isinstance(res[0],str)):
            idx.write('%02d: unsupported %s %dx%d\n'%(i,res[0],res[1],res[2])); continue
        w,h,rgba=res
        out=os.path.join(outdir,'%s_%02d.png'%(base,i))
        write_png(out,w,h,rgba)
        idx.write('%02d: %dx%d -> %s\n'%(i,w,h,os.path.basename(out)))
        print('%02d %dx%d'%(i,w,h))
    idx.close()

if __name__=='__main__':
    main()
