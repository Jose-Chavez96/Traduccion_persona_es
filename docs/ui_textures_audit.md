# UI Textures Audit — GIM en bt_menu / cm_menu / ch_menu

Fecha: 2026-06-21. Continuacion de `ui_strings_audit.md` (la UI no es texto: son sprites).

## Contenedores
Formato: `u32 count` + `count * u32 size` (tabla de tamanos), header alineado a 16,
blobs GIM concatenados desde `base = align(4 + 4*count, 16)`. Cada blob = un GIM
PSP (`MIG.00.1PSP\0`).

| bin | base | sub-GIMs |
|-----|------|----------|
| bt_menu.bin (46384 B) | 0x50 | 18 (17 GIM + 1 dummy de 10 B) |
| cm_menu.bin (130752 B) | 0x80 | 29 |
| ch_menu.bin (82640 B)  | 0x60 | 22 |

## GIM interno
Bloques: 0x02 root → 0x03 picture → 0x04 image → 0x05 palette.
Image header en `bloque+0x10`: u32 hsize(0x30), u16 format, u16 pixelOrder, u16 w, u16 h.
- format 4 = **INDEX4** (16 colores, 4bpp) — el usado por casi todos los rotulos.
- format 5 = INDEX8; 0..3 = RGBA directos (fondos/iconos).
- pixelOrder 1 = **swizzled** (bloques 16x8 bytes). Paleta tipica RGBA4444 (16 entradas).

## Mapa de texturas con TEXTO (las traducibles)

### cm_menu (menu principal / status / config)
- **cm_menu_20** (256x72, INDEX4) — **MENU PRINCIPAL**:
  `Command  Skill  Item  Equip  Persona  Status  Battle  System`
- **cm_menu_16** (328x48) — labels de status:
  `Lv  Exp  Next LV  Persona  Condition  Weapon  Cur  Attack  Hit  Defense  Evade  Magic Atk  Magic Def  Weapons  Armor`
- **cm_menu_18** (296x96) — menu de CONFIG/opciones:
  `Message speed / Slow Normal Fast / Synchronize / Upward Movement Orientation /
   Upper Left / Upper Right / Absolute / On Off / Minimap Bearings / Battle Cursor Memory /
   Battle Command Confirmation / Load Data / Suspend Game / Return to Title Screen`
- **cm_menu_21** (248x64) — cabeceras de tabla skill/persona (Name SP Cost Persona Own Atk/Def Hit/Eva Order Lv …)
- cm_menu_00 (480x128) y otros grandes = fondos/paneles (no INDEX simple / o RGBA) — no-texto.

### bt_menu (combate)
- **bt_menu_00** (296x64, INDEX4) — hints de botones de combate:
  `Confirm Back Select Details Persona Edit / Reverse Confirm Sub Cycle Attack Move /
   Switch Char Switch Info Hide Show Allocate / Stop Auto`
- **bt_menu_02** (296x32) — cabeceras de tabla (Lv Rank Name SP Cost Subtype Order Affinity Own Trait)
- **bt_menu_10** (144x16) — estados de animo de demonio: `Angry Happy Eager Scared`
- bt_menu_03 = digitos 0-9 + japones residual `現在の所持数 枚`. bt_menu_05/01/04 = iconos.

### ch_menu (seleccion de personaje)
- ch_menu_00..08 (64x72) = retratos. ch_menu_18..21 (88x16) = nombres/labels cortos. (revisar al editar)

PNGs de referencia en `docs/ui_textures/` (`*_view.png` = compuesto sobre fondo oscuro, x3).

## Editabilidad — PROBADA
Tooling nuevo, sin dependencias (solo zlib stdlib):
- `tools/gim2png.py` — contenedor/GIM → PNG (INDEX4/8 + RGBA, unswizzle). Genera `_index.txt`.
- `tools/png2gim.py` — re-inserta imagen editada IN-PLACE (re-indexa a paleta original + re-swizzle).
  Mantiene cabecera/format/dims/paleta → **tamano de blob identico** → TOC intacto.

**Round-trip a nivel indice: byte-identico en 100%** (bt_menu 17/17, cm_menu 29/29, ch_menu 22/22, 0 fail).
El swizzle PSP 16x8 invierte exacto. (Nota: re-indexar desde RGBA puede cambiar indices cuando la
paleta tiene colores duplicados — 6/16 en estas texturas — sin cambio visual; para xdelta minimo,
editar a nivel de indices/paleta, no RGBA.)

## Restriccion de traduccion (clave)
El codigo del menu referencia cada palabra por rectangulo UV fijo dentro de la textura.
**Cada palabra ES traducida debe caber en el ancho del slot original** (no se puede crecer sin
reprogramar UVs en EBOOT). Misma filosofia que el texto: comprimir.

Mapeo propuesto (≤ ancho original, fuente del juego):
Command→Orden · Skill→Tecn · Item→Obj · Equip→Equipo · Persona→Persona · Status→Estado ·
Battle→Combate · System→Sistema · Attack→Atac · Defense→Def · Evade→Esq · Magic Atk→Mag Atk ·
Magic Def→Mag Def · Weapon→Arma · Armor→Armadura · On→Si · Off→No · Move→Mover · Auto→Auto ·
Angry→Furia · Happy→Feliz · Eager→Ansia · Scared→Miedo.
(Equip/Persona/Battle/System mas anchos: validar pixel-a-pixel; si no caben, abreviar.)

## Workflow para la fase grafica (cuando se apruebe)
1. `python3 tools/gim2png.py <bin> <outdir>` → editar el PNG de cada textura con texto
   (redibujar glifos ES dentro del bounding box de cada palabra, respetando ancho).
2. `tools/png2gim.py` re-inserta cada blob editado en su offset (tamano identico).
3. Reempaquetar el .bin (TOC sin cambios), recolocar en la copia del ISO.
4. Verificar MD5 original `03ee31f32bcd3bb697de347fba4493d9` intacto → regenerar xdelta → round-trip.

Pendiente de construir para esa fase: editor de glifos (o fuente bitmap ES) + el paso de
reempaquetado .bin→ISO (analogo a `build_patch.py` pero para offsets de bin completos).
