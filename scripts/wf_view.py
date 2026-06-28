#!/usr/bin/env python3
"""Muestra slice de pendientes e2 para traducir.
Uso: wf_view.py <pendfile> <start> <count>"""
import json,sys
f,s,c=sys.argv[1],int(sys.argv[2]),int(sys.argv[3])
d=json.load(open(f,encoding="utf-8"))
for p in d[s:s+c]:
    print(f"=== {p['id']}  bytes={p['bytes']} chars={len(p['orig'])}")
    print(p['orig'])
