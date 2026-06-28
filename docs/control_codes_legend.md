# Leyenda de codificación y códigos de control — Persona PSP

## Codec de texto

Cada carácter = **u16 big-endian**. Dos segmentos lineales:

| ASCII | Rango u16 | Offset |
|-------|-----------|--------|
| `0x21`–`0x5F` (símbolos, dígitos, MAYÚSCULAS) | `0x00C0`–`0x00FE` | `+0x9F` |
| `0x60`–`0x7A` (minúsculas) | `0x0100`–`0x011A` | `+0xA0` |
| espacio | `0x0000` | — |

El gap de 1 (0x9F vs 0xA0) evita que un glifo caiga en `0xFFxx` (zona de control).

## Puntuación (código raw propio, NO sigue el offset)

| u16 | Carácter |
|-----|----------|
| `0x0003` | `,` |
| `0x0004` | `!` |
| `0x0008` | `?` |
| `0x0009` | `.` |
| `0x0026` | `'` (apóstrofo) |
| `0x003C` | `-` (guion) |

Estas se decodifican como caracteres reales (el traductor escribe `,` `!` `?` `.` `'` `-` con normalidad; el codec las re-codifica a su byte correcto).

## Tokens de control `<....>` — LITERALES, NO TOCAR (regla 5)

Aparecen como `<FFxx>` (control, 1 word) o `<xxxx>` (dato crudo no mapeado). **Deben conservarse exactos y en el mismo orden** en la traducción. El reinserter rechaza cualquier registro cuyo conjunto de tokens cambie.

Códigos de control más frecuentes (ver `extracted_text/control_codes.json` para el catálogo completo, 189 distintos):

| Token | Frecuencia aprox. | Función deducida |
|-------|-------------------|------------------|
| `<FFFF>` | 521k | relleno / terminador de tabla (zonas no-texto) |
| `<FF00>` | 142k | relleno / fin |
| `<FF03>` | 40k | **salto de línea** dentro del cuadro de diálogo |
| `<FF02>` | 18k | control de cuadro de mensaje (avance/cierre) |
| `<FF1B>` | 15k | **inicio de etiqueta de nombre** (precede al nombre del hablante) |
| `<FFF5>` | 15k | control de diálogo (pausa/fin de bloque) |
| `<FF04>`, `<FF01>` | ~10–18k | control de cuadro (variantes de avance) |
| `<FF07>` | — | **variable: nombre del jugador** (ej. `Cheese it, <FF07>.`) |
| `<FFEB>` | — | precede nombre/etiqueta en negociación |

> Las funciones exactas se confirman observando en PPSSPP (Fase 8). Mientras tanto, **se preservan literalmente**.

## Ejemplos verificados

```
<FF02><FF04><0044> Karma Pride has no intention of<FF03>negotiating with humans.<FFF5>
 You're on!<FF02><FF04><FF1B>Mark<FF03>I'll bet you an all-you-can-eat dinner...
<FF02><FF01><FF1B>Yukino<FF03>Tch
```

Aquí `<FF1B>Mark` / `<FF1B>Yukino` = etiqueta de nombre del hablante; `<FF03>` = salto de línea; `<FF07>` = nombre del jugador.
