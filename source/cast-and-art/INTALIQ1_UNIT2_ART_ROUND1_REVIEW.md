# Unit 2 art — review of round 1 (package `intaliq_unit2_art_round1.zip`, reviewed 2026-10-01)

**Mechanical checks: all passed.** 69 of 69 slots present, named correctly, PNG, right pixel sizes, pure white backgrounds, no transparency, no text, no duplicate files, every `delivered` field filled, 8 character sheets present. The style is right: stick figure, black line, flat colour on clothing only. Version A frames differ from Story 1 only in the changed object (pixel-checked). This is a good base; round 2 is corrections only.

**Rule for round 2:** redo only the slot ids listed below. Every other slot stays **byte-identical** to round 1. Return the full package again (`assets/art/` + `art_manifest_unit2.json`). Where one fix cascades into several files (the cat's tail, Khadija's plaits), apply it identically in every file listed so the character stays the same drawing everywhere.

## A · Fixes that cascade across files

**A1 — Khadija's marker.** Her plaits are drawn as four short ticks beside the head; they read as whiskers (the same mark as the cat's) and not as hair. The marker is **two plaits, one each side, hanging from the head down to shoulder level**, as her own sheet states. Redraw in: `av-khadija`, `av-khadija-happy`, `av-khadija-talk`, `sheets/khadija.png`, `u2-s2-5`, `u2-s2-6`, `u2-vb-2`, `u2-ph-07`. (The tiny figure inside `obj-photo` already hangs to the shoulder — leave the photo files alone.)

**A2 — The cat's tail.** The curled tail is a filled disc as large as the body; at strip size it reads as a ball. Draw the tail as a **curled line** (an open spiral or hook), thinner than the body. Redraw in: `av-qitt`, `av-qitt-talk`, `sheets/qitt.png`, `u2-s1-7`, `u2-s1-8`, `u2-va-7`, `u2-ph-17`. Keep `u2-va-7` identical to the new `u2-s1-7` except that the cat sits on the book.

**A3 — Hands.** The hand holding the key / the photo is a many-fingered claw. House style: the arm is a tube that **ends in a small circle**, and the object sits in that circle. Redraw in: `u2-s1-3`, `u2-ph-09`, `u2-ph-19`.

**A4 — Maha's topknot** floats detached above the head. Attach it: a small tie sitting on top of the head outline. Redraw in: `av-maha`, `sheets/maha.png`, `u2-s1-5`.

## B · Single-frame fixes

- `u2-s1-4` — Karim must be **holding the key up** in his free hand, legible at strip size; right now his hand is on the bag and the key is a speck. Zayd and his small bag are fine.
- `u2-s1-5` — same key-up fix for Karim. The book on the floor: the key's **bow must peep from under the book's bottom edge**, not sit on top of it (the phrase is *under the book*). Plus A4.
- `u2-s1-6` — the key must be **hanging on the door itself**, visible on the door panel; Omar points at it; Karim **points at his own bag** (not holding it up). At present no key is visible on the door.
- `u2-s2-5` — Khadija is drawn floating above the house roof. She must stand **in the open doorway** of the house, feet at floor-line level. Plus A1.
- `u2-vb-3` — Rana's bob is an outline here; everywhere else it is the filled dark bob. Match `av-rana`.
- `u2-vb-5`, `u2-vb-6` — "home" is a bare door; Razanne's home in `u2-s2-4` is the **house** (door + roof line). Use the house, with the bird on its door.
- `u2-ph-03` — the key on the door is too small to read at 64 × 54 px. Enlarge it to about a third of the door's width.
- `u2-ph-04` — bow peeps from **under** the book (as in `u2-s1-5`).
- `u2-ph-08` — the arrow must be a **curved return arrow** (a U-turn), not a caret; it should read as *comes back*.

## C · Accepted as delivered (do not touch)

`u2-s1-1`, `u2-s1-2`, `u2-s2-1`, `u2-s2-2`, `u2-s2-3`, `u2-s2-4`, `u2-va-2`, `u2-vb-1`, `u2-vb-4`, `u2-ph-01`, `u2-ph-02`, `u2-ph-05`, `u2-ph-06`, `u2-ph-10` to `u2-ph-16`, `u2-ph-18`, all `obj-*`, `av-karim` ×3, `av-zayd`, `av-omar` ×2, `av-razan` ×5, `av-rana` ×2, `fig-walk`, and the sheets for karim, zayd, omar, razan, rana.

Round 2 = 27 files redrawn, 50 unchanged.
