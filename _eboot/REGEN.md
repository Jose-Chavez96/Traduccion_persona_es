# EBOOT translation pipeline (durable)

Decrypted EBOOT lives in eboot_dec.elf (tag 0xD91613F0, type2). Regenerate from ISO:
  ./pspdecrypt -o eboot_dec.elf <EBOOT.BIN extracted from ISO @0x1245184 size 3838272>
(pspdecrypt binary here; source built from github.com/John-K/pspdecrypt)

## Translate loop (main thread):
1. Inventory: tools/eboot_strings2.py eboot_dec.elf eb_inventory.json  (2105 unique real strings)
2. Add ES into trans_master.json  {en: es}  (<= byte budget, no accents, preserve <FFxx> token count)
3. Regen chain (order matters): eboot_patch(trans_intro.json) -> eboot_patch(trans_blocks.json) -> eboot_apply(trans_records.json) -> eboot_translated.elf
   trans_intro=difficulty substrings; trans_blocks=multi-msg blocks split on <FF02><FF01> (EXPERIMENTAL: cmd menu+battle status, needs PPSSPP test for pointer safety); trans_records=full-record dict
4. Build ISO: pad ELF to 3838272 zeros, write @0x1245184 in ISO copy, xdelta. (see tools/patch_bin_iso uses basename;
   EBOOT has 2 entries — write SYSDIR one @1245184 by explicit offset.)
PPSSPP runs the decrypted ELF directly (no re-encryption). Original ISO MD5 03ee31f32bcd3bb697de347fba4493d9.

## Naming policy: keep proper nouns (Persona/demon/franchise-spell names: Pixie, Seiryuu, Zio, Megidola).
Translate: descriptions, status, menus, generic locations, descriptive item/skill names, dialogue.
