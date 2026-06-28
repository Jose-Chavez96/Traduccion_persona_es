#!/usr/bin/env python3
"""
Write-through de UN archivo talk: aplica su mapa de traduccion a
translated_text/<name>.json, valida (tokens + longitud via codec) y escribe
un checkpoint persistente en docs/checkpoints/<name>.json.

Uso: python3 wf_apply_one.py <name> <map.json>
  <name>    p.ej. talk_kemono   (sin extension)
  <map.json> mapa rico {"<id>":{"t":"...","shortened":bool}} o simple {"<id>":"..."}

Estados de registro: traducido | shortened | fallido | por_traducir (sin tocar)
Estado de archivo (checkpoint):
  validated   -> 0 por_traducir y 0 fallido (todo cabe)
  translated  -> hay traducciones aplicadas pero quedan por_traducir o fallidos
  pending     -> nada aplicado
Idempotente: re-aplicar el mismo mapa da el mismo resultado (no retraduce).
"""
import os, sys, json, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from persona_codec import encode

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TR = os.path.join(ROOT, "translated_text")
CKDIR = os.path.join(ROOT, "docs", "checkpoints")
TOKEN = re.compile(r"<[0-9A-Fa-f]{2,4}>")


def main():
    name = sys.argv[1]
    map_path = sys.argv[2]
    jf = os.path.join(TR, name + ".json")
    if not os.path.isfile(jf):
        print(json.dumps({"error": f"no existe {jf}"})); sys.exit(1)

    tmap = json.load(open(map_path, encoding="utf-8"))
    recs = json.load(open(jf, encoding="utf-8"))
    byid = {r["id"]: r for r in recs}
    ffail = []
    for rid, ent in tmap.items():
        r = byid.get(rid)
        if not r:
            continue
        trad = ent.get("t", "") if isinstance(ent, dict) else ent
        short = bool(ent.get("shortened", False)) if isinstance(ent, dict) else False
        orig = r["texto_original"]
        if not str(trad).strip():
            continue
        if sorted(TOKEN.findall(orig)) != sorted(TOKEN.findall(trad)):
            r["estado"] = "fallido"; r["texto_traducido"] = trad; r["notas"] = "tokens alterados"
            ffail.append(rid); continue
        try:
            b = encode(trad)
        except ValueError as e:
            r["estado"] = "fallido"; r["texto_traducido"] = trad; r["notas"] = f"no codificable: {e}"
            ffail.append(rid); continue
        if len(b) > r["longitud_original_bytes"]:
            r["estado"] = "fallido"; r["texto_traducido"] = trad
            r["notas"] = f"excede {len(b)}>{r['longitud_original_bytes']}"
            ffail.append(rid); continue
        r["texto_traducido"] = trad
        r["estado"] = "shortened" if short else "traducido"

    # write-through inmediato a disco persistente
    json.dump(recs, open(jf, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    from collections import Counter
    c = Counter(r["estado"] for r in recs)
    por_traducir = c.get("por_traducir", 0)
    fallido = c.get("fallido", 0)
    estado = ("validated" if (por_traducir == 0 and fallido == 0)
              else "translated" if (c.get("traducido", 0) + c.get("shortened", 0)) > 0
              else "pending")
    ck = {
        "file": name,
        "estado": estado,
        "traducido": c.get("traducido", 0),
        "shortened": c.get("shortened", 0),
        "fallido": fallido,
        "por_traducir": por_traducir,
        "total": len(recs),
        "fallido_ids": ffail,
        "map_path": os.path.abspath(map_path),
    }
    os.makedirs(CKDIR, exist_ok=True)
    json.dump(ck, open(os.path.join(CKDIR, name + ".json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print(json.dumps(ck, ensure_ascii=False))


if __name__ == "__main__":
    main()
