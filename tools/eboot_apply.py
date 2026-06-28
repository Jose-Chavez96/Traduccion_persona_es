#!/usr/bin/env python3
"""
eboot_apply.py — Aplica traducciones al EBOOT descifrado por OFFSET (seguro).

Lee el inventario eb.json (registros con off/rawlen/room/term/texto_original) y un
mapa JSON {texto_original: texto_traducido}. Para cada registro cuyo texto este en
el mapa: verifica que los bytes en `off` == encode(texto_original), exige que
encode(es) <= rawlen+room, sobreescribe y rellena:
  - term '00': relleno con espacios 0x0000
  - term 'FF': relleno con 0xFFFF (terminador de nombre); puede usar `room`
Valida que el conteo de tokens <FFxx> coincida.

Uso: python3 tools/eboot_apply.py <in.elf> <out.elf> <eb.json> <trans.json>
"""
import sys, os, json, re
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from persona_codec import encode

TOK=re.compile(r'<FF[0-9A-Fa-f]{2}>')

def main():
    inp,outp,ebj,trj=sys.argv[1:5]
    d=bytearray(open(inp,'rb').read())
    recs=json.load(open(ebj))
    tr=json.load(open(trj))
    # cap minimo por texto (todo-o-nada: ES debe caber en TODAS sus apariciones)
    mincap={}
    for r in recs:
        c=r['rawlen']+(r['room'] if r['term']=='FF' else 0)
        mincap[r['texto_original']]=min(mincap.get(r['texto_original'],10**9),c)
    ok=skip=mism=toolong=tokbad=0; errs=[]; toolong_set=set()
    for r in recs:
        en=r['texto_original']
        if en not in tr: continue
        es=tr[en]
        if es is None or es=='' or es==en:
            skip+=1; continue
        try:
            be=encode(en); bs=encode(es)
        except Exception as ex:
            errs.append(('ENC',en,str(ex))); continue
        off=r['off']
        if bytes(d[off:off+len(be)])!=be:
            mism+=1; errs.append(('MISMATCH',en,hex(off))); continue
        # SEGURIDAD: solo se puede sobrescribir el FOOTPRINT EXACTO del string
        # original (len(be)). rawlen suele ser MAYOR que el string real -> los bytes
        # [len(be)..rawlen] son OTRAS strings/estructura que el juego lee (render, etc).
        # Rellenar hasta rawlen los borraba (bug del descuadre). Ahora: es debe caber
        # en len(be); se rellena SOLO hasta len(be) y NO se toca nada despues.
        if len(bs)>len(be):
            if en not in toolong_set:
                toolong+=1; toolong_set.add(en); errs.append(('TOOLONG',en,es,len(bs),len(be)))
            continue
        if TOK.findall(en)!=TOK.findall(es):
            tokbad+=1; errs.append(('TOK',en,es)); continue
        pad = b'\xff\xff' if r['term']=='FF' else b'\x00\x00'
        span=bytearray(bs)
        while len(span)<len(be): span+=pad   # rellena solo el footprint del string original
        assert len(span)==len(be)
        d[off:off+len(span)]=span
        ok+=1
    open(outp,'wb').write(d)
    print('aplicadas=%d  skip=%d  mismatch=%d  toolong=%d  tokbad=%d'%(ok,skip,mism,toolong,tokbad))
    for e in errs[:15]: print('  ',e)

if __name__=='__main__': main()
