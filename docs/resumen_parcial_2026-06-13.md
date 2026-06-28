# Resumen parcial — sesiones 2026-06-13/14

Traduccion inline (sin subagentes, para evitar el limite de sesion). Write-through + parada limpia por presupuesto.

## talk_* completados e insertados (28 = TODOS)

talk_etc, gaki, kokuri, doppel, hiho, kemono, korou, kosiki, qsiruba, zombiko, tinpra,
yakuza, zomb_man, zmbityan, slime, polutar, kutisake, mayoeru, basket, kyouki, kouman, syoujo.

## Estado global del patch

- `rebuilt/patch_records.json`: **4701 records** insertados (1 excede limite, no insertable).
- `patches/persona_spanish_patch.xdelta`: 285558 bytes.
- ISO original MD5 `03ee31f32bcd3bb697de347fba4493d9` verificado intacto.
- `docs/checkpoints.json`: inserted 22, translated 7 (e0-e4/sys parciales), pending 8.

## Pendientes (6 talk, 2387 strings)

talk_toilet(312), talk_youen(376), talk_tensi(406), talk_wtensi(405),
talk_worm(440), talk_sinsi(448).

NOTA tecnica: archivos enormes (300+) hacerlos en 2 MITADES con wf_apply_one tras cada una (write-through);
si las paginas Read dejan hueco de ids, revisar `por_traducir` restantes al final. El backtick ` SI codifica.

NOTA: archivos con muchos registros-menu (bloques <FFF5> de opciones cortas) y duplicados casi-identicos
(estados de animo). Cuidar IDs al parchear el mapa (no copiar texto de un id vecino).

NOTA: fuentes telegraficas (mayoeru estilo) generan MUCHOS overflows (espanol expande). Traducir
extra-conciso desde el inicio. <FFF3>/<FFF0> son tokens (cuentan en token-set Y en longitud).

NOTA: talk_polutar y los menus (p.ej. polutar_00193/00195, yakuza_00112) tienen bloques largos de
opciones de menu con tokens basura (<9E00><0180>``<FFFF>...): traducir solo las frases legibles,
preservar todos los tokens.

## Como continuar

`scripts/wf_translate_resumable.js` tiene `PENDIENTES_DEFAULT` = estos 13.
- Inline (metodo usado): dump compacto de `por_traducir`, construir mapa rico {id:{t,shortened}} en
  `translated_text/_wfmaps/<name>_map.json` copiando tokens EXACTOS, pre-validar (chars permitidos +
  token-set identico + len(encode)<=longitud_original_bytes), aplicar `scripts/wf_apply_one.py <name> <map>`,
  corregir overflows/tokens, re-aplicar hasta fallido=0.
- Trampas frecuentes: (1) acentos colados; (2) colapsar dos <FF03> en uno -> token mismatch;
  (3) overflow ~1-2 unidades (cada unidad visible o token = 2 bytes).
- Al terminar tanda: `wf_checkpoints.py` + `reinsert.py` + `build_patch.py`.

Nada se pierde ante un corte: cada archivo se persiste al validarse.
