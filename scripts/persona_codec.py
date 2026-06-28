#!/usr/bin/env python3
"""
Codec del texto de Persona PSP (Europe).

Codificación custom verificada en Fase 1:
    cada carácter = u16 BIG-ENDIAN
    valor_u16 = ASCII + 0xA0
    espacio    = 0x0000
    control    = 0xFFxx   (saltos, color, pausas, fin de string, etc.)

Mapeo de rangos (DOS segmentos lineales, verificado contra texto real):
    0x0000              -> espacio (' ')
    ASCII 0x21..0x5F  (! .. _ : símbolos, dígitos, MAYÚSCULAS) -> u16 = ASCII + 0x9F  (0x00C0..0x00FE)
    ASCII 0x60..0x7A  (` .. z : minúsculas)                    -> u16 = ASCII + 0xA0  (0x0100..0x011A)
    0xFFxx              -> código de control (2 bytes) -> token "<FFxx>"
    cualquier otro u16  -> dato no-texto / puntuación especial (ej. apóstrofo=0x0026) -> token "<xxxx>"

El gap de 1 entre segmentos (0x9F vs 0xA0) evita que un glifo caiga en 0xFFxx (control).

REGLA DE ORO (regla 5 del proyecto): los tokens <....> son LITERALES.
Nunca se traducen, nunca se reordenan dentro de una línea.
"""

OFF_HI = 0x9F   # ASCII 0x21..0x5F  (símbolos, dígitos, MAYÚSCULAS)
OFF_LO = 0xA0   # ASCII 0x60..0x7A  (minúsculas)

# Puntuación con código RAW propio (no sigue el offset de segmento). Verificado por contexto.
PUNCT = {
    0x0003: ',',
    0x0004: '!',
    0x0008: '?',
    0x0009: '.',
    0x0026: "'",
    0x003C: '-',
}
PUNCT_REV = {v: k for k, v in PUNCT.items()}

def code_to_char(c):
    """u16 -> char ASCII si es texto imprimible, si no None."""
    if c == 0x0000:
        return ' '
    if c in PUNCT:                  # puntuación raw-low
        return PUNCT[c]
    if 0xC0 <= c <= 0xFE:           # segmento alto: símbolos/dígitos/MAYÚS
        a = c - OFF_HI
        if 0x21 <= a <= 0x5F:
            return chr(a)
    if 0x100 <= c <= 0x11A:         # segmento bajo: minúsculas
        a = c - OFF_LO
        if 0x60 <= a <= 0x7A:
            return chr(a)
    return None

def char_to_code(ch):
    """char ASCII -> u16. Lanza si no es codificable en la fuente base."""
    if ch == ' ':
        return 0x0000
    if ch in PUNCT_REV:             # puntuación con código raw propio
        return PUNCT_REV[ch]
    a = ord(ch)
    if 0x21 <= a <= 0x5F:
        return a + OFF_HI
    if 0x60 <= a <= 0x7A:
        return a + OFF_LO
    raise ValueError(f"char no codificable en fuente base: {ch!r} (0x{a:02x})")

def decode(data, start, end):
    """
    Decodifica region [start,end) (longitud par) a texto-display con tokens.
    Devuelve (texto, stats) donde stats = (n_print, n_ctrl, n_other).
    """
    out = []
    n_print = n_ctrl = n_other = 0
    i = start
    while i + 1 < end:
        c = (data[i] << 8) | data[i+1]
        ch = code_to_char(c)
        if ch is not None:
            out.append(ch)
            if ch != ' ':
                n_print += 1
        elif (c & 0xFF00) == 0xFF00:
            out.append(f"<FF{c & 0xFF:02X}>")
            n_ctrl += 1
        else:
            out.append(f"<{c:04X}>")
            n_other += 1
        i += 2
    return ''.join(out), (n_print, n_ctrl, n_other)

import re
_TOKEN = re.compile(r"<([0-9A-Fa-f]{2,4})>")

def encode(text):
    """
    Texto-display (con tokens <....>) -> bytes.
    Tokens <FFxx>/<xxxx> se reemiten literales como u16 BE.
    """
    out = bytearray()
    pos = 0
    for m in _TOKEN.finditer(text):
        # texto plano antes del token
        for ch in text[pos:m.start()]:
            c = char_to_code(ch)
            out += bytes([(c >> 8) & 0xFF, c & 0xFF])
        hexv = m.group(1)
        if len(hexv) == 2:        # <FFxx> abreviado -> 0xFFxx
            c = 0xFF00 | int(hexv, 16)
        else:
            c = int(hexv, 16)
        out += bytes([(c >> 8) & 0xFF, c & 0xFF])
        pos = m.end()
    for ch in text[pos:]:
        c = char_to_code(ch)
        out += bytes([(c >> 8) & 0xFF, c & 0xFF])
    return bytes(out)


if __name__ == "__main__":
    # autotest: round-trip
    sample = "Hello<FF03> world<FF02>"
    b = encode(sample)
    t, _ = decode(b, 0, len(b))
    print("encode/decode round-trip:", t == sample, repr(t))
