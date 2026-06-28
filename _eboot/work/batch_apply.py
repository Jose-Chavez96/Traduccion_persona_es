#!/usr/bin/env python3
"""Merge a {en:es} batch into trans_records.json with codec validation.
Validates: encode(es) <= mincap(en) bytes, token <FFxx> counts match, encodable (no accents).
Only valid entries are merged. Prints rejects. Does NOT apply to ELF (run regen chain after)."""
import sys, os, json, re
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "scripts"))
from persona_codec import encode
TOK = re.compile(r'<FF[0-9A-Fa-f]{2}>')
inv = json.load(open(os.path.join(os.path.dirname(__file__), "..", "eb_inventory.json")))
recs_path = os.path.join(os.path.dirname(__file__), "..", "trans_records.json")
R = json.load(open(recs_path))
cap = {}
for r in inv:
    c = r['rawlen'] + (r['room'] if r['term'] == 'FF' else 0)
    cap[r['texto_original']] = min(cap.get(r['texto_original'], 10**9), c)

batch = json.load(open(sys.argv[1]))
ok = []; rej = []
for en, es in batch.items():
    if en not in cap:
        rej.append((en, es, 'NOT_IN_INV')); continue
    if es == en or not es:
        rej.append((en, es, 'NOOP')); continue
    try:
        bs = encode(es)
    except Exception as ex:
        rej.append((en, es, 'ENC:' + str(ex))); continue
    if len(bs) > cap[en]:
        rej.append((en, es, f'TOOLONG {len(bs)}>{cap[en]}')); continue
    if TOK.findall(en) != TOK.findall(es):
        rej.append((en, es, 'TOKMISMATCH')); continue
    ok.append((en, es))

apply = '--apply' in sys.argv
print(f"batch={len(batch)}  ok={len(ok)}  rej={len(rej)}")
for e in rej: print("  REJ", e)
if apply:
    for en, es in ok:
        R[en] = es
    json.dump(R, open(recs_path, 'w'), ensure_ascii=False, indent=1)
    print(f"merged -> trans_records.json now {len(R)} entries")
