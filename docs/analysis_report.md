# Persona PSP (Europe) — Reporte de análisis (Fase 1)

> **Fase 1 = solo análisis.** No se modificó ningún archivo del juego. Acceso de solo lectura sobre el ISO montado.

## 1. Material de origen detectado

| Dato | Valor |
|------|-------|
| Archivo | `Shin Megami Tensei - Persona (Europe) (PSP) (PSN).iso` |
| Tipo | ISO 9660, etiqueta de volumen `PERSONA` |
| Tamaño | 821 788 672 bytes (~822 MB) |
| MD5 | `03ee31f32bcd3bb697de347fba4493d9` |
| Formato | ISO completo de UMD/PSP (NO es CSO, NO es carpeta extraída) |
| Juego | Shin Megami Tensei: Persona PSP (remake de Persona 1), versión europea → **texto base en INGLÉS** |

Montado solo-lectura en `/tmp/persona_mnt` (loop, ro). Estructura PSP estándar:

```
psp_game/
  param.sfo, icon0.png, icon1.pmf, pic0.png, pic1.png
  sysdir/   eboot.bin (PRX cifrado), boot.bin (vacío), opnssmp.bin, update/
  usrdir/
    datapack.bin
    movie/   mv00..mv2d.pmf   (vídeos — NO texto)
    pack/    <-- aquí está todo el contenido del juego
```

## 2. Formato de contenedores

Los `.bin` dentro de `pack/` son **archivos contenedor** con cabecera uniforme:

```
offset 0x00 : u32 LE  = número de entradas (count)
offset 0x04 : u32 LE[] = tabla de offsets a cada sub-archivo
luego       : sub-archivos, muchos con magic "MIG.00.1PSP" (formato gráfico de Atlus)
```

- **Hay punteros**: la tabla de offsets inicial ES una tabla de punteros. Cualquier cambio de tamaño de un sub-archivo obliga a recalcular esos offsets.
- Sub-archivos `MIG.00.1PSP` = texturas/tiles/fuentes (gráficos), no texto.

## 3. Codificación del texto (RESUELTA)

El texto **no** es ASCII plano, **no** es Shift-JIS, **no** está comprimido. Usa una **codificación custom de 16 bits por carácter, big-endian**:

```
código (u16 BE) = valor_ASCII + 0xA0
  espacio        = 0x0000
  letras/símbolos= 0x00A1 .. 0x017A   (ASCII 0x01..0x7A desplazado +0xA0)
  códigos control= 0xFFxx  (saltos, fin de línea, pausas, color, etc.)
```

**Verificado**: decodificado en `talk/etc.bin` →
`"…has no intention of negotiating with humans"` y `"intention of"`, `"of"`, `"has no"`, etc.
La regla `ascii+0xA0` da letras correctas de forma consistente. Es esencialmente un índice de glifo de fuente (deja 0x00–0x9F libre para bytes de control / medio-ancho).

Implicación: extracción y reinserción **muy viables**. El reto real son los **punteros** y los **códigos de control 0xFFxx** (hay que preservarlos intactos — regla 5).

## 4. Archivos candidatos con texto (medido por densidad del patrón 16-bit)

| Prioridad | Archivo(s) | Tamaño | Contenido probable |
|-----------|-----------|--------|--------------------|
| ALTA | `pack/talk/*.bin` (33 arch.) | 26–132 KB c/u | Diálogo de negociación con demonios (texto confirmado, 44–65% densidad) |
| ALTA | `pack/e0.bin … e4.bin` | 1.1–2.4 MB | Scripts de evento = **diálogo de historia principal** (12–32% densidad) |
| ALTA | `pack/kage.bin` | 390 KB | Eventos/script (41% densidad) |
| MEDIA | `pack/sys.bin` | 318 KB | Mensajes de sistema + gráficos MIG mezclados |
| MEDIA | `pack/title/title.bin` | 1.25 MB | Pantalla título / menús |
| MEDIA | `pack/moon.bin` | 10 KB | Texto (fase lunar?) |
| MEDIA | `pack/name/na.bin` | 12 KB | Nombres |
| MEDIA | `pack/shop/shall.bin` | 266 KB | Tienda |
| MEDIA | `pack/perall.bin` | 1.6 MB | Datos de Personas (nombres/habilidades) — por confirmar |
| MEDIA | `pack/*_menu.bin`, `cmdan.bin`, `over.bin` | varios | Menús (combate, personaje, común) |
| BAJA | `pack/mes/mes_all.bin` | 68 MB | Pack gráfico MIG (entradas fijas 0x41000). Texto plano NO visible en cabecera — requiere scan profundo en Fase 2 |
| BAJA | `pack/dng/*` | varios | Datos de mazmorras (mayormente mapas, poco texto) |
| NULA | `movie/*.pmf` | grande | Vídeo, sin texto editable |

## 5. ¿Texto comprimido?

No detectado en los archivos de texto principales (`talk/*`, `e*.bin`). El texto está en claro con la codificación +0xA0. Los sub-archivos `MIG` son gráficos (posible compresión de imagen, irrelevante para traducción de texto).

## 6. Punteros

Sí, dos niveles:
1. **Tabla de offsets del contenedor** (cabecera de cada `.bin`) → apunta a cada sub-archivo.
2. Posibles **punteros internos** dentro de cada bloque de texto (por confirmar en Fase 2 al mapear delimitadores 0xFFxx / fin-de-string).

Si una traducción cambia la longitud en bytes, hay que recalcular el/los nivel(es) afectados. Estrategia segura inicial: **mantener longitud ≤ original** (relleno con espacios/padding) para evitar recálculo de punteros mientras se valida el flujo.

## 7. Riesgos técnicos

| Riesgo | Severidad | Nota |
|--------|-----------|------|
| Recálculo de punteros al cambiar longitudes | ALTO | Núcleo del proyecto. Empezar con traducciones de longitud ≤ original. |
| Códigos de control 0xFFxx mal interpretados | ALTO | Hay que catalogarlos antes de extraer; nunca tocarlos. |
| Fuente sin acentos (á é í ó ú ñ ¿ ¡) | MEDIO-ALTO | Fase 5. Falta localizar el archivo de fuente (glifos). Versión Europa probablemente solo inglés → sin glifos acentuados. |
| `eboot.bin` cifrado (PRX `~PSP`) | MEDIO | Si algún texto vive en el eboot, requiere descifrado (no necesario aún; texto está en `pack/`). |
| `mes_all.bin` 68MB estructura no resuelta | BAJO-MEDIO | Confirmar si guarda texto o solo gráficos antes de descartarlo. |
| Tamaño del backup (822 MB) | BAJO | Crear backup antes de Fase 4+. |

## 8. Próximo paso recomendado

**Fase 2 — extractor** sobre los candidatos de prioridad ALTA primero (`talk/*.bin`, `e0–e4.bin`, `kage.bin`):
1. Implementar decodificador `u16 BE → ASCII (−0xA0)` con preservación literal de códigos `0xFFxx` y `0x00xx`.
2. Mapear la estructura de sub-archivos / delimitadores de string para asignar `offset_inicio`/`offset_fin`.
3. Catalogar todos los códigos de control vistos (tabla de control) — entregable crítico.
4. Volcar a JSON + CSV en `extracted_text/` con los campos pedidos.
5. NO traducir todavía.

Antes de Fase 4 (reinserción): crear backup del ISO en `backups/` y confirmar el algoritmo de punteros.

---
*Generado en Fase 1. Sin cambios sobre archivos del juego. ISO original intacto.*
