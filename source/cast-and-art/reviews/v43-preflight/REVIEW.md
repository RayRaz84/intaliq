# Unit 2 Corrective Review

Owner request: "fix them and push", following the audit of `0dd18c3`. Final Version 43 pre-push review: both required checks pass; no Unit 2 art integration blocker remains.

| Finding | Evidence And Action | Status |
|---|---|---|
| Rich style not recorded | SC-113 records the actual owner choice and cascades into the art spec, manifest, visual plan, Cast Bible and Author's Page. Unit 1 is not silently redrawn. References and hashes are in the repository. | Corrected and verified |
| Omar has Karim's curls | The pushed `u2-s1-6.png` has straight upward spikes on Omar, distinct from Karim's crown curls; `av-omar.png` agrees. No replacement justified by this claim. | Not reproduced in pushed bytes |
| Version A changes whole scenes | SC-115 records the owner's explicit Version A-only compositing permission. The two derivatives insert generated book artwork into original Story 1 scenes. The focused gate proves every outside-region pixel identical; six other frames use exact Story 1 files. | Corrected, pixel lock passed |
| Story 1 frame 3 exposes bag interior | New raw generated `u2-s1-3-v43.png` places the key behind an opaque lowered flap. No cavity or contents visible. Prior accepted PNG remains unchanged. | Corrected, thumbnail inspected |
| Frame 5 key bow invisible | A bow was present, but small. New raw generated `u2-s1-5-v43.png` enlarges the visible ring while keeping its shank under the book. | Corrected, thumbnail inspected |
| Story 2 frame 4 not clearly sad | New raw generated `u2-s2-4-v43.png` has a stronger downturned mouth, without tears or rain. | Corrected, thumbnail inspected |
| Black bag vs brown bag | The small black `obj-bag` matches Zayd in Story 1 frame 4. Large brown `obj-bag-big` matches Karim. Scope and assignment distinctions recorded. | Not a colour mismatch in pushed bytes |
| Changed build still says Version 42 | Text integration generator emits Version 43, with identical index and 404. SC-114 records the corrective build commission, not content approval. | Corrected and verified |
| Notebook lede says empty | Unit 2 lede now states student-strip reuse. Unit 3 N4 now reuses the mapped Unit 2 strip files, without replacing Unit 2 N4's legitimate Unit 1 retrieval portraits. | Corrected and verified |
| Engine not wired | Runtime patch removed. Canonical Unit 2 data build consumes the flat asset map and explicit bindings; engine source and embedded declarations have populated image paths. | Corrected and verified |
| Release gate skipped | Final TF-9 run against deploy/43 completed with no blockers across 14 routes; contact sheet inspected. Focused gate passes Version A pixel locks and all other art checks. | Final pre-push checks passed |

## Measured Checks

- Canonical engine QC: unit-02 226 activities / 172 words; unit-02p 141 / 114; no failures.
- All 69 served production PNGs match recorded accepted hashes; local candidate and accepted copies match.
- All 69 gallery images decode on desktop and mobile. Vocabulary and both reading practice paths pass their initial-task smoke checks without page errors.
- Build rerun produces byte-identical index, 404, source Studio, engine and canonical Unit 2 data.
- Corrected thumbnail image and the final TF-9 contact sheet were visually inspected.

These checks do not claim a full pedagogical audit or completion of every learner activity. Recorded audio, classroom pilot, pop-up decisions and Unit 3 Gate B are unchanged. The previous assertion that no art blocker remained was incorrect and is superseded by this review.

## Reviewed Warnings

Repeated files are intentional student/notebook/Version A/Unit 3 delayed-retrieval reuse. The remaining `illustration pending` occurrence is in CSS; Unit 3's own 14 empty frames remain outside this Unit 2 art commission. Two `PROPOSED` occurrences are the existing unapproved pop-ups, not new approval claims. Draft status remains unchanged.
