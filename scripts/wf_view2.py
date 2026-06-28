#!/usr/bin/env python3
"""Viewer que colapsa runs largos de tokens-basura (sprite/layout) para mostrar
solo el dialogo legible. Para repl() basta ver el dialogo (O(id) lee el original real).
Uso: wf_view2.py <pendfile> <start> <count>"""
import json,sys,re
f,s,c=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
d=json.load(open(f,encoding="utf-8"))
# colapsa secuencias de >=3 tokens/hex/espacios/backticks consecutivos sin letras
RUN=re.compile(r"(?:<[0-9A-Fa-f]{2,4}>|`|\s|[0-9A-Fa-f]{2,4}(?=[ <]))(?:\s*(?:<[0-9A-Fa-f]{2,4}>|`|[0-9A-Fa-f]{2,4}(?=[ <])|\s)){12,}")
for p in d[s:s+c]:
    o=p['orig']
    disp=RUN.sub(" [SOUP] ",o)
    print(f"=== {p['id']}  bytes={p['bytes']} chars={len(o)}")
    print(disp)
