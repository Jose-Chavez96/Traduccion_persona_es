# Guía de estilo — Traducción Persona PSP (ES latino)

Reglas OBLIGATORIAS para todos los agentes traductores. Consistencia total.

## 1. Variante e idioma
- **Español latino neutro** (no de España). Apto para audiencia LATAM amplia.
- Tono natural, NO calcado del inglés. Reescribir, no traducir palabra por palabra.

## 2. SIN acentos ni caracteres especiales
La fuente base no tiene glifos para `á é í ó ú ñ ¿ ¡`. **Prohibido usarlos.**
- "explicación" → `explicacion`, "niño" → `nino`, "¿qué?" → `que.?`, "está" → `esta`.
- Caracteres permitidos: `A-Z a-z 0-9 espacio` y puntuación `, . ! ? ' -`.
- Para preguntas: NO usar `¿`. Usar el código del juego: la pregunta termina en `.?`
  (el juego ya trae `?` como `.?` en muchos casos; respetar el patrón del original).

## 3. Tokens de control `<....>` — INTOCABLES
- Copiar EXACTOS, mismo número y mismo orden que el original. Nunca traducir, mover ni borrar.
- `<FF03>` = salto de línea. `<FF1B>` = etiqueta de nombre del hablante. `<FF07>` = nombre del jugador.
- Texto entre dos `<0056>` (ej. `<0056>yip<0056>`) son onomatopeyas: mantener la palabra interna tal cual.
- Si el original tiene 3 `<FF03>`, tu traducción debe tener exactamente 3 `<FF03>` en posiciones equivalentes.

## 4. Longitud máxima
- Cada registro tiene `limite_chars`. La traducción debe caber: `nº de caracteres visibles + nº de tokens ≤ limite_chars`.
- Cada token `<....>` cuenta como **1** unidad. Cada letra/espacio/signo cuenta como **1**.
- Si no cabe: **acortar** preservando el sentido y marcar `shortened: true`. NO resumir diálogo clave; recortar relleno.
- Preferir frases concisas. El español suele ser más largo que el inglés: economizar.

## 5. Espacios y bordes
- Respetar los espacios iniciales/finales del original (muchas líneas empiezan con ` ` o con un token).
  Si el original empieza con ` ` o `<FFEF>`, la traducción también.

## 6. Tono por tipo de demonio (negociación)
- Demonios groseros/punk (gaki/preta): jerga, "compa", "men", "tarado", "Bah".
- Demonios femeninos coquetos (zombie girl, etc.): tono provocador pero natural.
- Demonios formales/nobles (tensi/angel): registro elevado, "vos" NO; usar "tu" cortés.
- Demonios infantiles (kodama/kokuri): habla simple, exclamaciones.
- Mantener tartamudeos y repeticiones estilizadas del original (ej. "You-you" → "Tu-tu", "s-s-scary" → "m-m-miedo").

## 7. Nombres propios y términos
- Usar SIEMPRE `glossary.json`. Nombres de personajes, demonios, Personas y arcanas según el glosario.
- Onomatopeyas y nombres de hechizos: mantener como en el glosario (no traducir Gyahahaha, Agi, Bufu, etc.).

## 8. Puntuación del juego
- Apóstrofo `'`, guion `-`, coma `,`, punto `.`, `!`, `?` están soportados; usarlos con normalidad.
- No introducir comillas `"` ni otros signos no soportados.
