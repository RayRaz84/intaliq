# Unit 1 art readiness reconciliation

Baseline: repository commit `59309bc` (SC-126), Studio Version 50. The live site's retrieved HTML also displays Version 50. Engine checks: Unit 1 128 generated / 0 failed; second reading 78 / 0 failed.

**Verdict: content is ready for production. No unresolved owner content decision was found for these illustration slots.** The title proposal F-3 affects typography, not these image contents, and remains outside this work.

The Mac-only 35-slot readiness manifest supplied by the other session is not present in the current public repository and was not accessible here. The returned manifest is a reconstruction from current page/engine bindings and the user's inventory summary, not an asserted edit of that unseen file. Compare against the Mac copy at intake and preserve any additional slot-specific detail that agrees with current authority.

## Reconciliation

| Item | Final treatment |
|---|---|
| Six versus seven main frames | Six strip frames. `sc-tariq` is `u1-act-tariq`; ending is actual frame `u1-s1-6`. Legacy report IDs are recorded in JSON. |
| No-friend picture | `u1-act-alone`, activity only; not added to the strip. |
| Roster gap | Huda plus seven children; Tariq excluded. His portrait is production reference only, not a current learner binding. |
| Corrected read-match | Teacher Huda, list, Omar, friendship group and Sara have corresponding resources. No Razan-only portrait substituted for the group. |
| Speaker choices | First-reading five people; second-reading Karim-with-pen, Farida, Maha, Zayd and the pen. |
| Notebook | Same six plus three story files reused; corrected banks and N2 models require no extra story art. |
| Shared identities | Razan, Omar, Rana, Karim, Maha, Zayd use existing accepted Unit 2 identity sheets. Plain portraits reused where their content matches; Karim requires the existing Unit 1 behind-ear-pen variant. |
| Objects | Accepted Unit 2 pen and door reused by exact path/hash. Remaining list/chair/phrase supports stay manifest-specific. |
| Style | Owner adoption received directly; documented in `UNIT1_RICH_STYLE_AUTHORITY.md`, pending project transcription with no local SC number. |
| Photographs | Separate requirement; no generated substitutes. |

36 reconciled slots: 6 main-story frames, 3 second-story frames, 4 activity/spread/roster resources, 13 portrait/reference slots, 10 object/phrase supports. Seven accepted Unit 2 PNGs are reused unchanged; 29 new PNGs are produced and reviewed. The extra slot corrects a cross-reading phrase-support mismatch: Unit 1p’s masculine friend/possession phrase requires Karim and his pen, rather than the first story’s three-girl friendship group. Integration should override only Unit 1p’s `sadiq` / `li` support with `vg-sadiq-pen`; do not alter the first story’s matching resource or its Arabic.

## Governance handoff

The governing register lives in the Claude project. This session cannot access that project and therefore records the owner's ruling as pending transcription in its Art status section under SC-118. The style approval is not awaiting a second owner confirmation. Text/project intake should transcribe it using the next available register number and cascade the art-spec scope wording.

## Production and integration

All 29 new outputs were inspected for scene content, identity markers, clothing continuity, pen placement, roster membership and answer leakage. Individual drafts with colour drift or a scroll instead of the flat list were replaced before acceptance. The final set was also inspected as 118×98 scenes, 64×64 portraits and 64×54 supports. Small-size proofs are checks, never integration assets. B1 and the roster must receive their larger page-specific rendering checks at integration. The behind-ear pen must remain visible in the integrated speaker-choice portrait.

The manifest records raw production paths, dimensions and SHA-256 hashes. Final integration must use those bytes in student pages, notebook and digital consumers, preserve the six/three strips, and typeset existing B1 labels outside the PNG. Tariq’s portrait stays production-only. No engine, frozen Arabic, root generated page or accepted Unit 2 asset was changed. Main and the live site remain Version 50; this is a production branch, not a published update.

**Genuine unresolved content decisions: none for this batch.** F-3 remains a separate title/typography matter. Project-register transcription and final build proofs are handoff work, not new owner authorization. The three authentic photographs remain an external, non-illustration requirement.

## Authorities inspected

- `source/governance/SCHOOL_COURSE_DECISION_REGISTER.md` — exported rulings including SC-059, SC-118 and current SC-126 baseline.
- `source/governance/INTALIQ1_SESSION_PROTOCOL.md` — project register ownership and pending-transcription route.
- `source/units/unit1/SCHOOL_COURSE_U1_MAIN_STORY.md` and `SCHOOL_COURSE_UNIT1_BUILD.md` — frozen stories and approved strip architecture.
- `source/cast-and-art/INTALIQ1_ART_PACKAGE_SPEC.md` and `UNIT2_RICH_STYLE_AUTHORITY.md` — content controls, style precedent and byte preservation, extended by the direct owner ruling documented here.
- `source/pipeline/engine_core.js` and published Version 50 `index.html` — corrected readings, notebook, matching, speaker choices, vocabulary supports and actual bindings.
- `assets/art/unit2-rich/manifest.json`, `art_assets_map.json`, accepted PNGs and identity sheets — exact reuse and identity references.

## Subsequent integration pass

On the owner’s “continue working” instruction, the accepted PNGs were bound in the source build and rebuilt into `index.html` / `404.html`. The six/three strips reuse the same file paths in student book and notebook. Unit 1’s old SVG consumers are replaced, the roster reference row excludes Tariq, and Unit 1p receives the Karim-and-pen phrase support. Both frozen stories and every non-image engine property are unchanged. The inherited B1 greeting `مَرْحَبًا` escaped the previous SVG-excluding language sweep; integration exposed it as unlicensed. It was mechanically replaced with the unit’s already-authorized CH-01 greeting `السَّلَامُ عَلَيْكُمْ!`, without changing either reading or adding a licence. See `UNIT1_ART_INTEGRATION_2026-10-14.md` for release checks and publication status; the production-only statements above describe the earlier asset-delivery stage.
