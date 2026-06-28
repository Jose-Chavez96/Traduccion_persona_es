# Auditoría post-e2 (cierre de etapa) — 2026-06-14

Estado: **e2 COMPLETO e insertado**. Patch reconstruido y verificado. Proyecto en pausa hasta el viernes.

## Integridad (verificada este cierre)
- `reinsert.py`: 8592 insertados OK · 1 excede (`e0_00074`, demo viejo, no crítico) · 0 tokens alterados · 0 no codificables.
- `build_patch.py`: MD5 ISO original `03ee31f32bcd3bb697de347fba4493d9` **VERIFICADO INTACTO**.
- Aplicación de parches: **8592 aplicados, 0 no_coincide, 0 archivo_no_mapeado**.
- ISO parcheado MD5: `dcf7b3121478018b32d2403453e212e3`.
- `patches/persona_spanish_patch.xdelta`: **498641 bytes**.
- **Round-trip xdelta OK**: aplicar parche al original reproduce exactamente `dcf7b3121478018b32d2403453e212e3`. Original sigue `03ee31…493d9`.

## A) Estado global
- patch_records total: **8592**
- cobertura global: **8609 / 12837 = 67.06%**
- registros traducidos/cerrados: 8609 (incluye `no_traducible`)
- archivos completos: **34 / 37** · pendientes: **3** (e0, e1, e4)

## B) Estado por archivo (por_traducir exacto)
| archivo | total | por_traducir | nota |
|---------|-------|--------------|------|
| e0 | 1960 | **1941** | solo 19 demos hechos |
| e1 | 1128 | **1128** | sin empezar |
| e4 | 1191 | **1159** | solo 32 demos hechos |
| sys | 7 | **0** | 7 no_traducible (datos binarios) |
| title_title | 3 | **0** | 3 no_traducible |
| bt_menu | 2 | **0** | 2 no_traducible |
| kage | 4 | **0** | 4 no_traducible |
| e2 | 995 | **0** | COMPLETO (990 shortened + 5) |
| e3 | 520 | **0** | COMPLETO |

Pendiente real de traducción = **e0 + e1 + e4 = 4228 registros narrativos**.

## C) Estadísticas de traducción
- total shortened (global): **7120**
- total fallidos: **0**
- total no_traducible: 16 (sys/title/bt_menu/kage)
- reusados:
  - cross-file (wf_reuse.py inicial en e2): **272**
  - intra-file (wf_intrareuse en e2): **3**
  - casino dict-reuse: **203 frases** propagadas a **28 records** vía diccionario maestro orden-desc (1 disparo, 0 overflow)
- splices aplicados (repl sobre original, e2): **~180** records (garbage-soup/sprite preservada verbatim) — estimado de sesión
- overflows corregidos (e2): **~85** — estimado de sesión (recorte (X-Y)/2 chars, colapso espacios, drop pronombres)

## D) Hotspots técnicos aprendidos
**Tokens más peligrosos:**
- `<FF03>` (salto de línea): omitirlo al fusionar dos cláusulas PIERDE el token → fallo. Debe ir EXACTO dentro de cada frase de diálogo.
- `<FF02><FF01>` / `<FF02><FF04>` (nueva página): pares; no romper.
- `<FF1B>Nombre<FF03>` (etiqueta hablante): nombres largos EXPANDEN y causan overflow → acortar (Clerk→Mozo, etc.).
- garbage-soup sprite/layout (`<FF60> <FF55> <hex>` …, runs `<FFFF>`, `<FF22>/<FF54>/<FF44>`): NO traducible; preservar byte-a-byte.
- `<FF18>..<FF18>` item, `<0044>` icono, `<0028>..<0028>` énfasis, `<0056>palabra<0056>`, `<0029>..<002A>`, botones `<0039>..<003A>`/`<0043>Etiqueta<0044>`/`<0055>`/`<0006>`/`<0007>`, naipes `<0204>-<0207>`, contador `<FF11>`, `<FF1A><8200>`: todos literales, no tocar.
- `<FF05><1000/1500/2000/2500/3000>` control de animación: preservar exacto.

**Patrones que colapsan:**
- `put()` con string completo en records con trailing/leading soup → "tokens alterados" (olvidé reproducir la soup). FIX: usar `repl()` SIEMPRE que el record tenga `[SOUP]`.
- Colisión de substrings en diccionario (ej. "Low" dentro de "Low!", "Flush" dentro de "Straight flush", "button" dentro de "buttons"). FIX: aplicar pares en orden LONGITUD DESCENDENTE.

**Reglas de splice que funcionaron:**
- `repl(id,(en,es)...)` reemplaza SOLO el diálogo legible sobre `texto_original` → tokens/padding/soup se preservan automáticamente. Método dominante para e*.
- Viewer `wf_view2.py` colapsa runs de basura a `[SOUP]` para leer diálogo sin volcar 16KB.

**Reglas de compresión semántica que funcionaron:**
- Inglés es verboso → español equivalente suele caber en bloques grandes (casino: 0 overflow).
- Overflow fix: colapsar espacios, drop pronombres (YO/TU/MUY), sinónimos cortos (instalaciones→salas, perseguir→seguir, realidad→real), recortar muletillas (Whoa/Oh/Pero).
- Etiquetas hablante: glosario fijo de apodos cortos (ver memoria).

## E) Critical path restante (orden recomendado)
1. **e1** (1128, 0% — sin empezar)
2. **e4** (1159 pend — ya 32 demos)
3. **e0** (1941 pend — ya 19 demos)

Método idéntico a e2: dump pendientes → `wf_view2.py` → chunks de ~22 (`put`/`repl`) → `wf_apply_one` → corregir overflows → write-through. Reuse intra-file primero. Al cerrar cada archivo: reinsert + build_patch + verificar MD5.

## Cierre
Source-of-truth en `translated_text/*.json`. Patch y xdelta al día. ISO original intacta. Listo para reanudar el viernes en e1.
