#!/usr/bin/env python3
"""
build_unified.py — Parche UNICO: historia (bins) + interfaz (EBOOT) + (texturas).

Base = rebuilt/persona_es_patched.iso (ya tiene los 12821 parches de texto de
historia/negociacion). Encima escribe el EBOOT descifrado+traducido en
/PSP_GAME/SYSDIR/EBOOT.BIN (@0x1245184). Genera UN xdelta original->unificado.

Uso: python3 tools/build_unified.py
Salida: patches/persona_es_full.xdelta + rebuilt/persona_es_full.iso
"""
import os, json, hashlib, shutil, subprocess

ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ISO_SRC="/mnt/c/Users/59395/Downloads/Shin Megami Tensei - Persona (Europe) (PSP) (PSN)/Shin Megami Tensei - Persona (Europe) (PSP) (PSN).iso"
STORY_ISO=os.path.join(ROOT,"rebuilt","persona_es_patched.iso")
EBOOT_TR=os.path.join(ROOT,"_eboot","eboot_translated.elf")
OUT_ISO=os.path.join(ROOT,"rebuilt","persona_es_full.iso")
OUT_XD=os.path.join(ROOT,"patches","persona_es_full.xdelta")
EBOOT_OFF=1245184
EBOOT_SIZE=3838272
EXPECT="03ee31f32bcd3bb697de347fba4493d9"

def md5(p):
    h=hashlib.md5()
    with open(p,'rb') as f:
        for c in iter(lambda:f.read(1<<20),b''): h.update(c)
    return h.hexdigest()

def main():
    assert md5(ISO_SRC)==EXPECT, "original ISO MD5 mismatch"
    print("1. base = story-patched ISO (12821 record patches)")
    shutil.copy2(STORY_ISO, OUT_ISO)
    print("2. escribir EBOOT traducido @0x%X"%EBOOT_OFF)
    d=open(EBOOT_TR,'rb').read()
    if len(d)>EBOOT_SIZE: raise SystemExit("EBOOT too big")
    d=d+b'\x00'*(EBOOT_SIZE-len(d))
    with open(OUT_ISO,'r+b') as f:
        f.seek(EBOOT_OFF); f.write(d)
    # 2.5 capa de TEXTURAS: escribe menu-bins editados (mismo tamano) en su offset ISO
    TEXDIR=os.path.join(ROOT,"_tex","edited")
    iso_off=json.load(open(os.path.join(ROOT,"scripts","iso_offsets.json")))
    bm={os.path.basename(k).lower():(o,sz) for k,(o,sz) in iso_off.items()}
    wrote=[]
    if os.path.isdir(TEXDIR):
        with open(OUT_ISO,'r+b') as f:
            for fn in sorted(os.listdir(TEXDIR)):
                if not fn.endswith('.bin'): continue
                b=fn.lower()
                if b not in bm: raise SystemExit("offset desconocido para "+fn)
                off,sz=bm[b]; data=open(os.path.join(TEXDIR,fn),'rb').read()
                if len(data)!=sz: raise SystemExit(f"{fn} tamano {len(data)}!={sz} (debe ser identico)")
                f.seek(off); f.write(data); wrote.append(fn)
    print(f"2.5 texturas: {wrote if wrote else 'ninguna (sin _tex/edited)'}")
    print("3. xdelta original -> unificado")
    r=subprocess.run(["xdelta3","-e","-9","-f","-s",ISO_SRC,OUT_ISO,OUT_XD],capture_output=True,text=True)
    if r.returncode: raise SystemExit("xdelta err "+r.stderr)
    print("4. round-trip")
    tmp=OUT_ISO+".rt"
    r=subprocess.run(["xdelta3","-d","-f","-s",ISO_SRC,OUT_XD,tmp],capture_output=True,text=True)
    rt = r.returncode==0 and md5(tmp)==md5(OUT_ISO)
    if os.path.exists(tmp): os.remove(tmp)
    print("=== RESUMEN ===")
    print("  original   ",EXPECT,"(intacto)")
    print("  unificado  ",md5(OUT_ISO))
    print("  xdelta     ",os.path.getsize(OUT_XD),"bytes ->",OUT_XD)
    print("  round-trip ","OK" if rt else "FALLO")

if __name__=="__main__": main()
