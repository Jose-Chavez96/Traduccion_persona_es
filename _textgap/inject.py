#!/usr/bin/env python3
"""Inject/translate missing story records into translated_text/<file>.json.
map.json = {id: es}. Validates encode(es)<=longitud_original_bytes, token set equality, encodable.
Builds record from extracted_text if absent. --apply writes; default dry."""
import sys,os,json,re
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'..','scripts'))
from persona_codec import encode
TOK=re.compile(r'<[0-9A-Fa-f]{2,4}>')
name=sys.argv[1]; mp=json.load(open(sys.argv[2])); apply='--apply' in sys.argv
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ext={r['id']:r for r in json.load(open(f'{ROOT}/extracted_text/{name}.json')) if isinstance(r,dict) and 'id' in r}
trpath=f'{ROOT}/translated_text/{name}.json'
tr=json.load(open(trpath))
tridx={r['id']:r for r in tr if isinstance(r,dict) and 'id' in r}
ok=[];rej=[]
for rid,es in mp.items():
    if rid not in ext: rej.append((rid,'NO_EXT'));continue
    en=ext[rid]['texto_original']; lim=ext[rid]['longitud_original_bytes']
    if sorted(TOK.findall(en))!=sorted(TOK.findall(es)): rej.append((rid,'TOK'));continue
    try: b=encode(es)
    except Exception as e: rej.append((rid,f'ENC:{e}'));continue
    if len(b)>lim: rej.append((rid,f'LONG {len(b)}>{lim}'));continue
    ok.append((rid,es))
print(f"map={len(mp)} ok={len(ok)} rej={len(rej)}")
for r in rej: print("  REJ",r)
if apply:
    for rid,es in ok:
        if rid in tridx:
            tridx[rid]['texto_traducido']=es; tridx[rid]['estado']='shortened'
        else:
            base=dict(ext[rid]); base['texto_traducido']=es; base['estado']='shortened'
            base.setdefault('limite_chars',base['longitud_original_bytes']//2)
            tr.append(base)
    json.dump(tr,open(trpath,'w'),ensure_ascii=False,indent=1)
    print(f"applied -> {name}.json now {len(tr)} records")
