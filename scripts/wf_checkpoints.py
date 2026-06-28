#!/usr/bin/env python3
"""
Agrega docs/checkpoints/<name>.json -> docs/checkpoints.json (indice unico).
Tambien deriva el estado real desde translated_text/ por si falta algun
checkpoint individual (fuente de verdad = los .json de translated_text).

Estado por archivo: pending | translated | validated | inserted
  inserted = todos sus registros traducidos/shortened estan en rebuilt/patch_records.json

Uso: python3 wf_checkpoints.py
"""
import os, json, glob, re
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TR = os.path.join(ROOT, "translated_text")
DOCS = os.path.join(ROOT, "docs")
CKDIR = os.path.join(DOCS, "checkpoints")
PATCH = os.path.join(ROOT, "rebuilt", "patch_records.json")


def main():
    inserted_ids = set()
    if os.path.isfile(PATCH):
        inserted_ids = {r["id"] for r in json.load(open(PATCH))}

    index = {}
    for jf in sorted(glob.glob(os.path.join(TR, "*.json"))):
        name = os.path.basename(jf)[:-5]
        recs = json.load(open(jf, encoding="utf-8"))
        c = Counter(r["estado"] for r in recs)
        done = c.get("traducido", 0) + c.get("shortened", 0)
        por = c.get("por_traducir", 0)
        fail = c.get("fallido", 0)
        # cuantos registros traducidos ya estan en el patch
        in_patch = sum(1 for r in recs
                       if r["estado"] in ("traducido", "shortened") and r["id"] in inserted_ids)
        if done == 0:
            estado = "pending"
        elif por == 0 and fail == 0 and in_patch == done and done > 0:
            estado = "inserted"
        elif por == 0 and fail == 0:
            estado = "validated"
        else:
            estado = "translated"
        index[name] = {
            "estado": estado, "total": len(recs), "traducido": c.get("traducido", 0),
            "shortened": c.get("shortened", 0), "fallido": fail, "por_traducir": por,
            "en_patch": in_patch,
        }

    out = {
        "resumen": {
            "archivos": len(index),
            "pending": sum(1 for v in index.values() if v["estado"] == "pending"),
            "translated": sum(1 for v in index.values() if v["estado"] == "translated"),
            "validated": sum(1 for v in index.values() if v["estado"] == "validated"),
            "inserted": sum(1 for v in index.values() if v["estado"] == "inserted"),
        },
        "archivos": index,
    }
    json.dump(out, open(os.path.join(DOCS, "checkpoints.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print(json.dumps(out["resumen"], ensure_ascii=False))


if __name__ == "__main__":
    main()
