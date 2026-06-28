#!/usr/bin/env python3
import json,re
d={r['id']:r for r in json.load(open('translated_text/e2.json'))}
ids=['e2_00285','e2_00286','e2_00293','e2_00294','e2_00295','e2_00636','e2_00637','e2_00644','e2_00645','e2_00646','e2_00656','e2_00657','e2_00664','e2_00665','e2_00666','e2_01102','e2_01103','e2_01110','e2_01111','e2_01112','e2_01239','e2_01240','e2_01247','e2_01248','e2_01249','e2_01381','e2_01389','e2_01391']
# reemplaza TODO token salvo <FF03> por un delimitador \x00; conserva <FF03> dentro de frases
TOKEN=re.compile(r'<(?!FF03>)[0-9A-Fa-f]{2,4}>')
order=[]; seen=set()
for i in ids:
    o=d[i]['texto_original']
    masked=TOKEN.sub('\x00',o)
    for piece in masked.split('\x00'):
        piece=piece.strip()
        if re.search(r'[A-Za-z]{3,}',piece) and piece not in seen:
            seen.add(piece); order.append(piece)
print('frases unicas:',len(order))
json.dump(order, open('translated_text/_wfmaps/casino_phrases.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
