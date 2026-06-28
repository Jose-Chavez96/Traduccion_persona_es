#!/usr/bin/env python3
"""
Aplica todos los mapas de /tmp/wf_talk/*_map.json a translated_text/.
Mapa rico: { "<id>": {"t": "...", "shortened": bool}, ... }

Valida por registro: tokens intactos + longitud<=limite (via encode).
  cabe + shortened=false -> estado=traducido
  cabe + shortened=true  -> estado=shortened
  no cabe / token mal / no codificable -> estado=fallido (+nota)

Devuelve stats JSON globales + escribe /tmp/wf_talk/_failed.json (ids fallidos por archivo).
"""
import os, sys, json, glob, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from persona_codec import encode
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TR = os.path.join(ROOT, "translated_text")
WF = "/tmp/wf_talk"
TOKEN = re.compile(r"<[0-9A-Fa-f]{2,4}>")

def main():
    stats = {"traducido":0,"shortened":0,"fallido":0,"archivos":0}
    failed = {}
    for mp in sorted(glob.glob(os.path.join(WF, "*_map.json"))):
        name = os.path.basename(mp).replace("_map.json","")          # talk_xxx
        jf = os.path.join(TR, name + ".json")
        if not os.path.isfile(jf):
            continue
        tmap = json.load(open(mp, encoding="utf-8"))
        recs = json.load(open(jf, encoding="utf-8"))
        byid = {r["id"]: r for r in recs}
        ffail = []
        touched = 0
        for rid, ent in tmap.items():
            r = byid.get(rid)
            if not r:
                continue
            trad = ent.get("t","") if isinstance(ent, dict) else ent
            short = bool(ent.get("shortened", False)) if isinstance(ent, dict) else False
            orig = r["texto_original"]
            if not trad.strip():
                continue
            if sorted(TOKEN.findall(orig)) != sorted(TOKEN.findall(trad)):
                r["estado"]="fallido"; r["texto_traducido"]=trad; r["notas"]="tokens alterados"
                stats["fallido"]+=1; ffail.append(rid); touched+=1; continue
            try:
                b = encode(trad)
            except ValueError as e:
                r["estado"]="fallido"; r["texto_traducido"]=trad; r["notas"]=f"no codificable: {e}"
                stats["fallido"]+=1; ffail.append(rid); touched+=1; continue
            if len(b) > r["longitud_original_bytes"]:
                r["estado"]="fallido"; r["texto_traducido"]=trad
                r["notas"]=f"excede {len(b)}>{r['longitud_original_bytes']}"
                stats["fallido"]+=1; ffail.append(rid); touched+=1; continue
            r["texto_traducido"]=trad
            r["estado"]="shortened" if short else "traducido"
            stats["shortened" if short else "traducido"]+=1; touched+=1
        if touched:
            json.dump(recs, open(jf,"w",encoding="utf-8"), ensure_ascii=False, indent=1)
            stats["archivos"]+=1
        if ffail:
            failed[name]=ffail
    json.dump(failed, open(os.path.join(WF,"_failed.json"),"w"), indent=1)
    print(json.dumps(stats, ensure_ascii=False))

if __name__ == "__main__":
    main()
