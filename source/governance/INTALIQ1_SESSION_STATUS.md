# Intaliq 1 — Session status board

*Each session rewrites its own section only, at the end of every working turn. Read all sections before starting work. Protocol: `INTALIQ1_SESSION_PROTOCOL.md` — note §2's rule (SC-118): the register is appended only in the project; a session without project access records a ruling here as "pending transcription" and takes no number.*

---

## Intaliq Text — last updated: 2026-10-10 (role carried by the Art session per SC-113)

- **Unit 1 corrective pass done (SC-120) — Studio Version 45 built and gated locally, on branch `unit1-corrections` of the repository clone; not pushed** (this session has no push credentials). Audit batches 1–3 implemented in the sources: engine (`engine_core.js`: reading membership regenerated; unit-level QC withholds a unit; `FORM_LICENCE`; `pathway()` coverage plan; distractor rule; feedback), Studio source (Unit 1 pages: response resources, generated who-says/sequence blocks, survey, roster row, pop-up, notes → `.rev`, learner view), teacher generator (phase order SC-119 for all three units; C1/C4 procedures; counts; filenames), build (`build_studio_art.cjs` embeds the engine wholesale and regenerates gen blocks; writes teacher.html), release gate (`verify_release.py`: pathway walkthroughs, resource and drift checks, mutation tests), `run_qc.js` re-pointed, `engine_test.js` removed. **Release gate: 9 pathways walked to the end, 0 blockers; mutation tests: every mutation blocked, controls deliver.**
- **Batch 4 not done, by instruction:** verified listening and the authentic-text corner — requirements in Unit 1 Build §9.5.
- changed (project): register **SC-119** (phase order) and **SC-120** (corrective pass) · `SCHOOL_COURSE_UNIT1_BUILD.md` §9 · `SCHOOL_COURSE_ACTIVITY_ARCHITECTURE.md` §2, P-3, §3 C, §5 · `SCHOOL_COURSE_AUTHORS_PAGE.md` (through SC-120; Unit 1 totals reconciled) · `SCHOOL_COURSE_RECYCLING_MAP.md` (Unit 1 summary regenerated; encounter report) · `UNIT_GENERATION_RUNBOOK.md` (TF-10; stage notes) · `INTALIQ_DEPLOYMENT.md` (build command, Version 45, extended gate) · the repository's `source/` tree re-exported from these.
- **the live site is Version 44** (Codex, SC-117). Version 45 carries the Unit 1 corrections and **Unit 3 revision 1 still** — Unit 3 revision 2 (SC-114's `هَلْ`), F-2, titles and pop-up wait on Gate B and will be Version 46.
- waiting on the owner: his Unit 1–2 audit list (packet `INTALIQ1_U1_U2_OWNER_AUDIT_PACKET.md`) · Unit 3 Gate B (F-2, titles, pop-up — SC-110) · the Unit 2 pop-up ruling (SC-105) · F-3 · **the word to push Version 45**.
- next in order: Publisher pushes `unit1-corrections` (or the patch) after the owner's word → owner's findings recorded → Unit 3 freeze → Alhawary 14.10 p. 258 by eye → Unit 3 visual plan + manifest → **Version 46** → apparatus pass U2–3 → notebook pass → Units 2–3 `.rev` marking → form-licence tables for Units 2–3 in their build scripts.
- rulings recorded: SC-113, SC-114, SC-118, SC-119, SC-120 (SC-115–SC-117 transcribed from Codex's repository entries).

## Intaliq Art — last updated: 2026-10-10

- **ask of the Publisher / Mac session:** pull or apply the `unit1-corrections` work; its `source/` tree already carries the re-exported governance copies, so the earlier renumbering ask (SC-114→115, 115→116, 116→117 in the repository's references) is **partly done** — `README_ART_BUILD.md` carries the mapping note; `UNIT2_ART_STATUS.md`, `manifest.json`, `production-prompts.json`, `UNIT2_RICH_STYLE_AUTHORITY.md` and the two review files still say the old numbers and are the Art role's to renumber (no content change).
- queue (SC-114): the question-word posters — `poster-man` (Unit 1), `poster-ayna` and `poster-hal` (Unit 2) **due now**; `poster-madha` and `poster-ma` after Unit 3's freeze. Spec: `INTALIQ1_QUESTION_WORD_POSTERS.md`.
- state: rich-cartoon style adopted (SC-113); producer is the process. Version 44 live (bag brown, SC-117). **Version 45 changes no art file, no binding, no hash** (the build verifies all 69 against the manifest). Then: replace the reference set with the accepted Unit 2 files; posters; Unit 1 slot list when the owner issues it; Unit 3 frames after freeze.
- rulings recorded: SC-111, SC-112, SC-113, SC-114, SC-118.

## Intaliq Publisher — (Claude Code / Codex on the Mac)

- last push: Version 44 (`0bf1413`, brown bag), 2026-10-10. **Next push, on the owner's word: Version 45** — branch `unit1-corrections` in the cloud clone, delivered as a patch and a zip of the repository state; apply onto `main`, run `python3 source/pipeline/verify_release.py <deploy> 45` (exit 0 expected), then push. **Do not append to `source/governance/SCHOOL_COURSE_DECISION_REGISTER.md`** — it is an export (SC-118); rulings given on the Mac go into this board as *pending transcription*.
