# Intaliq 1 — Unit 2 Visual Plan

*Written 2026-09-17 on the owner's word ("ok"). **A plan, not an illustration.** The standing instruction — no illustrations for Unit 2 yet — is untouched: nothing here is drawn. This document is the complete specification from which the frames can be produced at any later date, in-house as SVG in the house style (as Unit 1's were) or by an outside hand, without reopening the text. Method: the Book 1 line's Visual Governance process (plan against frozen text → plan approved → image produced → per-image QC) applied to the School Course's own art direction (SC-034, SC-053). **Plan approval is not image authorization**; image approval is not page authorization (Visual Governance §1.4).*

*Source prose: `u2r7_s1.txt` (172 words, 22 paragraphs, numbered 0–21 below) · `u2r7_s2.txt` (114 words, 20 paragraphs, 0–19; SC-102 added «خَدِيجَة تَضْحَكُ فِي الصُّورَةِ.» to paragraph 1) — the frozen revision 6 texts of SC-095. Slots: the Studio's Unit 2 frames (`picfr.empty` ×8 and ×6), the nineteen phrase-page picture slots (`pslot`), and every `img:null` in `UNIT_02` / `UNIT_02P`.*

---

## 1 · Style lock (what every image obeys)

**Current precedence (SC-113, 2026-10-10):** the owner selected the rich-cartoon reference for Unit 2. The historical stick-style text and palette checks below are superseded for this unit only; `source/cast-and-art/UNIT2_RICH_STYLE_AUTHORITY.md` gives the current rendering and size rules. Frame content, must-not-show, markers, expression beats, spoiler protection, notebook reuse and Version A's pixel identity are unchanged. The historical final "images not authorized" line is superseded by SC-111; neither style adoption nor authorization is a per-image pass.

The house figure style, SC-053, unchanged: one ink, **one stroke weight (3)**, **two values — black line on white**, no greys, no tints, no accent colours; heads about a third of figure height, no neck; faces of two dots, a hooked nose, one mouth line carrying the whole expression; tube limbs; near-empty space — a floor line, a doorframe, one object, never a background. Framed panels for the strips. **Named characters have faces; generic action figures do not.** No text, letters or numerals inside any image (the picture strip is read before the text; a word in a frame would be a caption). No hearts, no romance-readable imagery (SC-027 · SC-036). Criterion 27: a frame supports the text and never spoils it.

**Why this style and not a picture-book one:** the strip is a sequencing task, Version A/B is spot-the-change, who-says offers faces, and the engine's feedback shows a picture — all of which need the same character and the same object to be recognisably identical across frames. Identity-by-one-fixed-marker is what makes that checkable (and what a generator is worst at; Book 1's C-11 is the record of that).

## 2 · Cast markers and object iconography (the consistency anchors)

**People — existing symbols in the Studio's SVG defs, reused unchanged (خَدِيجَة is new):**

| Character | Marker (fixed, every frame) | Symbol | Expression variants needed in Unit 2 |
|---|---|---|---|
| كَرِيم | curls (three arcs on the crown) | `av-karim` | neutral · questioning (`-q`) · **laughing** (new: mouth line up, eyes as two short arcs) |
| زَيْد | flat cap | `av-zayd` | neutral only |
| مَهَا | high hair tie | `av-maha` | neutral only |
| عُمَر | spikes | `av-omar` | neutral · happy (exists) |
| رَزَان | side bundles | `av-razan` | neutral · questioning · **sad** (new: mouth line down — the CR-8 word made visible once, frame S2-4 only) · happy · talking |
| خَدِيجَة ⟨SC-097, replaces سَارَة⟩ | **two plaits** (one each side, hanging to the shoulder) — a new marker, not Unit 1's hijab | `av-khadija` (new) | neutral · happy · talking |
| رَنَا | bob | `av-rana` | neutral · talking |

**New character — الْقِطّ.** A named speaking character, so it gets a face (two dots, one mouth line, **no nose** — the nose is the human marker). Marker: **two triangular ears and a tail curled around the front paws**, sitting upright, drawn at the same stroke weight, roughly half a child's height. Its knowledge is never shown by posture or expression before frame 8: in frame 7 it simply sits at the door, looking at nothing in particular. Symbol `av-qitt`, variants `-talk` (mouth as the small ellipse), `-walk` (frame 8, entering).

**Objects — fixed iconography (SC-034 guard 3), one drawing each, reused everywhere including engine feedback:**

| Object | Drawing | Symbol |
|---|---|---|
| مِفْتَاح | a round bow, a straight shank, two teeth; **always the same key** — the found key and Karim's key are the *same drawing* on purpose (that is the story) | `obj-key` |
| حَقِيبَة | a school bag: rounded rectangle, one flap, one strap; **Karim's is drawn larger** (كَبِيرَة) than Zayd's | `obj-bag`, `obj-bag-big` |
| كِتَاب | a closed book, spine left, two lines on the cover — never lined like the قَائِمَة | `obj-book` |
| قَلَم | existing `obj-pen` | `obj-pen` |
| بَاب | existing `obj-door`; a house is **door + a roof line** only | `obj-door`, `obj-house` |
| صُورَة | a rectangle with a thick lower border (a print), inside it two tiny figures — **always رَزَان's bundles and خَدِيجَة's plaits**, both pictures identical | `obj-photo` |
| الْأَرْض | the single floor line, slightly irregular | — |
| يَد | the figure's arm ends in a small circle holding the key | — |

## 3 · Story 1 — «أَيْنَ مِفْتَاحِي؟» — the eight-frame strip

Spoiler rule for this strip: **frames 1–7 never show that the cat knows anything, and never show the inside of Karim's bag after frame 1.** The reveal is frame 8 and nothing before it may let a reader work it out from the pictures.

| # | Text anchor (paragraphs) | Event clarified | Who · objects · state | Must NOT show | Load risks |
|---|---|---|---|---|---|
| **S1-1** | 0 | Karim has a big bag; in it a book, a pen and the house key | Karim (neutral), the big bag **open**, book, pen and key visible inside it | — | three objects in the bag must read as three distinct icons; nothing else in frame |
| **S1-2** | 1–3 | On the way home he sees a key on the ground | Karim (questioning) walking, the bag **closed** on his shoulder; a key on the floor line ahead of him; a house with a door far right | the bag's contents | the key on the ground must be the same drawing as frame 1's key — deliberately |
| **S1-3** | 4 | He puts the key in his bag and decides to ask Zayd | Karim's hand placing the key into the (closed-flap) bag; a small "?" is **not** drawn — the question is in the text | the bag's interior | keep the bag flap up so the interior stays unseen |
| **S1-4** | 5–6 | Zayd, at his door: no, my key is in my bag | Karim holding up the key at Zayd's door; Zayd (flat cap) in the doorway with his **small** bag on his shoulder, patting it | — | two bags in frame: Karim's big, Zayd's small; the key is in Karim's hand, not Zayd's |
| **S1-5** | 7–8 | Maha: my key is under the book | Karim at Maha's door with the key up; Maha (hair tie) in the doorway; **beside her, on the floor line, a book with a key's bow peeping from under it** | — | Maha and the book must not overlap; the peeping key must be small but the same drawing; sensitivity: two children at a doorway, no touch, ordinary distance |
| **S1-6** | 9–11 | Omar: my key is on the door — and you? | Karim at Omar's door; Omar (spikes, happy) pointing at **a key hanging on the door**; Karim pointing at his own bag | — | three keys exist in the story by now (found, Omar's, Karim's-in-bag): only two in frame — Karim's hand and the door |
| **S1-7** | 12–15 | Karim comes home; a cat at the door | Karim walking toward his own house (same house as frame 2); **the cat sitting upright at the door, neutral, looking at nothing** | any hint that the cat knows: no cat looking at the key, no cat looking at the bag, no cat mouth open | the cat's marker must be legible at strip size (ears + tail) |
| **S1-8** | 16–21 | The reveal: the bag holds book and pen but no key; the key in his hand is his own; he laughs; both go in | Karim (laughing) with the bag **open** showing book and pen only, the key in his other hand; the cat (`-talk`) beside him; the door ajar | — | the open bag must clearly show *two* objects where frame 1 showed three — that gap is the whole reveal; nothing else in frame |

**Frame 8 carries the ending as well as the reveal** (paragraphs 16–21 are one beat in pictures: he sees, he laughs, they enter). If a ninth frame is ever wanted, split it here: 8 = the look into the bag, 9 = key in the door and the cat entering. The strip is eight because Version A/B counts on a fixed length.

## 4 · Story 2 — «صُورَةُ رَزَان وَخَدِيجَة» — the six-frame strip

Spoiler rule: **Sara's picture does not exist in any frame before 6**, and no frame before 5 shows where Sara is.

| # | Text anchor | Event clarified | Who · objects · state | Must NOT show | Load risks |
|---|---|---|---|---|---|
| **S2-1** | 0–3 | Razanne has a picture of herself and Sara; puts it in her bag; sets off | Razanne (happy) holding `obj-photo` (its two tiny figures: bundles + hijab), her bag open beside her | Sara herself | the photo's tiny figures must read as the two girls at strip size — bundles and hijab only, no faces |
| **S2-2** | 4–5 | At Sara's house — calls — Sara isn't there | Razanne (talking) at a house with the door **closed**; nothing else | Sara anywhere; the photo | a closed door must read as "nobody" — no window, no second figure |
| **S2-3** | 6–7 | Rana: Sara went to your house | Rana (bob, talking) pointing **back along the floor line** the way Razanne came; Razanne (questioning) | Sara | Rana's pointing arm must point away from Sara's house, toward Razanne's |
| **S2-4** | 8–10 | Back home — not here either — Razanne is sad | Razanne (**sad** variant) at her own house, door closed; her bag on her shoulder | Sara | the sad mouth line is the only expression change in the strip; nothing else "sad" (no rain, no tear) |
| **S2-5** | 11–14 | Back at Sara's house — Sara is there — Razanne gives her the picture | Sara (happy) at her open door; Razanne (happy) holding out `obj-photo` | **Sara's own picture** — Sara's hands are empty or one hand on the doorframe | two identical-marker-bearing girls plus a photo of them: keep the photo small and held out between them |
| **S2-6** | 15–19 | Sara gives her one too — the same picture — both laugh | Both girls (happy), each holding a `obj-photo` **identical** to the other's, held up side by side | — | the two photos must be the same drawing, same size — the joke is identity; no hearts, no hug (SC-027): they stand apart, each holding a picture |

## 5 · Version A / Version B (S11 spot-the-change strips)

**Version A (Story 1):** the same eight frames with exactly these differences and no others — frame 2: the key is **under a book** on the ground, not bare on it; frame 7: **the cat sits on that book** (the book has travelled with the cat — nothing in the text says so; that is the point of a spot-the-change). Everything else identical to the pixel.

**Version B (Story 2, as the drafts file records it):** رَزَان finds **a pen** on the ground, visits **three** friends, and **a bird sits on the door** in the last frame. This is a six-frame parallel to Story 1's shape drawn with Story 2's cast: frames = pen on the ground · Sara's door · Rana's door · Omar's door · home, bird on the door · laugh. Bird: house style, two dots, no nose, one marker (a short tail fan).

## 6 · The phrase page — nineteen pictures

Each picture is one small drawing in the house style with **no people unless the phrase names one**, so the picture shows the phrase and nothing more.

| # | Phrase | Picture |
|---|---|---|
| 1 | أَيْنَ الْمِفْتَاحُ؟ | Karim (questioning), empty hands up; no key anywhere |
| 2 | فِي الْحَقِيبَةِ | the bag open, the key inside |
| 3 | عَلَى الْبَابِ | the door with the key hanging on it |
| 4 | تَحْتَ الْكِتَابِ | the book on the floor line, the key's bow peeping from under it |
| 5 | أَنَا هُنَا! | Razanne (talking), one arm raised, at a door |
| 6 | يَذْهَبُ إِلَى الْبَيْتِ | generic faceless walker (`fig-walk`) → arrow → house |
| 7 | أَذْهَبُ إِلَى بَيْتِكِ | Razanne walking → arrow → a house with Sara in its doorway |
| 8 | يَرْجِعُ إِلَى بَيْتِهِ | generic walker with a **curved return arrow** → house |
| 9 | أَضَعُ مِفْتَاحِي فِي حَقِيبَتِي | a hand placing the key into the bag (no face in frame — first person is the reader) |
| 10 | هٰذَا مِفْتَاحٌ | the key alone |
| 11 | هٰذِهِ حَقِيبَةٌ | the bag alone |
| 12 | هٰذَا كِتَابٌ | the book alone |
| 13 | هٰذَا بَابٌ | the door alone |
| 14 | هٰذِهِ صُورَةٌ | the photo alone (its two tiny figures inside) |
| 15 | هٰذَا بَيْتٌ | the house alone |
| 16 | عَلَى الْأَرْضِ | the key on the floor line |
| 17 | هٰذَا قِطٌّ | the cat alone, sitting |
| 18 | رَزَان حَزِينَةٌ | Razanne, the sad variant, alone |
| 19 | هٰذِهِ لَكِ | a hand holding out the photo toward the viewer |

## 7 · Engine image assignments (fills every `img:null`)

Items → `img`: `miftah`→`obj-key` · `haqiba`→`obj-bag` · `kitab`→`obj-book` · `bab`→`obj-door` · `bayt`→`obj-house` · `sura`→`obj-photo` · `qitt`→`av-qitt` · `ard`→`sc-key-ground` · `dhahab`→`vg-go` (phrase 6) · `rajaa`→`vg-return` (phrase 8) · `wadaa`→`vg-put` (phrase 9) · `fi`→phrase 2 · `ala`→phrase 3 · `tahta`→phrase 4 · `huna`→phrase 5 · `ayna`→phrase 1 · `hazina`→phrase 18. Sentences → `img`: each paragraph takes its frame's scene id (`sc-k1`…`sc-k8`, `sc-p1`…`sc-p6`). Cast → `img`: as §2. Once these are set, the engine will generate the picture-recognition families (arabic-to-picture, picture-to-arabic) that Unit 2 currently lacks; QC must be re-run and the activity count re-stated at that moment (SC-050).

**Notebook slots (SC-100).** N1 أ takes frames S1-1…S1-8 in order, one per line; N1 ب takes S2-1…S2-6; N4 reuses Unit 1's `av-razan · av-omar · av-huda · av-karim-pen`; N2, N3 and S6 print no picture — their boxes are the learner's. No notebook page receives a picture of its own.

## 8 · Acceptance checklist — run on every image before it is placed

1. Two values only: black line on white; no grey, no tint, no colour.
2. One stroke weight throughout; rounded caps; no tapering, no hatching, no shading.
3. No text, letters, numerals or glyph-like marks inside the image.
4. Every named character carries its §2 marker, identical to Unit 1's drawing of the same character; the cat carries ears + curled tail in every frame.
5. Every object matches §2's single drawing; the found key and Karim's key are the same drawing.
6. Frame content matches its row: nothing listed under *must not show* is visible; nothing not listed is added.
7. Expression variants appear only where the row names them (Karim laughs in S1-8 only; Razanne is sad in S2-4 and phrase 18 only).
8. No hearts, no embrace, no romance-readable pairing (SC-027 · SC-036); children at doorways stand apart.
9. Faceless generic figures for actions (phrases 6, 8); faces on named characters and the cat.
10. At strip size (118 × 98 px in the Studio; ~40 mm printed) the marker and the key are still legible — check reduced, not at full size.
11. Version A differs from Story 1's strip in exactly the two listed places; a pixel diff of the other six frames is clean.

## 9 · Order of work when the hold is lifted

Symbols first (§2: seven variants, seven objects), checked against Unit 1's existing defs for stroke and proportion → the two strips → the phrase page → Version A/B → engine assignments and QC re-run → Studio republish with the frame labels removed → production-record entry stating the new activity count. Estimated as in-house SVG: the same work Unit 1's nine scenes took, times two.

---

*Status: plan written; **images not authorized**. Recorded in the Unit 2 production record §12. When the owner lifts the hold, this file is the brief.*
