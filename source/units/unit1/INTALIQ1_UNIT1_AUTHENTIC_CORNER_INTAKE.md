# Intaliq 1 — Unit 1 authentic-text corner: intake (Batch 2, not yet delivered)

*Editor (Text role) · 2026-10-11 · SC-121. The corner's three recognition tasks are printed on the page and its three slots are wired; what is missing is the three real photographs. **Nothing is claimed delivered.** The release gate reports the corner as *not delivered* while any slot is empty.*

## 1 · What the page already carries

Rubric «عَرَبِيَّةٌ حَوْلَنَا», three photograph slots (`#authentic-corner` · `data-slot="ac-1|ac-2|ac-3"`, `data-status="not-delivered"`), and the three recognition tasks of Unit 1 Build §3, printed in rubric Arabic: **1 · ○ أَيْنَ الِاسْمُ؟** — find and circle the name you know; **2 · 👤 / 🏠 ؟** — person or place, answered by pointing at the icon; **3 · ○ حَرْفٌ — اسْمِي** — circle one letter from your own name. Recognition only; nothing is read in full — that is the point (SC-020).

## 2 · What has to be supplied

| Slot | Photograph | Must show | Must not |
|---|---|---|---|
| ac-1 | a real shop sign carrying a **person's name** — a pharmacy, bakery or shop named for someone | at least one name the learner can know from the unit's world (any name on the Unit 1 roll is ideal: آدَم · رَنَا · سَارَة · طَارِق · عُمَر · رَزَان · نُور · بَدْر, or هُدَى / كَرِيم / مَهَا / زَيْد / فَرِيدَة), in clear Arabic lettering | mock-ups, composites, AI-generated or edited signage; a sign carrying unrelated long text |
| ac-2 | a real **school or building door sign** | a short label a child can treat as "a place" (مَدْرَسَة, a room name, a number) | a poster or notice with running text |
| ac-3 | a real **street name plate** | a street name in Arabic script; a letter or two the learner may find in their own name | a plate dominated by Latin script |

**Authenticity is the point (SC-020, Unit 1 Build §3):** these are photographs of real objects in the world, taken or licensed by the owner, with any private information (house numbers tied to a person, faces, licence plates) out of frame or cropped. Mock realia would fake the claim the corner makes and is refused.

Format: JPEG or PNG, landscape, ≥ 1200 px on the long side, delivered as `assets/photos/unit1-authentic/ac-1.jpg` … `ac-3.jpg` with a one-line provenance note each (where, when, by whom, licence) in `assets/photos/unit1-authentic/PROVENANCE.md`.

## 3 · How it is wired in and verified

The Text build places the three files into the slots (replacing the placeholder text with `<img>` elements) and flips `data-status` to `delivered`; the release gate reports the slot count and stops warning only when all three images render. Before the build, the Editor checks the picture–task fit (SC-100's rule applied to the corner): the name in ac-1 is legible at page size and matches task 1; ac-2 is unmistakably a place for task 2; ac-3 contains letters a child can isolate for task 3.

## 4 · Status

| | |
|---|---|
| Tasks printed | yes (Arabic rubrics; chrome recorded in `apparatus_licence_u1.json`) |
| Slots wired, status visible | yes (`not-delivered`) |
| Photographs | **none** — owner to source or commission |
| Corner | **not delivered**; the unit is not complete until it is |
