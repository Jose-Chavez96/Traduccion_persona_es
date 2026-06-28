#!/usr/bin/env python3
"""Harvest the game's bitmap font from sys.bin (sys_01=upper/digits/punct, sys_02=lower)
and render proportional text as an alpha bitmap. 16x16 cell grid.
render(text) -> (alpha[h][w], w, h=16). Glyphs trimmed horizontally, 1px gap, space=4px."""
import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from gim2png import parse_gim, split_container
CELL=16
_cache={}
def _atlas(path,idx):
    key=(path,idx)
    if key not in _cache:
        g=split_container(open(path,'rb').read())[idx]
        w,h,rgba=parse_gim(g); _cache[key]=(w,h,rgba)
    return _cache[key]
# char -> (sys_idx, row, col)
M={}
up="ABCDEFGHIJKLMNOP"
for c,ch in enumerate(up): M[ch]=(1,14,c)
for c,ch in enumerate("QRSTUVWXYZ"): M[ch]=(1,15,c)
for c,ch in enumerate("abcdefghijklmno"): M[ch]=(2,0,c+1)
for c,ch in enumerate("pqrstuvwxyz"): M[ch]=(2,1,c)
# digits row13: col1..col10 = 1,2,..,9,0 (verify)
for c,ch in enumerate("1234567890"): M[ch]=(1,13,c+1)
SYS='_tex/sys.bin'
def cell_alpha(idx,row,col):
    w,h,rgba=_atlas(SYS,idx)
    x0,y0=col*CELL,row*CELL
    a=[[rgba[((y0+y)*w+(x0+x))*4+3] for x in range(CELL)] for y in range(CELL)]
    return a
def glyph(ch):
    if ch==' ': return [[0]*4 for _ in range(CELL)],4
    if ch not in M: return [[0]*4 for _ in range(CELL)],4
    idx,r,c=M[ch]; a=cell_alpha(idx,r,c)
    cols=[x for x in range(CELL) if any(a[y][x]>40 for y in range(CELL))]
    if not cols: return [[0]*4 for _ in range(CELL)],4
    x0,x1=min(cols),max(cols)
    trimmed=[[a[y][x] for x in range(x0,x1+1)] for y in range(CELL)]
    return trimmed,(x1-x0+1)
def render(text,gap=1,space=4):
    glyphs=[glyph(ch) for ch in text]
    W=sum(g[1] for g in glyphs)+gap*(len(glyphs)-1 if glyphs else 0)
    out=[[0]*W for _ in range(CELL)]
    x=0
    for a,w in glyphs:
        for y in range(CELL):
            for xx in range(w):
                out[y][x+xx]=a[y][xx]
        x+=w+gap
    return out,W,CELL
def width(text,gap=1,space=4):
    return render(text,gap,space)[1]
if __name__=='__main__':
    from gim2png import write_png
    words=sys.argv[1:] or ["Persona","Status","Command","Estado","Combate","Sistema","Atacar","Equipo"]
    # stack words vertically on dark bg
    rends=[render(w) for w in words]
    Wm=max(r[1] for r in rends); Hm=(CELL+4)*len(words)
    buf=bytearray(b'\x1e'*(Wm*Hm*4))
    for i in range(Wm*Hm): buf[i*4+3]=255
    for wi,(a,w,h) in enumerate(rends):
        oy=wi*(CELL+4)
        for y in range(h):
            for x in range(w):
                v=a[y][x]
                if v>0:
                    o=((oy+y)*Wm+x)*4
                    for c in range(3): buf[o+c]=v
    write_png('_tex/font_test.png',Wm,Hm,bytes(buf))
    print("rendered",words,"-> _tex/font_test.png widths:",[r[1] for r in rends])
