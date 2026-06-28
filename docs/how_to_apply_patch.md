# Cómo aplicar el parche de traducción

El parche `patches/persona_spanish_patch.xdelta` contiene **solo la diferencia binaria**
entre el ISO original y el ISO traducido. No incluye ningún archivo con copyright.
Necesitas tu **propia copia legal** del ISO original.

## Requisitos

- Tu ISO original de *SMT: Persona PSP (Europe)*.
  - MD5 esperado: `03ee31f32bcd3bb697de347fba4493d9`
- `xdelta3` instalado.
  - Linux: `sudo apt install xdelta3`
  - Windows: descargar `xdelta3.exe` (xdelta GitHub releases).

## Verificar tu ISO (recomendado)

```bash
md5sum "Shin Megami Tensei - Persona (Europe) (PSP) (PSN).iso"
# debe dar: 03ee31f32bcd3bb697de347fba4493d9
```

Si el MD5 no coincide, tu ISO es otra versión y el parche no aplicará correctamente.

## Aplicar el parche

```bash
xdelta3 -d -s "persona_original.iso" persona_spanish_patch.xdelta "persona_es.iso"
```

- `-d` = decodificar (aplicar)
- `-s` = archivo fuente (tu ISO original, intacto)
- salida = `persona_es.iso` (ISO traducido)

En Windows también puedes usar **xdelta UI** (arrastrar el .xdelta y el ISO original).

## Jugar

Carga `persona_es.iso` en **PPSSPP** (emulador) o en una PSP con CFW.
El ISO original no se modifica en ningún momento.

## Resultado esperado

- MD5 del ISO traducido: `eb6fe17d687c4a9321eb78a500ff12b7` *(con el set de traducción actual; cambiará al ampliar la traducción)*.
- Tamaño idéntico al original (la traducción reemplaza bytes in-place, no cambia punteros).
