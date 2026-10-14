# Unit 2 notebook N4 — stale art correction

Baseline: public `main` commit `35f1546`, Studio Version 50. The live Unit 2 notebook's last activity, N4 “Do you remember?”, still rendered `av-razan`, `av-omar`, `av-huda` and `av-karim-pen` as legacy SVG figures. This was an omission in the earlier Unit 1 integration: it covered the Unit 1 book/notebook, but missed this cross-unit consumer.

N4 retrieves Unit 1 language and identities under SC-100. The fix reuses the exact accepted Unit 1 portrait bindings, in the same numbered order:

| Number | Identity | Exact production file |
|---|---|---|
| 1 | Razan | `assets/art/unit2-rich/av-razan.png` |
| 2 | Omar | `assets/art/unit2-rich/av-omar.png` |
| 3 | Huda | `assets/art/unit1-rich/u1-face-huda.png` |
| 4 | Karim, with pen | `assets/art/unit1-rich/u1-face-karim.png` |

`integrate_unit1_art.cjs` now handles this consumer and validates its exact four paths. The Unit 1 manifest lists N4 as a consumer of those portraits. The source Studio and generated `index.html` / `404.html` have the same four replacements. No PNG bytes, Arabic, word bank, activity order, engine data, stories or other notebook resources changed. No new art was generated.

Validation: accepted SHA-256 hashes match; repeated build produces identical output; the rendered N4 has four loaded PNGs and zero SVGs; correct order and CSS containment; no page errors; desktop and 390px mobile proofs inspected. The full release gate passed, exit 0: fourteen routes, nine pathways completed, no blockers. As in the preceding pass, Playwright's virtual clock advances only the answer-transition delay; all gate assertions and activity interactions remain intact. Raw gate report: `source/pipeline/verify_report_u2_n4_art_v50.md`. Proofs: `unit1-production-proof/integrated-unit2-n4-desktop.png` and `integrated-unit2-n4-mobile.png`.

The registered Studio version stays 50. Publication is pending until the authenticated clone imports and pushes the follow-up commit. The correction bundle is `unit2-notebook-n4-art-fix.bundle`, based on `35f1546`. In the connected clone on `main`:

```sh
git fetch /absolute/path/unit2-notebook-n4-art-fix.bundle unit1-art-reconciliation
git merge --ff-only FETCH_HEAD
git push origin main
```

Do not reset or force if the fast-forward refuses. After deployment, check `#unit-02/notebook` → N4 at the bottom: four rich-cartoon portraits, numbered 1–4, with Karim's pen visible. Existing audio/photo/design-review completion requirements are untouched.
