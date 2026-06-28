#!/usr/bin/env python3
"""
Fase 3 - Preparacion para traduccion.

Lee extracted_text/*.json, toma los registros 'pendiente' (texto limpio),
y genera translated_text/*.json (+ .csv) listos para traducir, con metadatos:
  - tokens_protegidos : lista de <....> que NO se pueden tocar/reordenar
  - limite_chars      : nº maximo de caracteres codificables (= bytes/2)
  - estado            : 'por_traducir' | 'traducido' | 'excede_limite'

Incluye un diccionario DEMO_ES (traducciones de muestra, español latino,
SIN acentos por compatibilidad con la fuente base -> ver Fase 5) para
demostrar el pipeline completo end-to-end. El resto queda 'por_traducir'.

NO modifica archivos del juego.
"""
import os, sys, json, csv, re, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EX = os.path.join(ROOT, "extracted_text")
TR = os.path.join(ROOT, "translated_text")
TOKEN = re.compile(r"<[0-9A-Fa-f]{2,4}>")

# Traducciones de muestra (clave = texto_original .strip()), ES latino, sin acentos.
# Longitud en chars <= original para encajar sin recalcular punteros.
DEMO_ES = {
    "maybe some other time": "quizas en otro momento",
    "It's all right":        "Esta todo bien",
    "Leave me alone":        "Dejame en paz",
    "just kidding":          "solo bromeo",
    "What is that":          "Que es eso",
    "You all came":          "Ya llegaron",
    "I don't like him":      "No me agrada el",
    "the infirmary":         "la enfermeria",
    "Who is that girl":      "Quien es ella",
    "Just for you":          "Solo para ti",
    "I'm all right":         "Estoy bien",
    "What should I do":      "Que debo hacer",
    "The power of demons":   "El poder demoniaco",
    "Just end this already": "Ya termina con esto",
    "Did all those people die": "Murio toda esa gente",
}

def tokens_of(text):
    return TOKEN.findall(text)

def main():
    os.makedirs(TR, exist_ok=True)
    n_files = n_recs = n_demo = 0
    for jf in sorted(glob.glob(os.path.join(EX, "*.json"))):
        if os.path.basename(jf) == "control_codes.json":
            continue
        recs = json.load(open(jf, encoding="utf-8"))
        if not isinstance(recs, list):
            continue
        out = []
        for r in recs:
            if r["estado"] != "pendiente":
                continue
            orig = r["texto_original"]
            limite = r["longitud_original_bytes"] // 2     # chars codificables (2 bytes/char)
            trad = ""
            estado = "por_traducir"
            key = orig.strip()
            if key in DEMO_ES:
                trad = DEMO_ES[key]
                # preservar espacios/tokens de borde del original
                lead = orig[:len(orig) - len(orig.lstrip())]
                tail = orig[len(orig.rstrip()):]
                trad = lead + trad + tail
                estado = "traducido"
                n_demo += 1
            out.append({
                "id": r["id"],
                "archivo_origen": r["archivo_origen"],
                "offset_inicio": r["offset_inicio"],
                "offset_fin": r["offset_fin"],
                "longitud_original_bytes": r["longitud_original_bytes"],
                "limite_chars": limite,
                "tokens_protegidos": tokens_of(orig),
                "texto_original": orig,
                "texto_traducido": trad,
                "notas": "",
                "estado": estado,
                "raw_hex": r["raw_hex"],
            })
        if not out:
            continue
        n_files += 1
        n_recs += len(out)
        base = os.path.basename(jf)
        json.dump(out, open(os.path.join(TR, base), "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        with open(os.path.join(TR, base[:-5] + ".csv"), "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(["id","limite_chars","tokens_protegidos","texto_original","texto_traducido","estado","notas"])
            for r in out:
                w.writerow([r["id"], r["limite_chars"], " ".join(r["tokens_protegidos"]),
                            r["texto_original"], r["texto_traducido"], r["estado"], r["notas"]])
    print(f"Archivos: {n_files}  registros por_traducir: {n_recs}  con traduccion demo: {n_demo}")

if __name__ == "__main__":
    main()
