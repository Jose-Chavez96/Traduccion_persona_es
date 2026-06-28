#!/usr/bin/env python3
"""
patch_bin_iso.py — Inserta uno o varios .bin completos (mismo tamano) en una COPIA
del ISO, en su offset absoluto, sin tocar punteros. Verifica MD5 original, genera
xdelta y reporta. El ISO original NUNCA se modifica.

Uso:
  python3 tools/patch_bin_iso.py <salida.iso> <salida.xdelta> <nombre1.bin> <ruta1> [<nombre2.bin> <ruta2> ...]

  nombreN.bin = basename tal como aparece en scripts/iso_offsets.json (ej. cm_menu.bin)
  rutaN       = archivo .bin modificado (debe pesar exactamente lo mismo que el original)

Base = ISO original (parche UI aislado). El tamano de cada bin debe ser identico al
original (edicion in-place) para no recalcular el sistema de archivos del ISO.
"""
import os, sys, json, hashlib, shutil, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS = os.path.join(ROOT, "scripts")
ISO_SRC = "/mnt/c/Users/59395/Downloads/Shin Megami Tensei - Persona (Europe) (PSP) (PSN)/Shin Megami Tensei - Persona (Europe) (PSP) (PSN).iso"
EXPECTED_MD5 = "03ee31f32bcd3bb697de347fba4493d9"

def md5(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def basename_map(iso_off):
    m = {}
    for k, (off, sz) in iso_off.items():
        b = os.path.basename(k).lower()
        if b not in m:
            m[b] = (off, sz)
    return m

def main():
    iso_out = sys.argv[1]; xd_out = sys.argv[2]
    pairs = sys.argv[3:]
    assert len(pairs) % 2 == 0 and pairs, "faltan pares <nombre.bin> <ruta>"

    print("1. Verificando MD5 del ISO original...")
    cur = md5(ISO_SRC)
    if cur != EXPECTED_MD5:
        print(f"   ABORTA: MD5 {cur} != {EXPECTED_MD5}"); sys.exit(1)
    print(f"   OK {cur}")

    iso_off = json.load(open(os.path.join(SCRIPTS, "iso_offsets.json")))
    bmap = basename_map(iso_off)

    print("2. Copiando ISO original -> copia de trabajo...")
    shutil.copy2(ISO_SRC, iso_out)

    print("3. Insertando bins...")
    with open(iso_out, "r+b") as f:
        for i in range(0, len(pairs), 2):
            name = pairs[i].lower(); path = pairs[i+1]
            if name not in bmap:
                print(f"   ABORTA: {name} no esta en iso_offsets"); sys.exit(1)
            off, sz = bmap[name]
            data = open(path, "rb").read()
            if len(data) != sz:
                print(f"   ABORTA: {name} mod={len(data)} != orig={sz} (debe ser identico)"); sys.exit(1)
            f.seek(off); f.write(data)
            print(f"   {name}: {len(data)} B @ 0x{off:X} OK")

    print("4. Generando xdelta...")
    r = subprocess.run(["xdelta3", "-e", "-9", "-f", "-s", ISO_SRC, iso_out, xd_out],
                       capture_output=True, text=True)
    if r.returncode != 0:
        print("   ERROR xdelta3:", r.stderr); sys.exit(1)

    print("5. Round-trip (aplicar xdelta sobre original -> comparar)...")
    tmp = iso_out + ".rt"
    r = subprocess.run(["xdelta3", "-d", "-f", "-s", ISO_SRC, xd_out, tmp],
                       capture_output=True, text=True)
    rt_ok = (r.returncode == 0 and md5(tmp) == md5(iso_out))
    if os.path.exists(tmp): os.remove(tmp)

    print("6. Resumen:")
    print(f"   ISO original   MD5 {EXPECTED_MD5} (intacto)")
    print(f"   ISO parcheado  MD5 {md5(iso_out)}")
    print(f"   xdelta         {os.path.getsize(xd_out)} B")
    print(f"   round-trip     {'OK' if rt_ok else 'FALLO'}")

if __name__ == "__main__":
    main()
