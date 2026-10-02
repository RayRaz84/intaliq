# Book 1 Governance Rulings — 2026-09-04

*Arabic Through Stories — Book 1 (the classroom textbook program) · rulings by M. Adam Ziad, Program Owner, recorded 2026-09-04 in the "Arabic Reader serries" project · resolves items from `05_GOVERNANCE_REGISTER.md` (compiled 2026-08-06) · this document IS the record of decision the register's §5 asked for*

**Standing caveat.** These rulings were made from the register's own descriptions of each conflict, without the repository in hand. Each ruling binds the *decision*; the session that implements it in the repository must verify the register's account against the actual files before acting, and return here if the facts differ. No ruling below may be extended by analogy to a conflict not named in it.

---

## Ruling 1 — C-1: the relayed approvals of 2026-07-23

**Ruled: ratify Units 2 and 3; re-open Unit 4's gate.**

The relayed verbal approvals of Units 2 and 3 are hereby converted into a recorded Adam gate decision, effective today — their authority now rests on this document, not on the relay. Unit 4 is **not** ratified: its own approval file lists four items as "Adam ruling required," and a unit cannot be approved past its own open items. Unit 4 returns to an OPEN gate until those four items are presented and ruled.

Consequences: the production board and gate register are updated to show Units 2–3 gate-passed (citing this ruling) and Unit 4 OPEN. The 61 generated files' banners become true for Units 2–3 and must be removed or corrected for Unit 4.

## Ruling 2 — C-2(a): a cumulative-reading band of its own

**Ruled: cumulative readings get their own band — recycled share ≥75%, no ceiling.** This supersedes the earlier F-02 resolution ("band NOT extended"), on the record and deliberately.

Rationale of record: the 70–85% band was designed for teaching readings, where the ceiling forces the novelty budget to be spent. A cumulative reading introduces no new core by design; its high recycled share is its function, not a breach. The floor stays so the reading remains an integration test.

Consequences: Unit 3's cumulative (85.1% cumulative-scoped) and Unit 4's (91.2%) are compliant as shipped. The "cumulative-scoped metric" used in Unit 3's QC is **authorized as the metric for cumulative readings only**; the core metric remains authoritative for all other readings. The uncited "≥75% (substantial)" gate in Unit 2's QC is retroactively regularized as this band. M-1 is closed.

## Ruling 3 — C-2(b): Unit 2 Story B at 68.9%

**Ruled: accepted as a documented scoped exception.** 1.1 points below the floor on a corrected, shipped reading is measurement noise, not a design failure. The exception is scoped to this reading in its 2026-07-20 state; any future revision of the reading re-enters the ordinary band. The 70% floor remains binding for all new work.

## Ruling 4 — R-2: banner separation (adopted as law)

**Ruled: build tooling may never emit or assert an approval banner.** Banners are read from a status record the tooling cannot write; verification asserts *that the record says approved*, not that a string is present. The uncommitted `generate.mjs` / `verify.mjs` modifications that hardcode the banner string are to be reverted or rewritten to read from the status record. (This answers M-17; M-16 is answered by Ruling 1's method — a relay becomes valid only when converted into a recorded decision like this one.)

## Ruling 5 — R-7: no approvals against a dirty tree (adopted as law)

**Ruled: no approval is recorded against an uncommitted working tree.** The 130 uncommitted paths (C-12) are to be committed or formally parked before any new gate is run. Files cited as ACTIVE PRODUCTION SOURCES may not exist only untracked.

## Ruling 6 — R-8: the second-person homograph check (adopted as law)

**Ruled: adopted.** The تَجِدُ / تَبْحَثُ عَنْ second-person homograph risk becomes a standing named line on the unit QC checklist itself, assigned to human QC, so it cannot be lost behind a green mechanical gate.

## Ruling 7 — C-3: the six-reading ceiling is law

**Ruled: the six-reading architecture is reaffirmed.** The older component lists in `governance/04`, `06`, `10`, and `17_book_design…` (Parallel Story 2, mini-story bank as student-book defaults) are **superseded wholesale**; the consolidation (see Disposition below) retires them rather than amending them in place. Displaced readings continue to route per the existing displaced-material rule.

## Ruling 8 — C-4: rebuild the board from disk

**Ruled: the production board is rebuilt from an audit of actual unit state**, unit by unit, citing what exists on disk and in what QC state. The authority rule is made explicit: only Adam's recorded decisions change authority cells (stage, targets, open-decision cells); a working session may update progress cells only with a citation to the artifact that proves the change. Until the rebuild, the board is not to be trusted or cited.

## Ruling 9 — Product identity: the سلوى textbook is a different book

**Ruled: the beginner textbook containing the سلوى reading is a separate product from this corpus's Book 1.** Consequences:

- `claude/READING_GENERATION_PROMPT.md` (2026-09-04) governs the **new** textbook as written, including its past-tense authorization.
- Book 1's excluded-by-design past-tense ban (M-11) is **untouched** and remains in force.
- The new textbook requires its own charter and scope-and-sequence before unit production; it inherits nothing from Book 1's governance automatically, and each product refuses to be the other.

## Ruling 10 — C-8: renumber in consolidation

**Ruled: the rank-19 `governance/17_book_design_and_page_architecture_blueprint.md` is renumbered** as part of the consolidation; the collision with the top-four `governance/17_unit_story_production_protocol.md` disappears. Until then, citations use full filenames.

---

## Disposition: consolidation, not amendment

Per the Owner's 2026-09-04 decision preceding these rulings: the governance corpus is to be **consolidated into a single binding constitution** that restates every still-valid rule, incorporates these rulings, and declares the old corpus superseded and archival. The built units then get one audit against the new document (conforming / scoped exception / to-revise). These rulings are inputs to that consolidation; where a ruling and an old file conflict, the ruling governs.

---

## Still open — requires the repository, not a decision

These register items cannot be responsibly ruled from descriptions alone; they need the underlying files brought into a session (the whole repo, or the named files):

| Item | What it needs |
|---|---|
| C-5, C-6, C-7 + Q-3 — the interlocking allocation rulings (يَأْخُذُ authority · Unit 6 identity · Unit 7 gap · reallocating يَسْمَعُ and مَعَ) | `book1_high_frequency_structure_bank.md`, the `unit_04/06/07_*.json` inventories, the board's target rows — presented together as one batch per governance/26 §4 |
| C-10 — Unit 2 Story B mother-dialogue | the actual dialogue lines from `unit_02_prose_qc.md` |
| C-11 — illustration style wording | the proposed flat picture-book lock wording from Unit 2's Stage-6 package |
| Q-1 — Unit 5 phrase gate | `unit_05_phrase_gate_spec.md` (implementation + mutation testing plan) |
| Q-2 — Unit 5 culture topic | the candidate topics/sources, if drafted |
| Q-4 — Unit 10 capstone design | the board's U10 row and capstone options |
| Q-5 — Harakat Stages 4–5 | `governance/14` §4 |
| Unit 4's four open items (per Ruling 1) | `⚠_REQUIRES_ADAM_CONFIRMATION.md` contents |

Blocked-work map after these rulings: Units 2–3 stand approved; Unit 4 awaits its four items; Unit 5 stays blocked on Q-1/Q-2; Units 6–7 on the allocation batch; 7–10 additionally on Q-5; image generation on C-11.
