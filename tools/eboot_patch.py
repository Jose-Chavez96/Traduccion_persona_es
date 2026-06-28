#!/usr/bin/env python3
"""
eboot_patch.py — Reemplazo IN-PLACE de strings codec en el EBOOT descifrado (ELF).

Cada par (en, es): localiza los bytes codec de `en`, exige que `es` codifique a
<= bytes que `en`, y sobrescribe EXACTAMENTE ese span (padeando con espacios 0x0000
si es mas corto). No toca terminadores ni strings vecinas -> offsets intactos.
Valida que el conteo de tokens <FFxx> coincida (separadores de menu / saltos).

Uso (programatico): from eboot_patch import patch_file
  patch_file(in_elf, out_elf, [(en,es), ...])
CLI test: python3 tools/eboot_patch.py <in.elf> <out.elf> <pairs.json>
  pairs.json = [["en","es"], ...]
"""
import sys, os, json, re
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
from persona_codec import encode

TOK = re.compile(r'<FF[0-9A-Fa-f]{2}>')

def patch_file(in_elf, out_elf, pairs):
    d = bytearray(open(in_elf, 'rb').read())
    rep = {'ok':0, 'notfound':[], 'toolong':[], 'tokmismatch':[]}
    for en, es in pairs:
        be = encode(en)
        i = d.find(be)
        if i < 0:
            rep['notfound'].append(en); continue
        bs = encode(es)
        if len(bs) > len(be):
            rep['toolong'].append((en, es, len(bs), len(be))); continue
        if TOK.findall(en) != TOK.findall(es):
            rep['tokmismatch'].append((en, es)); continue
        # sobrescribir span exacto: es + relleno con espacios (0x0000) hasta len(be)
        span = bytearray(bs)
        while len(span) < len(be):
            span += b'\x00\x00'        # espacio
        # reemplaza TODAS las ocurrencias (misma frase puede repetirse en varios bloques)
        cnt = 0; j = d.find(be)
        while j >= 0:
            d[j:j+len(be)] = span; cnt += 1
            j = d.find(be, j+len(span))
        rep['ok'] += cnt
    open(out_elf, 'wb').write(d)
    return rep

if __name__ == '__main__':
    pairs = json.load(open(sys.argv[3]))
    r = patch_file(sys.argv[1], sys.argv[2], pairs)
    print('OK=%d  notfound=%d  toolong=%d  tokmismatch=%d' % (
        r['ok'], len(r['notfound']), len(r['toolong']), len(r['tokmismatch'])))
    for k in ('notfound','toolong','tokmismatch'):
        for x in r[k][:10]: print(' ', k, x)
