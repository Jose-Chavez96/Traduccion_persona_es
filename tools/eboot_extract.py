#!/usr/bin/env python3
"""
eboot_extract.py — Extrae islas de texto (codec del juego) del EBOOT DESCIFRADO (ELF).

El texto de UI/menus/items/skills/choices del EBOOT usa el MISMO codec u16-BE que
los dialogos (persona_codec). Aqui escaneamos el ELF en busca de runs de texto
imprimible + tokens <FFxx>, igual que extract.py hace con los .bin de datos.

Salida: JSON [{id, off, bytes, texto_original}] con offset ABSOLUTO en el ELF.
La reinsercion sera IN-PLACE: cada traduccion <= bytes original, terminador preservado.

Uso: python3 tools/eboot_extract.py <eboot_dec.elf> <out.json>
"""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from persona_codec import code_to_char, PUNCT

MIN_PRINT = 3      # min letras imprimibles
GAP = 2            # words OTHER consecutivos que cierran isla

def classify(c):
    if c == 0x0000: return 'T'          # espacio / terminador
    if c not in PUNCT and code_to_char(c) is not None: return 'T'
    if (c & 0xFF00) == 0xFF00: return 'C'   # token control <FFxx>
    return 'O'

def decode_run(d, a, b):
    out=[]; i=a
    while i+1 < b:
        c=(d[i]<<8)|d[i+1]
        ch=code_to_char(c)
        if ch is not None: out.append(ch)
        elif (c&0xFF00)==0xFF00: out.append('<%04X>'%c)
        elif c in (0x0000,): out.append(' ')
        else: out.append('<%04X>'%c)
        i+=2
    return ''.join(out)

def main():
    elf=sys.argv[1]; outp=sys.argv[2]
    d=open(elf,'rb').read()
    n=len(d)&~1
    islands=[]; i=0; run=None; nprint=0; gap=0; last=None
    while i+1<n:
        c=(d[i]<<8)|d[i+1]
        k=classify(c)
        if k in ('T','C'):
            if run is None: run=i; nprint=0
            if k=='T' and code_to_char(c) not in (None,' '): nprint+=1
            gap=0; last=i+2
        else:
            if run is not None:
                gap+=1
                if gap>=GAP:
                    if nprint>=MIN_PRINT: islands.append((run,last))
                    run=None
        i+=2
    if run is not None and nprint>=MIN_PRINT: islands.append((run,last))
    import re
    NONFF=re.compile(r'<(?!FF)[0-9A-F]{4}>')   # token <xxxx> que NO es <FFxx> = ruido de codigo
    recs=[]
    for a,b in islands:
        txt=decode_run(d,a,b)
        if NONFF.search(txt): continue                 # descarta islas con tokens no-FF (codigo/datos)
        letters=sum(ch.isalpha() for ch in txt)
        core=re.sub(r'<FF..>','',txt)                  # sin tokens FF
        if letters<3: continue
        if len(core)==0 or letters/len(core)<0.55: continue
        recs.append({'off':a,'bytes':b-a,'texto_original':txt,'texto_traducido':'','estado':'por_traducir'})
    recs.sort(key=lambda r:r['off'])
    for idx,r in enumerate(recs): r['id']='eb_%05d'%idx
    json.dump(recs, open(outp,'w'), ensure_ascii=False)
    total=sum(r['bytes'] for r in recs)
    print('islas:',len(recs),'  bytes texto total:',total)
    # muestra
    for r in recs[:30]:
        print('  %s @0x%X b%d %r'%(r['id'],r['off'],r['bytes'],r['texto_original'][:60]))

if __name__=='__main__':
    main()
