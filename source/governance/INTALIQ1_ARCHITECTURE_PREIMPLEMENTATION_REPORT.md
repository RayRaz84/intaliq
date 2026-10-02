# Intaliq 1 — Architecture adoption: pre-implementation report

*Required by §30 before any project document is rewritten · 2026-09-13 · **nothing in the project has been changed.** Counts are machine-generated from the built unit and the engine data; evidence claims are tested against the actual sources, not assumed.*

---

## 0. The two evidence tests, run first

| source | in project? | machine-readable? | consequence |
|---|---|---|---|
| **Buckwalter & Parkinson, frequency dictionary** | Yes | **Yes** — 1.79M characters of extractable text | Rank citation is possible |
| **Alhawary, *MSA Grammar: A Learner's Guide*** | Yes | **No — extracts as empty** | **Grammar Ledger cannot be completed** |

**The frequency dictionary works, with a caveat.** Ranks are recoverable and I verified three by hand against the extracted text: **قَلَم 1021** · **وَلَد 362** · **بِنْت 252** (the last confirmed twice, from the main index and a thematic table). But PDF extraction scrambles Arabic letter order and displaces diacritics, so **no automated sweep is trustworthy** — every lemma needs individual eyeball verification, and some entries do not extract cleanly at all. Of six test lemmas, **two failed to resolve**: صَدِيق and أَرَادَ returned only sample-sentence occurrences, not their headword entries. Both are certainly *in* the dictionary; the extraction simply did not surface them. They would need a different route (alphabetical index, thematic tables) or manual lookup.

**Alhawary returns nothing.** The PDF is image-only — no text layer. §3 requires *"the exact Alhawary subsection and printed page number for every Grammar Ledger entry"* and forbids leaving *"reference to be confirmed"* in the final ledger. **I cannot produce a single compliant Grammar Ledger row from the copy in the project.**

Worth knowing: the reader series never cited it either. Every grammar row in `READER_001_DESIGN_BRIEF` reads *"exact section ref to be confirmed at Gate 2."* **Alhawary has never been cited anywhere in this program.** §3 has just made that state non-compliant rather than merely untidy.

---

## 1. Proposed changes, by file

*Nothing done. This is the plan awaiting your approval.*

| file | change |
|---|---|
| `EDITORIAL_CONSTITUTION.md` | Add Intaliq 1 architecture as Part X; insert the §3 authority hierarchy; add the four lexical statuses and five grammar statuses; add the §11 counting rules |
| `SCHOOL_COURSE_CHARTER.md` | **O-4** rewritten: pacing is proficiency-oriented and calendar-flexible; the 75-hour floor is removed as a book-level requirement and demoted to implementation guidance. **O-6 locked at ten units** |
| `SCHOOL_COURSE_L1_SCOPE_AND_SEQUENCE.md` | Eight units → ten; budget bands replaced by §5–§8 figures; LC-1/LC-2 subordinated; deferred list reconciled with §20 domains and §21 bands |
| `SCHOOL_COURSE_VOCABULARY_ARCHITECTURE.md` | Rewritten to the four statuses; V-rules retained where compatible, superseded where not |
| `SCHOOL_COURSE_TWO_STORY_BLUEPRINT.md` | Design cards gain the §18 grammar fields and §15 chunk fields; rule 28 gate gains §23 assessment rules |
| `SCHOOL_COURSE_RECYCLING_MAP.md` | Re-scoped to ten units; §25 four-return requirement and §9 recycled-item fields added |
| `SCHOOL_COURSE_ACTIVITY_ARCHITECTURE.md` | §23 assessment rules added as binding constraints on the closed catalog |
| `SCHOOL_COURSE_ACTFL_ALIGNMENT.md` | Audited against §2's permitted and prohibited wording |
| **NEW** `INTALIQ1_VOCABULARY_LEDGER.md` | Created (§26.5) |
| **NEW** `INTALIQ1_GRAMMAR_LEDGER.md` | Created (§26.6) — **blocked on Alhawary** |
| **NEW** `INTALIQ1_CHUNK_INVENTORY.md` | Created (§26.7) — none exists today |
| **NEW** `INTALIQ1_TEN_UNIT_TABLE.md` | The §28 planning table |
| `tools/school_course_studio.html` · `engine_core.js` | **Data-model change** — see conflict **H** |

---

## 2. Conflicts found

### A · **Past tense from Unit 6 contradicts SC-041 and the built unit** — the largest conflict

> ⟨**HISTORICAL RECORD — CLOSED BY SC-073, 2026-09-15.** This section states the conflict as it stood on 2026-09-13 and its options are superseded. The ruling: Story 1 present, Story 2 past, **in every unit from Unit 1**. §20K's Unit-6 clause survives only as a schedule for **explicit and productive** past work; it is void as a bar on past narration in Story 2, and §21's assumption that Unit 6 carries the past-tense introduction is void with it. Preserved unedited below.⟩

§20K: *"Units 1–5 remain present/imperfect-based… Beginning in Unit 6, selected high-frequency past-tense forms may be introduced."*

**SC-041 puts past narration in every unit's second reading from Unit 1**, and Unit 1 is built that way: دَخَلَ · قَالَ/قَالَتْ · رَأَى are productive in the second reading right now, with 17 platform activities among them.

§20K allows *"unless an earlier explicit ruling authorizes a specific exception"* — SC-041 is precisely such a ruling. But the two cannot both stand as written: either SC-041 survives as the standing exception and §20K applies from Unit 2, or SC-041 is withdrawn and **Unit 1's second reading must be rewritten in the present**, which also unwinds the tense law that four rulings depend on. **This needs your word before anything else moves.**

### B · **Ten units against an eight-unit map, and two rulings placed on the old scale**

§26.2 locks ten. The working map's affordance ordering fills eight. Two units must be added, or the existing eight respread — and **SC-060/061 placed the dual, سَوْفَ and الَّذِي/الَّتِي at U5/U6 on the eight-unit scale two hours ago.** Those placements are now against a different ruler and should be re-decided rather than carried over arithmetically.

### C · **§11's counting rules break the engine's data model**

§11 requires lemmas, forms and chunks counted separately: *"يَذْهَبُ، تَذْهَبُ، أَذْهَبُ are licensed forms of one lemma, not three vocabulary words."*

The Studio's item table has **no lemma/form distinction.** It stores `تَدْخُلُ` and `دَخَلَ` as two items, `تَرَى` and `رَأَى` as two, `تَقُولُ` and `قَالَ` as two, `لِي` and `لَهَا` as two, `عِنْدَهَا` and `عِنْدَهُ` as two. Under §11 those ten items are **five lemmas**. Every count the platform has ever reported is therefore a form count wearing a lemma label.

This is a schema change, not a relabel: the engine needs `lemma`, `form`, and `chunk_ref` fields, and the QC needs to count lemmas for budget and forms for licensing. **Affects `engine_core.js`, the Studio, the activity dump, and every figure in the recycling map.**

### D · **No Chunk Inventory exists, and Unit 1 is running chunks unlicensed**

§26.7 says *"create or repair."* It is create — there is none. Meanwhile Unit 1 operates at least five de-facto chunks with no licensing record: «السَّلَامُ عَلَيْكُمْ / وَعَلَيْكُمُ السَّلَامُ» · «لِي صَدِيقٌ: ___!» (the signature frame, four speakers) · «لَيْسَ عِنْدِي ___» · «هُنَاكَ اسْمٌ: ___» · «أُرِيدُ ___». §15 requires each to record function, wording, permitted variation, slots, status and recycling obligations. None has any of that.

### E · **The 75-hour floor and O-4**

§1 removes it as a book-level requirement. Charter O-4 currently reads *"stated minimum contact-hours floor — the number the pacing must survive."* The item does not disappear; it changes character, from a gate to guidance.

### F · **Naming**

§1 names the course **Intaliq 1**. Every instrument in the project is named `SCHOOL_COURSE_*`, and a separate `INTALIQ_DEPLOYMENT.md` exists. Either the files are renamed (breaking every internal cross-reference, of which there are dozens) or a one-line alias is recorded. **Recommend the alias**; renaming buys nothing and costs a day.

### G · **Budget supersession, and it roughly doubles the level**

> ⟨**SUPERSEDED BY SC-107, 2026-09-27.** The 220–260 target and the 18–26-per-unit figure govern nothing; the operative band is 3–5 new core per unit, and no level total is claimed until measured. Preserved as recorded.⟩

Old: ≈120–150 active total across eight units. New: **220–260 productive core lemmas** across ten, plus 30–50 recognition, 60–100 support, 50–70 chunks. Internally consistent (§6's 18–26 per unit × 10 ≈ 220–260 ✓). Recorded as a deliberate supersession, not a drift.

### H · **ACTFL wording not yet audited**

`SCHOOL_COURSE_ACTFL_ALIGNMENT.md` predates §2's prohibited phrasings. It has **not** been checked for claims of the *"Unit 6 equals Novice Mid"* type. Flagged as an audit task, not asserted as a defect.

---

## 3. Definitions that remain ambiguous

1. **"Anchor target" vs "productive core."** §6 gives 8–12 anchors *and* 18–26 total new productive lemmas. Anchors are a subset receiving *"the most intensive input, interaction, retrieval, and recycling"* — but no threshold separates them. **Proposal: an anchor is any item carrying ≥3 encounter-channels and appearing in both readings.** Awaiting your definition.
2. **"Licensed reusable chunk" (§12, 50–70) vs "new chunks" (§6, 3–7 per unit).** 3–7 × 10 = 30–70, which reaches the range only at the top. Is 50–70 the target or the ceiling?
3. **§20N case and mood endings.** The section explicitly returns this as an editorial decision if unsettled. **It is unsettled.** The working map says case endings are *"printed correctly and absorbed, never explained"* — that covers orthographic presence and reading support but says nothing about oral realization, recognition, or assessment, which §20N asks to separate.
4. **"Sufficient recycling" before assessment (§23).** No number. §25 names four required returns; is all four the threshold?
5. **Chunk components and the lemma total.** §11 says do not recount a chunk's components. But «أُرِيدُ ___» contains أَرَادَ, which is *also* productive core in Unit 1 on its own. Does it count once, or is the chunk separate?

---

## 4. Unit 1 audit (§27)

*Measured from the engine data as built today. Reported, not repaired — §27 forbids changing Unit 1 to make its numbers match later units.*

| § | measure | Unit 1 | §6 range | |
|---|---|---|---|---|
| | **tracked lexical items (engine's own count)** | **26** | — | |
| §11 | **productive core lemmas** *(after collapsing forms)* | **≈16** | 18–26 | **below — permitted by §5** |
| §10 | productive function words *(within the above)* | **7** — هُنَاكَ · مَنْ · لَيْسَ · أَنَا · لِـ · عِنْدَ · أَهْلًا | — | |
| §6 | anchor targets *(≥5 activity channels)* | **11** | 8–12 | ✓ |
| §7 | recognition items | **2** | 3–5 | below |
| §8 | support items | **3** — قَائِمَة · فَصْل · قَلَم | 6–10 | below |
| §14 | chunks | **≈5, none licensed** | 3–7 | **unlicensed** |
| | **unclassified vocabulary** | **0** | — | ✓ |

**Licensed forms, by lemma.** دَخَلَ → تَدْخُلُ + دَخَلَ · رَأَى → تَرَى + رَأَى · قَالَ → تَقُولُ + قَالَ + قَالَتْ · لِـ → لِي + لَهَا · عِنْدَ → عِنْدَهَا + عِنْدِي + عِنْدَهُ · أَرَادَ → أُرِيدُ · أَحَبَّ → تُحِبُّ · تَكَلَّمَ → يَتَكَلَّمُ. **Twenty-one forms across eight verbal/relational lemmas.** Every one of these is a §17 licensing decision that has never been recorded as one.

**Grammar status of every form: unrecorded.** No form in Unit 1 carries `G-new_productive`, `G-input_first`, `G-recognition` or any other status. The course has been operating a four-way *lexical* status system and **no grammatical status system at all.**

**Alhawary references: none exist, and none can be produced** from the copy in the project.

**Recycling obligations:** recorded for U1 in the Recycling Map with planned ⟨U2⟩ and ⟨U3+⟩ returns, but §25's four-return requirement (in-unit · near · delayed cumulative · cross-modal) is met for **none** of the 16 lemmas, because units 2+ do not exist.

**Assessment mismatches:** the platform assesses **قَلَم** (support, 13 activities) as heavily as any core item. §23 forbids requiring productive use of support vocabulary. The activities are recognition-type, so this is a **risk, not yet a breach** — but it becomes one the moment a productive task uses it.

**Forms exceeding the current license:** none detectable, because no license exists to exceed.

**Unnatural Arabic caused by the ceiling:** one, already on record — the rule-19 residue. Nine of sixteen narration clauses are [verb] + لِينَا, driven by encounter floors that reward a countable printed subject. §24 now reinforces rule 19, and the residue is structural: reducing it further means fewer speaker alternations, not line edits.

---

## 5. Proposed ten-unit lexical budget

*Derived from §5–§8. Unit 1 column is measured; all others are proposed.*

| unit | new productive lemmas | function words | anchors | recognition | support | chunks |
|---|---|---|---|---|---|---|
| 1 *(built)* | **16** ✱ | 7 | 11 | 2 | 3 | 5 unlicensed |
| 2 | 18–20 | 3–4 | 8–10 | 3 | 6–8 | 5–6 |
| 3 | 20–24 | 3–4 | 9–11 | 4 | 6–8 | 5–7 |
| 4 | 22–26 | 2–3 | 9–12 | 4 | 7–9 | 5–7 |
| 5 | 22–26 | 2–3 | 9–12 | 4 | 7–9 | 5–7 |
| 6 | **18–22** ↓ | 2–3 | 8–10 | 4 | 6–8 | 4–6 |
| 7 | 22–26 | 2–3 | 9–12 | 5 | 7–9 | 5–7 |
| 8 | 22–26 | 2 | 9–12 | 5 | 7–9 | 5–7 |
| 9 | 24–28 | 2 | 10–12 | 5 | 8–10 | 6–7 |
| 10 | 20–24 | 1–2 | 8–10 | 4 | 6–8 | 4–6 |
| **total** | **≈224–258** ✓ | ≈26–30 | — | **≈40** ✓ | **≈64–81** ✓ | **≈49–66** ✓ |

✱ Unit 1 sits below the band under §5's literacy allowance. **Unit 6 is deliberately reduced** — §19 requires the lexical load to fall when structural complexity rises, and Unit 6 carries the past-tense introduction under §21. Every total lands inside §12's ranges.

---

## 6. Proposed ten-unit grammar progression

# **BLOCKED.**

I can propose a *dependency shape* from §20–§21 — which is your own text, not evidence — but **I cannot produce a Grammar Ledger**, because §3 and §18 require an exact Alhawary subsection and printed page for every row and the source will not yield one.

Producing this section without the guide would mean asserting a grammatical sequence from my own judgement under an authority that exists specifically to prevent that. **§30's final instruction forbids it:** *do not invent missing evidence; do not use placeholder citations in the final ledgers.*

**Three ways to unblock, for your decision:**

| option | what it costs | what it gives |
|---|---|---|
| **(a)** Supply a text-layer copy of Alhawary *(OCR or another edition)* | Your time sourcing it | **Full compliance.** Recommended |
| **(b)** You supply subsection + page per structure as each unit reaches Gate A | Your time, ten times | Compliant, but slow and serialized |
| **(c)** Build the ledger with `ALHAWARY_REF: PENDING` and fill later | Nothing now | **§3 explicitly forbids this as an end state.** Acceptable only as an interim marked as non-compliant |

---

## 7. Proposed chunk progression

Deliverable and not blocked — §14–§15 need no external source. **Proposed shape:** Units 1–3 carry the highest chunk density (5–7 each), because §21 makes chunks the foundation band's main vehicle; Units 4–5 fall to 5–6 as recombination replaces holistic use; Units 6–8 hold at 4–7 with new chunks weighted toward temporal anchors; Units 9–10 fall to 4–6 as connected sentences take over.

**Unit 1's five existing chunks would be licensed retroactively**, each with §15's full record. The signature frame «لِي صَدِيقٌ / صَدِيقَةٌ: ___!» is the clearest case: it already has a fixed part, a variable slot, four speakers using it, and a recycling role — it has been functioning as a licensed chunk without the licence.

---

## 8. Outstanding Gate A decisions (§29)

*Each with the conflict, the affected files, options, a recommendation, and consequences.*

**1 · Past tense from Unit 6 vs SC-041.** ⟨**CLOSED BY SC-073, 2026-09-15** — the ruling went beyond option (i): Story 1 present, Story 2 past, in every unit from Unit 1. Preserved as written.⟩ *(Conflict A — decide first; the others are cheap by comparison.)* Affects both Unit 1 readings, the engine data, SC-041/046/052/055/056/059, the blueprint's tense law, and §21's bands. **Options:** (i) SC-041 stands as §20K's named exception — Unit 1 keeps its past reading, §20K governs from Unit 2; (ii) SC-041 withdrawn — Unit 1's second reading rewritten in the present, four rulings unwound; (iii) SC-041 narrowed to Unit 1 only as a legacy exception, §20K governs Units 2–10. **Recommend (i).** The two-story tense contrast is the structural idea the whole blueprint rests on, it is built and validated, and §20K's own wording anticipates exactly this exception. (ii) costs the most and gains a consistency nobody asked for.

**2 · Dual and plural policy.** §20L defers it explicitly. **Options:** (i) plurals lexically only through Unit 10, dual deferred to Level 2; (ii) dual at Unit 5 per SC-060; (iii) sound plurals productive from Unit 7, dual receptive from Unit 8. **Recommend (i)** — §20L's own warning is that exposure to plural words must not be read as licensing plural formation, and a ten-unit Novice course has better uses for the room.

**3 · أَنْتَ / أَنْتِ pacing.** **Options:** (i) both from Unit 1 as now built; (ii) أَنْتَ from Unit 1, أَنْتِ from Unit 2. **Recommend (i)** — both are already in Unit 1's story and working; splitting them now would make the built text non-compliant to no purpose.

**4 · Rule 23's oral TPRS phase vs the absence of a teacher book.** Unchanged from SC-057 and still open. **Options:** (i) the oral phase is classroom practice the course assumes, binding the author's design not the product's contents; (ii) one printed sheet of circling questions per unit; (iii) reopen SC-045. **Recommend (i)** — cheapest, keeps SC-045 intact, and §22's input-first sequence describes teaching rather than pages.

**5 · قَائِمَة · فَصْل · قَلَم classification.** **Recommend:** فَصْل and قَلَم **promote to core at their next return** — a classroom is where every story in this course happens, and قَلَم already carries 13 activities, which is core-level exposure in everything but name; قَائِمَة **remains support**, tied to one story's plot.

**6 · Case and mood endings (§20N).** Genuinely unsettled. **Options:** (i) orthographic presence + reading support only, no recognition or productive expectation anywhere in Intaliq 1; (ii) add recognition of the three short-vowel case markers from Unit 7; (iii) defer entirely to Level 2. **Recommend (i)** — it matches what the course already does and §20N asks only that the distinction be *stated*, not that expectation be added.

**7 · نُور's gender.** Still open from SC-054. **Recommend girl** — it balances the roll four and four, and the marker vocabulary settles it on sight.

**8 · Diacritic-removal progression.** §29 names it; **nothing in the School Course authorizes any taper.** The reader series has one (`VOLUME_FRONT_MATTER`: full vowelling in story 1, tapering after). The working map says *"full vocalization throughout Level 1."* **Recommend: no taper in Intaliq 1**, and record that the reader series' taper does not transfer.

---

## 9. Claims I cannot support with the supplied evidence

1. **Any Alhawary reference whatsoever.** The copy in the project has no text layer. Every grammatical placement in §20–§21 is *your* specification, and I can implement it — but I cannot cite the authority that §3 says governs it.
2. **Frequency ranks for صَدِيق and أَرَادَ.** Both failed to resolve in the extracted text. I know approximate ranks for both from training; **§13 prohibits asserting them**, so they are recorded as unresolved rather than guessed.
3. **Any rank for the remaining ~19 Unit 1 lemmas.** Not yet attempted at scale. Given the extraction quality, expect roughly **10–20% to fail** and need manual lookup.
4. **That ten units is the right number.** §26.2 locks it and I will implement it; nothing in the evidence derives it, and the charter's contact-hours question that would have informed it is being removed rather than answered.
5. **That Unit 1's ≈16 lemmas is the right load.** §5 permits a lighter Unit 1; whether *this* is the right lightness is a judgement no source settles.
6. **Any ACTFL performance claim.** §2 permits "targets Novice Mid"; I have no learner data, and the existing alignment document has not been audited against §2's prohibited wording.
