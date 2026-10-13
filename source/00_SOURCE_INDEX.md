# Intaliq 1 — Source Index

*Exported 2026-10-02 from the project "Arabic Reader serries" for the instructional auditor. Every file under `source/` is a byte-exact copy of the project document of the same name as it stood on that date (project path given per row; `claude/…` is the project folder, `tools/` its code subfolder). Nothing was reconstructed, edited, renumbered or reconciled for this export. Where a file's own masthead lags the register, the row says so and the register governs (SC-071).*

*The published website — `index.html`, `404.html`, `teacher.html` at the repository root — is untouched by this export.*

---

## 0 · How authority works in this record

The order of precedence, as the record states it (Author's Page §1, SC-090): **Story Standard** (SC-031) → **Two-Story Blueprint** (SC-057) → **Vocabulary Recycling Architecture** (SC-058) and its CR-1–CR-16 → the LC rules of the scope map → everything else. The **Decision Register** records every owner ruling; **nothing is operational until recorded there** and no ruling exists by relay (charter §8, SC-071). The **Author's Page** is the daily entry point and is amended in the same pass as any ruling that changes it. The **runbook** is the production procedure. All frequency evidence is Buckwalter & Parkinson (2011/2014) at lemma level, verified by eye or recorded "lookup owed" — never estimated; all grammar citations are Alhawary (2011) by subsection and printed page.

Status vocabulary used below: **ACTIVE** (governs today) · **ACTIVE, masthead lags** (governs; the file's own header predates a later ruling named in the row) · **RECORD** (a completed evidence or production record; not a rule) · **SUPERSEDED** (kept as history; marked so in the register or in the file) · **RETIRED-IN-EFFECT** (never formally retired, but a recorded ruling says it does not govern) · **INHERITED** (a document of the reader line, *Arabic Through Stories* Book 1, that the Intaliq record cites) · **STALE TOOL** (a script whose inputs are an earlier revision).

---

## 1 · `governance/`

| file | project path | purpose | authority | status | depends on / feeds |
|---|---|---|---|---|---|
| `SCHOOL_COURSE_CHARTER.md` | `claude/SCHOOL_COURSE_CHARTER.md` | The course charter: product identity (Intaliq 1, SC-062/063), the three products, governance article, standing rules §8 | Owner-ratified founding instrument; sits on top of the Design Description | ACTIVE | — |
| `SCHOOL_COURSE_DESIGN_DESCRIPTION.md` | `claude/SCHOOL_COURSE_DESIGN_DESCRIPTION.md` | Owner-authored course design and governing concept (2026-09-04) — "the constitution of method" | Owner's document, verbatim | ACTIVE | charter defers to it on method |
| `SCHOOL_COURSE_DECISION_REGISTER.md` | `claude/SCHOOL_COURSE_DECISION_REGISTER.md` | Append-only register SC-001 … **SC-122**; each entry = an owner ruling or a record-maintenance entry, with its cascade | The record of decision; the only place a status changes | ACTIVE | every other file cites it |
| `SCHOOL_COURSE_AUTHORS_PAGE.md` | `claude/SCHOOL_COURSE_AUTHORS_PAGE.md` | What governs drafting today: precedence, method, tense slots, support, measurement, apparatus, standing risks and owed work, pointers. "Current through SC-122." | Consolidation instrument (SC-093); amended with every ruling | ACTIVE | reads the register; is the first read of every session |
| `INTALIQ1_LEARNING_EFFECTIVENESS_STANDARD.md` | `claude/INTALIQ1_LEARNING_EFFECTIVENESS_STANDARD.md` | The evidence standard (instructional auditor, proposal 1.0, 2026-10-12): five evidence categories reported separately; evidence plan per unit; *not run / not observed* is a status; builds never write outcomes; claim limits | Owner-adopted instrument, precedence Author's Page §1 item 4 | **ACTIVE — ADOPTED SC-122** | template; Gate A field 3b; runbook 3/14; ACTFL §5.6; `verify_release.py` status check |
| `INTALIQ1_LEARNING_EFFECTIVENESS_ADOPTION_PACKET.md` | `claude/INTALIQ1_LEARNING_EFFECTIVENESS_ADOPTION_PACKET.md` | Text's presentation of the package: verification against the record, the Route A / Route B decision, the drafted entry, the cascade, the plan for the real check | Editor's packet; adopted as presented | RECORD (adopted SC-122, Route A) | — |
| `INTALIQ1_LEARNING_EFFECTIVENESS_HANDOFF_2026-10-12.md` | `claude/INTALIQ1_LEARNING_EFFECTIVENESS_HANDOFF_2026-10-12.md` | The auditor's handoff and adoption note (verbatim) | Source of the package | RECORD | — |
| `INTALIQ1_ARCHITECTURE_PREIMPLEMENTATION_REPORT.md` | `claude/INTALIQ1_ARCHITECTURE_PREIMPLEMENTATION_REPORT.md` | Pre-implementation report on adopting the "Intaliq 1 Architecture" (2026-09-13): counts, conflicts, what adoption would change. §G carries the SC-107 supersession note. | Editor's report; the Architecture it reports on was adopted by rulings SC-057–SC-075 and partly superseded by SC-107 | RECORD (its §G 220–260 budget is SUPERSEDED by SC-107) | — |
| `INTALIQ1_RECONCILIATION.md` | `claude/INTALIQ1_RECONCILIATION.md` | The reconciliation / open-decisions instrument R-1 … R-12 (nine ruled, three awaiting at last update) | Editor's instrument; rulings recorded in the register | ACTIVE, masthead lags (last updated 2026-09-15; later rulings on R-8/R-11/R-12 are in the register, not here) | register |
| `INTALIQ1_READINESS_PACKET.md` | `claude/INTALIQ1_READINESS_PACKET.md` | Evidence packet assembled 2026-09-15 for the owner's readiness verdict | Evidence, no verdict | RECORD | — |
| `INTALIQ1_SESSION_PROTOCOL.md` | `claude/INTALIQ1_SESSION_PROTOCOL.md` | How the Text, Art and Publisher sessions divide ownership of files (SC-112) | Record-maintenance ruling | ACTIVE | `INTALIQ1_SESSION_STATUS.md` |
| `INTALIQ1_SESSION_STATUS.md` | `claude/INTALIQ1_SESSION_STATUS.md` | Hand-over board, one section per session | Process instrument | ACTIVE (changes every turn) | — |
| `SCHOOL_COURSE_REVIEWER_BRIEF.md` | `claude/SCHOOL_COURSE_REVIEWER_BRIEF.md` | Survey packet for an outside reviewer of Unit 1 (2026-09-11): the constraints to judge against, what is known missing | Editor's brief; "reviewer notes are input, not approval" | RECORD (Unit 1 has since been revised to v8, SC-059; the eleven constraints still hold) | — |

**Requested but not a separate file:** "Editorial Constitution" — the Intaliq charter + Design Description are its constitution; the reader line's `EDITORIAL_CONSTITUTION.md` is in `inherited-line/`. "INTALIQ 1 Architecture" as a standalone document — the owner's Architecture text was pasted into the session and adopted by rulings (SC-057–SC-075); the only file form is the pre-implementation report above and the instruments it spawned (ledgers, progression, chunk inventory). The Architecture text itself is **not available** as a project file.

## 2 · `curriculum/`

| file | project path | purpose | authority | status | depends on / feeds |
|---|---|---|---|---|---|
| `SCHOOL_COURSE_L1_SCOPE_AND_SEQUENCE.md` | `claude/SCHOOL_COURSE_L1_SCOPE_AND_SEQUENCE.md` | Level 1 scope and sequence v4 (ADOPTED SC-048); LC-1–LC-6 rules; per-unit lines; the SC-107 budget line; the old 12–16/8–12 table marked superseded inside the file | Adopted working map | ACTIVE (one internal table SUPERSEDED, marked) | outcomes sheets, curriculum map |
| `INTALIQ1_TEN_UNIT_PROGRESSION.md` | `claude/INTALIQ1_TEN_UNIT_PROGRESSION.md` | Provisional vocabulary and grammar progression across ten units (Architecture §26.10, §28) | Editor's instrument; every item a candidate until its Gate A | ACTIVE (provisional by design) | Gate A briefs |
| `INTALIQ1_CURRICULUM_MAP.md` | `claude/INTALIQ1_CURRICULUM_MAP.md` | One-row-per-unit map with entry/exit profile and U1–U3 rows as built | Editor's instrument | ACTIVE | — |
| `SCHOOL_COURSE_TWO_STORY_BLUEPRINT.md` | `claude/SCHOOL_COURSE_TWO_STORY_BLUEPRINT.md` | Owner's 30 rules for the two-story unit; design cards (26, 27) and quality gate (28) | Owner's document, adopted verbatim SC-057 | ACTIVE | Gate A/B instruments |
| `SCHOOL_COURSE_STORY_STANDARD.md` | `claude/SCHOOL_COURSE_STORY_STANDARD.md` | Owner's 30-criterion Story Design Standard (SC-031); §E tense slots (SC-073) | Owner's document; top of precedence | ACTIVE | the 30-line Gate B audit |
| `SCHOOL_COURSE_CI_CALIBRATION_RULES.md` | `claude/SCHOOL_COURSE_CI_CALIBRATION_RULES.md` | Rules taken from two published CI/TPRS samples (SC-091) | Owner ruling "turn what you take into rules" | ACTIVE | — |
| `INTALIQ1_CI_SAMPLE_CALIBRATION.md` | `claude/INTALIQ1_CI_SAMPLE_CALIBRATION.md` | Evidence file: measurements of the Blaine Ray sample | Evidence | RECORD | calibration rules |
| `SCHOOL_COURSE_ACTIVITY_ARCHITECTURE.md` | `claude/SCHOOL_COURSE_ACTIVITY_ARCHITECTURE.md` | Closed catalog of activity formats, the five-phase unit arc, platform rules (v2.1 per SC-024/SC-038; §3 C and §4 amended SC-104) | Adopted instrument | ACTIVE | runbook, teacher's page generator |
| `SCHOOL_COURSE_OUTPUT_LADDER_SCHEDULE.md` | `claude/SCHOOL_COURSE_OUTPUT_LADDER_SCHEDULE.md` | Scaffold-fade schedule: Captions U1–2 · Frames U3–4 · Chains U5–6 · Stories U7–8 (SC-096) | Adopted | ACTIVE | notebook builds |
| `SCHOOL_COURSE_ACTFL_ALIGNMENT.md` | `claude/SCHOOL_COURSE_ACTFL_ALIGNMENT.md` | Method for mapping levels to ACTFL (v1, ADOPTED SC-048) | Adopted | ACTIVE | outcomes sheets |
| `INTALIQ1_UNIT_OUTCOMES_SHEETS.md` | `claude/INTALIQ1_UNIT_OUTCOMES_SHEETS.md` | Per-unit outcomes as the textbook presents them (Part 1 chart; Part 2 one section per unit; §2.9 Alhawary pass) — SC-096, SC-106 | Editor's instrument; U1–U3 as built, U4–U8 design targets | ACTIVE | ledgers, ACTFL framework |
| `INTALIQ1_GATE_A_TEMPLATE.md` | `claude/INTALIQ1_GATE_A_TEMPLATE.md` | The Gate A brief template (SC-078); field 4 carries the operative 3–5 band (SC-107); **field 3b evidence plan (SC-122)** | Adopted | ACTIVE | every Gate A brief |
| `INTALIQ1_LEARNING_EVIDENCE_TEMPLATE.md` | `claude/INTALIQ1_LEARNING_EVIDENCE_TEMPLATE.md` | Unit evidence plan and record template (§A plan · §B administration · §C observations · §D ledger · §E decision · §F integrity); copied per unit at freeze | Companion to the standard | **ACTIVE — ADOPTED SC-122** | every unit's `INTALIQ1_UNIT<n>_LEARNING_EVIDENCE_RECORD.md` |

## 3 · `lexicon-grammar/`

| file | project path | purpose | authority | status | depends on / feeds |
|---|---|---|---|---|---|
| `INTALIQ1_GRAMMAR_LEDGER.md` | `claude/INTALIQ1_GRAMMAR_LEDGER.md` | One row per structure with Alhawary subsection and page; statuses; U1 complete, U2 verified, U3 rows G-40–G-54 open (14.10 p. 258 to verify by eye) | Ledger (Architecture §26.6) | ACTIVE | Alhawary index; outcomes sheets |
| `SCHOOL_COURSE_VOCABULARY_ARCHITECTURE.md` | `claude/SCHOOL_COURSE_VOCABULARY_ARCHITECTURE.md` | Owner's Vocabulary Recycling Architecture V1–V22 (SC-058) | Owner's document, verbatim | ACTIVE | recycling map |
| `INTALIQ1_VOCABULARY_LEDGER.md` | `claude/INTALIQ1_VOCABULARY_LEDGER.md` | One row per lemma: status (six-status system, SC-075), rank/page or "lookup owed", unit, encounters; §2.10 Unit 3 rows | Ledger (Architecture §26.5) | ACTIVE | frequency manual / verified bank (inherited) |
| `INTALIQ1_CHUNK_INVENTORY.md` | `claude/INTALIQ1_CHUNK_INVENTORY.md` | Chunks CH-01 … CH-26 with status and unit | Ledger (Architecture §26.7) | ACTIVE | — |
| `INTALIQ1_FUNCTION_WORD_PROGRESSION.md` | `claude/INTALIQ1_FUNCTION_WORD_PROGRESSION.md` | Authoritative cumulative table of function words across U1–U10 (SC-082) | Adopted | ACTIVE | Gate A briefs |
| `SCHOOL_COURSE_RECYCLING_MAP.md` | `claude/SCHOOL_COURSE_RECYCLING_MAP.md` | Cumulative recycling map required by V21; per-unit sections through Unit 3 | Instrument (SC-058) | ACTIVE | vocabulary ledger |
| `SCHOOL_COURSE_L1_VERB_INVENTORY.md` | `claude/SCHOOL_COURSE_L1_VERB_INVENTORY.md` | The owner's thirty-three-verb Level 1 inventory as adopted (SC-094); `عَادَ` dropped SC-109 | Owner ruling | ACTIVE | — |
| `ALHAWARY_SECTION_INDEX.md` | `claude/ALHAWARY_SECTION_INDEX.md` | Section/page index of Alhawary (2011) for citation; bibliographic reference | Reference aid | ACTIVE | grammar ledger |

**Tense/form authorizations** are not a separate document: they are the Story Standard §E (E-1 fixed tense slots, E-2 narration past / dialogue present, SC-073) and SC-095, with licensed forms per row in the Grammar Ledger. **Frequency Manual and verified bank** are the inherited line documents in §4.

## 4 · `inherited-line/` — reader-line documents the Intaliq record cites

| file | project path | purpose | authority for Intaliq | status | note |
|---|---|---|---|---|---|
| `EDITORIAL_CONSTITUTION.md` | `claude/EDITORIAL_CONSTITUTION.md` | The reader line's (Arabic Through Stories, Book 1) permanent editorial law | **Not cited by the Intaliq register or Author's Page**; included because requested. Intaliq's constitution is the charter + Design Description; the lines inherit a method, not a document (Book 1 Ruling 9: "each product refuses to be the other") | INHERITED | — |
| `03_VOCABULARY_AND_FREQUENCY_MANUAL.md` | `03_VOCABULARY_AND_FREQUENCY_MANUAL.md` (project root) | The reader line's Vocabulary & Frequency Manual — status system, authorization, recycled-share method, B&P methodology, the recorded evidence table (bank §2 copy), §6 allocation | Cited by the Intaliq vocabulary ledger for ranks/pages ("bank §2 with rank and page") and by the reconciliation (§6 is the **reader line's** allocation, not Intaliq's — R-finding) | INHERITED (its §6 allocation does **not** govern Intaliq) | derived reference work of the Book 1 bank |
| `FREQ_VERIFICATION_L1_FOUNDATION.md` | `claude/FREQ_VERIFICATION_L1_FOUNDATION.md` | The 2026-08-08 lemma-level verification pass ("verified bank") against Buckwalter & Parkinson — ranks the Intaliq ledger accepts as recorded evidence (rank only) | Cited by the Intaliq vocabulary ledger | INHERITED | the source PDF is excluded (copyright); bibliographic reference retained in §4 of the manual |
| `BOOK1_GOVERNANCE_RULINGS_2026-09-04.md` | `claude/BOOK1_GOVERNANCE_RULINGS_2026-09-04.md` | Owner rulings for Book 1; **Ruling 9** separates the textbook product (Intaliq) from Book 1 and assigns `READING_GENERATION_PROMPT.md` to it | Ruling 9 is the product-identity ruling the Intaliq charter rests on | INHERITED (Ruling 9 ACTIVE for Intaliq) | — |
| `READING_GENERATION_PROMPT.md` | `claude/READING_GENERATION_PROMPT.md` | The 2026-09-06 paste-ready reading-generation prompt (derived from the Razanne craft record) | **RETIRED-IN-EFFECT.** Reconciliation R-12 recommends retirement; the register (entry preceding SC-071) states it "is not amended … an instrument that contradicts an operational ruling is superseded by the ruling whether or not the file says so"; its §3 existential-opener ban was overruled (R-1). Its fate is a recorded open item. | RETIRED-IN-EFFECT | **Still referenced** by `units/unit1/SCHOOL_COURSE_UNIT1_BRIEF.md` §4 ("drafted via `READING_GENERATION_PROMPT.md`") and by the register's history. Not referenced by the runbook or the Author's Page, which govern drafting today. |

**Active generation prompts:** there are none as separate files. Drafting is governed by the Author's Page and the runbook (stages 4–14), with the Gate A brief as the per-unit work order; the Unit 2 and Unit 3 texts were drafted under those, not under the prompt above.

## 5 · `units/`

### `unit1/` — «مَنْ أَنْتَ؟» (texts frozen; "pre-calibration unit", SC-093: stands as built, not the model)

| file | project path | purpose | status |
|---|---|---|---|
| `SCHOOL_COURSE_UNIT1_BRIEF.md` | `claude/SCHOOL_COURSE_UNIT1_BRIEF.md` | Unit 1 design brief v1 (Gate A proposal; rulings R-1…R-7 → SC-016–SC-023) | RECORD, masthead lags ("PROPOSED"; approved and amended by SC-016–SC-023; core later 23 items). References the retired prompt (§4). |
| `SCHOOL_COURSE_UNIT1_BUILD.md` | `claude/SCHOOL_COURSE_UNIT1_BUILD.md` | Unit 1 build: remaining components, both readings approved 2026-09-10 | RECORD |
| `SCHOOL_COURSE_U1_MAIN_STORY.md` | `claude/SCHOOL_COURSE_U1_MAIN_STORY.md` | **Canonical Unit 1 main story «قَائِمَةُ رَزَان», v8** (SC-059), with its version history v2–v8 | ACTIVE canon (also embedded verbatim in `pipeline/engine_core.js` `UNIT_01`) |
| `SCHOOL_COURSE_U1_QUALITY_GATE.md` | `claude/SCHOOL_COURSE_U1_QUALITY_GATE.md` | Blueprint rule-28 gate run on the v7 readings | RECORD |
| `SCHOOL_COURSE_U1_GAP_INVENTORY.md` | `claude/SCHOOL_COURSE_U1_GAP_INVENTORY.md` | Audit of what Unit 1 still lacked (2026-09-12) | RECORD |
| `SCHOOL_COURSE_U1_STATION.md` | `claude/SCHOOL_COURSE_U1_STATION.md` | In-class input station spec v1 (SC-023/SC-024) | ACTIVE spec, not built (no audio; platform choice open) |
| `INTALIQ1_UNIT1_LEARNER_CHECK_PROTOCOL.md` | `claude/INTALIQ1_UNIT1_LEARNER_CHECK_PROTOCOL.md` | **v2 (SC-122):** Check A cold-read diagnostic (preparation recorded; *restricted preparation* label) · Check B after the unit sequence · listening/corner not delivered · delayed probe · §9 closure rule (Route A) | Instrument | ACTIVE — **not run** |
| `INTALIQ1_UNIT1_LEARNING_CHECK_ADDENDUM.md` | `claude/INTALIQ1_UNIT1_LEARNING_CHECK_ADDENDUM.md` | The auditor's addendum (verbatim), merged into the protocol v2 | Source | RECORD (merged SC-122) |
| `INTALIQ1_UNIT1_LEARNING_EVIDENCE_RECORD.md` | `claude/INTALIQ1_UNIT1_LEARNING_EVIDENCE_RECORD.md` | Unit 1's evidence record on the template: §A plan filled; §B–§E *not run*; §D ledger technical **run** (V46) · design review **not run** · learner/delayed/transfer **not observed**; §F status line read by the gate | Record; written only by a named observer | ACTIVE (status only; no result) |
| `INTALIQ1_UNIT1_AUDIO_INTAKE.md` · `INTALIQ1_UNIT1_AUTHENTIC_CORNER_INTAKE.md` | `claude/…` | What the 72 recordings and the three photographs must be and how each is verified (SC-121) | Intake instruments | ACTIVE — nothing delivered |
| `SCHOOL_COURSE_PLATFORM_ACTIVITY_DUMP.md` | `claude/SCHOOL_COURSE_PLATFORM_ACTIVITY_DUMP.md` | Machine dump of every Unit 1 engine activity as of 2026-09-11 (title «مَنْ أَنْتَ؟», cast لِينَا) | SUPERSEDED snapshot (Unit 1 later re-cast and retitled, SC-059; engine `unit-01` title field corrected SC-106). **Removed from the repository and from the project in the 2026-10-12 cleanup**; git history (`109640f`) keeps it. The current activities are generated live by `engine_core.js`. |

Unit 1's second reading and apparatus sources live in `SCHOOL_COURSE_UNIT1_BUILD.md` and in the engine (`UNIT_01P`). There is no separate Unit 1 production record or visual plan: Unit 1 predates the runbook (SC-078) and its art was drawn in-house as SVG inside the Studio (SC-034/SC-053).

### `unit2/` — «أَيْنَ مِفْتَاحِي؟» · «صُورَةُ رَزَان وَخَدِيجَة» (texts frozen rev 6, SC-095; Gate B signed off SC-105 — closes on the pop-up ruling)

| file | project path | purpose | status |
|---|---|---|---|
| `INTALIQ1_UNIT2_GATE_A_BRIEF.md` | `claude/INTALIQ1_UNIT2_GATE_A_BRIEF.md` | Gate A brief revision 4 | RECORD, masthead lags ("awaiting Gate A approval"; Gate A approved with amendments **SC-083**, re-approved after the SC-087 rewrite at **SC-088**, texts frozen **SC-095**) |
| `INTALIQ1_UNIT2_STORY_DRAFTS.md` | `claude/INTALIQ1_UNIT2_STORY_DRAFTS.md` | Design cards, revisions, measurements, disclosures, apparatus, **§8 thirty-line Story Standard audit** (SC-105) | ACTIVE record of the frozen texts |
| `INTALIQ1_UNIT2_PRODUCTION_RECORD.md` | `claude/INTALIQ1_UNIT2_PRODUCTION_RECORD.md` | Runbook v0 trial, stages 4–13; §17–18 added at SC-104/105 | RECORD, masthead lags ("HALTED AT STAGE 13" was the 2026-09-15 state; later sections record completion) |
| `INTALIQ1_UNIT2_VISUAL_PLAN.md` | `claude/INTALIQ1_UNIT2_VISUAL_PLAN.md` | Frame-by-frame must-show / must-not-show plan for every Unit 2 image | ACTIVE as the content brief for art; masthead lags ("images not authorized" — hold lifted SC-111; two rows predate SC-097 and still say "Sara/hijab" for خَدِيجَة/plaits, reconciled in the art manifest, not in this file) |
| `canon/u2r7_s1.txt`, `canon/u2r7_s2.txt` | *(workspace files; not in the project as separate docs)* | **The frozen revision-6 texts** as the build reads them (172 / 114 words by the record's count; the engine canon is generated from these) | ACTIVE canon — also embedded in `engine_core.js` `UNIT_02` / `UNIT_02P` and printed in the drafts file |
| `unit02_data.js` | `claude/tools/…` (not stored separately; generated) | Output of `build_unit02.py`: items, phrases, activity seeds for Unit 2 | Generated; its content is merged into `engine_core.js` |
| `u2_measure.py` | *(workspace)* | CR-1 / encounter measurement script for Unit 2 revision 4 | **STALE TOOL, removed from the repository in the 2026-10-12 cleanup** — it read `u2r4_s1.txt`/`u2r4_s2.txt`, which the repository does not hold; the revision-6 measurements recorded in the drafts file were made with a later run of the same method (`u3_measure.py` is the live form of it). Git history (`109640f`) keeps it. |

### `unit3/` — «مَنْ عِنْدَهُ الْكُرَةُ؟» · «هَدِيَّةُ رَزَان» (revision 1 built, Studio Version 42, SC-110; **Gate B open — texts not frozen**)

| file | project path | purpose | status |
|---|---|---|---|
| `INTALIQ1_UNIT3_GATE_A_BRIEF.md` | `claude/INTALIQ1_UNIT3_GATE_A_BRIEF.md` | Gate A brief revision 1 | RECORD, masthead lags ("awaiting Gate A approval"; **approved SC-109** with §22 items ruled as recommended) |
| `INTALIQ1_UNIT3_STORY_DRAFTS.md` | `claude/INTALIQ1_UNIT3_STORY_DRAFTS.md` | Design cards, object-state tables, measurements, disclosure, apparatus, §8 thirty-line audit | ACTIVE draft record; awaiting Gate B |
| `INTALIQ1_UNIT3_PRODUCTION_RECORD.md` | `claude/INTALIQ1_UNIT3_PRODUCTION_RECORD.md` | Runbook stages 4–14, second trial | RECORD (open) |
| `canon/u3r1_s1.txt`, `canon/u3r1_s2.txt` | *(workspace)* | The revision-1 texts as built (158 / 118 words) | PROVISIONAL canon until Gate B |
| `unit03_data.js` | `claude/tools/build_unit03.py` output | Generated Unit 3 data | Generated |
| `u3_measure.py` | `claude/tools/u3_measure.py` | CR-1 by lemma and encounter counts for the rev-1 texts | ACTIVE tool (reads `u3r1_*.txt`, `engine_core.js`) |

## 6 · `cast-and-art/` (record only — no illustration work is part of this export)

| file | project path | purpose | status |
|---|---|---|---|
| `SCHOOL_COURSE_CAST_BIBLE.md` | `claude/SCHOOL_COURSE_CAST_BIBLE.md` | Retired as a cast instrument (SC-089); §2 house figure style (SC-053, amended SC-111) and the marker reservation table remain in force | PARTLY ACTIVE (§2, reservation table), rest SUPERSEDED and marked |
| `INTALIQ1_ART_PACKAGE_SPEC.md` | `claude/INTALIQ1_ART_PACKAGE_SPEC.md` | Intake contract for externally produced art (SC-111, TF-8) | ACTIVE |
| `art_manifest_unit2.json` | `claude/tools/art_manifest_unit2.json` | The 69-slot Unit 2 art work order | ACTIVE |
| `INTALIQ1_ART_V2_EVALUATION.md` | `claude/INTALIQ1_ART_V2_EVALUATION.md` | Evaluation of the external tool's first site build; basis of SC-111 | RECORD |
| `INTALIQ1_UNIT2_ART_ROUND1_REVIEW.md` | `claude/INTALIQ1_UNIT2_ART_ROUND1_REVIEW.md` | Round-1 acceptance review | RECORD |

## 7 · `pipeline/`

| file | project path | purpose | status | reads → writes |
|---|---|---|---|---|
| `UNIT_GENERATION_RUNBOOK.md` | `claude/UNIT_GENERATION_RUNBOOK.md` | Runbook v0 (SC-078): stages 1–14; §17 trial findings TF-1 … TF-9 | ACTIVE (v1 owed: fold TF-1–TF-9) | — |
| `INTALIQ_DEPLOYMENT.md` | `claude/INTALIQ_DEPLOYMENT.md` | How the Studio reaches GitHub Pages; the release check | ACTIVE | — |
| `school_course_studio.html` | `claude/tools/school_course_studio.html` | **The Studio source, Version 42** — the artifact body (no doctype wrapper). `index.html` and `404.html` at the repo root are this file wrapped in a page skeleton; the engine is embedded between `(function(root){` and `})(typeof window!=="undefined"?window:globalThis);` | ACTIVE source of the published site | written by `build_studio_unit03.py`; read by `build_teacher_pages.py` (assert: no teacher link) |
| `engine_core.js` | `claude/tools/engine_core.js` | The engine: six unit bundles (`unit-01`, `01p`, `02`, `02p`, `03`, `03p`) with canonical sentences, items, phrases; `gen()`, `qc()`, `canonCheck()`. QC clean 124/75/166/105/158/110 at Version 42. | ACTIVE source | read by `build_studio_unit03.py`, `build_teacher_pages.py`, `u3_measure.py` |
| `build_unit02.py` | `claude/tools/build_unit02.py` | Builds `unit02_data.js` from the frozen Unit 2 texts | ACTIVE | `u2r7_s1.txt`, `u2r7_s2.txt` → `unit02_data.js` |
| `build_unit03.py` | `claude/tools/build_unit03.py` | Builds `unit03_data.js` from the Unit 3 rev-1 texts | ACTIVE | `u3r1_s1.txt`, `u3r1_s2.txt` → `unit03_data.js` |
| `build_studio_unit03.py` | `claude/tools/build_studio_unit03.py` | Assembles the Unit 3 views into the Studio, patches the engine block, wires routes; verifies bank words against canon; idempotent | ACTIVE | `school_course_studio.html`, `engine_core.js`, `u3r1_*.txt` → `school_course_studio.html` |
| `build_teacher_pages.py` | `claude/tools/build_teacher_pages.py` | Generates the per-unit teacher's page (SC-104); asserts no answer keys and no Studio link; refuses on an undeliverable unit; reports generated vs selected-pathway counts (SC-120) | ACTIVE | `engine_core.js`, `school_course_studio.html` (assert only) → `intaliq1_teacher_pages.artifact-body.html` |
| `build_studio_art.cjs` | *(pipeline)* | **The Text build (SC-120):** refreshes Unit 2's declarations, embeds `engine_core.js` wholesale into the Studio, regenerates the `<!-- gen:… -->` blocks from engine data, verifies Unit 2 art hashes, runs the teacher generator, writes `index.html`, `404.html`, `teacher.html`; refuses on any undeliverable unit. `INTALIQ_STUDIO_VERSION=<n> node source/pipeline/build_studio_art.cjs` | ACTIVE | `engine_core.js`, `school_course_studio.html`, `unit02_data.js`, `art_assets_map.json`, `manifest.json` → root `index.html`, `404.html`, `teacher.html`; `build_report.json` |
| `intaliq1_teacher_pages.artifact-body.html` | *(generated; the project's former copy `claude/tools/intaliq1_teacher_pages.html` was deleted 2026-10-12 — the build regenerates it)* | Teacher's pages, body (Units 1–3). **The generator now writes this name itself** (SC-120): the former pair `intaliq1_teacher_pages.html` / `Intaliq1_Teacher_Pages.html` differed by letter case only and collided on macOS/Windows. | Generated (ACTIVE) | — |
| `verify_release.py` | `claude/tools/verify_release.py` | Release gate (TF-9, extended SC-120): renders every route, **walks every digital pathway to its end**, checks Unit 1 print-task response resources and quotation drift, unresolved `<use>` refs, learner-view hiding, and runs **mutation tests against the deployed engine**; blocks on broken images, missing assets, teacher links, "answer key", wrong version chip | ACTIVE | `deploy/` folder → `verify_report.md`, screenshots |
| `test_listening.js` | *(pipeline)* | Fixture test of the listening machinery (F9): complete bindings → deliverable and sound-first; each malformed binding → withheld. No recording involved (SC-121) | ACTIVE | `engine_core.js` → stdout; re-run by the gate against the deployed engine |
| `../units/unit1/apparatus_licence_u1.json` | *(unit1)* | Every learner-visible Arabic token on the Unit 1 pages beyond the canons, with its authority; the gate's language sweep reads it (SC-121) | ACTIVE | — |
| `../units/unit1/audio/clips_manifest.json` | *(unit1)* | 72 clip rows generated from the engine (text to record, expected path); `sha256` / `verified_by` empty until recordings exist (SC-121) | ACTIVE — **unfilled** | `engine_core.js` → manifest |
| `run_qc.js` | *(pipeline)* | Node harness that loads **`engine_core.js`** and reports QC, deliverability and pathway counts per unit; exit 1 on any withheld unit (SC-120) | ACTIVE | `engine_core.js` → stdout |
| ~~`engine_test.js`~~ | — | **Removed 2026-10-10 (SC-120)** — a Unit-1-era fixture that `run_qc.js` used to load; a pass against it verified nothing about the deployed engine (audit §11) | REMOVED | — |

**Production / version record:** Studio Versions are issued in the register entries (V39 SC-104, V40 SC-105, V41 SC-106, V42 SC-110, V43 SC-115, V44 SC-117, V45 SC-120 (built, never pushed), **V46 SC-121**; Text session only per SC-112; sequence held in the project register, SC-118). Earlier Studio versions V32–V41 exist as files in the workspace and are **not** included (superseded builds; available on request).

---

## 8 · Owner decision carried forward — **recorded as SC-119 on 2026-10-10**

Recorded here verbatim as supplied by the owner on 2026-10-02 for the subsequent correction batch, without a decision number at the time; **it is now SC-119** in the project register, and its cascade (Activity Architecture §2, P-3, §3 C, §5; Unit 1 Build §9.1; the Studio's tour and Unit 1 notebook; the teacher generator's flows for all three units; runbook stage 11) was made in the Version 45 pass (SC-120):

> Scaffolded interaction, including C1, occurs before notebook writing; Phase 5 is reserved for fuller communication and transfer. The survey therefore runs before parallel-story writing.

Its cascade, when recorded: Activity Architecture §2 (phase order) and §3 C; runbook stages 12–13 (notebook build after the C-format placement); the teacher's page flow (`build_teacher_pages.py` UNITS flows); the Unit 2 and Unit 3 teacher's pages regenerated.

## 9 · Not included, and why

- **Copyrighted reference works** — Buckwalter & Parkinson, *A Frequency Dictionary of Arabic* (Routledge, 2014; ISBN 9780203883280) and Alhawary, *Modern Standard Arabic Grammar: A Learner's Guide* (Wiley-Blackwell, 2011; ISBN 9781405155014): PDFs excluded; references retained in `ALHAWARY_SECTION_INDEX.md` and `03_VOCABULARY_AND_FREQUENCY_MANUAL.md` §4.
- **The reader line's other documents** (Book 1 / Judhuree: `READER_*`, `VOLUME_*`, `SERIES_BIBLE`, `CURRICULUM_FRAMEWORK`, `LEVEL_SPEC_L1_v2`, `01_…`, `02_…`, `04_…`, `05_GOVERNANCE_REGISTER`, `DECISION_REGISTER.md` (Book 1), `GOVERNANCE_AMENDMENT_00x`, `STORY_CRAFT_CONDITIONS`, `LESSONS_FROM_LEVEL_ONE`, `VISUAL_GOVERNANCE`, `ROLES_AND_AUTHORITY`, `PROJECT_CHARTER`, `tools/build_reader.py`, `build_volume.py`, `build_deck.py`, `build_pilotpack.py`, `make_mockup.py`, `established_share.py`, `SNAPSHOT*_lexicon.txt`): a different product; not cited by the Intaliq record except as noted in §4.
- **`SAMPLE_LESSON_S1_L1.md`** — reassigned to the script manual (a third product) by ruling; not Intaliq.
- **Superseded Studio builds** V32–V41 and superseded text revisions (`u2_s1.txt`, `u2r4–r6_*.txt`, `v7_*.txt`, `story2_v8.txt`): history recorded in the drafts files; available on request.
- **Workspace scratch** (OCR text of the references, measurement outputs, verification screenshots).
- **Nothing was unavailable that the record names as existing**, with two exceptions already stated: the owner's Architecture text exists only as pasted prose inside the session that adopted it (its adoption is in the register; its content is reflected in the instruments it spawned), and no "tense/form authorizations" document exists apart from the Story Standard §E, SC-073/SC-095 and the Grammar Ledger.

## 10 · Private information and credentials

None present. The platform keeps no accounts or profiles for children (SC-048 item 7); no student data exists anywhere in the record. No tokens, keys or passwords are in any exported file.
