# Reporte de fuente y caracteres especiales (Fase 5)

## ¿Soporta el juego á é í ó ú ñ ¿ ¡?

**Casi con certeza NO.** La versión europea de Persona PSP es inglés-only. El codec usa
índices de glifo fijos: MAYÚS/símbolos en `0x00C0–0x00FE`, minúsculas en `0x0100–0x011A`.
El rango **`0x011B`–`0x01FF` está libre** y es el candidato natural para glifos nuevos
(á é í ó ú ñ ¿ ¡). No hay glifos acentuados en el set actual.

> No se modificó ningún archivo en esta fase (regla 8).

## Archivo de fuente — candidatos

No existe un archivo llamado `*font*`/`*fnt*`. La fuente es una imagen **MIG** (formato gráfico de Atlus). Candidatos:

| Archivo | Tamaño | Por qué |
|---------|--------|---------|
| `usrdir/datapack.bin` | 75 KB | **Candidato principal.** Pack global pequeño en la raíz de usrdir (se carga siempre). Contiene 3 imágenes MIG (`MIG.00.1PSP`, sub-header tipo `0x0010`). Tamaño típico de hoja de fuente. |
| `usrdir/pack/sys.bin` | 318 KB | Sistema; contiene varias MIG. Posible fuente de menús. |
| `usrdir/pack/title/title.bin` | 1.25 MB | Fuentes decorativas de título. |

Para confirmar cuál es la fuente del texto hay que **renderizar las MIG** (decodificar formato MIG → PNG) y ver la rejilla de glifos. Herramienta pendiente: decodificador MIG (no incluido aún).

## Estrategia recomendada (en orden)

1. **Traducir SIN acentos primero** (ya aplicado en el set demo: "Esta todo bien", "la enfermeria", "demoniaco").
   - Ventaja: 0 edición de fuente, parche funciona ya. Español latino legible.
   - Es la base segura para validar todo el flujo en PPSSPP.
2. **Editar la tabla/fuente para añadir acentos** (fase futura):
   - Decodificar la MIG de `datapack.bin`, localizar la rejilla de glifos.
   - Dibujar á é í ó ú ñ ¿ ¡ en slots libres (`0x011B+`) o reemplazar glifos no usados
     (ej. caracteres ASCII poco frecuentes en español).
   - Extender el codec: mapear esos chars a los nuevos índices.
3. **Reemplazar caracteres poco usados**: si no hay slots, sacrificar glifos como `~` `^` `` ` `` `{` `}` que no se usan en diálogo y mapear acentos ahí.

## Conclusión

La traducción puede completarse YA en español sin acentos (calidad aceptable, latino natural).
Los acentos requieren editar la fuente MIG de `datapack.bin` — viable pero es trabajo gráfico
adicional que se aborda después de validar el texto base en el juego.
