# UI Strings Audit — Persona PSP (Europe) ES

Fecha: 2026-06-21. Fase: UI (interfaz, menus, opciones de seleccion).

## Objetivo
Localizar y traducir cadenas de interfaz (menus de combate, opciones, casino),
distintas de la narrativa (ya 100% traducida).

## Metodo de busqueda
1. Auditados los 37 `translated_text/*.json` y todos los `extracted_text/*.json`.
2. Buscadas, en texto ASCII y en codec u16 (`persona_codec.encode`), las palabras:
   Attack, Guard, Item, Persona, Escape, Equip, Status, Buy, Sell, Exit, Use,
   Check, Order, Auto, Analyze, Contact, Magic, Bet on, Bet on Mark/Brown, Yes, No.
3. Barrido codec de **todos** los `.bin` del ISO (EBOOT, BOOT, bt_menu, cm_menu,
   ch_menu, RESULT, MES_ALL, SHALL, casino/minigame_*, sys/over/moon, etc.).
4. Sanidad del metodo verificada: `encode("Persona")` aparece 154x en `E0.BIN`
   (coincide con la narrativa) → el buscador funciona.

## Hallazgo principal (concluyente)
**Los rotulos de UI / comandos de menu / botones de casino NO existen como texto
editable en ningun archivo.** Resultados:

| Fuente buscada                | Attack/Guard/Item/Escape/Equip/Status/Bet on (codec) |
|-------------------------------|------------------------------------------------------|
| EBOOT.BIN / BOOT.BIN          | NONE |
| bt_menu.bin / cm_menu.bin / ch_menu.bin | NONE |
| RESULT.BIN (pantalla victoria)| NONE |
| MES_ALL.BIN (68 MB)           | NONE |
| SHALL.BIN (tienda)            | NONE |
| casino/minigame_{cb,dice,poker,slot}.bin | NONE |
| **Barrido global de todos los .bin** | **NONE** |

- ASCII en EBOOT: solo coincidencias basura dentro de codigo (`bEt`, `uSE`, `nO`)
  — no son rotulos reales.
- `extracted_text/{ch_menu,cm_menu,over,moon,shop_shall,...}.json`: las "islas"
  extraidas son ruido de fuente/graficos (`aaaa`, `!1AQ`, datos de layout),
  marcadas `no_traducible`. No contienen palabras.
- `sys.json`, `bt_menu.json`, `title_title.json`, `kage.json` (en translated_text):
  **todos los registros = `no_traducible`** (datos de fuente/graficos, sin texto).
- Registros de eleccion Yes/No autonomos: **0**. Los 100 "Yes" / 427 "No"
  detectados son substrings de dialogo ("No way", "Yes, that's right"), ya
  traducidos como parte de la narrativa.
- "Bet on Mark" / "Bet on Brown": no existen como texto (ni narrativa ni binario).
  La apuesta del combate de casino se dibuja como grafico.

## Conclusion
La UI (Attack, Guard, Item, Persona, Escape, Equip, Status, Buy/Sell, casino, etc.)
esta **pre-renderizada como sprites de fuente / texturas**, no como cadenas. Por eso
el pipeline de parche-por-texto (extract → reinsert → build_patch) **no puede
tocarla**: no hay bytes de texto que reemplazar.

Todo el texto *traducible* del juego (dialogo, narrativa, talk de demonios, ayuda
de casino que SI era texto) ya esta al 100% (ver `persona_spanish_patch.xdelta`).

## Para traducir la UI haria falta otro workstream (fuera de este pipeline)
1. Identificar las texturas de fuente/menu (probable formato GIM/TIM/SWIZZLE dentro
   de `bt_menu.bin`, `cm_menu.bin`, `title.bin`, `RESULT.BIN`, `*minigame*.bin`).
2. Decodificar/extraer esas imagenes, redibujar los glifos de cada rotulo en ES
   (Atac, Def, Obj, Huir, Estado, Comprar, Vender, Apostar a Mark/Brown…),
   respetando ancho/alto del sprite.
3. Re-empaquetar la textura y re-parchear con verificacion MD5 + xdelta.

Esto es edicion grafica, no de texto. Mapeo de compresion propuesto por el usuario
(Attack→Atac, Item→Obj, Guard→Def, Escape→Huir, Status→Estado, Save→Guard,
Load→Cargar, Buy→Comprar, Sell→Vender, Exit→Salir, Use→Usar, Check→Ver,
Bet on→Apostar a) queda registrado aqui para esa fase grafica futura.

## Acciones de cierre
NO se ejecuto reinsert/build_patch/xdelta: no hubo strings nuevas que insertar
(0 cadenas UI editables). El parche actual permanece valido e intacto
(ISO original MD5 `03ee31f32bcd3bb697de347fba4493d9`).
