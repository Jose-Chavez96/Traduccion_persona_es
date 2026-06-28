#!/usr/bin/env python3
"""Edita cm_menu.bin blob 20 (menu de campo) EN->ES, in-place (mismo tamano de blob).
Redibuja cada palabra ES dentro del footprint de la EN (mismo x_start, ancho<=caja).
Color RGB(153,153,153), alpha=glyph*102/255 (rampa de la paleta original).
Genera _tex/edited/cm_menu.bin y un preview gris. NO toca el parche; build_unified lo pliega."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
import glyphfont
from gim2png import split_container, parse_gim, u32, write_png
from png2gim import reencode_blob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "_tex", "cm_menu.bin")
BLOB = 20
TXTCOL = (153, 153, 153)
APEAK = 102

# (es_word, x_start, clear_x0, clear_x1, y_top)  -- Persona se deja sin tocar
EDITS = [
    # row1  y3-20
    ("Orden", 2, 2, 86, 4),
    ("Tecn", 88, 86, 138, 4),
    ("Obj", 147, 146, 186, 4),
    ("Equipo", 192, 191, 255, 4),
    # row2  y24-42 (Persona intacto)
    ("Estado", 82, 81, 146, 25),
    ("Combate", 148, 147, 235, 25),
    # row3  y48-66
    ("Sistema", 2, 2, 70, 49),
]
ROW_BANDS = {4: (3, 21), 25: (23, 43), 49: (47, 67)}


def main():
    D = bytearray(open(SRC, "rb").read())
    cnt = u32(D, 0)
    sizes = [u32(D, 4 + 4 * i) for i in range(cnt)]
    base = (4 + 4 * cnt + 15) & ~15
    off = base + sum(sizes[:BLOB])
    g = bytes(D[off:off + sizes[BLOB]])
    w, h, rgba = parse_gim(g)
    rgba = bytearray(rgba)

    def setpx(x, y, r, gg, b, a):
        if 0 <= x < w and 0 <= y < h:
            o = (y * w + x) * 4
            rgba[o], rgba[o + 1], rgba[o + 2], rgba[o + 3] = r, gg, b, a

    for es, xs, cx0, cx1, yt in EDITS:
        y0, y1 = ROW_BANDS[yt]
        for y in range(y0, y1):
            for x in range(cx0, cx1 + 1):
                setpx(x, y, 0, 0, 0, 0)            # limpia caja EN
        alpha, rw, rh = glyphfont.render(es)
        for y in range(rh):
            for x in range(rw):
                ga = alpha[y][x]
                if ga > 0:
                    setpx(xs + x, yt + y, *TXTCOL, ga * APEAK // 255)

    ng = reencode_blob(g, bytes(rgba), w, h)
    assert len(ng) == sizes[BLOB], "blob size changed"
    D[off:off + len(ng)] = ng

    outdir = os.path.join(ROOT, "_tex", "edited")
    os.makedirs(outdir, exist_ok=True)
    open(os.path.join(outdir, "cm_menu.bin"), "wb").write(D)
    print("wrote", os.path.join(outdir, "cm_menu.bin"), "size", len(D))

    # preview gris desde el blob editado RE-leido (verifica el round-trip de indexado)
    g2 = bytes(D[off:off + len(ng)])
    w2, h2, rg2 = parse_gim(g2)
    gray = bytearray(w2 * h2 * 4)
    for i in range(w2 * h2):
        a = rg2[i * 4 + 3]
        v = 255 - a * 2 if a else 255
        gray[i * 4:i * 4 + 4] = bytes([v, v, v, 255])
    pv = os.path.join(ROOT, "_tex", "cm20_es_preview.png")
    write_png(pv, w2, h2, bytes(gray))
    print("preview", pv)


if __name__ == "__main__":
    main()
