#!/usr/bin/env python3
"""AUTO-REUSO: LUT[texto_original]=texto_traducido de todos los archivos ya
traducidos (+ maps), reaplica a por_traducir de <target> con original identico.
Escribe map de reuso a translated_text/_wfmaps/<target>_reuse.json (no aplica).
Uso: python3 wf_reuse.py <target>   p.ej. e2"""
import os,sys,json,glob
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TR=os.path.join(ROOT,"translated_text")
target=sys.argv[1]
lut={}
for jf in glob.glob(os.path.join(TR,"*.json")):
    if os.path.basename(jf)==target+".json": continue
    try: recs=json.load(open(jf,encoding="utf-8"))
    except: continue
    if not isinstance(recs,list): continue
    for r in recs:
        if r.get("estado") in ("traducido","shortened"):
            o=r.get("texto_original"); t=r.get("texto_traducido")
            if o and t and o not in lut: lut[o]=t
print("LUT size",len(lut))
recs=json.load(open(os.path.join(TR,target+".json"),encoding="utf-8"))
hit={}
for r in recs:
    if r.get("estado")=="por_traducir":
        t=lut.get(r["texto_original"])
        if t: hit[r["id"]]={"t":t,"shortened":True}
print("reuse hits",len(hit))
os.makedirs(os.path.join(TR,"_wfmaps"),exist_ok=True)
out=os.path.join(TR,"_wfmaps",target+"_reuse.json")
json.dump(hit,open(out,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("wrote",out)
