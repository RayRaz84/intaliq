# Unit 1 illustration integration — ready to publish

Baseline: current public `main` `59309bcd621fad282a2dc5eb2590fbbe1b1bc4f8`, registered Studio Version 50. Accepted production assets: commit `30d90e8`. The owner's follow-up “continue working” authorizes the integration and publication pass. No new Studio version or register number is allocated outside the project sequence. `data-u1-art-release="30d90e8"` distinguishes this art update from the previous Version 50 HTML.

## Delivered behavior

- The student book has 37 exact PNG placements; the notebook has 9. Unit 1's learner views have no remaining SVG image consumers.
- Main strip: six frames. Second strip: three frames. Notebook reuse is checked against the same exact paths at build time. `sc-tariq` and `sc-alone` remain digital/activity scenes.
- Huda and seven children appear in the roster picture. Tariq's reference portrait remains production-only, excluded from the named learner row and the picture. The build rejects portrait leakage into Unit 1 print views.
- Matching resources and both speaker-choice rows use accepted PNGs, including Karim's visible behind-ear pen. Reading 2 uses the distinct Karim-and-pen support for its masculine friendship phrase.
- B1's Arabic is typeset outside the PNGs, with named phrase-picture supports. The old SVG printed `مَرْحَبًا`, which the former SVG-excluding sweep missed and which has no Unit 1 licence. That apparatus greeting is replaced by licensed CH-01 `السَّلَامُ عَلَيْكُمْ!`. Neither frozen story, title, sentence array, vocabulary licence nor non-image engine data changed.
- All 36 accepted image bindings are checked against SHA-256 at build. Unit 2's accepted assets and its 69-entry map are unchanged. No accepted PNG is resized, cropped, regenerated or recompressed. CSS uses containment.
- Unit 1 bindings live in the source build, not only in generated HTML, so a subsequent rebuild retains them. Unit 1's scoped layout additions do not change Unit 2's styling.

## Verification

- Build succeeds; repeat build reproduces identical engine and generated HTML bytes.
- Release gate: **exit 0, no blockers**. All fourteen routes mount; all nine digital pathways reach their ends; no broken local images, unresolved image symbols or console errors.
- Language sweep: **749 learner-visible Arabic tokens, zero unknown**. The count now includes B1 text previously hidden from the SVG-excluding sweep.
- All six engine units are identical to the baseline after ignoring only `img` fields. Activity totals remain Unit 1 **128 / 78**.
- Main/second strip paths, notebook exact reuse, no activity image promoted into a strip, no Tariq portrait exposed, and every accepted PNG hash checked independently.
- Rendered main strip, second strip, speaker choices, roster picture/reference and notebook checked. The student page fits a 390px viewport without horizontal overflow. Proof PNGs under `unit1-production-proof/` are QA derivatives, never production replacements.
- The initial normal-time gate walked all nine pathways and caught the inherited B1 greeting. After that label correction, the complete gate was repeated using Playwright's virtual clock solely to advance the existing 650ms answer-transition delay; assertions, navigation, images, engine and activity responses were unchanged. The gate source was not modified.

Existing release warnings remain: three real photographs are not delivered; expected image reuse; Unit 3's pending illustrations/proposals; external font fetch unavailable in this verification workspace. This is an illustration update, not Unit 1 course completion or evidence of learner effectiveness.

## Publication and project intake

**Not pushed / not live from this workspace.** GitHub write preflight fails: `fatal: could not read Username for 'https://github.com': terminal prompts disabled`. No force push or credential workaround was attempted.

The bundle `unit1-art-integrated.bundle` contains the production and integration commits, including all PNGs and already-built deploy files. From an authenticated clone based on `59309bc` (first review/preserve any local work), import and publish:

```sh
git fetch /absolute/path/unit1-art-integrated.bundle unit1-art-reconciliation
git merge --ff-only FETCH_HEAD
git push origin main
```

If the fast-forward refuses, preserve the diverging work and reconcile the histories; do not force or reset. After GitHub Pages deployment, check `#unit-01/student`, `#unit-01/notebook`, and both digital readings. The version chip stays **50**; confirm the new PNGs and the `data-u1-art-release="30d90e8"` marker rather than expecting a new number.

The next session with Claude-project access transcribes the owner style ruling through SC-118 using the next free register number and cascades its scope into the art spec. No second owner authorization is needed. Authentic photographs and the remaining Unit 1 completion requirements are outside this illustration delivery.
