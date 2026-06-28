#!/usr/bin/env python3
"""Helper para construir mapas de chunk de e2.
Uso en script: from wf_chunk import O, repl, put, dump
  put(id, full_string)             # registro limpio: string completo
  repl(id, (en,es), (en,es), ...)  # splice: reemplaza dialogo sobre el ORIGINAL (preserva tokens/padding)
  dump(out_path)
O(id) devuelve texto_original."""
import json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_recs=json.load(open(os.path.join(ROOT,"translated_text","e2.json"),encoding="utf-8"))
_byid={r["id"]:r for r in _recs}
_M={}
def O(i): return _byid[i]["texto_original"]
def put(i,s): _M[i]={"t":s,"shortened":True}
def repl(i,*pairs):
    s=O(i)
    for en,es in pairs:
        if en not in s:
            print("WARN no-match",i,repr(en)); 
        s=s.replace(en,es)
    _M[i]={"t":s,"shortened":True}
def dump(p):
    json.dump(_M,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    print("wrote",len(_M),p)
