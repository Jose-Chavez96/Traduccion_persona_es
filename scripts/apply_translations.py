#!/usr/bin/env python3
"""
Aplica traducciones a translated_text/<file>.json.

Uso: python3 apply_translations.py <archivo.json> <map.json>
  map.json = { "<id>": "traduccion", ... }

Para cada id:
  - valida tokens de control intactos (mismo conjunto que el original)
  - re-codifica y valida longitud <= limite original
      * si cabe        -> estado=traducido
      * si NO cabe      -> estado=fallido, nota='excede pese a traduccion' (requiere acortar a mano)
  - una traduccion marcada por el llamador como ya-acortada se pasa con estado 'shortened'
    si el id aparece tambien en el set SHORT (segundo arg opcional --short=ids.json)

Devuelve resumen JSON: {traducido, shortened, fallido, sin_tocar, excede_ids:[...]}.
"""
import os, sys, json, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from persona_codec import encode
TOKEN = re.compile(r"<[0-9A-Fa-f]{2,4}>")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def main():
    jf = os.path.join(ROOT, "translated_text", sys.argv[1])
    tmap = json.load(open(sys.argv[2], encoding="utf-8"))
    short_ids = set()
    for a in sys.argv[3:]:
        if a.startswith("--short="):
            short_ids = set(json.load(open(a[8:], encoding="utf-8")))
    recs = json.load(open(jf, encoding="utf-8"))
    res = {"traducido": 0, "shortened": 0, "fallido": 0, "excede_ids": [], "tok_ids": []}
    for r in recs:
        rid = r["id"]
        if rid not in tmap:
            continue
        trad = tmap[rid]
        # preservar espacios/borde del original (lead/tail) si la traduccion no los trae
        orig = r["texto_original"]
        if sorted(TOKEN.findall(orig)) != sorted(TOKEN.findall(trad)):
            r["estado"] = "fallido"; r["notas"] = "tokens de control alterados"
            res["fallido"] += 1; res["tok_ids"].append(rid); continue
        try:
            b = encode(trad)
        except ValueError as e:
            r["estado"] = "fallido"; r["notas"] = f"char no codificable: {e}"
            res["fallido"] += 1; continue
        if len(b) > r["longitud_original_bytes"]:
            r["texto_traducido"] = trad
            r["estado"] = "fallido"
            r["notas"] = f"excede {len(b)}>{r['longitud_original_bytes']} bytes"
            res["fallido"] += 1; res["excede_ids"].append(rid); continue
        r["texto_traducido"] = trad
        r["estado"] = "shortened" if rid in short_ids else "traducido"
        res["shortened" if rid in short_ids else "traducido"] += 1
    json.dump(recs, open(jf, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(json.dumps(res, ensure_ascii=False))

if __name__ == "__main__":
    main()
