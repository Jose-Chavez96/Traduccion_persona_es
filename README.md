# Persona (PSP) — Traducción al Español Latino

Parche de fan-traducción **inglés → español latino** de
**Shin Megami Tensei: Persona (Europe) (PSP) (PSN)** — el remake del Persona 1 original.

> **Hecho por `Quete_importa`.**
> Todo el proyecto fue creado en su totalidad con **Claude Opus 4.8** (Anthropic).
> Lo único que quería en la vida era **jugar Persona 1 en español**. Ya casi está.
> Si alguien puede terminar de refinarlo y, algún día, continuar con la traducción de **Persona 2**,
> les estaré eternamente agradecido. Este proyecto es libre: tómenlo, mejórenlo, compártanlo. 

---

##  Índice

1. [Qué es esto](#-qué-es-esto)
2. [Estado del proyecto](#-estado-del-proyecto)
3. [Cómo aplicar el parche](#-cómo-aplicar-el-parche-instrucciones-para-jugar)
4. [Cómo está hecho — pipeline técnico](#-cómo-está-hecho--pipeline-técnico)
5. [Filtros de seguridad y reglas de codificación](#-filtros-de-seguridad-y-reglas-de-codificación)
6. [Bugs encontrados y cómo se arreglaron](#-bugs-encontrados-y-cómo-se-arreglaron-lecciones-críticas)
7. [Qué falta / cómo continuar y refinar](#-qué-falta--cómo-continuar-y-refinar)
8. [Estructura del repositorio](#-estructura-del-repositorio)
9. [Glosario y política de nombres](#-glosario-y-política-de-nombres)
10. [Legal](#-legal)
11. [Créditos](#-créditos)

---

##  Qué es esto

Un **parche externo `.xdelta`** que, aplicado sobre una copia **legal** del ISO original, lo convierte
en un ISO con todo el diálogo de la historia en español latino.

**No se redistribuye el ISO ni ningún archivo original con copyright.** Lo que se publica aquí son:
- Los archivos de traducción (JSON con el texto traducido).
- Las herramientas (scripts Python) para extraer, traducir, validar y reinsertar.
- El parche binario de diferencias `patches/persona_es_full.xdelta`.

El parche contiene **únicamente las diferencias** entre el ISO original y el traducido — no contiene
datos originales del juego. Para usarlo necesitas **tu propia copia** del ISO.

### Juego objetivo

| Campo | Valor |
|---|---|
| Título | Shin Megami Tensei - Persona (Europe) (PSP) (PSN) |
| Plataforma | PSP (corre perfecto en **PPSSPP**, PC y Android) |
| **MD5 del ISO original (obligatorio)** | `03ee31f32bcd3bb697de347fba4493d9` |
| MD5 del ISO ya parcheado | `3a8ab147864b3bffb8f03c771e694967` |
| Tamaño del parche | `persona_es_full.xdelta` ≈ 2.26 MB |

 **Tu ISO DEBE tener el MD5 `03ee31f32bcd3bb697de347fba4493d9`.** Si no coincide (otra región,
otro dump), el parche **no aplicará**. Esta es la versión Europa de PSN.

---

##  Estado del proyecto

###  Completado (jugable de inicio a fin en español)

- **Diálogo de historia — 100%.** Los 37 archivos de texto del juego (`e0`–`e4` = arcos narrativos,
  `talk_*` = negociación con demonios). **13,906 / 13,924 registros traducidos** (los ~18 restantes son
  archivos vacíos/estructurales, sin texto). **0 diálogo real en inglés.**
- **EBOOT.BIN — texto de sistema y eventos.** Corpus separado del texto de historia.
  **662 registros + 14 substrings** traducidos: nombres y descripciones de ítems/habilidades,
  ubicaciones, mensajes de batalla, pools de negociación de demonios, tutoriales de Igor (fusión),
  ayuda del casino (blackjack/póker/dados/Code Breaker/tragamonedas), selector de dificultad,
  y diálogo de escenas de batalla. **0 diálogo de historia en inglés.**
- **Bugs críticos arreglados y verificados en hardware** (ver sección de bugs): crash al salir de la
  escuela, descuadre de la recepción del hospital, escena renderizada en la esquina, diálogos de NPC
  que abrían/cerraban de golpe.

###  Parcial / por refinar (no rompe el juego, pero se nota)

- **~570 registros de diálogo con desborde mínimo.** Son diálogos ya traducidos al español donde el
  texto en español se pasa por **muy poco** (mediana 3 caracteres, máximo 16) en **un** segmento.
  Renderizan en español, pero su bloque interno queda corrido unos bytes. **Solo 2** tienen riesgo
  visual real (ancla `<FFFF>`); los otros 568 son chatter de negociación de demonios y son
  prácticamente inofensivos. Ver [cómo continuar](#-qué-falta--cómo-continuar-y-refinar).

###  No hecho (intencionalmente fuera de alcance)

- **Texturas / UI gráfica.** Los menús (Attack/Guard, Yes/No, RESULT, entrada de nombre, iconos de
  humor de demonios) **no son texto: son sprites GIM pre-renderizados**. Existe el pipeline para
  editarlos (`tools/gim2png.py`, `tools/png2gim.py`, `tools/glyphfont.py` con la fuente del juego ya
  extraída) y un sprite de prueba editado, pero **se decidió no traducir la UI**. Quien quiera puede
  retomarlo (ver `docs/`).
- **Mensajes genéricos de campo no extraídos.** Ejemplo: `> The door is locked.` (mensaje genérico de
  examinar puertas/cofres) vive en una tabla aún no localizada. Las variantes específicas que sí están
  en el corpus ya están traducidas.
- **Intro Zhuangzi (mariposa) + disclaimer de Atlus.** Es texto de video/sprite, fuera de los corpus de
  texto. No localizado.
- **Nombres propios de franquicia** (Personas, demonios, hechizos, ítems icónicos) y **listas de
  afinidad elemental** se dejan en inglés **a propósito** (ver [política de nombres](#-glosario-y-política-de-nombres)).

---

##  Cómo aplicar el parche (instrucciones para jugar)

Necesitas: tu ISO original (MD5 `03ee31f32bcd3bb697de347fba4493d9`) y la herramienta **xdelta3**.

### 1. Verifica el MD5 de tu ISO

**Windows (PowerShell):**
```powershell
Get-FileHash -Algorithm MD5 "Persona.iso"
```
**Linux / macOS:**
```bash
md5sum "Persona.iso"      # Linux
md5 "Persona.iso"         # macOS
```
Debe dar exactamente `03ee31f32bcd3bb697de347fba4493d9`. Si no, tienes otra versión y el parche no sirve.

### 2. Aplica el parche con xdelta3

**Línea de comandos (todas las plataformas):**
```bash
xdelta3 -d -s "Persona.iso" "persona_es_full.xdelta" "Persona_ES.iso"
```
- `-d` = decodificar/aplicar
- `-s "Persona.iso"` = ISO original (source)
- siguiente = el parche
- último = el ISO de salida traducido

**Windows con interfaz gráfica:** usa **xdelta UI** (delta patcher). Selecciona el parche `.xdelta`,
luego el ISO original, y presiona *Apply Patch*.

### 3. Verifica el resultado (opcional pero recomendado)

```bash
md5sum "Persona_ES.iso"   # debe dar 3a8ab147864b3bffb8f03c771e694967
```

### 4. Juega

Carga `Persona_ES.iso` en **PPSSPP** (PC o Android). No requiere re-firmar ni descifrar nada.

>  **Tu ISO original queda intacto.** El parche genera un archivo nuevo; nunca modifica la fuente.

---

##  Cómo está hecho — pipeline técnico

El juego guarda su texto en dos lugares completamente distintos, con dos pipelines separados.

### A. Texto de historia (37 archivos `.bin` dentro del ISO)

```
ISO  →  extract.py        →  extracted_text/*.json   (texto original + offsets + raw_hex)
        [traducción]       →  translated_text/*.json  (texto_traducido, estado)
        reinsert.py        →  rebuilt/patch_records.json  (parches byte-exactos)
        build_patch.py     →  rebuilt/persona_es_patched.iso  (base con texto de historia)
```

Cada registro tiene: `texto_original`, `texto_traducido`, `longitud_original_bytes`, `raw_hex`,
`offset_inicio`, `estado` (`por_traducir` → `traducido`/`shortened`). El texto usa un **codec propio**
(`scripts/persona_codec.py`): cada carácter y cada token de control ocupa **2 bytes** (u16 big-endian;
ASCII desplazado, espacio = `0x0000`, control = `0xFFxx`).

### B. EBOOT.BIN (ejecutable — corpus separado)

```
EBOOT.BIN (@0x130000 en el ISO)  →  pspdecrypt  →  _eboot/eboot_dec.elf
        eboot_strings2.py  →  _eboot/eb_inventory.json   (4253 strings con off/rawlen/term)
        [traducción]        →  _eboot/trans_records.json  ({texto_original: texto_traducido})
                            +  _eboot/trans_intro.json    (14 substrings: dificultad)
        eboot_patch.py  (substrings)  →  eboot_apply.py (por offset)  →  eboot_translated.elf
```

### C. Unificación (el parche final)

```
tools/build_unified.py:
   base = rebuilt/persona_es_patched.iso  (texto de historia ya parcheado)
   + escribe eboot_translated.elf  @0x130000  (EBOOT traducido)
   + (opcional) capa de texturas _tex/edited/*.bin
   → rebuilt/persona_es_full.iso
   → xdelta3 (original → unificado)  →  patches/persona_es_full.xdelta
   → verifica MD5 original intacto + round-trip (aplica el parche y compara)
```

**`patches/persona_es_full.xdelta` es el único archivo que el usuario instala** (historia + EBOOT en uno).

### Método de traducción (chunk + reuse + validación)

Por archivo: extraer registros pendientes → reusar traducciones repetidas entre archivos
(`wf_reuse.py`) → traducir en lotes de ~22 registros → validar cada lote (tokens, bytes, codec) →
aplicar (`wf_apply_one.py`). Para registros con "soup" estructural (bloques de layout al final) se usa
**reemplazo por tramos** (`_textgap/repl.py`): se traducen solo los tramos de texto libre y se preservan
los tokens y la soup **byte por byte**.

---

##  Filtros de seguridad y reglas de codificación

Estas reglas **bloquean** cualquier traducción que rompería el juego. Son la parte más importante del
proyecto y cualquier contribuyente DEBE respetarlas.

1. **Preservar tokens de control.** Todo token `<FFxx>` / `<NNNN>` debe aparecer en la traducción
   **el mismo número de veces y en el mismo orden** que en el original. El validador rechaza si no.
2. **Presupuesto de bytes.** `encode(traducción) ≤ longitud_original_bytes`. Como cada carácter = 2
   bytes, el español (que suele ser más largo) debe **comprimirse**. No hay espacio para crecer.
3. **Sin acentos ni ñ.** La fuente del juego **no tiene** caracteres acentuados; el codec lanza error si
   se usan. Se escribe `nino`, `peleo`, `mas`, `corazon`. (Limitación de la fuente original.)
4. **Preservar el OFFSET ABSOLUTO de los tokens estructurales.** Esta es la regla que costó más sangre.
   Cuando la traducción es más corta que el original, **NO** se rellena al final: se rellena **cada
   tramo de texto** hasta la longitud de su tramo en inglés, de modo que cada token de ancla
   (`<NNNN>` punteros, `<FFFF>` soup de fondo) **quede en su byte exacto original**. El motor lee esos
   tokens a offset fijo; si se corren, la pantalla se descuadra o el juego crashea. Ver
   `scripts/reinsert.py` (`_align_per_run`, `_align_trailing_soup`).
5. **Nunca tocar el ISO original.** Todo se trabaja sobre copias; `build_unified.py` verifica el MD5
   original (`03ee31…`) en cada build y aborta si cambió.
6. **No redistribuir datos originales.** Salida pública = solo `.xdelta` + traducciones + scripts.
7. **Round-trip obligatorio.** Cada build aplica el parche recién generado sobre el original limpio y
   verifica que reproduce el ISO traducido exacto. Si falla, no se publica.

---

##  Bugs encontrados y cómo se arreglaron (lecciones críticas)

Estos son los errores que descubrimos jugando en hardware real y cómo se resolvieron. Léelos antes de
modificar cualquier cosa, porque es muy fácil reintroducirlos.

###  Crash "leaving school" (al salir de la escuela)
**Causa:** registros con datos estructurales (punteros) en la soup final; el español más corto rellenaba
al final → la soup se corría → el juego leía punteros a offset incorrecto → *Invalid Memory Access*.
**Fix:** rellenar preservando la longitud/offset (regla de seguridad #4). Verificado: crash eliminado.

###  Descuadre de la recepción del hospital (fondo negro + HUD al borde)
**Causa:** `reinsert.py` rellenaba con `0x0000` al **final** del registro; en registros con bloque de
soup `<FFFF>` que el motor lee a offset fijo, el texto español más corto desplazaba esa soup → el puntero
del fondo de la sala se leía corrido. **Fix:** anclar cada token de soup a su offset absoluto
(`_align_per_run`). Confirmado en hardware: descuadre eliminado, diálogo en español.

###  Escena renderizada en la esquina (EBOOT over-pad)
**Causa:** `eboot_apply` rellenaba cada string hasta `rawlen`, pero `rawlen` suele ser mayor que el
string real — los bytes extra son OTRAS strings / datos de render. Rellenar los borraba. **Fix:** rellenar
**solo** hasta `len(encode(original))`; nunca tocar bytes más allá del footprint real del string.

###  Diálogo de NPC que abre y cierra de golpe
**Causa:** mismo problema de offset pero con tokens `<NNNN>` no-FF (punteros de layout a offset fijo, no
recalculables). El gate inicial solo cubría soup `<FFFF>`. **Fix:** `_align_per_run` ahora ancla por
**todos** los tokens no-FF ∪ `<FFFF>`; el texto fluye entre anclas.(este no esta solucionado asi que unos dialogos de unos pj aun se abren y cieran de golpe )

###  Regresión de `trans_records.json` (diálogo de batalla en inglés)
**Causa:** un rebuild revirtió `_eboot/trans_records.json` de 619 → 512 entradas, perdiendo 107
traducciones de diálogo (escenas de batalla, tutoriales de Igor). **Fix:** los lotes de trabajo en
`_eboot/work/*.json` son la fuente recuperable; se re-fusionaron con `_eboot/work/batch_apply.py`.
**Lección:** si el conteo de `trans_records.json` baja, re-fusiona los batches de `_eboot/work/`.

---

##  Qué falta / cómo continuar y refinar

Orden sugerido de prioridad para quien quiera continuar:

### 1. Los ~570 registros con desborde mínimo (refinamiento fino)
- **Qué son:** diálogos ya en español donde un segmento se pasa por 3–16 caracteres, así que su bloque
  interno queda corrido unos bytes (cae al fallback de relleno-al-final de `reinsert.py`).
- **Riesgo real:** solo **2** registros con ancla `<FFFF>` tienen impacto visual; los otros 568 son
  chatter de demonios leído en secuencia (inofensivo).
- **Cómo arreglar (recomendado, 100% español):** acortar el segmento que desborda esos 3–16 caracteres
  (quitar un artículo, contraer una palabra). Al quedar `encode(ES_segmento) ≤ encode(EN_segmento)`,
  `_align_per_run` ancla todo y el desborde desaparece.
- **Alternativa (híbrido EN/ES, factible pero NO recomendada):** dejar **solo** el segmento que desborda
  en inglés (el original siempre cabe exacto). Funciona para los 570, pero mete una frase inglesa en
  medio del español; con desbordes tan chicos no vale la pena.
- **Cómo localizarlos:** un script que recorre `translated_text/*.json`, parte cada registro por tokens
  de ancla (no-FF ∪ `<FFFF>`) y marca los segmentos donde `encode(ES) > encode(EN)`.

### 2. Mensajes genéricos de campo no extraídos
Localizar la tabla de `> The door is locked.` y similares (probablemente en EBOOT no inventariado o un
`.bin` de mensajes de campo), extraerla y traducirla.

### 3. UI / texturas (opcional)
El pipeline existe (`tools/gim2png.py`, `png2gim.py`, `glyphfont.py` con la fuente del juego ya
extraída de `pack/sys.bin`). La parte difícil es el recorte UV por palabra: cada sprite debe verificarse
en PPSSPP. Ver `docs/` para el audit de texturas.

### 4. Pulido de traducción
El español es funcional y comprimido (sin acentos por la fuente). Un hablante nativo puede pulir tono,
naturalidad y consistencia de glosario. Respetar SIEMPRE los [filtros de seguridad](#-filtros-de-seguridad-y-reglas-de-codificación).

### 5.  Persona 2
Mi sueño. Persona 2 (Innocent Sin / Eternal Punishment) en PSP usa estructuras de texto similares. Las
herramientas y el método de este repo son un punto de partida directo. Si alguien lo retoma — gracias
infinitas.

---

## Estructura del repositorio

```
scripts/          Pipeline de texto de historia
  extract.py          extrae texto de los .bin → extracted_text/
  reinsert.py         reinserta traducción con anclaje de offset → patch_records.json
  build_patch.py      construye el ISO base con texto de historia
  persona_codec.py    codec del juego (encode/decode, 2 bytes por carácter)
  wf_*.py             utilidades de flujo (chunk, reuse, validate, apply, view)
tools/            Pipeline de EBOOT + texturas + unificación
  eboot_strings2.py   inventario de strings del EBOOT
  eboot_apply.py      aplica traducción al EBOOT por offset (seguro)
  eboot_patch.py      aplica substrings (dificultad)
  build_unified.py    une historia + EBOOT (+ texturas) → parche final .xdelta
  gim2png.py / png2gim.py / glyphfont.py   herramientas de texturas/fuente
extracted_text/   texto original extraído (JSON + CSV) — 37 archivos
translated_text/  texto traducido (la fuente de verdad de la traducción) — 37 archivos
_eboot/           trabajo de EBOOT
  eb_inventory.json   inventario (4253 strings)
  trans_records.json  traducciones por registro (662)
  trans_intro.json    substrings de dificultad (14)
  work/*.json         lotes de trabajo + batch_apply.py (fuente recuperable)
  REGEN.md            cómo regenerar el EBOOT traducido
_textgap/         herramientas de "huecos" de diálogo (repl.py por tramos)
_tex/             trabajo de texturas (fuente del juego, sprites)
_wfmaps/          mapas de reemplazo por chunk
patches/          persona_es_full.xdelta  ← EL PARCHE FINAL
rebuilt/          ISOs reconstruidos localmente (NO se publican)
docs/             reportes y auditorías
backups/          respaldo del ISO original (NO se publica)
```

> **Nota para publicar en git:** NO subas `rebuilt/*.iso` ni `backups/` (contienen datos originales con
> copyright). Sube scripts, `extracted_text/`, `translated_text/`, `_eboot/` (sin ELFs), `_textgap/`,
> `_wfmaps/`, `docs/` y `patches/persona_es_full.xdelta`. Añade un `.gitignore` para `*.iso`, `*.elf`,
> `*.bin`, `backups/`.

---

##  Glosario y política de nombres

**Se traducen:** descripciones, mensajes de sistema/batalla, menús, ubicaciones genéricas
(Class→Clase, Infirmary→Clínica/Clinica, Library→Biblioteca, Mikage Ruins→Ruinas Mikage), verbos/
respuestas de negociación, ayuda del casino, y **todo el diálogo**.

**Se dejan en inglés (decisión de diseño):**
- Nombres de Personas y demonios (Pixie, Alice, Cerberus, Nemesis…).
- Hechizos de la franquicia (Zio, Megido, Garudyne, Diarahan, Recarm…).
- Razas de demonios (Fiend, Jaki, Yoma, Femme…).
- Nombres propios de ítems icónicos (Snow Queen Mask, Spiegel Shield, Rosetta Stone…).
- Lugares de franquicia (Deva Yuga, Devil's Peak, SEBEC, Alaya Shrine, Dream World…).
- Listas de afinidad elemental (Electric, Nuclear, Gravity, Blast / "Force Weak"…).
- Nombres de personajes (Maki, Mark/Hidehiko, Nanjo, Yukino, Elly, Reiji, Kandori…).

**Etiquetas de hablante traducidas (ejemplos):** Principal→Director(a), Vice-Principal→Subdirector,
Student→Estudiante/Alumno, Nurse→Enfermera, Mr!/Ms!→Sr!/Sra!, Drama club member→Miembro de Drama,
Masked man/girl→Enmascarado/Enmascarada, compact→polvera.

El glosario completo y las decisiones por arco están documentados en `docs/`.

---

##  Legal

- Este es un proyecto de **fan-traducción sin fines de lucro**.
- **No se distribuye el juego.** El parche `.xdelta` contiene solo diferencias binarias; es inútil sin
  tu propia copia legal del ISO original(Giño Giño).
- Persona y Shin Megami Tensei son propiedad de **Atlus / SEGA**. Este proyecto no está afiliado ni
  respaldado por ellos.
- Debes **poseer una copia legal**(Giño giño) del juego para usar este parche.
- Se publica con la intención de que la comunidad lo continúe y mejore libremente.

---

## Créditos

- **Autor / dirección del proyecto:** `Quete_importa`
- **Traducción, ingeniería, herramientas y todo el código:** generado en su totalidad con
  **Claude Opus 4.8** (Anthropic).
- **Herramientas de terceros:** `xdelta3` (parcheo binario), `pspdecrypt` (descifrado del EBOOT,
  de github.com/John-K/pspdecrypt), `PPSSPP` (emulador para probar).

---

> *"Lo único que quería en la vida era jugar Persona 1 en español pero en vista que la comunidad se olvido de este juego intente hacerlo yo."* — `Quete_importa`
>
> Si llegaste hasta aquí y tienes ganas de seguirlo: el código es tuyo. Refínalo, corrige los ~570
> desbordes, traduce la UI si te animas, y si algún día haces Persona 2 en español… habrás cumplido un
> sueño que no era solo mío. Gracias. 


>posdata: lo testie hasta entrar a la fabrica abandonada despues de la invacion de los demonios tal vez haya mas errores adelante pero por el momento esta bien hasta este punto
