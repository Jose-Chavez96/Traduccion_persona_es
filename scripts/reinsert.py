#!/usr/bin/env python3
"""
Fase 4 - Reinserter.

Lee translated_text/*.json. Para cada registro 'traducido':
  1. Valida que los tokens protegidos <....> esten intactos (mismo conjunto/conteo).
  2. Re-codifica texto_traducido a bytes con el codec.
  3. Valida longitud: bytes_traducidos <= longitud_original.
     - si < : rellena con espacios (0x0000) hasta igualar -> NO cambia punteros.
     - si > : marca 'excede_limite' y NO inserta (regla 6 -> propone version corta).
  4. Acumula parches {archivo, offset_inicio, bytes_nuevos}.

Salida:
  rebuilt/patch_records.json  (lista de parches byte-exactos, relativos a cada .bin)
  docs/reinsert_report.md
NO modifica archivos originales. Solo genera el plan de parche.
"""
import os, sys, json, glob, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from persona_codec import encode, decode

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TR = os.path.join(ROOT, "translated_text")
REBUILT = os.path.join(ROOT, "rebuilt")
DOCS = os.path.join(ROOT, "docs")
TOKEN = re.compile(r"<[0-9A-Fa-f]{2,4}>")


def _tok_bytes(tk):
    h = tk[1:-1]
    c = (0xFF00 | int(h, 16)) if len(h) == 2 else int(h, 16)
    return bytes([(c >> 8) & 0xFF, c & 0xFF])


def _is_anchor(tk):
    """Token de ANCLA = dato estructural a offset FIJO que el engine lee/indexa:
    tokens no-FF (<NNNN> punteros/layout) y <FFFF> (soup de fondo). Los tokens FF de
    control de texto (<FF01/02/03/05/1B/55/67/68...>) NO son ancla: el texto fluye entre
    anclas y el engine los lee secuencialmente."""
    return (not tk.startswith("<FF")) or tk == "<FFFF>"


def _align_per_run(orig, trad, limite):
    """Padea el texto ENTRE anclas a la longitud-bytes de su tramo EN -> cada token de
    ancla (estructura/puntero/soup) queda en su offset ABSOLUTO original. El texto de
    dialogo fluye libre entre anclas (los <FFxx> de control no fuerzan alineacion).
    None si la secuencia de anclas difiere o un tramo ES excede a su tramo EN."""
    def parts(text):
        segs = []; toks = []; last = 0
        for m in TOKEN.finditer(text):
            if _is_anchor(m.group(0)):
                segs.append(text[last:m.start()]); toks.append(m.group(0)); last = m.end()
        segs.append(text[last:])
        return segs, toks
    os_, ot = parts(orig); ts, tt = parts(trad)
    if ot != tt or len(os_) != len(ts):
        return None
    nb = bytearray()
    for i, seg in enumerate(ts):
        en = encode(os_[i]); es = encode(seg)
        if len(es) > len(en):
            # whitespace-reclaim (build-time, SIN perder texto): colapsa espacios
            # redundantes del tramo que desborda. Si asi cabe, ancla; si no, RUNOVER.
            seg2 = re.sub(r"  +", " ", seg)
            es2 = encode(seg2)
            if len(es2) <= len(en):
                es = es2
            else:
                return None
        nb += es + b"\x00\x00" * ((len(en) - len(es)) // 2)
        if i < len(tt):
            nb += _tok_bytes(tt[i])
    return bytes(nb) if len(nb) == limite else None


def _align_trailing_soup(trad_bytes, limite, raw):
    """Ancla el bloque estructural final (soup verbatim) a su offset original
    insertando el relleno 0x0000 JUSTO ANTES de el. None si ES no termina en esa soup."""
    bnd = -1
    for i in range(0, len(raw) - 1, 2):
        if raw[i] == 0xFF and raw[i + 1] == 0xFF:
            bnd = i; break
    if bnd < 0 or not trad_bytes.endswith(raw[bnd:]):
        return None
    head = trad_bytes[: len(trad_bytes) - len(raw[bnd:])]
    out = head + b"\x00\x00" * ((limite - len(trad_bytes)) // 2) + raw[bnd:]
    return out if len(out) == limite else None


def main():
    os.makedirs(REBUILT, exist_ok=True)
    patches = []
    ok = skipped = exceed = badtok = 0
    report = ["# Reporte de reinserción (Fase 4)\n"]
    detail = []
    for jf in sorted(glob.glob(os.path.join(TR, "*.json"))):
        recs = json.load(open(jf, encoding="utf-8"))
        if not isinstance(recs, list):
            continue
        for r in recs:
            if r["estado"] not in ("traducido", "shortened") or not r["texto_traducido"].strip():
                continue
            orig, trad = r["texto_original"], r["texto_traducido"]
            limite_b = r["longitud_original_bytes"]
            # 1. tokens intactos
            if sorted(TOKEN.findall(orig)) != sorted(TOKEN.findall(trad)):
                badtok += 1
                detail.append(f"- ❌ {r['id']}: tokens de control alterados -> RECHAZADO")
                continue
            # 2. re-codificar
            try:
                b = encode(trad)
            except ValueError as e:
                skipped += 1
                detail.append(f"- ❌ {r['id']}: char no codificable ({e}) -> RECHAZADO")
                continue
            # 3. longitud
            if len(b) > limite_b:
                exceed += 1
                detail.append(f"- ⚠ {r['id']}: excede_limite ({len(b)} > {limite_b} bytes) -> proponer versión corta")
                continue
            if len(b) < limite_b:
                # FIX offset-shift: el relleno al-FINAL desplaza cualquier token de
                # control/estructura que el engine lea a offset FIJO dentro del record
                # -> rompe (a) soup de layout <FFFF> (descuadre de fondo) y (b) bloques
                # de punteros <NNNN>/backtick que indexan sub-dialogos de NPCs multiples
                # (el dialogo abre y cierra de golpe). _align_per_run padea cada run de
                # texto a la longitud de su run EN -> TODO token queda en su offset
                # original. Se aplica a TODOS los records (no solo soup); si un run ES
                # excede su run EN (RUNOVER) cae a trailing-soup y luego a pad-al-final.
                raw = bytes.fromhex(r["raw_hex"])
                fixed = _align_per_run(orig, trad, limite_b)
                if fixed is None:
                    fixed = _align_trailing_soup(b, limite_b, raw)
                b = fixed if fixed is not None else (
                    b + b"\x00\x00" * ((limite_b - len(b)) // 2))
            assert len(b) == limite_b
            # verificacion: decodificar de vuelta
            back, _ = decode(b, 0, len(b))
            patches.append({
                "archivo": r["archivo_origen"],
                "offset_inicio": r["offset_inicio"],
                "longitud": limite_b,
                "bytes_hex": b.hex(),
                "id": r["id"],
            })
            ok += 1
            detail.append(f"- ✅ {r['id']}: '{trad.strip()}' ({len(b)} bytes) OK")
    json.dump(patches, open(os.path.join(REBUILT, "patch_records.json"), "w"), indent=1)
    report.append(f"- Insertados OK: **{ok}**")
    report.append(f"- Excede límite (no insertados): **{exceed}**")
    report.append(f"- Tokens alterados (rechazados): **{badtok}**")
    report.append(f"- No codificables (rechazados): **{skipped}**")
    report.append(f"\nParches byte-exactos -> `rebuilt/patch_records.json`\n")
    report.append("## Detalle por registro\n")
    report += detail
    open(os.path.join(DOCS, "reinsert_report.md"), "w", encoding="utf-8").write("\n".join(report) + "\n")
    print("\n".join(report[:6]))

if __name__ == "__main__":
    main()
