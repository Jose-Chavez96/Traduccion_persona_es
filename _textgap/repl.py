#!/usr/bin/env python3
"""Translate missing story records by REPLACING token-free EN text runs with ES.
map.json = {id: [[en_run, es_run], ...]}. Applies str.replace (once each, in order) to
the ORIGINAL -> tokens/soup preserved automatically. Validates token multiset unchanged
+ encode<=longitud_original_bytes + encodable. --apply injects into translated_text/<file>.json."""
import sys,os,json,re
sys.path.insert(0,os.path.join(os.path.dirname(__file__),'..','scripts'))
from persona_codec import encode
TOK=re.compile(r'<[0-9A-Fa-f]{2,4}>')
name=sys.argv[1]; mp=json.load(open(sys.argv[2])); apply='--apply' in sys.argv
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ext={r['id']:r for r in json.load(open(f'{ROOT}/extracted_text/{name}.json')) if isinstance(r,dict) and 'id' in r}
trpath=f'{ROOT}/translated_text/{name}.json'
tr=json.load(open(trpath)); tridx={r['id']:r for r in tr if isinstance(r,dict) and 'id' in r}
ok=[];rej=[]
for rid,repls in mp.items():
    if rid not in ext: rej.append((rid,'NO_EXT'));continue
    en=ext[rid]['texto_original']; lim=ext[rid]['longitud_original_bytes']; cur=en
    bad=False
    for a,b in repls:
        if a not in cur: rej.append((rid,f'RUN_NOT_FOUND {a[:30]!r}'));bad=True;break
        cur=cur.replace(a,b)
    if bad: continue
    if sorted(TOK.findall(en))!=sorted(TOK.findall(cur)): rej.append((rid,'TOK'));continue
    try: bb=encode(cur)
    except Exception as e: rej.append((rid,f'ENC:{e}'));continue
    if len(bb)>lim: rej.append((rid,f'LONG {len(bb)}>{lim}'));continue
    ok.append((rid,cur))
print(f"map={len(mp)} ok={len(ok)} rej={len(rej)}")
for r in rej: print("  REJ",r)
if apply:
    for rid,es in ok:
        if rid in tridx: tridx[rid]['texto_traducido']=es; tridx[rid]['estado']='shortened'
        else:
            base=dict(ext[rid]); base['texto_traducido']=es; base['estado']='shortened'
            base.setdefault('limite_chars',base['longitud_original_bytes']//2)
            tr.append(base)
    json.dump(tr,open(trpath,'w'),ensure_ascii=False,indent=1)
    print(f"applied -> {name}.json now {len(tr)} records")
