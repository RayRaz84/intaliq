# Intaliq (School Course Studio) — public deployment

*Recorded 2026-09-12. Delivery fix only; the book's content is unchanged. **Updated 2026-09-26** for Studio Version 40 and the teacher's page (SC-104). **Updated 2026-10-10** for the one-command Text build, Version 45 and the extended release gate (SC-120).*

**Public URL:** https://rayraz84.github.io/intaliq/
**Source repo:** https://github.com/RayRaz84/intaliq (public, owner RayRaz84, branch `main`, GitHub Pages "deploy from a branch", root)

Deep links: `#unit-01/student` · `#unit-01/practice` · `#unit-01/notebook` · `#unit-02/student` · `#unit-02/practice` · `#unit-02/notebook` · `#tour`.

**Teacher's page:** `https://rayraz84.github.io/intaliq/teacher.html` — a separate file at the repo root, **never linked from `index.html`** (SC-104; the build asserts it). Unlisted, not secret: it carries no answers. Give the address to teachers directly.

## Why
The claude.ai artifact link requires a Claude session; external reviewers hit a Cloudflare loop or "Page not found". GitHub Pages serves the same single-file app to anyone over HTTPS with no login.

## What the deployable files are
- `index.html` = the Studio artifact body wrapped in a proper `<head>` (charset, viewport, favicon-silencer, font preconnects, the `[hidden]` rule the artifact skeleton normally supplies). Body markup, CSS, data and JS are byte-identical to the artifact.
- `404.html` = copy of `index.html` (so deep links survive a cold load).
- `teacher.html` = the teacher's-pages artifact body, wrapped the same way.
- `.nojekyll` present.

## Updating ⟨procedure from 2026-09-29⟩
A local clone of the repo lives on the owner's Mac at `~/Documents/Documents - Work’s MacBook Air/GitHub/intaliq` (curly apostrophe in the folder name), next to the Book 1 repo, which is unrelated and never touched. At each freeze the Cowork session regenerates `deploy/` from `claude/tools/school_course_studio.html` and `claude/tools/intaliq1_teacher_pages.html`, writes `index.html`, `404.html` and `teacher.html` into that clone through the linked-computer bridge, and verifies them there (`git status`, version chip, `teacher.html` never referenced by `index.html`). The owner then tells the Mac session (Claude Code, signed in to `gh` as RayRaz84): *"push the Intaliq site"* with a commit message — it stages only those three files, commits, and pushes `main`. Pages rebuilds in about a minute. The cloud session cannot push itself (github.com is refused by its network policy). The zip route (`Add file → Upload files` on the repo page) remains the fallback.

**Version now built (2026-10-15):** Studio **51** — the Unit 1 production refinement (SC-128: noticing task S15, the class card and newcomer exchange, the genre labels), on top of Version 50 (SC-126) and the Unit 1 rich-art integration (`30d90e8` / `35f1546` / `ec1abd9`). **Version on the public site:** whatever was last pushed. **Pushing (2026-10-14 onward):** the cloud session can push directly when the repository is attached to it (`RayRaz84/intaliq`, push access); the Mac clone then syncs with `git fetch` + `git merge --ff-only origin/main`. The owner's own `git push origin main` from the Mac clone remains equally valid; the zip route is the fallback.

## Building ⟨SC-120, 2026-10-10⟩ — the sources, not the outputs
The deployable files are **generated**; an edit made to `index.html`, `404.html` or `teacher.html` alone is overwritten by the next build. The authoritative sources are `source/pipeline/engine_core.js` (the engine and all unit data), `source/pipeline/school_course_studio.html` (the Studio source — its embedded engine is replaced by `engine_core.js` at build and its `<!-- gen:… -->` blocks are regenerated from the engine), `source/pipeline/build_teacher_pages.py` (the teacher's page) and `source/units/unit2/unit02_data.js` (from `build_unit02.py`). One command builds everything, from the repository root:

```
INTALIQ_STUDIO_VERSION=46 node source/pipeline/build_studio_art.cjs
python3 source/pipeline/verify_release.py <folder-with-index-404-teacher-assets> 46
```

The build refuses when any unit is undeliverable (a unit-level QC failure), when the Unit 2 art inventory or hashes disagree with the manifest, when the Studio mentions the teacher page, or when a forbidden string (first-person gender self-categorisation, SC-021) is printed. It writes `source/pipeline/build_report.json` with per-unit words, generated and planned-pathway counts.

## Known limitations
- Two webfonts (Noto Naskh Arabic, Baloo Bhaijaan 2; the teacher's page also uses Source Serif 4 / Source Sans 3) load from fonts.googleapis.com; system fallbacks are declared.
- "Audio" is the browser's built-in speech synthesis, not recorded audio; voice quality depends on the visitor's OS.
- The site is public and unlisted, not private. Unit 2's frames carry the accepted rich-cartoon art (SC-113); Unit 1's are in-house SVG pending the redraw; Unit 3's are empty until its Gate B freeze.
- There is **no recorded, verified audio and therefore no listening task** anywhere; the 🔊 buttons are the browser's preview voice on request. Listening is Batch 4 work (Unit 1 Build §9.5).


## Release check before every push (added 2026-10-01; extended 2026-10-10, SC-120)

`tools/verify_release.py deploy/ <version>` serves the deploy folder exactly as GitHub Pages serves it, opens every Studio route in a real browser, screenshots each one (`verify_shots/`, contact sheet `verify_sheet.png`) and writes `verify_report.md`. **Blockers** (exit 1, no push): a route with no view mounted · any broken image · any `assets/` path referenced but missing · any link or mention of `teacher.html` in the Studio (SC-104) · the words "answer key" (SC-048) · a version chip that is not the expected version · console errors or failed requests from the site's own files. **Warnings** (listed, judged by eye): art files used more than once · "illustration pending" / "not yet commissioned" / "PROPOSED" counts · external resources unreachable from the workspace (fonts; fine on Pages). **Extended (SC-120):** every digital pathway of every unit is **walked to its end** in the browser (a pathway that stops is a blocker — the Unit 1 Reading 1 crash would have been caught); Unit 1's print-style tasks are checked for their response resources and for quotation drift from the printed story; an unresolved `<use href="#…">` and a review note visible in the learner view are blockers; `index.html` and `404.html` must be identical and `teacher.html` present; and **mutation tests** run against the engine extracted from `index.html` — a canon, form, membership or audio-flag mutation must leave the unit undeliverable, and the unmodified unit must deliver. **Extended again (SC-121):** every learner-visible Arabic token on the Unit 1 pages must be a canon word or an entry of `source/units/unit1/apparatus_licence_u1.json`; every print task must have an Arabic rubric and items and no English instruction in learner view; the listening fixture test (`test_listening.js`) is re-run against the deployed engine; the authentic corner's slot count is reported (a warning while any is empty). The Editor then looks at the contact sheet before writing the files into the clone. Charter §8's "rendered-page verification and presence inventory before any release" is this script plus that look.

**⟨WITHDRAWN — SC-124: the gate no longer reads any evidence record.⟩** ~~**Gate extension ⟨SC-122, 2026-10-13⟩.**~~ `verify_release.py` reads `source/units/unit1/INTALIQ1_UNIT1_LEARNING_EVIDENCE_RECORD.md` and blocks when it is missing, names a version other than the one deployed, or lacks one of its five status fields. It reads statuses; it never writes one. *Not run / not observed* pass the gate and print as warnings, so a release never hides them.
