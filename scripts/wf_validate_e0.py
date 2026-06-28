#!/usr/bin/env python3
"""Valida un mapa de traduccion de e1 SIN aplicarlo a e0.json.
Reporta, por id: tokens alterados, no codificable, o overflow (bytes>limite).
Uso: python3 wf_validate_e1.py <map.json>
Salida: lineas 'OK n / FAIL m' y detalle por id problematico. Codigo 0 si todo OK."""
import os,sys,json,re
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from persona_codec import encode
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOKEN=re.compile(r"<[0-9A-Fa-f]{2,4}>")
recs={r["id"]:r for r in json.load(open(os.path.join(ROOT,"translated_text","e0.json"),encoding="utf-8"))}
m=json.load(open(sys.argv[1],encoding="utf-8"))
ok=bad=0
for rid,ent in m.items():
    r=recs.get(rid)
    if not r: print("MISSING-ID",rid); bad+=1; continue
    t=ent.get("t","") if isinstance(ent,dict) else ent
    o=r["texto_original"]; lim=r["longitud_original_bytes"]
    if sorted(TOKEN.findall(o))!=sorted(TOKEN.findall(t)):
        print(f"TOKENS {rid}: orig={sorted(TOKEN.findall(o))} trad={sorted(TOKEN.findall(t))}"); bad+=1; continue
    try: b=encode(t)
    except ValueError as e:
        print(f"ENCODE {rid}: {e}"); bad+=1; continue
    if len(b)>lim:
        print(f"OVER {rid}: got {len(b)} > lim {lim} (over {len(b)-lim} bytes = {(len(b)-lim+1)//2} chars)"); bad+=1; continue
    ok+=1
print(f"OK {ok} / FAIL {bad}")
sys.exit(1 if bad else 0)
