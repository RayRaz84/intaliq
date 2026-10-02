# Intaliq 1 — Art Package Specification (intake for externally produced art)

*Written 2026-10-01 under **SC-111** and runbook **TF-8**. This is the contract between the art tool (makes pictures) and the build (places them). The tool never edits `index.html` or any generated file; it delivers files under `assets/art/` named by the ids below, plus character sheets. The Editor wires them through an asset map that the build scripts consume. Style and content authority: Cast Bible §2 as amended by SC-111, and each unit's visual plan.*

---

## 1 · Division of labour (fixed)

| the art tool | the build (Editor) |
|---|---|
| draws every slot the manifest lists, one file per slot id | issues the manifest (ids, sizes, must-show / must-not-show) from the visual plan |
| keeps characters identical across frames; delivers a character sheet per named character | transcribes markers into the Cast Bible reservation table; runs the collision check |
| keeps every object to its single drawing | maps slot ids → engine `img` fields, Studio frames, phrase page, notebook N1/N4 (SC-100) |
| does **not** reuse one file for two different story moments | fixes the one legitimate reuse itself (Version A's six unchanged frames = Story 1's files) |
| does **not** draw anything without a slot id (no "hero", no covers, no extras) | re-runs QC, re-states the activity count (SC-050), bumps the Studio version, writes the production-record entry |
| does **not** touch Unit 3 until its slot list is issued (after Gate B freeze) | writes the Unit 3 visual plan after freeze and issues its manifest then |

## 2 · File format and size

- **Format: PNG (lossless) or SVG. Not JPG** — JPG softens black line on white into grey halos and noise, which fails the true-white rule (SC-037) and prints badly in greyscale. If the tool can only emit JPG, deliver at quality ≥ 95 and the build converts to PNG; prefer PNG at source.
- **Background: pure white #FFFFFF**, no transparency, no border drawn inside the image (the Studio draws the frame).
- **Story frames** (`*-s1-*`, `*-s2-*`, `*-va-*`, `*-vb-*`): the Studio slot is 118 × 98 px. Deliver **590 × 490 px** (5×, aspect 59 : 49). Prints at ~40 mm; check legibility *reduced*, not at full size.
- **Phrase pictures** (`*-ph-*`): slot 64 × 54 px. Deliver **512 × 432 px** (8×, aspect 32 : 27).
- **Faces / objects for the engine** (`av-*`, `obj-*`): square, **400 × 400 px**, figure or object centred with ~10 % margin.
- **Character sheets**: one PNG per named character, any size, showing every expression variant the unit's plan names, with the marker and the clothing colour written beside it (text is allowed on sheets, never inside slot images).

## 3 · Naming

```
assets/art/
  unit1/   u1-…            (slot ids from the Unit 1 manifest)
  unit2/   u2-s1-1.png … u2-s1-8.png     Story 1 strip
           u2-s2-1.png … u2-s2-6.png     Story 2 strip
           u2-va-2.png, u2-va-7.png      Version A — only the two changed frames
           u2-vb-1.png … u2-vb-6.png     Version B — six frames
           u2-ph-01.png … u2-ph-19.png   phrase page
  common/  obj-key.png obj-bag.png obj-bag-big.png obj-book.png obj-pen.png
           obj-door.png obj-house.png obj-photo.png
           av-karim.png av-karim-q.png av-karim-laugh.png
           av-zayd.png av-maha.png av-omar.png av-omar-happy.png
           av-razan.png av-razan-q.png av-razan-sad.png av-razan-happy.png av-razan-talk.png
           av-khadija.png av-khadija-happy.png av-khadija-talk.png
           av-rana.png av-rana-talk.png
           av-qitt.png av-qitt-talk.png
           fig-walk.png
  sheets/  karim.png zayd.png maha.png omar.png razan.png khadija.png rana.png qitt.png
  art_manifest.json      (returned filled: every id → the file delivered, plus any note)
```

Ids are the build's; the tool does not invent ids. A slot the tool cannot draw stays empty in the manifest with a note — never filled with a neighbour's file.

## 4 · Style (what every image obeys — Cast Bible §2 as amended by SC-111)

One stroke weight, uniform, rounded caps, no tapering, no hatching, no shading. Heads about a third of figure height, no neck; two-dot eyes, hooked nose, one mouth line carrying the expression; tube limbs. Near-empty space: a floor line, a doorframe, one object — no backgrounds, no perspective. **Black line on pure white; flat colour on clothing only** — teal #2F7D78, ochre #D3A344, coral #D97668 — never on faces, hair, props, animals or ground. No text, letters, numerals or glyph-like marks inside any slot image. Named characters have faces; generic action figures (`fig-walk`) do not. No hearts, no embrace, no romance-readable pairing (SC-027 · SC-036); children at doorways stand apart.

**Identity is one fixed marker per character, identical in every frame.** A clothing colour may be part of a character's identity only if it never changes between frames. The marker reservation table (Cast Bible) is the authority — no two characters share a marker, and a marker the table lists as taken is not given to anyone else.

## 5 · Content authority

Each frame's content is its row in the unit's visual plan: *who · objects · state* is what the frame shows; *must NOT show* is binding; nothing not listed is added. Expression variants appear only where a row names them. Objects are one drawing each (the found key and Karim's key are the *same* key — that is the story). Where the plan and this spec disagree on style, SC-111 governs; where they disagree on content, the plan governs.

## 6 · Acceptance (run by the Editor on every image before placement)

1. Line on white; colour on clothing only; background #FFFFFF.
2. One stroke weight; no shading.
3. No text or glyphs inside the image.
4. Every named character carries the marker on their sheet, identical across frames; the cat has ears + curled tail everywhere.
5. Every object matches its single drawing.
6. Frame content matches its row; nothing from *must not show* is visible; nothing extra.
7. Expression variants only where the row names them.
8. SC-027 / SC-036 clean.
9. Faceless generic figures for actions; faces on named characters.
10. Legible at 118 × 98 (frames) and 64 × 54 (phrase) — checked reduced.
11. Version A: only frames 2 and 7 differ from Story 1; Version B is six frames in Story 2's cast.
12. No file serves two slot ids (except the Version A reuse the build makes itself); no slot points at a neighbouring file.

## 7 · Delivery

A zip containing only `assets/art/` and the filled `art_manifest.json` — no `index.html`, no CSS, no scripts. Attached to the Editor's session or dropped into the connected repository clone (not committed). The Editor runs §6, transcribes the sheets into the Cast Bible, wires the map, re-runs QC, and issues the next Studio version; the Mac session pushes.

## 8 · Faults in the first delivery (2026-09-30 package) — each one is a rejection on its own

Recorded so they are not repeated. The package was inspected on 2026-10-01.

1. **Frames missing.** `index.html` referenced 42 files under `assets/art/u1/`, `u2/`, `u3/`; none of those folders existed. Every story frame would have been a broken image.
2. **Crops, not drawings.** The fifteen files delivered were 120 × 100 px cut-outs from one larger generated sheet: English text fragments ("Props", "SVG-read", "Hand Poses", numbered badges, English captions) ran through them and subjects were cut off at the edges. A slot image contains one complete subject and no text.
3. **Filenames not matching contents.** `obj-key` was a football, `obj-cat` a boy with a key, `obj-house` two girls at a door, `obj-gift` a laptop, `obj-ball` a gift box. The id names the content; a file that shows something else is a defect even if the picture is good.
4. **Background not white.** Every file was cream (#FBF8F3). SC-037 requires #FFFFFF.
5. **Wrong style.** Full cartoon figures with detailed hair, hoodies and shaded faces — not the stick figure (two-dot eyes, one mouth line, tube limbs, near-empty space) that SC-111 approved with colour on clothing only.
6. **Wrong marker.** رَزَان was drawn with two buns on top of her head; her recorded marker is two low side bundles. Markers come from the manifest, not from the drawing hand.
7. **Size.** 120 × 100 px JPG cannot print at 40 mm. Sizes are in §2.
8. **A site was delivered instead of an art package.** `index.html`, `404.html` and `teacher.html` are the build's outputs and are never part of an art delivery.
