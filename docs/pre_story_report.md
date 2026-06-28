# Pre-story report — 2026-06-14

Cierre de pendientes pequeños antes de entrar a la historia (e*.bin).

## Acción de esta sesión
- `sys` (7), `title_title` (3), `bt_menu` (2), `kage` (4) = **16 records inspeccionados**.
- **No son texto**: datos binarios (gráficos/fuente/tablas de control). 0 palabras reales (heurística vocal+consonante).
- Marcados `estado=no_traducible` (no se insertan → bytes originales del ISO intactos).
- `reinsert.py` + `build_patch.py` ejecutados. Parche **sin cambios** (eran no-ops binarios).

## Records totales insertados
- `rebuilt/patch_records.json`: **7088 records**
- `patches/persona_spanish_patch.xdelta`: **392 967 bytes**
- ISO original MD5 `03ee31f32bcd3bb697de347fba4493d9` (intacto)
- ISO parcheado MD5 `b921a86c36d2039214c3e9925a9663e5` · 7088 aplicados, 0 no_coincide

## Archivos 100% completos: 32 / 37
- 28 `talk_*` (todos)
- 4 cerrados como no_traducible: `sys`, `title_title`, `bt_menu`, `kage`

## Archivos pendientes: 5 (solo e*.bin = historia)
| archivo | traducidos | por_traducir |
|---|---|---|
| e0 | 19 | 1941 |
| e4 | 32 | 1159 |
| e1 | 0 | 1128 |
| e2 | 5 | 990 |
| e3 | 6 | 514 |

## Total restante exacto
- **5732 strings** por_traducir (todos en e0-e4)
- 16 records no_traducible (cerrados)
- Cobertura global: **7089 / 12837 = 55.2%** traducido+insertado

## Estimación e3 (siguiente objetivo lógico, el e*.bin más chico)
- 514 records por_traducir · 258 936 bytes originales · promedio **503 bytes/record** (~250 unidades visibles)
- e3 es diálogo de historia: más largo por record que talk_*, menos bloques repetidos → menos reuso, más overflows a corregir a mano.
- Plan: **2 mitades** (~257 records c/u), write-through con `wf_apply_one` tras cada mitad.
- Estimación de esfuerzo (basada en youen/tensi/worm/sinsi de esta sesión, ~400-450 records c/u):
  - dump + build + pre-validación + fixes de overflow por mitad ≈ comparable a un talk grande.
  - e3 completo ≈ **2 talk-grandes de trabajo** → del orden de **~130-180k tokens** de salida (dump de 2 mitades + scripts de build + 2-3 rondas de corrección de overflow/tokens).
  - Sin tope de presupuesto duro; depende del % restante al arrancar.

## Estado de budget
- Suficiente para este cierre. e3 NO iniciado (era solo estimación).
- Regla activa: si budget < 5%, STOP limpio antes de e3.
