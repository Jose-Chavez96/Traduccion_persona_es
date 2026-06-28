# Auditoria global — 2026-06-14

## Cobertura total
- Records totales (extracted): **12837**
- Traducidos+insertados: **7089** (55.2%)
- Por traducir: **5748** (44.8%)

## talk/* — COMPLETO
- **28/28 archivos, 7027/7027 records (100%)**
- Todos validados (tokens + longitud) e insertados en patch_records.

## Patch actual
- `rebuilt/patch_records.json`: 7088 records (1 excede limite, no insertable)
- `patches/persona_spanish_patch.xdelta`: **392967 bytes**
- ISO original MD5 03ee31f32bcd3bb697de347fba4493d9 (intacto)
- ISO parcheado MD5 b921a86c36d2039214c3e9925a9663e5
- Aplicacion: 7088 aplicados, 0 no_coincide, 0 archivo_no_mapeado

## Pendientes (5748 strings, 9 archivos)
| archivo | traducidos | por_traducir | nota |
|---|---|---|---|
| e0 | 19 | 1941 | dialogo historia/eventos |
| e1 | 0 | 1128 | dialogo historia/eventos |
| e2 | 5 | 990 | dialogo historia/eventos |
| e3 | 6 | 514 | dialogo historia/eventos |
| e4 | 32 | 1159 | dialogo historia/eventos |
| sys | 0 | 7 | textos de sistema |
| kage | 0 | 4 | |
| title_title | 0 | 3 | pantalla titulo |
| bt_menu | 0 | 2 | menu batalla |

## Estimate e*.bin
- e0-e4 suman **5732 strings** (~99.7% de lo pendiente).
- A ritmo talk (2 mitades/archivo, write-through): e3(514) y e2/e1 medianos ~1 sesion c/u; e0(1941) y e4(1159) son los mas grandes.
- e*.bin = dialogo de HISTORIA (eventos, cutscenes) -> mas variado, menos bloques repetidos que talk_* -> menos reuso, mas trabajo por record. Esperar mas overflows por expansion ES.

## Critical path (orden sugerido)
1. **sys / title_title / bt_menu / kage** (16 strings) — rapido, alto impacto visible (UI/titulo).
2. **e3** (514) — el e*.bin mas chico, buen arranque.
3. **e2, e1** (990, 1128) — medianos.
4. **e4, e0** (1159, 1941) — los grandes, dejar al final.

NO iniciado por instruccion del usuario: esperar orden antes de e*.bin.
