export const meta = {
  name: 'persona-talk-translate-resumable',
  description: 'Traduce talk/* pendientes de Persona PSP a ES latino, write-through a disco persistente + checkpoints, reanudable',
  phases: [{ title: 'Traducir', detail: 'un agente por archivo talk pendiente; cada uno aplica y checkpointea al terminar' }],
}

const ROOT = '/home/josechavez/persona_es'
// args = [{name, n}, ...]  lista de pendientes calculada en vivo por el main thread.
// Tolera array directo o string JSON.
// Fallback embebido. Recalcular y editar al reanudar tras un corte.
// Estado 2026-06-14: faltan 6. Inserted incluye ...kouman/syoujo.
// 2026-06-14: talk_* + e2 + e3 COMPLETOS. Pendiente narrativo restante (orden critical-path):
const PENDIENTES_DEFAULT = [
  { name: 'e1', n: 1128 }, { name: 'e4', n: 1159 }, { name: 'e0', n: 1941 },
]
let _pend = args
if (typeof _pend === 'string') { try { _pend = JSON.parse(_pend) } catch (e) { _pend = null } }
if (_pend && !Array.isArray(_pend) && Array.isArray(_pend.pendientes)) _pend = _pend.pendientes
if (!Array.isArray(_pend) || !_pend.length) _pend = PENDIENTES_DEFAULT
const files = (Array.isArray(_pend) ? _pend : []).map(f => ({
  name: f.name,
  n: f.n,
  data: `${ROOT}/translated_text/${f.name}.json`,
  map: `${ROOT}/translated_text/_wfmaps/${f.name}_map.json`,
}))

if (!files.length) { log('No hay archivos pendientes. Nada que hacer.'); return { archivos: 0 } }
log(`Pendientes: ${files.length} archivos, ${files.reduce((a, f) => a + f.n, 0)} strings`)

const SUMMARY = {
  type: 'object',
  properties: {
    file: { type: 'string' },
    estado: { type: 'string' },
    traducido: { type: 'integer' },
    shortened: { type: 'integer' },
    fallido: { type: 'integer' },
    por_traducir: { type: 'integer' },
    notes: { type: 'string' },
  },
  required: ['file', 'estado', 'traducido', 'shortened', 'fallido', 'por_traducir'],
  additionalProperties: false,
}

const RULES = `
REGLAS OBLIGATORIAS:
1. Lee PRIMERO estos archivos del repo:
   - ${ROOT}/glossary.json            (terminologia fija OBLIGATORIA)
   - ${ROOT}/docs/style_guide.md
   - ${ROOT}/docs/banned_translations.md
2. Espanol LATINO neutro. SIN acentos ni n-tilde ni signos de apertura. Solo: A-Za-z0-9 espacio y , . ! ? ' -
3. Tokens <....> INTOCABLES: copia exactos, mismo numero y mismo orden que el original. No traducir/mover/borrar.
   - <FF03>=salto linea, <FF1B>=etiqueta nombre, <FF07>=nombre jugador.
   - Palabra dentro de <0056>palabra<0056> es onomatopeya: dejala igual.
4. LONGITUD: (caracteres visibles + numero de tokens) <= limite_chars. Cada token cuenta 1, cada letra/espacio/signo cuenta 1.
   Si NO cabe: acorta manteniendo el sentido y marca shortened=true. Recorta relleno, no dialogo clave.
5. Respeta los espacios/tokens iniciales y finales del original.
6. Usa el glosario EXACTO. Mantiene sin traducir: nombres propios, nombres de Persona/demonios, hechizos (Agi, Bufu, Zio, Garu, Dia, Mudo, Hama...), onomatopeyas (Gyahahaha, Heeheehee, yip, ring, crackle, splat...), "Persona", "Arcana".
7. Manten el tono del demonio (grosero/coqueto/noble/infantil) y los tartamudeos estilizados (You-you -> Tu-tu).
`

const results = await pipeline(
  files,
  // Stage 1: traducir + escribir mapa persistente + aplicar write-through + checkpoint
  (f) => agent(
    `Traduces UN archivo de dialogo de demonios del juego Persona PSP a espanol latino.
${RULES}

ARCHIVO DE DATOS: ${f.data}
Es un array JSON de registros. Traduce SOLO los que tengan "estado":"por_traducir" (aprox ${f.n} registros).
Cada registro tiene: id, limite_chars, tokens_protegidos, texto_original.

PASOS (en este orden EXACTO):
1. Lee los 3 archivos compartidos y el archivo de datos.
2. Traduce cada registro por_traducir cumpliendo TODAS las reglas. Cuenta la longitud con cuidado.
3. ESCRIBE el mapa como JSON en ESTA ruta persistente (no /tmp):
   ${f.map}
   Forma EXACTA: { "<id>": {"t": "<traduccion>", "shortened": true|false}, ... }
   Incluye TODOS los ids por_traducir. No incluyas otros.
4. APLICA write-through inmediato ejecutando exactamente:
   cd ${ROOT} && python3 scripts/wf_apply_one.py ${f.name} ${f.map}
   Ese script fusiona a translated_text/${f.name}.json, valida (tokens+longitud) y escribe
   docs/checkpoints/${f.name}.json. Lee su salida JSON.
5. Si el script reporta "fallido">0, CORRIGE esos ids en el mapa (acorta mas / arregla tokens) y
   RE-EJECUTA el paso 4 hasta que fallido=0 o sea imposible. No dejes fallidos por descuido.
6. Devuelve el resumen estructurado usando los numeros del checkpoint final (file, estado, traducido,
   shortened, fallido, por_traducir, notes).

IMPORTANTE: la calidad y consistencia con el glosario son criticas. No inventes tokens. No uses acentos.
El paso 4 PERSISTE tu trabajo: si lo ejecutas, tu avance sobrevive aunque la sesion se corte.`,
    { label: `tr:${f.name}`, phase: 'Traducir', agentType: 'general-purpose', schema: SUMMARY }
  ).catch(() => null),
)

const ok = results.filter(Boolean)
return {
  archivos: ok.length,
  validated: ok.filter(r => r.estado === 'validated').length,
  con_fallidos: ok.filter(r => (r.fallido || 0) > 0).map(r => r.file),
  total_traducido: ok.reduce((a, r) => a + (r.traducido || 0), 0),
  total_shortened: ok.reduce((a, r) => a + (r.shortened || 0), 0),
  total_fallido: ok.reduce((a, r) => a + (r.fallido || 0), 0),
  detalle: ok,
}
