# Intaliq (School Course Studio) — public deployment

*Recorded 2026-09-12. Delivery fix only; the book's content is unchanged. **Updated 2026-09-26** for Studio Version 40 and the teacher's page (SC-104).*

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

**Version now written to the clone:** Studio 42 — Units 1–3, teacher's page for all three units. **Version on the public site:** whatever was last pushed.

## Known limitations
- Two webfonts (Noto Naskh Arabic, Baloo Bhaijaan 2; the teacher's page also uses Source Serif 4 / Source Sans 3) load from fonts.googleapis.com; system fallbacks are declared.
- "Audio" is the browser's built-in speech synthesis, not recorded audio; voice quality depends on the visitor's OS.
- The site is public and unlisted, not private. Unit 2's picture frames are empty by standing instruction until the illustrations are authorized.


## Release check before every push (added 2026-10-01)

`tools/verify_release.py deploy/ <version>` serves the deploy folder exactly as GitHub Pages serves it, opens every Studio route in a real browser, screenshots each one (`verify_shots/`, contact sheet `verify_sheet.png`) and writes `verify_report.md`. **Blockers** (exit 1, no push): a route with no view mounted · any broken image · any `assets/` path referenced but missing · any link or mention of `teacher.html` in the Studio (SC-104) · the words "answer key" (SC-048) · a version chip that is not the expected version · console errors or failed requests from the site's own files. **Warnings** (listed, judged by eye): art files used more than once · "illustration pending" / "not yet commissioned" / "PROPOSED" counts · external resources unreachable from the workspace (fonts; fine on Pages). The Editor then looks at the contact sheet before writing the files into the clone. Charter §8's "rendered-page verification and presence inventory before any release" is this script plus that look.
