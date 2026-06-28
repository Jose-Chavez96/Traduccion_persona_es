# Translator brief — Persona PSP e1 (Snow Queen quest), EN -> ES latino

You translate one slice of English game dialogue into Latin-American Spanish.
You do NOT touch `translated_text/e1.json`. You only produce a validated map file.

## Hard rules (validator enforces, but get them right first time)
1. **No accents / no ñ / no ¿ ¡**. Use plain vowels, `n` for ñ, `?`/`!` only at END.
   Banned chars: á é í ó ú ñ ü ¿ ¡ " « » … —  (the font cannot encode them; encode() will reject).
2. **Tokens `<....>` are LITERAL**: never translate/move/add/remove. The set AND count of
   tokens in your translation must match the original exactly. This includes:
   - `<FF03>` = line break — if original has 3, you must have 3, in equivalent spots.
   - `<FF02><FF01>` / `<FF02><FF04>` / `<FF02><FF0E>` = page breaks (pairs, don't split).
   - `<FF1B>Name<FF03>` = speaker label.  `<FF07>` = player name.
   - `<0028>..<0028>`, `<0056>word<0056>` (onomatopoeia, keep inner word), `<0044>`, `<0043>..<0044>`,
     `<FF18>..<FF18>` (item), `<FF05><nnnn>` (anim), card/menu codes — all literal.
3. **Byte budget**: encoded translation must be `<= bytes` (the slice gives each record's limit).
   English is verbose; Spanish usually fits. If over: drop pronombres (yo/tu), collapse spaces,
   short synonyms (instalaciones->salas), trim fillers (Whoa/Oh/Pero). 2 bytes = 1 char.
4. **Leading/trailing spaces in the original are part of the string — preserve them.**

## Glossary (use EXACTLY)
- Keep untranslated (names): Mark, Brown, Yukino, Maki, Nanjo, Elly, Reiji, Kandori, Philemon,
  Igor, Hypnos, Comet, Ayase, Yuka, Saeko (and "Ms! Saeko" stays "Ms! Saeko"), **Snow Queen**, Mask object name.
  Persona, SEBEC, Arcana. Spells: Agi, Bufu, Zio, Garu, Dia, Mudo, Hama... Onomatopoeia: Hahaha,
  Teeheehee, Gyahahaha, Whoa (keep), etc. Demon types: preta, slime, yaksa, gaki, kodama, zombie.
- Translate generic speaker labels to SHORT latino (keep label short to avoid overflow):
  Clerk->Mozo, Gambler->Apostador, Gossip->Chismosa, **Mask->Mascara**, Boy->Chico, Girl->Chica,
  Man->Hombre, Woman->Mujer, Old man->Viejo, Voice->Voz, Student->Estudiante.
- Terms: spell card->carta de hechizo, card->carta, demon->demonio, negotiate->negociar,
  negotiation->negociacion, life stone->piedra de vida, gem->gema, yen->yen, human->humano,
  soul->alma, full moon->luna llena, incense->incienso, rank->rango, Velvet Room->Sala Aterciopelada,
  St. Hermelin->St! Hermelin (keep as in source, do NOT expand), Mikage-cho->Mikage-cho.
- Register: rude demon = rude/informal; keep it natural latino, not Spain (no vosotros/tio/vale/flipar).

## SOUP records (garbage runs)
Some originals contain long runs of layout/sprite tokens+hex (sprite soup). Do NOT retype them.
For those, use `repl(id,(en,es),...)` which splices ONLY the readable English dialogue substrings
over the ORIGINAL (tokens/padding/soup auto-preserved). Pick short, UNIQUE English substrings as keys.
For clean records (no big garbage run) use `put(id, full_string)` with the entire translated string.

## How to emit (exact workflow)
1. Read your slice file (given path): list of `{id, bytes, orig}`.
2. Write a python file `<slice_dir>/e1_<name>.py`:
   ```
   import sys; sys.path.insert(0,"/home/josechavez/persona_es/scripts")
   from wf_chunk_e1 import put,repl,dump
   put("e1_00053", "....")
   repl("e1_00060", ("English bit","Trozo espanol"), ...)   # for soup records
   ...
   dump("/home/josechavez/persona_es/translated_text/_wfmaps/<name>.json")
   ```
3. Run it: `python3 <that file>` — writes the map json.
4. Validate: `python3 /home/josechavez/persona_es/scripts/wf_validate_e1.py <map.json>`
5. Fix every OVER/TOKENS/ENCODE line and re-run until output is `OK <n> / FAIL 0` for ALL records in your slice.
6. Return: the map json path, count OK, and any record you could not fit (should be none).

Translate every record in your slice. Do not skip. Quality + exact tokens + fit are all required.
