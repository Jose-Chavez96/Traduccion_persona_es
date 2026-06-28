#!/usr/bin/env python3
"""
Fase 2 - Extractor de texto Persona PSP.

Escanea archivos contenedor, detecta islas de texto (runs de chars imprimibles
+ codigos de control intercalados), y vuelca cada isla como registro.

Salida: extracted_text/<nombre>.json  y  .csv
Catalogo global de codigos de control: extracted_text/control_codes.json
Log: extracted_text/extract.log

NO traduce. NO modifica los archivos originales (lectura sola).

Diseno seguro: cada registro guarda offset_inicio/offset_fin/longitud + raw_hex.
La reinsercion (Fase 4) reemplaza ese rango exacto -> sin recalcular punteros
mientras la traduccion ocupe <= longitud_original.
"""
import os, sys, json, csv, struct
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from persona_codec import code_to_char, PUNCT

MNT = "/tmp/persona_mnt/psp_game/usrdir/pack"
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "extracted_text")

# archivos candidatos (prioridad ALTA + MEDIA del reporte Fase 1)
CANDIDATES = [
    "sys.bin", "moon.bin", "kage.bin", "over.bin", "cmdan.bin",
    "e0.bin", "e1.bin", "e2.bin", "e3.bin", "e4.bin",
    "bt_menu.bin", "ch_menu.bin", "cm_menu.bin",
    "name/na.bin", "shop/shall.bin", "title/title.bin",
]
# todos los talk/*
TALK_DIR = os.path.join(MNT, "talk")
if os.path.isdir(TALK_DIR):
    CANDIDATES += ["talk/" + f for f in sorted(os.listdir(TALK_DIR)) if f.endswith(".bin")]

MIN_PRINT = 4        # min chars imprimibles para aceptar una isla
GAP_WORDS = 3        # nº de words "OTHER" consecutivas que cierran una isla
MIN_RATIO = 0.55     # imprimibles / words totales para considerar texto "limpio"

def classify(c):
    # Solo LETRAS y espacio siembran/sostienen una isla de texto.
    # Puntuación (PUNCT) y control NO siembran islas (aparecen mucho en datos binarios),
    # pero tampoco la rompen si están entre letras (cuentan como 'O' con tolerancia GAP_WORDS).
    if c == 0x0000:
        return 'T'                      # espacio
    if c not in PUNCT and code_to_char(c) is not None:
        return 'T'                      # letra real (segmento)
    if (c & 0xFF00) == 0xFF00:
        return 'C'                      # control
    return 'O'                          # puntuación-suelta / opcode / gráfico

def scan(data):
    """Devuelve lista de (ini, fin) de islas de texto, alineadas a 2 bytes."""
    islands = []
    n = len(data) & ~1
    i = 0
    run_start = None
    n_print = 0
    gap = 0
    last_text_end = None     # fin tras el ultimo word T/C
    while i + 1 < n:
        c = (data[i] << 8) | data[i+1]
        k = classify(c)
        if k in ('T', 'C'):
            if run_start is None:
                run_start = i
                n_print = 0
            if k == 'T' and code_to_char(c) != ' ':
                n_print += 1
            gap = 0
            last_text_end = i + 2
        else:  # 'O'
            if run_start is not None:
                gap += 1
                if gap >= GAP_WORDS:
                    if n_print >= MIN_PRINT:
                        islands.append((run_start, last_text_end))
                    run_start = None
                    gap = 0
        i += 2
    if run_start is not None and n_print >= MIN_PRINT:
        islands.append((run_start, last_text_end))
    return islands

from persona_codec import decode
import re

def control_codes_in(text):
    return re.findall(r"<(FF[0-9A-F]{2})>", text)

_WORD = re.compile(r"[A-Za-z]{3,}")
_VOWEL = re.compile(r"[aeiouAEIOU]")

def is_real_word(w):
    # palabra real: tiene vocal y al menos 2 letras distintas (descarta 'aaaa', 'xxxx')
    return _VOWEL.search(w) is not None and len(set(w.lower())) >= 2

def quality(text):
    """Devuelve (estado, nota). 'pendiente'=texto limpio, 'revisar'=ruido probable."""
    n_tokens = text.count("<")
    n_alpha = sum(c.isalpha() for c in text)
    words = _WORD.findall(text)
    real_words = [w for w in words if is_real_word(w)]
    total_units = max(1, n_alpha + n_tokens)
    ratio = n_alpha / total_units
    # rechazar si un solo carácter domina el texto (relleno gráfico tipo 'aaaa')
    letters = [c.lower() for c in text if c.isalpha()]
    if letters:
        from collections import Counter as _C
        if _C(letters).most_common(1)[0][1] / len(letters) > 0.6:
            return "revisar", "carácter repetido dominante (probable relleno gráfico)"
    real_letters = sum(len(w) for w in real_words)
    if len(real_words) >= 2 and real_letters >= 8 and ratio >= MIN_RATIO:
        return "pendiente", ""
    if len(real_words) >= 1:
        return "revisar", "baja densidad de texto (posible mezcla con datos)"
    return "revisar", "sin palabras reconocibles (probable gráfico/opcode)"

def extract_file(relpath, ctrl_global, idbase, log):
    path = os.path.join(MNT, relpath)
    data = open(path, 'rb').read()
    islands = scan(data)
    records = []
    for k, (ini, fin) in enumerate(islands):
        text, (npr, nct, noth) = decode(data, ini, fin)
        raw = data[ini:fin]
        for cc in control_codes_in(text):
            ctrl_global[cc] += 1
        estado, nota = quality(text)
        records.append({
            "id": f"{idbase}_{k:05d}",
            "archivo_origen": relpath,
            "offset_inicio": ini,
            "offset_fin": fin,
            "longitud_original_bytes": fin - ini,
            "texto_original": text,
            "texto_traducido": "",
            "notas": nota,
            "estado": estado,
            "raw_hex": raw.hex(),
        })
    n_clean = sum(1 for r in records if r["estado"] == "pendiente")
    log.append(f"{relpath}: {len(records)} islas ({n_clean} limpias / {len(records)-n_clean} revisar), {len(data)} bytes")
    return records

def main():
    os.makedirs(OUT, exist_ok=True)
    ctrl_global = Counter()
    log = []
    total = 0
    for rel in CANDIDATES:
        p = os.path.join(MNT, rel)
        if not os.path.isfile(p):
            log.append(f"{rel}: NO EXISTE, omitido")
            continue
        idbase = rel.replace("/", "_").replace(".bin", "")
        try:
            recs = extract_file(rel, ctrl_global, idbase, log)
        except Exception as e:
            log.append(f"{rel}: ERROR {e}")
            continue
        total += len(recs)
        name = idbase
        with open(os.path.join(OUT, name + ".json"), "w", encoding="utf-8") as f:
            json.dump(recs, f, ensure_ascii=False, indent=1)
        with open(os.path.join(OUT, name + ".csv"), "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=[
                "id","archivo_origen","offset_inicio","offset_fin",
                "longitud_original_bytes","texto_original","texto_traducido",
                "notas","estado"])
            w.writeheader()
            for r in recs:
                w.writerow({k: r[k] for k in w.fieldnames})
    # catalogo de codigos de control
    with open(os.path.join(OUT, "control_codes.json"), "w", encoding="utf-8") as f:
        json.dump(dict(sorted(ctrl_global.items(), key=lambda x:-x[1])), f, indent=1)
    log.append(f"TOTAL registros: {total}")
    log.append(f"Codigos control distintos: {len(ctrl_global)}")
    with open(os.path.join(OUT, "extract.log"), "w", encoding="utf-8") as f:
        f.write("\n".join(log) + "\n")
    print("\n".join(log))

if __name__ == "__main__":
    main()
