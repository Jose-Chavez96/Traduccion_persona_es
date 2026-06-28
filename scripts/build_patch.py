#!/usr/bin/env python3
"""
Fase 6 + 7 - Reconstrucción local del ISO y generación del parche .xdelta.

Flujo SEGURO:
  1. Verifica MD5 del ISO original contra el esperado (Fase 1).
  2. Copia el ISO original -> rebuilt/persona_es_patched.iso.
     EL ORIGINAL NUNCA SE TOCA (queda como respaldo pristino).
  3. Aplica patch_records.json sobre la COPIA, mapeando offset-en-.bin -> offset-absoluto-ISO
     via scripts/iso_offsets.json. Antes de sobrescribir, VERIFICA que los bytes
     actuales en ese offset coincidan con raw_hex original (aborta el registro si no).
  4. Genera patches/persona_spanish_patch.xdelta = diff(original, copia parcheada).
  5. Reporta tamaños y MD5.

El parche .xdelta contiene SOLO la diferencia binaria (ningún archivo con copyright).
"""
import os, sys, json, hashlib, shutil, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS = os.path.join(ROOT, "scripts")
REBUILT = os.path.join(ROOT, "rebuilt")
PATCHES = os.path.join(ROOT, "patches")
ISO_SRC = "/mnt/c/Users/59395/Downloads/Shin Megami Tensei - Persona (Europe) (PSP) (PSN)/Shin Megami Tensei - Persona (Europe) (PSP) (PSN).iso"
ISO_OUT = os.path.join(REBUILT, "persona_es_patched.iso")
EXPECTED_MD5 = "03ee31f32bcd3bb697de347fba4493d9"

def md5(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def basename_map(iso_offsets):
    """basename.lower() -> (abs_offset, size). Avisa colisiones."""
    m = {}
    for k, (off, sz) in iso_offsets.items():
        b = os.path.basename(k).lower()
        if b in m and m[b][0] != off:
            print(f"  AVISO: basename duplicado {b}, uso el primero")
            continue
        m[b] = (off, sz)
    return m

def main():
    os.makedirs(REBUILT, exist_ok=True)
    os.makedirs(PATCHES, exist_ok=True)

    print("1. Verificando MD5 del ISO original...")
    cur = md5(ISO_SRC)
    if cur != EXPECTED_MD5:
        print(f"   ABORTA: MD5 {cur} != esperado {EXPECTED_MD5}")
        sys.exit(1)
    print(f"   OK {cur}")

    print("2. Copiando ISO original -> copia de trabajo (original intacto)...")
    shutil.copy2(ISO_SRC, ISO_OUT)

    iso_off = json.load(open(os.path.join(SCRIPTS, "iso_offsets.json")))
    bmap = basename_map(iso_off)
    patches = json.load(open(os.path.join(REBUILT, "patch_records.json")))

    print(f"3. Aplicando {len(patches)} parches sobre la copia...")
    applied = mism = nofile = 0
    with open(ISO_OUT, "r+b") as f:
        for p in patches:
            b = os.path.basename(p["archivo"]).lower()
            if b not in bmap:
                nofile += 1
                continue
            base_off = bmap[b][0]
            abs_off = base_off + p["offset_inicio"]
            new = bytes.fromhex(p["bytes_hex"])
            # leer registro original esperado para verificar
            orig_rec = bytes.fromhex(_orig_hex(p))
            f.seek(abs_off)
            cur_bytes = f.read(len(orig_rec))
            if cur_bytes != orig_rec:
                mism += 1
                continue
            f.seek(abs_off)
            f.write(new)
            applied += 1
    print(f"   aplicados={applied} no_coincide={mism} archivo_no_mapeado={nofile}")

    # 4. (texto-solo xdelta DESACTIVADO) El parche unico es persona_es_full.xdelta,
    #    generado por tools/build_unified.py (texto + EBOOT). Aqui solo dejamos el
    #    ISO base parcheado que build_unified necesita; no emitimos xdelta redundante.
    print("4. Parche texto-solo omitido (el unico parche es persona_es_full.xdelta).")

    print("5. Resumen:")
    print(f"   ISO original   MD5 {EXPECTED_MD5}")
    print(f"   ISO parcheado  MD5 {md5(ISO_OUT)}")

# necesitamos el raw_hex original del registro: lo guardamos en patch_records via reinsert? no.
# lo recuperamos de translated_text por id.
_ORIG_CACHE = None
def _orig_hex(p):
    global _ORIG_CACHE
    if _ORIG_CACHE is None:
        import glob
        _ORIG_CACHE = {}
        for jf in glob.glob(os.path.join(ROOT, "translated_text", "*.json")):
            for r in json.load(open(jf, encoding="utf-8")):
                _ORIG_CACHE[r["id"]] = r["raw_hex"]
    return _ORIG_CACHE[p["id"]]

if __name__ == "__main__":
    main()
