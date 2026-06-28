# Checklist de pruebas en PPSSPP (Fase 8)

Cargar `rebuilt/persona_es_patched.iso` (o el ISO resultante de aplicar el parche) en PPSSPP.
Marcar cada punto. Anotar cualquier texto cortado, carácter raro o cuelgue.

## Arranque y menús
- [ ] 1. **Arranque del juego** — llega a la intro sin cuelgue.
- [ ] 2. **Menú principal / título** — opciones visibles y legibles.
- [ ] 3. **Nueva partida** — inicia sin error.

## Diálogo
- [ ] 4. **Diálogos iniciales** — texto en español, saltos de línea (`<FF03>`) correctos.
- [ ] 5. **Nombre del jugador** (`<FF07>`) — aparece bien insertado en las frases.
- [ ] 6. **Etiquetas de hablante** (`<FF1B>nombre`) — el nombre se muestra correcto.

## Menús de sistema
- [ ] 7. **Menú de objetos** — nombres y descripciones no se salen del cuadro.
- [ ] 8. **Menú de habilidades / Personas** — texto encaja.
- [ ] 9. **Tienda** (`shall.bin`) — precios y nombres OK.

## Combate y negociación
- [ ] 10. **Combate** — mensajes de turno/daño OK.
- [ ] 11. **Negociación con demonios** (`talk/*.bin`) — diálogo traducido, sin corrupción.

## Guardado y caracteres
- [ ] 12. **Guardar / cargar partida** — funciona, sin corromper el save.
- [ ] 13. **Tildes y ñ** — si aún no se editó la fuente: confirmar que el texto sin acentos
        se lee bien. Tras editar fuente (Fase 5): verificar á é í ó ú ñ ¿ ¡.
- [ ] 14. **Textos cortados / desbordados** — revisar cuadros donde la traducción llene el límite.

## Notas de regresión
- [ ] 15. Comparar pantallas clave contra el original en inglés (mismo punto de guardado)
        para detectar cualquier byte mal insertado.

---

### Cómo reportar un fallo
Anotar: pantalla, texto mostrado vs esperado, y si es posible el `id` del registro
(buscar el texto original en `translated_text/*.csv`). Eso permite corregir el
`texto_traducido` y regenerar el parche con `reinsert.py` + `build_patch.py`.
