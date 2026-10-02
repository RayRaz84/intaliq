# Document 3 — Vocabulary & Frequency Manual

*Vocabulary authorization and frequency methodology*
*Arabic Through Stories — Book 1*

```
DERIVED REFERENCE WORK — CREATES NO NEW PROJECT AUTHORITY
No rank, page, status, or authorization in this document is new. Every one is reproduced from
book1_high_frequency_structure_bank.md §2 or the records cited beside it.
All Arabic below is planning reference only, never learner-facing text.
```

---

## §1 — The Status System

### 1.1 The four statuses

Every Arabic item in a unit carries **exactly one** of four statuses, assigned in the unit inventory.

| Status | Code | What it means | What it costs | What it permits |
|---|---|---|---|---|
| **Core target** | CORE | The unit's new acquisition objective | Consumes the 3–5 target budget | Plot-bearing use; carries recycling obligations; may be recognized in assessment in context |
| **Recycled target** | — | A core target introduced in an earlier unit | Free | Full use; counts toward the recycled numerator |
| **Support chunk** | SUP | Established language that supports meaning but is not an objective | Free | Props, settings, scaffolding — **may not carry the causal chain** |
| **Recognition-only** | REC | Ambient language the learner meets but is never held to | Free | Ambient presence only — **never assessed; never promoted silently** |

Plus one cross-cutting category:

| **Controlled dialogue chunk** | DLG | A fixed phrase admitted so dialogue can sound natural | Free | Fixed use only; **never productive** unless separately approved; must be listed and classified in prose QC |

Sources: `book1_recycling_and_retention_protocol.md` §6; `book1_high_frequency_structure_bank.md` §4;
`book1_vocabulary_frequency_baseline.md` §§1–3; `governance/02` §"Controlled Dialogue Chunk Policy".

### 1.2 The three rules that make the system work

**1.2.1 Status does not drift.**
> "The four statuses — core target, recycled target, support chunk, recognition-only — are assigned in
> the unit inventory and may not drift." — `recycling protocol` §6

**1.2.2 Appearing in a reading does not make a word a target.**
> "Appearing in a reading does not make a word a target." — ibid.

This is the anti-inflation rule. A support noun used forty times is still support.

**1.2.3 Promotion is a decision, not a consequence.** Promotion of any support or recognition item to
core is a **map-level decision requiring approval**, and it triggers "a full recycling path from the
promotion unit onward." — ibid.

Recorded promotion cases, each requiring its own gate: `يُسَاعِدُ` (legacy recognition → U8 core),
`كَبِيرٌ/صَغِيرٌ` (legacy recognition → U9 core), `أُرِيدُ` (approved dialogue/PQA chunk → U6 core),
`ثُمَّ` (legacy support chunk → U2 core, approved at the U2 gate 2026-07-07).

### 1.3 Productive vs. receptive — how this project draws the line

The project does not use the words "productive" and "receptive" as its primary axis. It uses
**acquisition status** (the four above) plus **explicit per-item use conditions**. The mapping is:

| Repository formulation | Conventional term |
|---|---|
| "core target" = *an input-acquisition status, not a grammar-production requirement* (`architecture QC` Gate 6) | acquisition objective |
| `INPUT-FIRST ONLY` condition on `عِنْدِي / لَيْسَ عِنْدِي` (B-PA5) | receptive-first; production needs a later, separate approval |
| "meaningful chunk only — never presented, drilled, or assessed as a conjugation sequence" (`أُرِيدُ`, B-PA6) | productive as a lexical chunk, not as a paradigm slot |
| "non-productive unless separately approved" (all controlled dialogue chunks) | receptive / fixed-phrase only |
| "recognition-only … never assessed" (REC) | receptive, unassessed |
| "licensed support: interpretive only, non-core, never independent productive targets" (`لَا يَجِدُ / لَا تَجِدُ`, U5-C) | receptive support form |

**The rule to carry away:** *core status is about what the unit is teaching, not about what the learner
must produce.* Output demands are set separately, later, and always after input.

### 1.4 Form-level licensing

A licensed form licenses **only itself**.

> "No authorization may be inferred from the separate presence of individual tokens."
> — `unit_05_phrase_gate_spec.md` §3.4

Worked example — the Unit 5 search/find family, as ruled (U5-C):

| Tier | Forms | Standing |
|---|---|---|
| New core, affirmative | `يَبْحَثُ عَنْ` · `تَبْحَثُ عَنْ` · `يَجِدُ` · `تَجِدُ` | Required to occur; productively assessable within the later approved output ceiling |
| Licensed negative support | `لَا يَجِدُ` · `لَا تَجِدُ` | Permitted, not required; interpretive only; never core; creates no assessment requirement |
| Banned until a later ruling | `لَا يَبْحَثُ عَنْ` · `لَا تَبْحَثُ عَنْ` · `أَبْحَثُ عَنْ` · `أَجِدُ` · all other first/second-person, past-tense, and object-pronoun forms | Fail |

The same discipline appears throughout the bank as **"prohibited premature expansion"** columns —
e.g. no `يُرِيدُ أَنْ + verb` in Book 1; no `عِنْدَ + name` possession pattern; no plural possessors;
`إِلَى` never isolated; `عَنْ` never isolated; no `يَعْرِفُ أَنَّ` clauses; no `أَمْ` contrast work;
`لَيْسَ` as a chunk only, never negation grammar.

### 1.5 Phrase-level licensing

Where the target is a phrase, the **phrase** is the licensed unit. The Unit 5 gate spec is the
reference implementation: every `يَبْحَثُ` / `تَبْحَثُ` must be *immediately* followed by `عَنْ`, with
no intervening token, and a bare search verb fails (§3.2 items 5–6).

**Implication for writers.** You cannot borrow half a frame. If the sentence you want needs the verb
without its preposition, the sentence is unauthorized — rewrite it.

---

## §2 — Authorization

### 2.1 The three permitted sources of Arabic

Every Arabic item in any output must trace to exactly one of:

1. **verbatim binding reading language**;
2. **the officially approved target inventory** (produced through that unit's own gate);
3. **a separately authorized teacher-language bank**.

Anything else is `NEW TEACHER LANGUAGE — REQUIRES AUTHORIZATION` or a
`SOURCE GAP — REQUIRES AUTHORIZATION` halt.
— `governance/26` §4; `CLAUDE.md`; `book1_vocabulary_frequency_baseline.md` §"Vocabulary-Control Rules" 2

### 2.2 Source codes (provenance, not permission)

Recorded provenance codes (`book1_high_frequency_structure_bank.md` §3):

| Code | Meaning |
|---|---|
| **U1-SPINE** | ACTIVE approved Unit 1 inventory |
| **U1-READ** | binding readings / prose QC |
| **U1-PQA** | retained personalization chunks |
| **LEG-U2..U6** | legacy candidate JSONs — dispositions in the disposition ledger |
| **LEG-ARCH** | archived legacy readings |
| **NEW** | no repository source — **requires explicit approval** |

> **Critical distinction, stated in the source:** *"Legacy presence does not make it binding, approved,
> or learner-established."* Finding a word in a legacy JSON tells you where it came from. It does not
> tell you that you may use it.

### 2.3 The canonical NEW list

Items with **no repository source**, each inadmissible in any unit design until the explicit approval
named at that unit's gate (`book1_high_frequency_structure_bank.md` §3;
`book1_vocabulary_frequency_baseline.md` rule 6):

`مَعَ` (unallocated as of 2026-07-27) · `هُنَا` (U3 support) · `يَضَعُ` (U7) · `يَعْرِفُ / لَا أَعْرِفُ`
(U8) · `أَوْ` (U8) · `كُلَّ يَوْمٍ` (U9) · `جَدِيدٌ` (U9) · `يَقْرَأُ` (U10) · `حَسَنًا`، `تَعَالَ`،
`مَعًا` (dialogue/support) · family-noun set `أَب / جَدّ / جَدَّة`.

The list must be **reproduced identically** in the bank and in the map's compliance notes (finding
F-09's resolution). If you find them differing, that is a `SOURCE CONFLICT:` and you halt.

### 2.4 Excluded by design

Entry requires an approved amendment (`book1_vocabulary_frequency_baseline.md` §4, from bank §5.5):

past tense · `أَنْ` subordination · plurals and duals · comparatives · case work · `كَيْفَ / مَتَى` ·
additional motion verbs · abstract vocabulary.

Legacy `archive/` material is reference only: `ARCHIVED / DO NOT REUSE` without a new per-item ruling.

### 2.5 Deferred, not forbidden

The disposition ledger's `DEFERRED` ruling is a third state, and the baseline is explicit that it means
**"DEFERRED per the disposition ledger — not 'do not reuse'"** (§3, B-RO5). Deferred items
(`شَيْء`, `غَرِيب / غَرِيبَة`, `هُنَاكَ شَيْءٌ`, `جِدًّا`, `صَوْتٌ`, assorted props) sit in a future
story-engine pool. They are not in any unit, and each requires a fresh per-item decision if ever
proposed.

### 2.6 Ceilings and caps (the hard numbers)

| Cap | Value | Source |
|---|---|---|
| New core targets per unit | 3–5 **normal range**, not a minimum; lower load allowed **with recorded rationale** | `governance/02`; protocol §6 amendment |
| New core targets per Story A | 3–5 maximum | `governance/02` Story A |
| Recycled/transparent share per reading | **70–85%** | `governance/02`; protocol §9 |
| New settings per unit | 1 | baseline §3 (B-RO3) |
| New family nouns per unit | 1 | bank §4.2 (B-PP4) |
| Connectors introduced at once | 1 | bank §4.8 (B-TS1) |
| Word-family box per unit | ≤1 by default; 2–3 words maximum in early Book 1 | `governance/13` §C |
| Root-recognition activity per unit (U2+) | exactly 1 | `governance/02` |
| Major noticing focus per lesson | 1 | `governance/12` §C |
| Learner-facing readings per unit (U2+) | ≤6 | `governance/02` |
| New support forms in a cumulative reading | ≤3 *(recorded at Unit 4 §9.1)* | `unit_04_input_map.md` |

### 2.7 Lexical density and novelty

`NO ACTIVE PROJECT RULE FOUND` for a type–token ratio, a lexical-density formula, or a
new-words-per-hundred-tokens ceiling.

What the project uses **instead** is the recycled-share band (§3 below) plus the target cap plus the
per-category caps in §2.6. The recycled band is doing the work a density metric would do elsewhere:
it bounds novelty from above (≤30% new) *and from below* (≥15% new), which is why exceeding 85% is a
finding and not a bonus.

> **Reading the band correctly.** A reading at 91% recycled is **out of band**, not "extra
> comprehensible." The floor at 70% protects comprehensibility; the ceiling at 85% protects the
> reading from being a restatement of what the learner already owns. Both edges are real. See
> Register **C-2** for the readings currently sitting outside it.

---

## §3 — The Recycled-Share Calculation

The full method, reproduced from `book1_recycling_and_retention_protocol.md` §9 (added 2026-07-04 by
ruling). This is the only approved method; do not substitute another.

### 3.1 When it is run

At **Stage 5 (Arabic Prose QC)**, on **final learner-facing prose**, **per reading**, separately for
every reading.

> "It is a future production-QC requirement verified at Stage 5 — **never a map-stage achievement
> claim.** No planning document may state that a unit or reading 'has' a recycled-language percentage
> before this calculation is run."

### 3.2 The method

1. **Counting unit** — orthographic word tokens of the Arabic reading text.
2. **Denominator** — total counted word tokens of the reading, after exclusions.
3. **Numerator** — counted word tokens that are established/recycled lexical-structural content:
   - core targets introduced in **earlier** units;
   - support chunks and vocabulary already established through earlier binding readings;
   - transparent items previously classified as such in the curriculum inventory.

   Outside the numerator: genuinely new core content of the current unit, new support vocabulary, new
   recognition-only items.
4. **Exclusions (from both numerator and denominator)** — proper names; punctuation; illustration
   labels/captions. The article `الـ` and attached clitics are **not** counted as independent tokens: a
   word is counted once, in the classification of its lexical host.
5. **Reporting** — the prose-QC file must state numerator, denominator, a reference to this method, the
   resulting percentage, and whether it falls within 70–85%.
6. **Out-of-band** — return to Stage 4 for revision, or obtain an explicitly documented, approved
   exception recorded in the unit QC.

### 3.3 Measured, not estimated

The requirement is scripted measurement. The reference implementation is
`units/unit_02/qc/recycled_pct.py`, with raw output frozen at
`units/unit_02/qc/recycled_pct_output.txt`; each reading's `## Arabic Reading` section is read
verbatim so the percentage matches the frozen Arabic exactly.

Reported Unit 2 figures (2026-07-11 measurement pass):

| Reading | numerator | new | denominator | recycled % | band |
|---|---:|---:|---:|---:|---|
| Story A | 30 | 7 | 37 | 81.1% | in band |
| Story B | 45 | 19 | 64 | 70.3% | in band |
| Parallel 1 | 44 | 9 | 53 | 83.0% | in band |
| Parallel 2 | 39 | 7 | 46 | 84.8% | in band |
| Picture retell | 31 | 6 | 37 | 83.8% | in band |
| Mini-story bank | 45 | 15 | 60 | 75.0% | in band |

Two readings first measured **over** the ceiling (85.3% and 88.2%) and were revised at Stage 4 "with
genuine new-target density — not padding." That is the sanctioned repair for an over-ceiling reading:
add real new content, do not delete recycled content.

> ⚠ **Re-measurement, 2026-07-20.** After unsupported closing emotions were removed, Story A moved to
> 80.6% and the retell to 83.3% (both in band), while **Story B fell to 68.9% — 1.1 points below the
> floor, recorded as an open blocker requiring a band ruling.** Register **C-2**.

### 3.4 Cumulative readings

`NO ACTIVE PROJECT RULE FOUND` for a cumulative-specific band. Finding F-02 proposed extending the band
for cumulative readings and the recorded resolution was: *band **NOT** extended per Adam ruling*
(`book1_10_unit_architecture_qc.md` §B).

Unit QC files nevertheless apply a `≥75% (substantial)` gate to cumulative readings
(`units/unit_02/qc/unit_02_prose_qc.md` §7), and Units 3 and 4 report cumulative readings at 85.1% and
91.2%. **This is unreconciled.** Do not treat the `≥75%` gate as authority; see Register **C-2**.

---

## §4 — Frequency Methodology

### 4.1 The adopted source

> Buckwalter, Tim, and Dilworth Parkinson. 2011. *A Frequency Dictionary of Arabic: Core Vocabulary for
> Learners*. Routledge.

Verified 2026-07-04 against the full PDF: complete frequency index (ranks 1–5,000, book pp. 9–433),
alphabetical index (from p. 433), part-of-speech index (from p. 515). **The main frequency index is the
primary evidence**; the alphabetical and POS indexes were used only to locate and cross-check entries.
This supersedes an earlier truncated-copy audit; every rank was re-verified against the full PDF.
— `book1_high_frequency_structure_bank.md` §1

**Copyright constraint:** the source PDF is **not** stored in this repository and must not be committed
or reproduced. Whether extracts may ever be archived in-repo is an open governance-hardening question
(Decision Area 5 remainder), explicitly **not** a production blocker.
— `book1_frequency_evidence_verification_log.md`; gate register Decision Area 5

### 4.2 The six evidence labels — and no others

| Label | Short | Meaning |
|---|---|---|
| `DOCUMENTED FREQUENCY-RANKED MSA WORD` | DFR | The exact lemma is a verified main-index entry |
| `FREQUENCY-SUPPORTED HIGH-UTILITY CHUNK` | FSC | A teaching chunk/frame whose frequency-bearing lexical item is a verified entry |
| `HIGH-UTILITY CANDIDATE — FREQUENCY RANK VERIFIED` | HUC-V | Rank verified but modest; inclusion rests primarily on story utility |
| `HIGH-UTILITY CANDIDATE — LOW PRIORITY OR UNSUITABLE FOR BOOK 1` | — | — |
| `SUPPORT / RECOGNITION-ONLY` | S/R | — |
| `REMOVE OR REPLACE` | — | *(no audited item currently classifies here)* |

— `book1_high_frequency_structure_bank.md` §1

### 4.3 The chunk rule (the most important rule in this section)

> **"A multiword teaching frame is never itself called a ranked corpus item."**

Worked out in the source: `أَرَادَ` is a ranked word; `يُرِيدُ ___` is a frequency-supported chunk;
`لِأَنَّهُ يُرِيدُ ___` is a teaching frame, not a ranked entry. Component ranks belong to the frame's
lexical head(s), and no chunk-level frequency claim is made.

Items explicitly recorded as **not ranked as chunks**: `أَنَا أَيْضًا`; `كُلَّ يَوْمٍ`; the
`لِأَنَّهُ + clause` frame; `مَاذَا تُرِيدِينَ…` and all Unit 1 controlled dialogue chunks. The
verification log is careful to state this "is correct per bank §1, **not** a gap requiring
authorization."

### 4.4 Lemma policy, homographs, and related forms

Four disciplines, each with recorded worked examples:

**(a) Match type is recorded.** Every row states whether the evidence is a *lexical match*, a
*component match*, *within-entry documentation*, or a *related form*.

**(b) A related noun is never cited as evidence for a verb.**
- `يَبْحَثُ عَنْ` — evidence is the verb `بَحَثَ` 676/p.70; the noun `بَحْث` (332/p.38) is
  **corroborating only**.
- `يَضَعُ` — evidence is `وَضَعَ` 359/p.40; the verbal noun `وَضْع` (167) is "a related form, **not** the
  verb evidence."
- `يُسَاعِدُ` — evidence is the verb `سَاعَدَ` v. III 1056/p.104, **not** the noun `سَاعِد` "forearm"
  (6556).

**(c) Homographs are separated explicitly.**
- `ثُمَّ` (conj., 108) vs. `ثَمَّ` adv. "there" (1310) — different lemmas.
- `يَجِدُ` ← `وَجَدَ` (139) vs. `وَجْد` n. (4933).
- `يَسْمَعُ` ← `سَمِعَ` (154) vs. `سَمْع` n. (3194).
- `يَأْخُذُ` ← `أَخَذَ` (198) vs. `أَخْذ` n. (1785).
- `يَعْرِفُ` ← `عَرَفَ` v. I (49) vs. `عَرَّفَ` v. II (4513).
- `جَدّ` (1226) vs. `جِدّ` "seriousness" (171) vs. Jeddah (place box).

**(d) The dictionary's own lemmatization is followed, not overridden.** `أَيْضًا` is ranked via the
headword `أَيْض` (146/p.21) because that is how B&P lemmatizes it.

### 4.5 Inflected forms

An inflected form of a ranked verb is recorded as such and labelled FSC, not DFR — e.g. `أُرِيدُ` is
"an inflected form of ranked verb" `أَرَادَ` (126/p.20). Frequency evidence attaches to the lemma; the
teaching item is the chunk.

### 4.6 Within-entry documentation

Where the evidence is a phrase or usage documented *inside* another entry, the match type says so and
the item is a chunk, not a headword:
- `مَعًا` — "within-entry documentation" of `مَعَ` (17/p.10); "no own main entry located."
- `تَعَالَ / تَعَالَيْ` — within-entry imperative documentation of `تَعَالَى` (420/p.47), with the
  caution that "the lemma's primary sense is religious quoting; **use only the documented imperative**."
- `حَسَنًا` — within-entry adverb/interjection of `حَسَن` (1729/p.165).
- `عِنْدِي` possession — the possessive use of `عِنْدَ` (40/p.12) is "documented in the entry" by the
  dictionary itself, which is why the possessive reading is defensible.

### 4.7 Register and diglossia screening

Every row carries a register/diglossia note. Dialect equivalents are named and excluded as separate
lemmas: `وين/فين` for `أَيْنَ`; `كمان` (768) / `برضو` (2715) for `أَيْضًا`; Levantine/Iraqi `زغير` and a
separate Egyptian lemma (4916) for `صَغِير`; dialect `شي` forms; dialect `قرا`; Levantine `لتحت`,
`تَعْ`. Sub-standard spellings are flagged (`لاكن` for `لٰكِن`).

### 4.8 Frequency is one criterion among nine — and never sufficient

> "**No numerical 'high-frequency cutoff' is defined, because no approved project source defines one.**
> Frequency is one criterion alongside CI/TPRS suitability, comprehensibility, story utility,
> visualizability, target-load discipline, recycling value, natural beginner Arabic, and Book 1 scope.
> **No item is retained merely because it appears in the top 5,000.**"
> — `book1_high_frequency_structure_bank.md` §1

And the converse, stated as a lane rule:

> "**No unit lane may add Arabic merely because it is common, useful, visually convenient, or needed for
> a preferred story idea.** … If a story idea needs unapproved language, change the story, not the
> inventory."
> — `book1_vocabulary_frequency_baseline.md` §"Vocabulary-Control Rules" 1

The HUC-V label exists precisely for the case where utility outranks rank: `يُسَاعِدُ` at 1056 and
`حَسَنًا` at 1729 are admitted on story utility with the rank recorded as modest.

### 4.9 Reproducibility rules

1. **No rank or page may be asserted that is not already recorded in bank §2.** Do not fabricate ranks.
   — baseline rule 4
2. **No lane may call a multiword frame a ranked item.** — verification log Use Rule 2
3. **The verification log is a restatement, not a re-verification.** It "adds no rank not already in
   bank §2." — log Use Rule 1
4. **Provenance of the single verification pass:** all ranks verified 2026-07-04 during the architecture
   package build; the log carries that provenance forward and does **not** constitute an independent
   second verification.
5. **Every rank is external-source-verified only.** Until Decision Area 5 is ruled, treat every rank as
   *"recorded, externally verified 2026-07-04, not re-verifiable in-repo."* — baseline rule 5

**What "reproducible" therefore means here.** Any claim can be traced to a specific row of bank §2 with
a rank, page, match type, and qualification. It cannot be re-derived from repository materials, because
the corpus is external and copyrighted. That limitation is recorded, deliberate, and not a defect to be
quietly fixed by backfilling.

### 4.10 The Unit 1 evidence gap — deliberate, recorded, not to be filled

The ten Unit 1 spine targets carry **no frequency evidence and make no frequency claim**. They were
approved on **narrative-affordance** grounds through two recorded human amendments *before* the source
was adopted.

> "`SOURCE GAP — REQUIRES AUTHORIZATION` for frequency purposes — but no frequency claim is made for
> the spine." … "**do not backfill without a recorded decision.**"
> — `book1_frequency_evidence_verification_log.md` §§1, 4; baseline §1

This is the clearest instance of the project's governing instinct: an honest hole beats a plausible
filling.

---

## §5 — The Recorded Evidence Table

Reproduced from `book1_high_frequency_structure_bank.md` §2 (source = Buckwalter & Parkinson 2011 for
every row; verification date 2026-07-04 for every row). **This table is a copy for convenience. The bank
is the record.**

### 5.1 Core-target candidates

| Bank ID | Teaching item | Freq-bearing head | Rank / page | Label | Qualification |
|---|---|---|---:|---|---|
| B-PR1 | `يُحِبُّ / لَا يُحِبُّ ___` | `أَحَبَّ` (+ `لَا` 11/p.10) | 342 / 39 | FSC | Verb lexical match; frame is a chunk |
| B-TS1 | `ثُمَّ` | `ثُمَّ` | 108 / 18 | DFR | Homograph `ثَمَّ` (1310) distinct |
| B-ML1 | `أَيْنَ ___؟` | `أَيْنَ` | 461 / 50 | DFR | Dialect `وين/فين` separate lemmas |
| B-NF1 | `يَبْحَثُ عَنْ ___` | `بَحَثَ` | 676 / 70 | FSC | Noun `بَحْث` (332) corroborating only |
| B-NF2 | `يَجِدُ / تَجِدُ ___` | `وَجَدَ` | 139 / 21 | FSC | Homograph `وَجْد` (4933) distinct |
| B-TS3 | `لِمَاذَا؟` | `لِمَاذَا` | 375 / 42 | DFR | `مَاذَا` 275/p.33 |
| B-TS4 | `لِأَنَّهُ / لِأَنَّهَا + clause` | `لِأَنَّ` | 57 / 13 | FSC | Component match; taught frame not a ranked item |
| B-NF3 | `يَأْخُذُ / تَأْخُذُ ___` | `أَخَذَ` | 198 / 26 | FSC | Noun `أَخْذ` (1785) distinct |
| B-TS2 | `وَلَكِنْ` | `لٰكِن` | 91 / 17 | FSC | Component match (و + لكن); `لٰكِنَّ` 58/p.14; `لاكن` sub-standard |
| B-NF4 | `يَسْمَعُ / تَسْمَعُ ___` | `سَمِعَ` | 154 / 22 | FSC | Noun `سَمْع` (3194) distinct |
| B-ML5 | `مَعَ ___` | `مَعَ` | 17 / 10 | DFR | canonical NEW — approval required |
| B-PA5 | `عِنْدِي / لَيْسَ عِنْدِي ___` | `عِنْدَ` | 40 / 12 | FSC | Possessive use documented in entry; **input-first only** |
| B-PA6 | `أُرِيدُ ___` | `أَرَادَ` | 126 / 20 | FSC | Inflected form of ranked verb; chunk only |
| B-TS5 | `أَيْضًا` | `أَيْض` | 146 / 21 | DFR | B&P lemmatizes under `أَيْض` |
| B-NF5 | `يَضَعُ / تَضَعُ ___ + place` | `وَضَعَ` | 359 / 40 | FSC | Verbal noun `وَضْع` (167) is not the evidence; canonical NEW |
| B-ML2 | `تَحْتَ ___` | `تَحْت` | 216 / 27 | DFR | Lev. `لتحت` noted |
| B-ML3 | `أَمَامَ ___` | `أَمَام` | 153 / 22 | DFR | — |
| B-PR3 | `يُسَاعِدُ / تُسَاعِدُ ___` | `سَاعَدَ` v. III | 1056 / 104 | HUC-V | **Not** the noun `سَاعِد` (6556); modest rank, utility-based |
| B-TS6 | `أَوْ` | `أَو` | 23 / 11 | DFR | canonical NEW |
| B-PR4 | `يَعْرِفُ / لَا أَعْرِفُ` | `عَرَفَ` | 49 / 13 | FSC | `عَرَّفَ` v. II (4513) distinct; canonical NEW |
| B-DQ1 | `كَبِيرٌ / صَغِيرٌ (+fem.)` | `كَبِير` ؛ `صَغِير` | 65 / 14 ؛ 230 / 29 | DFR (words) / FSC (set) | Egy. lemma 4916 separate |
| B-TS7 | `كُلَّ يَوْمٍ` | `كُلّ` + `يَوْم` | 19 / 10 ؛ 26 / 11 | FSC | **Component matches; chunk not a ranked item**; canonical NEW |
| B-DQ2 | `جَدِيدٌ / جَدِيدَةٌ` | `جَدِيد` | 60 / 14 | DFR (word) / FSC (pair) | canonical NEW |
| B-PR5 | `يَقْرَأُ / تَقْرَأُ ___` | `قَرَأَ` v. I | 727 / 75 | FSC | Prior false archive-usage note withdrawn; canonical NEW |

### 5.2 Support / dialogue / recognition candidates

| Bank ID | Item | Head | Rank / page | Label | Qualification |
|---|---|---|---:|---|---|
| B-ML4 | `هُنَا` | `هُنَا` | 159 / 22 | DFR (support role) | canonical NEW (support); not a core |
| B-DI8 | `مَعًا` | `مَعَ` entry | 17 / 10 | FSC (support) | Within-entry; no own main entry located |
| B-DI7 | `تَعَالَ / تَعَالَيْ` | `تَعَالَى` | 420 / 47 | FSC (dialogue) | Within-entry imperative only; lemma's primary sense religious |
| B-DI5 | `حَسَنًا` | `حَسَن` | 1729 / 165 | HUC-V | Within-entry; modest rank; optional |
| B-DI6 | `أَنَا أَيْضًا` | `أَنَا` + `أَيْض` | 25 / 11 ؛ 146 / 21 | FSC (dialogue) | Component matches; **legacy U6 provenance — not NEW** |
| B-PP4 | `أَب` | `أَب` | 76 / 15 | DFR (support role) | First family-noun candidate |
| B-PP4 | `جَدّ / جَدَّة` | `جَدّ` | 1226 / 120 | HUC-V | Fem. documented in same entry; DEFER unless a U7+ brief casts a grandparent |
| B-RO5 | `شَيْء` | `شَيْء` | 39 / 12 | DFR (deferred pool) | DEFERRED per disposition ledger |
| B-RO5 | `غَرِيب / غَرِيبَة` | `غَرِيب` | 526 / 55 | HUC-V (deferred pool) | DEFERRED per disposition ledger |

### 5.3 Unit 1 spine — no frequency claim

`هُنَاكَ` · `اسْمُهُ / اسْمُهَا` · `عِنْدَهُ / عِنْدَهَا` · `لَيْسَ عِنْدَهُ / لَيْسَ عِنْدَهَا` ·
`يُرِيدُ / تُرِيدُ` · `يَذْهَبُ / تَذْهَبُ إِلَى` · `يَرَى / تَرَى` · `يُعْطِي / تُعْطِي ___ لِ___` ·
`يَقُولُ / تَقُولُ: «...»` · `يَسْأَلُ / تَسْأَلُ`

Status: ACTIVE, approved, **frozen**. Frequency evidence: none recorded, none claimed, not to be
backfilled without a recorded decision. Approval basis: narrative affordance, via two recorded human
amendments.

---

## §6 — Allocation Status (read before you plan a unit)

Allocation moves. As of the last recorded ruling (Adam, 2026-07-27, `unit_05_allocation_rulings.md`):

| Item | Current allocation | Note |
|---|---|---|
| `يُحِبُّ / لَا يُحِبُّ`, `ثُمَّ` | Unit 2 core | Gate passed 2026-07-07; two-target lower-load design approved |
| `أَيْنَ ___؟` | Unit 3 core | Unit 3 completed **without** search/find |
| `تَحْتَ`, `أَمَامَ` | **Recycled — introduced Unit 3** | Reclassified 2026-07-27; U7 duplicate removed |
| `لِمَاذَا؟`, `لِأَنَّهُ / لِأَنَّهَا` | Unit 4 core | — |
| `يَأْخُذُ` | **Authority state unresolved** | `UNIT 4 AUTHORITY STATE REQUIRES REPOSITORY STABILIZATION` |
| `وَلَكِنْ`, `يَبْحَثُ عَنْ`, `تَبْحَثُ عَنْ`, `يَجِدُ`, `تَجِدُ` | Unit 5 core | Source production **BLOCKED** pending the phrase gate |
| `يَسْمَعُ / تَسْمَعُ` | **Unallocated** | Available for Unit 6 consideration |
| `مَعَ` | **Unallocated** | Returned to the canonical-NEW pool |
| `عِنْدِي`, `أُرِيدُ`, `أَيْضًا` | Unit 6 (proposed) | `عِنْدِي` input-first only; `UNIT 6 NEW-CORE IDENTITY CONFLICT` open |
| `يَضَعُ` | Unit 7 (proposed) | `UNIT 7 NEW-CORE ALLOCATION GAP — ADAM RULING REQUIRED` |
| `يُسَاعِدُ`, `أَوْ`, `يَعْرِفُ` | Unit 8 (proposed) | — |
| `كَبِيرٌ/صَغِيرٌ`, `كُلَّ يَوْمٍ`, `جَدِيدٌ` | Unit 9 (proposed) | — |
| `يَقْرَأُ` | Unit 10 — **not locked** | Open unit-design decision |

Superseded allocations are preserved in the bank and board marked ⚠. **Read them as history, never as
instruction.**

---

## §7 — Author's Checklist

Before submitting a unit's language plan:

- [ ] Every Arabic item traces to binding readings, an approved inventory, or an authorized bank
- [ ] Every item carries exactly one of: CORE / recycled / SUP / REC (plus DLG where applicable)
- [ ] No support or recognition item has silently become core
- [ ] Every controlled dialogue chunk is listed, classified, and marked non-productive
- [ ] Canonical-NEW items in the plan each have their named gate approval — or are removed
- [ ] No excluded-by-design category (past tense, `أَنْ`, plurals, comparatives, case, `كَيْفَ/مَتَى`, extra motion verbs, abstract vocabulary) has crept in
- [ ] Every licensed form is licensed *as that form*; no person/tense/pronoun expansion inferred
- [ ] Phrase targets are used as whole phrases, with no isolated components
- [ ] Per-unit caps respected: ≤1 new setting, ≤1 new family noun, 1 connector, ≤1 word-family box, exactly 1 root activity
- [ ] Target count within 3–5 — or below it **with a recorded rationale**
- [ ] Recycled share **measured by script**, per reading, reported with numerator/denominator/method
- [ ] Any out-of-band reading returned to Stage 4 or carrying a recorded, approved exception
- [ ] No frequency rank asserted that is not in bank §2; no chunk called a ranked item
- [ ] The Unit 1 spine's evidence gap left as it is
