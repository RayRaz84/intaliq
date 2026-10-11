# Intaliq 1 — Session status board

*Each session rewrites its own section only, at the end of every working turn. Read all sections before starting work. Protocol: `INTALIQ1_SESSION_PROTOCOL.md` — note §2's rule (SC-118): the register is appended only in the project; a session without project access records a ruling here as "pending transcription" and takes no number.*

---

## Intaliq Text — last updated: 2026-10-11 (role carried by the Art session per SC-113)

- **Unit 1 closure, part 1 (SC-121) — Studio Version 46, a review build, built and gated locally on branch `unit1-corrections` (two commits on top of `109640f`); not pushed** (no push credentials here). Version 45 was never pushed and is superseded by 46.
- Batch 1 closed: `لَهُ` not licensed in Unit 1 → N3 frame uses «لِي ___!»; read-match sentences each name one picture; every core item met in a sentence on the pathways (SC-075 cards wired; staged post-reading tasks); ledger §1d / engine header / teacher flows / build docs synchronised; absent learner's alternative printed on N2 in Arabic; audio bindings validated as a schema (`audioCheck`) and by the build. Batch 2 built but **not delivered**: listening families and sound-first pathways proven on fixture bindings only; corner tasks printed, slots empty. New instruments: `apparatus_licence_u1.json` + the gate's language sweep (698 tokens, 0 unknown); `clips_manifest.json` (72 rows); `INTALIQ1_UNIT1_AUDIO_INTAKE.md`; `INTALIQ1_UNIT1_AUTHENTIC_CORNER_INTAKE.md`; `INTALIQ1_UNIT1_LEARNER_CHECK_PROTOCOL.md`.
- **Unit 1 is not complete.** Owed: 72 verified recordings · 3 real photographs · the learner / panel check run and recorded. Each needs someone outside this session (a speaker, a camera, a room). One owner policy point would shorten the path: whether synthesised speech may stand in for the pilot (a change to SC-028) — not assumed.
- changed (project): register SC-121 · Unit 1 Build §9.6 · Grammar Ledger §1d · Author's Page (through SC-121) · deployment doc (Version 46; gate extensions) · the three intake/protocol docs (new) · tools (`engine_core.js`, `school_course_studio.html`, `verify_release.py`, `build_studio_art.cjs`, `test_listening.js`, `apparatus_licence_u1.json`, `clips_manifest.json`).
- waiting on the owner: the word to push Version 46 (patch series / bundle delivered) · his Unit 1–2 audit list · Unit 3 Gate B (F-2, titles, pop-up) · the Unit 2 pop-up ruling · F-3 · recordings / photographs / a date for the learner check.
- next in order: push 46 → owner's findings → Unit 3 freeze → Version 47 (Unit 3 rev 2) → Units 2–3 `.rev` marking, form-licence tables and apparatus licences → when clips land: bind, build, gate, push.
- rulings recorded: SC-113, SC-114, SC-118, SC-119, SC-120, SC-121 (SC-115–SC-117 transcribed from Codex's repository entries).

## Intaliq Art — last updated: 2026-10-10

- **ask of the Publisher / Mac session:** pull or apply the `unit1-corrections` work; its `source/` tree already carries the re-exported governance copies, so the earlier renumbering ask (SC-114→115, 115→116, 116→117 in the repository's references) is **partly done** — `README_ART_BUILD.md` carries the mapping note; `UNIT2_ART_STATUS.md`, `manifest.json`, `production-prompts.json`, `UNIT2_RICH_STYLE_AUTHORITY.md` and the two review files still say the old numbers and are the Art role's to renumber (no content change).
- queue (SC-114): the question-word posters — `poster-man` (Unit 1), `poster-ayna` and `poster-hal` (Unit 2) **due now**; `poster-madha` and `poster-ma` after Unit 3's freeze. Spec: `INTALIQ1_QUESTION_WORD_POSTERS.md`.
- state: rich-cartoon style adopted (SC-113); producer is the process. Version 44 live (bag brown, SC-117). **Versions 45–46 change no art file, no binding, no hash** (the build verifies all 69 against the manifest). Then: replace the reference set with the accepted Unit 2 files; posters; Unit 1 slot list when the owner issues it; Unit 3 frames after freeze.
- rulings recorded: SC-111, SC-112, SC-113, SC-114, SC-118.

## Intaliq Publisher — (Claude Code / Codex on the Mac)

- last push: Version 44 (`0bf1413`, brown bag), 2026-10-10. **Next push, on the owner's word: Version 45** — branch `unit1-corrections` in the cloud clone, delivered as a patch and a zip of the repository state; apply onto `main`, run `python3 source/pipeline/verify_release.py <deploy> 45` (exit 0 expected), then push. **Do not append to `source/governance/SCHOOL_COURSE_DECISION_REGISTER.md`** — it is an export (SC-118); rulings given on the Mac go into this board as *pending transcription*.
