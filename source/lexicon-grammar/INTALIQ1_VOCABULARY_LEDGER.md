# Intaliq 1 — Vocabulary Ledger

*Architecture §26.5 · created 2026-09-14 · Editor · **Unit 1 complete; Units 2–10 open***

```
EVIDENCE DISCIPLINE FOR THIS FILE
Every rank below is reproduced from a recorded project source, named in the row.
No rank in this file was produced by text extraction, estimated, or inferred.
Where no recorded source carries a lemma, the row reads PENDING and says so.
Architecture §13 · §30 · Frequency Manual §4.9 rule 1.
```

---

## 0. Why several rows read PENDING, and why that is the correct state

An extraction pass over the frequency dictionary's text was attempted on 2026-09-14 and **rejected before any row was written.** Strict whole-word matching returned three ranks that proved false on inspection:

| returned | the string it actually matched |
|---|---|
| قَالَ = 4807 | بُرْتُقَال "oranges" |
| مَنْ = 2322 | مُنَى (a given name) |
| لِـ = 41 | أَوَّل |

These are substring collisions — the SC-047 whole-word failure recurring in a new instrument. Loose matching produced plausible hits; strict matching produced confirmed-wrong ones; neither is separable from the true hits at scale by machine. **Extraction is therefore not an admissible evidence source for this ledger.** Rows are filled from eye-verified project records only, and the remainder are flagged for editorial resolution per §13 rather than filled with something that looks like evidence.

---

## 1. The two recorded evidence sources, and the conflict between them

| Source | What it carries | Standing |
|---|---|---|
| **BANK** — `03_VOCABULARY_AND_FREQUENCY_MANUAL` §5, reproducing `book1_high_frequency_structure_bank.md` §2 | 33 rows, each with rank **and printed page**, match type, register note, verified 2026-07-04 | The record. Manual §4.9 rule 1: *no rank may be asserted that is not already recorded here.* |
| **FVL** — `FREQ_VERIFICATION_L1_FOUNDATION.md` | ~180 lemma ranks, eye-verified 2026-08-08, method validated against nine independently confirmed ranks; **page numbers mostly absent** | An independent later pass. Its ranks are *not* in bank §2. |

**Flag V-1 — for the Program Owner.** FVL asserts ranks that Manual §4.9 rule 1 forbids asserting. One of the two is wrong about its own authority. The ledger below cites FVL rows as `FVL` and marks them **`rank recorded, page not recorded`**, which is honest about both the rank and the gap, but the governance question — does FVL's 2026-08-08 pass amend bank §2, or is it subordinate to it? — is not the Editor's to settle. Intaliq architecture §3 makes the frequency dictionary the lexical authority and asks for citations; Book 1's Manual §4.10 deliberately declines them for the spine. **Both cannot govern Unit 1 unchanged.**

**Flag V-2 — the spine gap.** Manual §4.10 / §5.3 record a standing decision that the ten Unit 1 spine targets carry **no frequency claim** and are **not to be backfilled without a recorded decision**. Four items in Intaliq Unit 1 are spine items. They are marked `SPINE — no claim` below, not PENDING: the absence is a ruling, not a hole.

---

## 2. Unit 1 — the ledger

Twenty-nine lexical entries. Statuses are the four of Architecture §9; labels are the six of Manual §4.2 and no others. **Forms are the surfaces the books actually print** — verified against the printed canon 2026-09-14 by `canonCheck`; a form not listed here is not licensed (Manual §1.4).

### 2.1 Core targets — evidence recorded

| # | Lemma | Gloss | Printed forms (R1 · R2) | Status | Rank / page | Label | Source |
|---|---|---|---|---|---:|---|---|
| 1 | **قَالَ** | to say | تَقُولُ ×11 · يَقُولُ ×3 · وَتَقُولُ ×3 · وَيَقُولُ ×1 · قَالَ ×4 · قَالَتْ ×4 · وَقَالَ ×2 | new (R1) → recycled (R2) | **15** / page not recorded | DFR | FVL §1 |
| 2 | **رَأَى** | to see | تَرَى ×5 · يَرَى ×1 · رَأَى ×1 | new (R1) → recycled (R2) | **75** / page not recorded | DFR | FVL §1 |
| 3 | **اِسْم** | name | اسْمٌ ×4 · اسْمُهَا ×1 · اسْمِي ×1 | new_core | **89** / page not recorded | DFR | FVL §2 |
| 4 | **أَرَادَ** | to want | أُرِيدُ ×1 · أُرِيدُ ×1 | new_core (R1) → recycled (R2) | **126** / **p. 20** | **FSC** | BANK B-PA6 |
| 5 | **وَلَد** | boy | وَلَدًا ×1 · الْوَلَدُ ×1 | new_core | **362** / **p. 41** | DFR | FVL §2; **page resolved 2026-09-15** — running-head derivation, see the readiness packet §6 |
| 6 | **صَدِيق** | friend | صَدِيقٌ ×2 · صَدِيقًا ×1 · صَدِيقَةٌ ×2 · صَدِيقٌ ×1 | new_core | **398** / page not recorded | DFR | FVL §2 |
| 6b | **صَدِيقَاتٌ** | friends (f. pl.) | صَدِيقَاتٌ ×1 — the last word of Reading 1 | **lexical plural entry** | rank at the lemma `صَدِيق` 398 | — | **SC-062 §20L**: a plural noun may be learned lexically, as a word, *each one an explicit ledger entry*. **This is Intaliq 1's first.** Licenses itself and no other plural; no plural morphology is taught |
| 7 | **أَحَبَّ** | to like | تُحِبُّ ×1 | new_core | **342** / **p. 39** | FSC | BANK B-PR1 |
| 8 | **أَنَا** | I | أَنَا ×8 · وَأَنَا ×1 · أَنَا ×4 | new_core | **25** / **p. 11** | DFR | BANK B-DI6 (component) |
| 9 | **لَا** | no / not | لَا ×2 · لَا ×3 | new_core | **11** / **p. 10** | DFR | BANK B-PR1 (within-frame) |
| 10 | **عِنْدَ** | to have (things) | وَعِنْدَهَا ×1 · عِنْدَهُ ×2 · عِنْدِي ×3 | new_core | **40** / **p. 12** | FSC | BANK B-PA5 — **input-first only** |
| 11 | **قَلَم** | pen | *(not printed in R1)* · قَلَمٌ ×8 · قَلَمًا ×1 · الْقَلَمَ ×1 · الْقَلَمُ ×1 · قَلَمُ ×1 | support | **1021** / **p. 101** | DFR | FVL §2; **page corrected 2026-09-15** from p. 99 — running-head derivation, see the readiness packet §6 |
| 12 | **فَصْل** | class / classroom | الْفَصْلَ ×1 | support | **1856** / page not recorded | HUC-V | FVL §2 — classroom sense documented in-entry |

### 2.2 Spine items — no frequency claim, by standing decision

Manual §4.10 and §5.3. These are **not** PENDING; the absence of a rank is the recorded ruling, and backfilling requires a decision the Editor may not make.

| # | Lemma | Printed forms | Status | Standing |
|---|---|---|---|---|
| 13 | **هُنَاكَ** | هُنَاكَ ×4 · وَهُنَاكَ ×1 · هُنَاكَ ×1 | new_core | SPINE — no claim (§5.3) |
| 14 | **لَيْسَ** | لَيْسَ ×2 · لَيْسَ ×4 | new_core | SPINE — `لَيْسَ عِنْدَهُ` listed; chunk only, never negation grammar (§1.4) |
| 15 | *(اسْمُهَا, عِنْدَهَا — recorded under #3 and #10 above)* | | | SPINE forms of ranked lemmas |

### 2.3 PENDING — no recorded source carries this lemma

Per §13: *flag missing lemmas, conflicting lemmas, homographs, and lemmatization ambiguities for editorial review.* Each row states what a resolution would need.

| # | Lemma | Gloss | Printed forms | Status | What closing it requires |
|---|---|---|---|---|---|
| 16 | **بِنْت** | girl | بِنْتٌ ×1 · بِنْتًا ×1 · الْبِنْتُ ×1 | new_core | Eye-lookup. Note: FVL records اِبْن 145 and اِمْرَأة 321 but not بِنْت — a real gap, not an oversight of mine. Check for lemmatization under اِبْن. |
| 17 | **دَخَلَ** | to enter | تَدْخُلُ ×1 · دَخَلَ ×1 | new_core | Eye-lookup. Homograph check against دَخْل "income". |
| 18 | **قَائِمَة** | list | قَائِمَةٌ ×1 · الْقَائِمَةَ ×4 | support | Eye-lookup. Check lemmatization under قَامَ; قَائِم "standing" is a likely homograph trap. |
| 19 | **مَنْ** | who? | مَنْ ×2 · وَمَنْ ×2 · مَنْ ×3 | new_core | Eye-lookup, **by eye only** — extraction returned 2322 (مُنَى), confirmed false. Separate from مِنْ "from". |
| 20 | **لِـ** | to have (people), to/for | لِي ×3 · وَلِي ×1 · لَهَا ×1 · وَلِي ×1 | new_core | Eye-lookup, **by eye only** — extraction returned 41 (أَوَّل), confirmed false. |
| 21 | **أَهْلًا** | welcome / hello | أَهْلًا ×3 | new_core | Within-entry documentation under أَهْل is the likely evidence shape (cf. مَعًا under مَعَ, Manual §4.6). |
| 22 | **نَعَمْ** | yes | نَعَمْ ×2 · نَعَمْ ×1 | new_core | Eye-lookup. |
| 23 | **يَا** | O (vocative) | يَا ×3 · يَا ×2 | support | Eye-lookup; may not be a headword. |
| 24 | **أَنْتَ** | you | أَنْتَ ×1 · أَنْتِ ×1 · وَأَنْتِ ×1 · أَنْتَ ×1 | new_core | Eye-lookup. **Uncarded — see Flag V-3.** |
| 25 | **هِيَ** | she | هِيَ ×1 | recognition | Eye-lookup. **Uncarded — see Flag V-3.** |
| 26 | **هٰذِهِ** | this (f) | هٰذِهِ ×1 | new_core | Eye-lookup. **Uncarded — see Flag V-3**; the can-do page teaches هٰذَا/هٰذِهِ as a frame. |
| 27 | **تَكَلَّمَ** | to speak | يَتَكَلَّمُ ×1 | recognition | Eye-lookup, v. V. Not urgent: recognition-only items are never assessed (§1.1). |

### 2.4 Chunks — ranked at their lexical heads, never as chunks

Manual §4.3: *a multiword teaching frame is never itself called a ranked corpus item.* Full entries in the Chunk Inventory.

| # | Chunk | Printed | Status | Head evidence |
|---|---|---|---|---|
| 28 | **السَّلَامُ عَلَيْكُمْ** | ×1 · ×1 | new_core | `CH-01` — head سَلَام PENDING; no chunk-level claim made |
| 29 | **وَعَلَيْكُمُ السَّلَامُ** | ×1 · ×1 | recognition | `CH-02` — same head; no chunk-level claim made |

### 2.5 Resolved 2026-09-15 — ten new evidenced rows (SC-077)

*Source: Buckwalter & Parkinson, **A Frequency Dictionary of Arabic**, first edition published 2011 by Routledge, © 2011, ISBN-13 978-0-415-44434-7 (pbk). Verified 2026-09-15 by the approved protocol: locate, read the surrounding context by eye to confirm an entry, derive the printed page from the running head. Numeric proximity alone was not accepted for any row.*

| Lemma | Printed forms (U1) | Rank | Printed p. | POS | Sense | Homograph / variant control | Evidence |
|---|---|---:|---:|---|---|---|---|
| **بِنْت** | بِنْتٌ · بِنْتًا · الْبِنْتُ | **252** | **43** | n. | daughter; girl | distinct from `اِبْن` 145 (son) and `اِمْرَأة` 321 (woman) | family-terms thematic box, rank-ordered: `226 أخت · **252 بنت** daughter, girl · 264 شاب` |
| **دَخَلَ** | تَدْخُلُ · دَخَلَ | **297** | **194** | v. I (u) | to enter (`إلى` sth) | **not** `أَدْخَلَ` IV **1601**; **not** the noun `دَخْل` "income" | `دخل 297 | I (u) to enter (إلى sth)` — corroborated in the verb index p. 550 |
| **قَائِمَة** | قَائِمَةٌ · الْقَائِمَةَ | **1098** | **106** | n., pl. قَوَائِم | list, index; legs (of a chair) | **not** the a.p. `قَائِم` "standing" | `مة 1098 | .n قائ | list, index` with the example «قائمة الاغتيالات» |
| **يَا** | يَا | **35** | **432** | part. voc. | O — address particle | `يا..يا` conj. "either…or" and Iraqi interrog. "which" are separately glossed in-entry | root index: `يا part.voc. 35` with «يا أُسْتاذ!» and «يا سَلام!». **Independently confirmed**: the entry's example sentence is «هَلْ أَنْتَ شِيُوعِيٌّ يَا صَدِيقِي؟» |
| **هِيَ** | هِيَ | **33** | **11** | pron. | she; it (fem. sg.); they (non-human pl.) | dialect `/hiyya/`, `/hiyye/`, `هيه` named in-entry as variants, not separate lemmas | `ي 33 | ه pron. she; it (fem.sg.)…` with «هي تعرف أن الولد يسرق» |
| **هٰذِهِ** | هٰذِهِ | **22** | **11** | dem. pron. | this (fem. sg.); these (things) | **B&P lemmatizes `هٰذِهِ` separately from `هٰذَا`** — see the pending note below | `22 | هذه dem.pron. this (fem.sg.), these (things)`, sequenced between rank 21 and `أو` 23 |
| **تَكَلَّمَ** | يَتَكَلَّمُ | **926** | **129** | v. V | to speak | **not** `كَلَّمَ` II **2986** "to speak with, talk to sb" | verb thematic list: `926 تكلم to speak` |
| **سَلَام** | *(chunk head — CH-01/CH-02)* | **188** | **101** | n. | peace | **not** `إسْلَام` **365**; **not** `اسْتِسْلَام` **4250** | opposites box: `peace war سلام 188 165 حرب`. **Manual §4.3: no chunk-level claim is made; this is the head's rank only** |
| **مِفْتَاح** | *(U2 candidate)* | **1845** | **166** | n. | key | — | technology box: `key مفتاح 1845` |
| **صَفّ** | *(U2 candidate)* | **905** | **90** | n., pl. صُفُوف | line, row, rank; **class, classroom** | **not** `نِصْف` **607** "half"; **not** `مُنْتَصَف` **1649** "middle" — both returned by a bare match and both rejected | `صفوف .pl .n ص ف 905 | line, row, rank; class, classroom` with «صف طويل». Corroborated in the root index p. 432 |

**Two collisions caught, recorded because they are the protocol's whole point.** A bare match on `صف` returned **607** and **1649**, which are `نِصْف` and `مُنْتَصَف`. And `أَنْتَ` appeared to have an entry at rank 35 until the context was read: that sentence is **`يَا`'s example**, which is why `يَا` is confirmed and `أَنْتَ` is still pending.

### 2.6 Still pending — 6 rows

| Lemma | Why it resisted | What will close it |
|---|---|---|
| `مَنْ` | every candidate is the preposition `مِن` or a digit in an example | the interrogative's own entry, by eye |
| `لِـ` | the extraction splits the clitic from its host | likely within-entry documentation |
| `أَهْلًا` | no entry-shaped candidate | expect within-entry documentation under `أَهْل` (cf. `مَعًا` under `مَعَ`) |
| `نَعَمْ` | the entry is visible — `interj. yes, OK, uh-huh` with «إيه واالله» — but the rank did not fall in the readable window | one page read; the entry is located |
| `أَنْتَ` | the apparent rank-35 hit is `يَا`'s example sentence | the pronoun's own entry |
| **`هٰذَا`** | **new item.** `هٰذِهِ` 22 is its own headword, so the masculine has a separate rank | its own entry; expect a rank below 22 |

**Unit 2 candidates still pending: `كُرْسِيّ` · `نَافِذَة` · `طَاوِلَة` · `شُبَّاك` · `بِجَانِبِ`.** All five appear only inside example sentences in the extraction. `شُبَّاك` and `بِجَانِبِ` may not be headwords at all.

---

### 2.7 Lookup reconciliation — every original item, one row (SC-080)

| # | Item | Set | Status |
|---:|---|---|---|
| 1 | `بِنْت` | U1 | **resolved** — 252 / p. 43 |
| 2 | `دَخَلَ` | U1 | **resolved** — 297 / p. 194 |
| 3 | `قَائِمَة` | U1 | **resolved** — 1098 / p. 106 |
| 4 | `مَنْ` | U1 | pending |
| 5 | `لِـ` | U1 | pending |
| 6 | `أَهْلًا` | U1 | pending |
| 7 | `نَعَمْ` | U1 | pending — entry located, rank outside the readable window |
| 8 | `يَا` | U1 | **resolved** — 35 / p. 432 |
| 9 | `أَنْتَ` | U1 | pending |
| 10 | `هِيَ` | U1 | **resolved** — 33 / p. 11 |
| 11 | `هٰذِهِ` | U1 | **resolved** — 22 / p. 11 |
| 12 | `تَكَلَّمَ` | U1 | **resolved** — 926 / p. 129 |
| 13 | `سَلَام` | chunk head | **resolved** — 188 / p. 101 |
| 14 | `كُرْسِيّ` | U2 | pending |
| 15 | `نَافِذَة` | U2 | pending |
| 16 | `طَاوِلَة` | U2 | pending |
| 17 | `مِفْتَاح` | U2 | **resolved** — 1845 / p. 166 |
| 18 | `شُبَّاك` | U2 | pending — may not be a headword |
| 19 | `صَفّ` | U2 | **resolved** — 905 / p. 90 |
| 20 | `بِجَانِبِ` | U2 | pending — expect within-entry under `جَانِب` |
| **21** | **`هٰذَا`** | **added 2026-09-15** | pending — **not one of the original twenty**; became a lookup when `هٰذِهِ` proved to be its own headword |

**Of the original 20: 10 resolved · 10 pending · 0 duplicates · 0 removed.** With the one discovered item, **21 tracked, 10 resolved, 11 pending.** The earlier "six Unit 1 pending" folded `هٰذَا` into the original twelve; it is a twenty-first item.

---

### 2.8 Unit 2 — rows opened 2026-09-16 ⟨SC-088 · SC-090 · SC-092⟩

*Ranks are recorded only where read by eye in the frequency dictionary (Buckwalter & Parkinson 2011). The dictionary was **not in session** on 2026-09-16; every "lookup owed" row is exactly that — no rank is estimated. Source: `INTALIQ1_UNIT2_STORY_DRAFTS.md` revision 4, §5.*

| # | Lemma | Gloss | Printed forms (rev-4 drafts) | Status | Rank / page | Evidence |
|---|---|---|---|---|---|---|
| U2-01 | **أَيْنَ** | where | أَيْنَ | new_core | **461 / p. 50** | eye-confirmed (SC-077) |
| U2-02 | **فِي** | in | فِي | new_core | top-stratum closed class | brief §3 |
| U2-03 | **عَلَى** | on | عَلَى | new_core | top-stratum closed class | brief §3 |
| U2-04 | **تَحْتَ** | under | تَحْتَ | new_core | **216 / p. 27** | eye-confirmed |
| U2-05 | **هُنَا** | here | هُنَا | new_core | **159 / p. 22** | eye-confirmed |
| U2-06 | **ذَهَبَ** (chunk CH-18 with `إِلَى`) | to go | يَذْهَبُ · ذَهَبَتْ | **new_core (SC-092)** | **lookup owed** | — |
| U2-07 | **إِلَى** | to | إِلَى | **new_core (SC-092)**, inside CH-18 | **lookup owed** | — |
| U2-08 | **مِفْتَاح** | key | مِفْتَاحًا · مِفْتَاحٌ · الْمِفْتَاحُ · مِفْتَاحِي · مِفْتَاحُكَ · مِفْتَاحُكِ | support | **1845 / p. 166** | ledger §2.5 |
| U2-09 | **كِتَاب** | book | الْكِتَابِ · كِتَابٌ | support | **196** | brief §5 |
| U2-10 | **بَاب** | door | الْبَابِ · الْبَابَ | support | **298** | brief §5 |
| U2-11 | **حَقِيبَة** | bag | حَقِيبَتِي · الْحَقِيبَةِ | support | **2931** | brief §5 |
| U2-12 | **صُورَة** | picture | صُورَةٌ · الصُّورَةُ · الصُّورَةَ · الصُّورَةِ | support | **120** | brief §5 |
| U2-13 | **بَيْت** | house | الْبَيْتِ · الْبَيْتَ · بَيْتِ · بَيْتِي · بَيْتُكِ · بَيْتِهِ · بَيْتِهَا | support | **lookup owed** | scope map U2 list |
| U2-14 | **أَرْض** | ground | الْأَرْضِ | support | **lookup owed** | — |
| U2-15 | **يَد** | hand | يَدَهُ · يَدِهِ | support | **lookup owed** | — |
| U2-16 | **رَجَعَ** | to go back | يَرْجِعُ · رَجَعَتْ | support (story verb) | **lookup owed** | — |
| U2-17 | **أَعْطَى** | to give | أَعْطَتْهَا | support (story verb) | **lookup owed** | — |
| U2-18 | **ضَحِكَ** | to laugh | يَضْحَكُ · ضَحِكَتْ | support (story verb) | **lookup owed** | — |
| U2-19 | **أَيْضًا** | also | أَيْضًا | support, early (SC-082 allocates U4) | **lookup owed** | — |
| U2-20 | **حَزِين / سَعِيد** | sad / happy | not yet printed; CR-8 reserve | support | **lookup owed** | — |
| — | `غُرْفَة` | room | — | **dropped** at rev 4 (no longer printed) | — | — |

#### 2.8b Rows opened 2026-09-17 from revisions 5–6 ⟨SC-090 · SC-094 · SC-095⟩

*Printed forms counted by script on the frozen rev-6 texts (`u2r7_s1.txt` 172 words · `u2r7_s2.txt` 110 words). Rows U2-24 to U2-27 are the owner's own additions to Story 1 (SC-095). Dictionary still not in session; no rank is estimated.*

| # | Lemma | Gloss | Printed forms (rev 6) | Status | Rank / page | Evidence |
|---|---|---|---|---|---|---|
| U2-21 | **وَضَعَ** | to put | يَضَعُ ×2 · تَضَعُ ×1 (PQ, 2sg) · وَضَعَتْ ×1 | **new_core, target verb (SC-094)** | **lookup owed** | assimilated Form I — Alhawary 13.4.4, page to verify by eye |
| U2-22 | **قِطّ** | cat | قِطٌّ ×3 · الْقِطُّ ×3 · وَالْقِطُّ ×1 | support (CR-9 element) | **lookup owed** | rev 5 |
| U2-23 | **كَبِير** | big | كَبِيرَةٌ ×1 | support (CR-10 detail) | **lookup owed** | rev 5 |
| U2-20 → | **حَزِين** | sad | حَزِينَةٌ ×1 (Story 2 — the CR-8 word) | support | **lookup owed** | row U2-20 now printed; `سَعِيد` remains unprinted |
| U2-24 | **هَلْ** | (yes/no question particle) | هَلْ ×4 | support, early (scope map allocates U4) | **lookup owed** | owner's edit, SC-095 |
| U2-25 | **عِنْدَ** (locative) | at, by | عِنْدَ الْبَابِ ×1 | `G-input_first` — the possessive `عِنْدَ` is U1 #10 (rank 40 / p. 12); the **locative** use is a new sense, not a new lemma | rank as U1 #10 | owner's edit, SC-095; Alhawary section for `عِنْدَ` as adverbial of place **to verify by eye** |
| U2-26 | **نَظَرَ إِلَى** | to look at | يَنْظُرُ ×2 | support (story verb, home U4) | **lookup owed** | owner's edit, SC-095 |
| U2-27 | **وَلٰكِنْ** | but | وَلٰكِنْ ×1 | support, early | **lookup owed** | owner's edit, SC-095 |
| U2-15 → | **يَد** | hand | يَدِهِ ×1 | support | **lookup owed** | rev 6 keeps one encounter |

**SC-102:** `ضَحِكَ` gains the printed form `تَضْحَكُ` (Story 2, «خَدِيجَة تَضْحَكُ فِي الصُّورَةِ.»); still support, still one of the three story verbs.

**Story verbs in Unit 2 after rev 6:** `أَعْطَى · ضَحِكَ · نَظَرَ إِلَى` — three, the CR-6 ceiling exactly. `رَجَعَ` left the support count when SC-094 made it a target.

### 2.9 The verb inventory — rows opened 2026-09-16 ⟨SC-094⟩

*All lookup owed unless stated. Home unit = where productive; forms are licensed at that Gate A.*

| Verb | Home | Verb | Home | Verb | Home |
|---|---|---|---|---|---|
| ذَهَبَ | U2 | رَجَعَ | U2 | **وَضَعَ** | U2 |
| أَعْطَى | U3 | أَخَذَ | U3 | اِحْتَاجَ | U3 |
| عَادَ | U3 | عَاشَ | U3 | أَكَلَ | U4 |
| شَرِبَ | U4 | نَظَرَ إِلَى | U4 | قَرَأَ | U5 |
| كَتَبَ | U5 | لَعِبَ | U5 | سَكَنَ | U5 |
| خَرَجَ | U5 | مَشَى | U5 | عَمِلَ | U5 |
| بَدَأَ | U5 | بَحَثَ عَنْ | U6 | وَجَدَ | U6 |
| سَأَلَ | U6 | عَرَفَ | U6 | سَمِعَ | U6 |
| أَتَى (alt. جَاءَ) | U6 | شَعَرَ بِـ | U7 | بَكَى | U7 |
| ضَحِكَ | U7 | فَهِمَ | U7 | فَعَلَ | U7 |
| تَذَكَّرَ | U8 | صَنَعَ | U8 | — | — |

### 2.10 Unit 3 — rows opened 2026-09-28 ⟨SC-109⟩

*Source: `INTALIQ1_UNIT3_STORY_DRAFTS.md` revision 1. The dictionary is not in session; every "lookup owed" is exactly that. Printed forms verified by `canonCheck` (unit-03 158 / unit-03p 118, QC clean).*

| # | Lemma | Gloss | Printed forms (rev 1) | Status | Rank / page | Evidence |
|---|---|---|---|---|---|---|
| U3-01 | **أُمّ** | mother | أُمُّهُ · أُمِّي · أُمِّهِ · أُمُّ | new_core | lookup owed | SC-109 band |
| U3-02 | **أَب** | father | أَبُوهُ · أَبِي · أَبُوكَ | new_core | lookup owed | SC-109 band; five-noun forms nominative only |
| U3-03 | **أُخْت** | sister | أُخْتُهُ · أُخْتِهِ | new_core | **226 / p. 43** | eye-read (§2.5 family box) |
| U3-04 | **أَخ** | brother | أَخُو · أَخُوكِ · أَخِي | new_core | lookup owed | SC-109 band |
| U3-05 | **مَعَ** | with | مَعِي · مَعَهَا · مَعَهُ · مَعَ | new_core | **17 / p. 10** | function-word progression §4.5; canonical NEW, gate passed SC-109 |
| U3-06 | **عِنْدَ** | has (system) | عِنْدِي · عِنْدَكِ · عِنْدَكَ · عِنْدَهُ · عِنْدَهَا · عِنْدَ | **promoted: input-first → productive** | 40 / p. 12 (U1) | B-PA5 scheduled promotion; SC-109 |
| U3-07 | **لَيْسَ** | is not / has no | لَيْسَ · لَيْسَتْ · وَلَيْسَ | productive with agreement | spine, no claim | G-32 promoted |
| U3-08 | **لِـ** | for | لَكَ · لَكِ · لِخَدِيجَة · لِسَامِي | productive (suffixed) | lookup owed (U1 pending) | G-30 |
| U3-09 | **أَعْطَى** | give | يُعْطِيهِ · يُعْطِيهَا · تُعْطِيهِ · أَعْطَتْ · أَعْطَاهَا | **target verb** (from support) | lookup owed | verb inventory U3 |
| U3-10 | **أَخَذَ** | take | يَأْخُذُ · أَخَذَ | target verb | lookup owed | verb inventory U3 |
| U3-11 | **اِحْتَاجَ إِلَى** | need | أَحْتَاجُ | target verb (chunk CH-23) | lookup owed | verb inventory U3 |
| U3-12 | **عَاشَ** | live | يَعِيشُ | target verb | lookup owed | verb inventory U3 |
| U3-13 | **أَرَادَ** | want | أُرِيدُ · تُرِيدُ | recycled; `تُرِيدُ` first printed (V13) | 126 / p. 20 | U1 row 4 |
| U3-14 | **كُرَة** | ball | الْكُرَةَ · الْكُرَةُ · الْكُرَةِ · كُرَةٌ | support | lookup owed | drafts §5 |
| U3-15 | **هَدِيَّة** | gift | هَدِيَّةٌ · الْهَدِيَّةُ · الْهَدِيَّةَ | support | lookup owed | drafts §5 |
| U3-16 | **صَغِير** | small | الصَّغِيرَةُ · صَغِيرٌ · الصَّغِيرُ | support | lookup owed | drafts §5 |
| U3-17 | **بِجَانِبِ** (`جَانِب`) | beside | بِجَانِبِ | support (SC-103) | lookup owed (`جَانِب`) | Alhawary 8.2 p. 147 lists *jaanib-a* |
| U3-18 | **مَاذَا** | what? | مَاذَا | support inside CH-22 (SC-109 item 4) | lookup owed | 7.1.5 p. 136 |
| U3-19 | **نَظَرَ** | look | يَنْظُرُ · نَظَرَ · نَظَرَتْ | support story verb (home U4); first past forms | lookup owed | CR-6 |
| — | recycled unchanged | — | `أَيْنَ · فِي · عَلَى · تَحْتَ · هُنَا · هُنَاكَ · ذَهَبَ · إِلَى · رَجَعَ · وَلَد · اِسْم · رَأَى · قَالَ · دَخَلَ · لَا · نَعَمْ · أَنْتَ · هٰذَا · أَنَا · مَنْ · قَلَم · فَصْل · يَا · كِتَاب · بَيْت · بَاب · مِفْتَاح · أَرْض · قِطّ · كَبِير · ضَحِكَ · أَيْضًا · وَلٰكِنْ` | as before | — | engine items unit-03 / unit-03p |

**Unit 3 totals ⟨SC-107 running count⟩:** new core **5** · promotions 3 · support 4 lexical + 1 in-chunk + 1 story-verb form · target verbs 4 · chunks CH-21–CH-26 · recognition 0 · owed lookups 10 + `جَانِب`.

## 3. What the ledger found

**Recounted 2026-09-15 (SC-077). Thirty rows, every one accounted for:**

| Category | Count |
|---|---:|
| Entries with recorded frequency evidence | **19** |
| Separately authorized lexical-plural entry (`صَدِيقَاتٌ`, SC-062 §20L) | **1** |
| Spine entries making no frequency claim (`هُنَاكَ` · `لَيْسَ`, Manual §4.10) | **2** |
| Pending | **6** |
| Chunks making no independent frequency claim (CH-01 · CH-02) | **2** |
| **Total** | **30** |

**The packet's proposed accounting was 12 / 1 / 2 / 12 / 2 = 29 and is superseded**: ten rows moved from pending to evidenced this pass, and `هٰذَا` was added as a thirtieth row when `هٰذِهِ` proved to be its own headword.

### Flag V-3 — six lexical items, eight printed forms, no engine card for any of them

*Recount 2026-09-15 under reconciliation item R-6. The earlier summary of this flag said "six" and then listed four; the figure below is machine-derived and exact.*

| Item | Printed forms | Occurrences |
|---|---|---:|
| `لَا` | لَا | 5 |
| `يَا` | يَا | 5 |
| `نَعَمْ` | نَعَمْ | 3 |
| `أَنْتَ` | أَنْتَ · أَنْتِ · وَأَنْتِ | 4 |
| `هٰذِهِ` | هٰذِهِ | 1 |
| `هِيَ` | هِيَ | 1 |

`أَنْتَ / أَنْتِ` is **one item**: SC-062 item 3 rules them together (*"both from Unit 1… splitting them would have made shipped text non-compliant to no purpose"*). `لَا` and `نَعَمْ` have rows in this ledger (#9, #22) and still have **no engine card**; the other four have no entry anywhere.

**And the recount produced a finding.** The scope map's Unit 1 new-core list reads *"greetings chunk… person words… **نَعَمْ / لَا**، مَنْ؟، a first adjective pair."* **`نَعَمْ` and `لَا` were designed as Unit 1 core in the first scope map and were never carded.** Carding them delivers something already authorized rather than admitting anything new.

A learner meets `أَنْتِ` in the unit titled «مَنْ أَنْتَ؟» and the platform never teaches it. Statuses proposed and band consequence computed at **R-6**; **no Unit 2 recycled-share figure may be run or quoted until this closes (R-11).**

### Flag V-4 — encounter floors, measured

LC-6 asks ≥3 at debut, ≥6 across readings, ≥8 counting activities. Measured 2026-09-14 across both readings plus every activity the engine generates and qc passes:

| Lemma | readings | activities | total | ≥8? |
|---|---:|---:|---:|---|
| قَالَ | 28 | 24 | 52 | ✓ |
| أَنَا | 13 | 11 | 24 | ✓ |
| قَلَم | 12 | 13 | 25 | ✓ |
| رَأَى | 7 | 12 | 19 | ✓ |
| لِـ | 6 | 13 | 19 | ✓ |
| صَدِيق | 7 | 9 | 16 | ✓ |
| مَنْ | 7 | 7 | 14 | ✓ |
| لَيْسَ | 6 | 8 | 14 | ✓ |
| هُنَاكَ | 6 | 7 | 13 | ✓ |
| اِسْم | 6 | 6 | 12 | ✓ |
| عِنْدَ | 6 | 5 | 11 | ✓ |
| دَخَلَ | 2 | 8 | 10 | ✓ |
| قَائِمَة | 5 | 4 | 9 | ✓ |
| **أَهْلًا** | 3 | 4 | **7** | ✗ |
| **بِنْت** | 3 | 4 | **7** | ✗ |
| **السَّلَامُ عَلَيْكُمْ** | 2 | 4 | **6** | ✗ |
| **أَرَادَ** | 2 | 4 | **6** | ✗ |
| **وَلَد** | 2 | 3 | **5** | ✗ |
| **أَحَبَّ** | 1 | 4 | **5** | ✗ |
| فَصْل | 1 | 2 | 3 | ✗ — support, floor does not apply |
| تَكَلَّمَ | 1 | 2 | 3 | ✗ — recognition, floor does not apply |

**Six core targets sit below the with-activities floor.** The sharpest is **أُرِيدُ at 6**: SC-059 promoted it into Story 1 precisely because V3 puts new core there, and it occurs twice in print. أَحَبَّ at 5 is the unit's closing emotional beat and is said once.

**A limit on this measurement, stated rather than hidden.** It counts the platform only. The textbook's twelve activity sets, the roster tasks, the authentic corner and the can-do page are not in the engine and add encounters this table cannot see. The table is therefore a **floor on the floor** — it proves these six are not carried by the platform, not that the unit fails LC-6. Closing the question needs the textbook activities counted by the same method.

---

## 4. Method, so this is reproducible

Forms verified by `canonCheck` and `wordRe` against the printed canon now stored in the engine (SC-064/065): `node -e 'API.qc(API.UNITS["unit-01"], API.gen(...))'` fails the unit if any card claims a form the book does not print. Reading encounters are whole-word counts over that same canon. Activity encounters are `qc().ok` entries carrying an `item`, mapped to lemmas by the §11 lemma map in `ledger/lemmas.py`. Every count in this file was re-run at the moment it was written, 2026-09-14 (SC-050).
