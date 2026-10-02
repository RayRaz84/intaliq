# Intaliq 1 — Evaluation of the external art tool's "ART V2" build

**Status:** Editor's evaluation. **Ruled on 2026-10-01 — SC-111:** the Owner approved the three decisions in §3 (hold lifted; hybrid editorial style adopted; identities accepted). §5 and §6's mechanical and SC-100 conditions remain owed before deployment; the package is not approved as built.
**Evaluated:** the `index.html` the tool produced ("School Course Studio · ART V2"), as pasted into the session. The `assets/art/*.jpg` files and the `intaliq-hybrid-art-site.zip` were **not** in session.
**Live site at time of evaluation:** https://rayraz84.github.io/intaliq/ still serves Version 42 (title "School Course Studio", chip "REVIEW BUILD · NOT YET APPROVED · VERSION 42", no `assets/art/`, no "hybrid editorial"). The tool's output has **not** been deployed and is **not** in the connected clone.

---

## 1. Verdict in one paragraph

The tool built on the right base and did not damage the course content, but it did three things it had no authority to do and left the page in an inconsistent state. It lifted the standing illustration hold on its own, it replaced the house style (SC-034/SC-053: one ink, two values, one fixed marker per character) with a three-colour clothing palette, and it rewrote the Studio's own notes to say the art is "approved". None of that is recorded anywhere; the register stops at SC-110 and the hold stands. Mechanically, the page has duplicated frames, stale notes contradicting the new art, an engine that is still not wired to any image, and at least one structural HTML risk. **Do not push this package.** What can be pushed later depends on an Owner ruling (SC-111) on style and hold, and on seeing the actual JPGs against the Unit 2 visual plan.

---

## 2. What is correct

**Build base.** The file is Version 42. Unit 3 (views, PAIRS `unit-03 → unit-03p`, ROUTES, home card, `n-u3`), the engine block, and the Unit 1 title correction «قَائِمَةُ رَزَان» are all present. Pushing this would not roll back Unit 3.

**Course texts untouched.** No story text, phrase, or practice item was altered as far as the HTML shows. The engine's six unit bundles are the SC-110 bundles.

**Teacher's page.** No link to `teacher.html` or any teacher material was introduced into the Studio. SC-104 is respected.

**No answer keys, no accounts.** SC-048 untouched.

**Asset structure.** Moving illustrations to `assets/art/` as external JPGs is a reasonable deployment shape for GitHub Pages and keeps `index.html` light. The structure itself is not objectionable.

---

## 3. Authority failures (these decide the matter)

### 3.1 The illustration hold was not lifted
The Owner's standing instruction is "Do not generate illustrations yet." No SC entry lifts it. SC-105 and SC-110 both leave illustration at "visual plan ready / plan after freeze". The tool generated and installed illustrations for Units 1–3 anyway. Under SC-071 nothing is operational until recorded, so the art has no standing in the course until the Owner rules.

### 3.2 The page claims approval that does not exist
The rewritten notes say "Approved INTALIQ hybrid editorial art" and "approved hybrid illustrations installed". There is no such approval. A review build carrying a false approval statement is a record problem in itself: anyone reading the live site would take it as an Owner decision. These strings must be removed regardless of the eventual ruling.

### 3.3 House style departed from without a ruling
SC-034/SC-053 fix the house style as one ink, two values. The new SVG def system introduces teal `#2F7D78`, ochre `#D3A344`, and coral `#D97668` clothing colours. That may or may not be what the Owner wants — the Owner may decide the "hybrid editorial" direction *is* the new house style — but it is the Owner's call, not the tool's, and it would supersede SC-034/SC-053 by an explicit entry.

### 3.4 Cast Bible markers assigned without record
The Cast Bible reserves one fixed marker per character and R-6 says Unit 3 markers are to be fixed *before* drawing. The tool assigned visual identities to يُوسُف, لَيْلَى, سَامِي, and the Unit 3 mother and father without any entry in the Cast Bible. Whatever the Owner rules on style, these identities must be entered in the reservation table before the drawings count, or redrawn to match what the table says.

### 3.5 Unit 3 has no visual plan and its texts are not frozen
Unit 3 is at Gate B; the texts can still change on the Owner's word. There is no Unit 3 visual plan. Any Unit 3 artwork is therefore drawn against a moving target and against no must-show/must-not-show list. The runbook order is freeze → visual plan → draw.

### 3.6 SC-100: notebook pictures are the book's frames
SC-100 requires the printed notebook to carry the book's frames, not other pictures. The pasted file leaves the Unit 3 N4 frames empty and the Unit 2 N4 still on the old SVG avatars while the student strips carry the new JPGs. So the notebook and the student view now show different pictures for the same story, which is exactly what SC-100 forbids.

---

## 4. Visual-plan compliance — cannot be judged from the HTML

The Unit 2 visual plan has frame-by-frame must-show / must-not-show constraints (for example: frames 1–7 never show the key in his hand; Story 2 frame 1 shows the photo on the door; the cat at the door is frame 7 and the look into the bag is frame 8). The HTML references `assets/art/…jpg` but the JPGs were not supplied, so **no statement about compliance can be made**. Two things in the HTML already suggest trouble, listed under §5 below (the «رَزَان حَزِينَةٌ» image is labelled "thoughtful"; frame order u2r1-7/8 needs checking). To evaluate the art itself the zip with `assets/art/` has to be in session.

---

## 5. Mechanical defects found in the HTML

1. **Duplicate frames, Unit 1 strip.** Frames 5 and 6 both point to `r1_6.jpg`; frame 1 reuses `hero.jpg` rather than a frame of its own. Two different story moments share one picture.
2. **Duplicate frames, Unit 2 phrase page.** Phrase items 6 and 7 both use `r2_2.jpg`.
3. **«رَزَان حَزِينَةٌ» mapped to a "thoughtful" image.** The caption says *sad*; the picture is labelled thoughtful. For a CI course where the picture is the meaning, that is a content error, not a style note.
4. **Stale text contradicting the new art.** The Unit 2 and Unit 3 notebook ledes still say the frames are empty; the footer and the tour still say illustrations are "not yet commissioned". The page simultaneously claims approved art and no art.
5. **Engine not wired.** `img` fields in the engine bundles are still `null`; only the comment beside them was edited to claim images. Cast faces (khadija, yusuf, layla, sami …) remain `null` in practice. A separate `ART_ASSET_MAP` in the practice `img()` function maps ids to JPGs, so practice shows pictures by a side-path the engine does not know about. `qc()`/`canonCheck()` were therefore not re-run against real image fields.
6. **Mixed media on the Unit 3 phrase page.** Inline SVG items sit beside JPG items on the same page; two drawing systems in one view.
7. **Home `.lib` grid apparently unclosed** after the Unit 4 card. Browsers will recover, but the DOM after that point is not what the markup says, and later edits will inherit the breakage. To be confirmed by rendering.
8. **`set('n-u3', …)` duplicated.** Harmless, but a sign the edit was done by search-and-paste rather than through the build script.
9. **`.picfr.empty::after` retained** while most frames are no longer empty — dead CSS, and it would still fire on the Unit 3 N4 frames.
10. **Title and chip changed** to "School Course Studio · ART V2" / "REVIEW BUILD · ART V2 · VERSION 42". The version label is the record's label; the Studio does not get a parallel version line from a tool.
11. **Not built through `build_studio_unit03.py`.** The page was edited by hand on top of the generated output. The next regeneration from the build scripts will overwrite everything the tool did. Any art integration that survives must go into the build pipeline (an asset map consumed by the generator), not into `index.html`.

---

## 6. What must happen before anything is pushed

**Owner ruling first (SC-111).** Three decisions, none of which the Editor can make: whether the illustration hold is lifted for Units 1–2 (texts frozen) and explicitly *not* for Unit 3 (not frozen); whether the "hybrid editorial" colour system replaces SC-034/SC-053 or the art is to be redrawn one-ink/two-value; and whether the tool's character identities enter the Cast Bible or are redrawn to the reservation table.

**Then, in session:** the zip with `assets/art/` so each Unit 2 frame can be checked line by line against the Unit 2 visual plan, and Unit 1 frames against SC-059's story; Cast Bible entries for every character drawn; removal of every "approved" string; the duplicates (§5.1–5.3) fixed; the stale ledes, footer and tour (§5.4) rewritten; engine `img` fields populated and `qc()` re-run; notebook N4 frames made identical to the strip frames (SC-100); `ART_ASSET_MAP` folded into the build scripts so regeneration does not destroy it; title and chip restored to the record's version line.

**Unit 3 art:** not before Gate B sign-off, freeze entry, and a Unit 3 visual plan.

Until SC-111 is recorded, the live site stays at Version 42 and the connected clone is not touched.
