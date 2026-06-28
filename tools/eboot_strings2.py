#!/usr/bin/env python3
"""
eboot_strings2.py — Extractor preciso por offset del EBOOT descifrado (ELF).

Cada registro = un run de texto codec, con:
  off       : offset absoluto en el ELF
  end       : fin del run (exclusivo) = primer terminador
  rawlen    : end-off (bytes sobreescribibles sin tocar terminador)
  room      : bytes extra de padding muerto tras el terminador (FFFF/0000 repetidos)
              -> para nombres de ancho fijo se puede crecer hasta off+rawlen+room
  term      : 'FF' (0xFFFF) | '00' (0x0000) | '?'
  texto_original, estado, texto_traducido

Run: empieza en letra/token-FF; 0x0000 = espacio interno; corta en 0xFFFF,
o en 2+ ceros seguidos, o token no-FF de datos.
Uso: python3 tools/eboot_strings2.py <elf> <out.json>
"""
import sys, os, json, re
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from persona_codec import code_to_char, PUNCT

def cls(c):
    if c==0x0000: return 'Z'
    if c in PUNCT or code_to_char(c) is not None: return 'T'
    if (c&0xFF00)==0xFF00: return 'C'
    return 'O'

def main():
    d=open(sys.argv[1],'rb').read(); n=len(d)&~1
    recs=[]; i=0
    while i+1<n:
        c=(d[i]<<8)|d[i+1]
        if cls(c) in ('T','C'):
            a=i; zeros=0
            j=i
            while j+1<n:
                cc=(d[j]<<8)|d[j+1]
                k=cls(cc)
                if cc==0xFFFF: break
                if k=='Z':
                    zeros+=1
                    if zeros>=2: break
                elif k=='O': break
                else: zeros=0
                j+=2
            end=j if zeros<2 else j  # j at terminator/break
            # recortar ceros de cola del run
            e=end
            while e-2>=a and (d[e-2]<<8|d[e-1])==0x0000: e-=2
            seg=d[a:e]
            recs.append([a,e,seg])
            i=max(end+2,i+2)
        else:
            i+=2
    # decodificar + filtrar
    NONFF=re.compile(r'<(?!FF)[0-9A-F]{4}>')
    def dec(seg):
        out=[]
        for p in range(0,len(seg)-1,2):
            c=(seg[p]<<8)|seg[p+1]
            ch=code_to_char(c)
            if ch is not None: out.append(ch)
            elif c==0x0000: out.append(' ')
            elif (c&0xFF00)==0xFF00: out.append('<%04X>'%c)
            else: out.append('<%04X>'%c)
        return ''.join(out)
    out=[]
    for a,e,seg in recs:
        txt=dec(seg)
        letters=sum(ch.isalpha() for ch in txt)
        core=re.sub(r'<....>','',txt)
        if letters<2: continue
        if len(core)==0 or letters/max(1,len(core))<0.5: continue
        # term + room
        term='?'; p=e
        if p+1<len(d):
            t=(d[p]<<8)|d[p+1]
            term='FF' if t==0xFFFF else ('00' if t==0x0000 else '?')
        room=0; p=e
        while p+1<len(d):
            t=(d[p]<<8)|d[p+1]
            if t in (0xFFFF,0x0000): room+=2; p+=2
            else: break
        out.append({'off':a,'rawlen':e-a,'room':room,'term':term,
                    'texto_original':txt,'texto_traducido':'','estado':'por_traducir'})
    out.sort(key=lambda r:r['off'])
    for idx,r in enumerate(out): r['id']='eb_%05d'%idx
    json.dump(out,open(sys.argv[2],'w'),ensure_ascii=False)
    print('strings:',len(out),'bytes:',sum(r['rawlen'] for r in out))

if __name__=='__main__': main()
