# Reporte de traducción — archivos talk/* (negociación de demonios)

**Alcance:** 27 archivos `talk/*.bin`. **Total registros (texto limpio):** 7027

## Porcentaje completado

- Traducidos + acortados: **111 / 7027 = 1.6%**
- Líneas acortadas (`shortened`): **13**
- Líneas fallidas (`fallido`): **0**

## Archivos completados esta tanda

| archivo | total | traducido | acortado | fallido | estado |
|---|---|---|---|---|---|
| talk_basket | 312 | 0 | 0 | 0 | · pendiente |
| talk_doppel | 149 | 0 | 0 | 0 | · pendiente |
| talk_etc | 198 | 0 | 0 | 0 | · pendiente |
| talk_gaki | 98 | 85 | 13 | 0 | ✅ COMPLETO |
| talk_hiho | 336 | 0 | 0 | 0 | · pendiente |
| talk_kemono | 463 | 0 | 0 | 0 | · pendiente |
| talk_kokuri | 8 | 8 | 0 | 0 | ✅ COMPLETO |
| talk_korou | 364 | 0 | 0 | 0 | · pendiente |
| talk_kosiki | 367 | 0 | 0 | 0 | · pendiente |
| talk_kouman | 422 | 0 | 0 | 0 | · pendiente |
| talk_kutisake | 192 | 0 | 0 | 0 | · pendiente |
| talk_kyouki | 328 | 0 | 0 | 0 | · pendiente |
| talk_mayoeru | 200 | 0 | 0 | 0 | · pendiente |
| talk_polutar | 175 | 0 | 0 | 0 | · pendiente |
| talk_qsiruba | 77 | 0 | 0 | 0 | · pendiente |
| talk_sinsi | 448 | 0 | 0 | 0 | · pendiente |
| talk_slime | 134 | 0 | 0 | 0 | · pendiente |
| talk_syoujo | 269 | 0 | 0 | 0 | · pendiente |
| talk_tensi | 408 | 2 | 0 | 0 | ◐ parcial |
| talk_tinpra | 99 | 0 | 0 | 0 | · pendiente |
| talk_toilet | 312 | 0 | 0 | 0 | · pendiente |
| talk_worm | 440 | 0 | 0 | 0 | · pendiente |
| talk_wtensi | 407 | 2 | 0 | 0 | ◐ parcial |
| talk_yakuza | 106 | 0 | 0 | 0 | · pendiente |
| talk_youen | 377 | 1 | 0 | 0 | ◐ parcial |
| talk_zmbityan | 131 | 0 | 0 | 0 | · pendiente |
| talk_zomb_man | 114 | 0 | 0 | 0 | · pendiente |
| talk_zombiko | 93 | 0 | 0 | 0 | · pendiente |

## Archivos reconstruidos en el parche

- Parches talk insertados byte-exactos: **98**
- Archivos .bin afectados: talk/gaki.bin, talk/kokuri.bin, talk/tensi.bin, talk/wtensi.bin, talk/youen.bin

## Validación de offsets y round-trip

- Aplicación sobre copia ISO: **0 no-coincidencias** (cada offset verificado contra bytes originales antes de sobrescribir).
- Round-trip xdelta: aplicar el parche al ISO original reproduce el ISO parcheado **exacto** (MD5 idéntico).
- MD5 ISO parcheado actual: `f7ff077da3a86b8ef62dc57d2fb9f55f`
- Parche: `patches/persona_spanish_patch.xdelta`

## Líneas acortadas (versión corta, marcadas `shortened`)

- `talk_gaki_00021`: 'Mundo humano esta mal'
- `talk_gaki_00022`: '<FFF5>   Bah. Eres chica audaz'
- `talk_gaki_00035`: '<FF03>Eres soso, compa'
- `talk_gaki_00038`: 'Ahora debo andar<FF03>con cuidado'
- `talk_gaki_00040`: '<FFF5>Quieres mi ayuda? Mal<FF03>presentimiento de esto'
- `talk_gaki_00058`: 'Toma esto.<FFEF>Humano tan lamentable'
- `talk_gaki_00060`: 'Te ves distinto a nosotros'
- `talk_gaki_00061`: '<FFEF>   Espera'
- `talk_gaki_00078`: 'bien? Nada de pelear'
- `talk_gaki_00089`: 'Ah, olvidalo.<FF03>Que quieres que haga?<FFEF>   Asi'
- `talk_gaki_00094`: 'Me impresionas. La otra<FF03>palabra es? Ad'
- `talk_gaki_00098`: 'Las piedras de vida son clave<FF03>al negociar'
- `talk_gaki_00100`: '<FFEF>Oye. Nadie se burla de un preta.<FF03>Nadie.<FFEF>  Tch.<FFEF>   Quiero gema. Dame una <FFF4>.<FFEF>   Gyahahaha.<FF03>Asi.<FFEF>Estas bromeando'

## Líneas fallidas

Ninguna en los archivos procesados.

## Pendiente

- Restan **6916** registros talk (6916 de 7027) en 23 archivos sin empezar.
- Próximos por volumen pequeño: kokuri ✅, qsiruba, zombiko, zomb_man, tinpra, yakuza, slime, doppel, etc.
