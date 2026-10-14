# Intaliq 1 — Unit 1 readiness for instructional verification (SC-123) · Studio Version 47 · review build

> ⟨**SUPERSEDED IN PART — SC-124, 2026-10-13.** A record. Its completion rule (§1, §7), its evidence plan and learner check (§3) and every *not run / not observed* requirement are **cancelled**: no pilot, observation, evaluation survey or evidence record is required. **Current completion rule:** 72 verified recordings · 3 authentic photographs · release gate and content checks · the SC-009 content and design review recorded — Unit 1 Build §9.8. What stands from this report: the two notebook corrections (§2), the verification results of Version 47 (§4), and the supply list (§5).⟩

*Editor (Text role) · 2026-10-13. Governance applied and instruments prepared; **nothing has been administered and no learning effectiveness is demonstrated or claimed.** Unit 1 remains a review build.*

## 1 · Governing entry and the completion rule

**SC-122** (2026-10-13) adopted the learning-effectiveness standard and the evidence template and reconciled the closure rule — **Route A**. The standard, the template, runbook stages 3 and 14 (and §16), and the Unit 1 protocol v2 agree. The contradiction you named is settled by that entry, not by this pass: SC-009 permits panel verification; SC-121's "the learner check has been run and recorded" is read per SC-122 (b); protocol v2 §9 states it. The two places that still restated SC-121's old wording (Unit 1 Build §9.6 and the status board) now carry the SC-122 reading. **Unit 1 is complete when the 72 clips are verified and bound, the three photographs are in their slots, and the expert panel has run the check and recorded a design review.** Three statuses are kept apart everywhere: technical verification (run, Version 47) · panel design review (not run) · observed learner performance, delayed, transfer (not observed). No genuine contradiction remains; no owner decision is needed to proceed.

## 2 · Changed files and why

| File | Change | The learner difficulty it prevents |
|---|---|---|
| `source/pipeline/school_course_studio.html` → `index.html`, `404.html` | **N1 أ line 1** now the story's words «تَدْخُلُ [ ]. رَزَان لَيْسَ [ ] صَدِيقٌ.»; bank `الْفَصْلَ` replaces `رَزَان` | the old answer (رَزَان) contradicted the story's line «تَدْخُلُ الْفَصْلَ»; a learner checking the page against the story — the self-checking design — found the story's word missing from the bank and a leftover word that fit nowhere the story put it |
| same | **N2 models row** «يَدْخُلُ عُمَر · تَدْخُلُ رَزَان · يَقُولُ عُمَر · تَقُولُ رَزَان · «عُمَر صَدِيقِي!» · «رَزَان صَدِيقَتِي!»» | three slash choices with no model, and `صَدِيقِي` met nowhere in the input before the line: the gender choice the check measures would have been a guess, not a use of language the unit supplied |
| `INTALIQ1_UNIT1_LEARNING_EVIDENCE_RECORD.md` | §A expanded to eight functions; Version 47 | — (the plan names, before anyone is observed, what each task needs and what would count) |
| `INTALIQ1_UNIT1_LEARNER_CHECK_PROTOCOL.md` (v2) | pointer to the kit; Version 47 | — |
| `INTALIQ1_UNIT1_OBSERVATION_KIT.md` (new) | the observer's materials | an observer improvising probes in the room, unlabelled help counted as success, restricted preparation read as design failure |
| `INTALIQ1_UNIT1_SUPPLY_LIST.md` (new) | the one list of external inputs | recordings or photographs arriving in a form the build or the tasks cannot use |
| `SCHOOL_COURSE_DECISION_REGISTER.md` | SC-123 | — |
| `SCHOOL_COURSE_UNIT1_BUILD.md` | §9.6 line read per SC-122; §9.7 added | — |
| `SCHOOL_COURSE_AUTHORS_PAGE.md` · `00_SOURCE_INDEX.md` · status board | synchronised | — |

Untouched, verified: both frozen stories, every canon and licence, every art file, the engine.

### Audit findings, batched

**Blocking:** none found. **Important, fixed:** the two above. **Important, watched (not changed):** C1's question form `عِنْدَكَ / عِنْدَكِ` (licensed SC-016) is first met on the C1 page itself, carried by the one planned teacher reading and the printed answer models; Check A counts every prompt beyond that reading, and if learners cannot ask or answer without more, the prepared revision is to print the exchange «هَلْ عِنْدَكَ قَلَمٌ؟ — نَعَمْ! عِنْدِي قَلَمٌ.» as a labelled phrase on the picture spread and add a pathway card for it — evidence first, then the change. **Confirmed sound:** C1 precedes N2 (p. 9 before p. 5; N2 heading; teacher flow); both stories feed preparation (C1's «لَيْسَ عِنْدِي قَلَمٌ.» model is Story 2's, so the five-phase order reads both before C1; Check A's shortened order is labelled a diagnostic); the absent learner's alternative is printed on N2; N1 ب copies past forms from its bank; N3 has a model for every choice; Reading 2's match uses its numbered strip. **Minor polish, left:** N1 أ line 3 elides «لَيْسَ اسْمِي سَارَة!» from هُدَى's protest — its slot still has one answer.

## 3 · The evidence plan and the operative check

**Plan** (`INTALIQ1_UNIT1_LEARNING_EVIDENCE_RECORD.md` §A): reading meaning of Story 1 · reading meaning of Story 2 · listening (held: no recordings) · the C1 exchange · supported speaking C3/C4 · supported writing N1–N3 · functional text · delayed retention and small transfer — each with authorized language, preparation, repeated processing, supports, observable behaviour, evidence sought. Every observation: **not run / not observed**.

**Check** (protocol v2 + kit): **Check A**, a forty-minute cold-read diagnostic — decoding check, Phase 1 with the task number recorded (an unfinished pathway is *restricted preparation*, never completed preparation), Reading 1 with the page sets and pointing probes P1–P3, C1, N2, N3. **Check B**, inside ordinary teaching after the actual five-phase sequence, at six observation points, with the repeated-processing probes R1–R2 and the Reading 2 probes Q1–Q3. **Delayed probe** at the next lesson before review (D1–D3 meaning, D4 exchange with a new partner, D5–D6 changed-name and changed-object captions); listening probes L1–L2 held. Every response labelled **W** within planned support · **X** extra assistance · **S** answer supplied · **N** not observed, with a reason for each difficulty. Sheets A, B, D; then sheet → record §B–§E → *supported / revise and recheck / insufficient evidence* → source change → recheck Version. Children labelled A–F; no names, scores, keys or public results.

## 4 · Verification

Rebuilt from the authoritative sources (`INTALIQ_STUDIO_VERSION=47 node source/pipeline/build_studio_art.cjs`); `verify_release.py . 47` **exit 0**: 14 routes clean; all nine pathways walked to their end in a browser (Unit 1 vocab 48/48 · reading 46 · reading-2 28); Unit 1 print and notebook resources present (read-match 5 pictures / 5 sentences, who-says faces and slots, sequence boxes, every sheet's Arabic rubric); **language sweep 711 learner-visible Arabic tokens, 0 outside the canons and the apparatus licence**; mutation tests block all six units; listening fixture test holds; evidence-record check reads VERSION 47, design review *not run*, learner evidence *not observed*. Learner-view screenshots of N1 أ, N2 and the Reading 2 match inspected. The kit's probes swept separately (141 tokens; three observer-facing words outside the licence, never shown to a learner). **Limits:** no person has used any of this; the gate proves the pages work and print what they should, not that children understand them. Listening machinery is tested on fixtures only. Version 47 is built and committed but **not yet pushed** — the live site shows Version 46 until the Mac clone pushes.

## 5 · Missing inputs (one list: `INTALIQ1_UNIT1_SUPPLY_LIST.md`)

72 recordings — 46 for «قَائِمَةُ رَزَان» (24 sentences + 22 items) and 26 for «مَنْ أَنْتَ يَا قَلَم؟» (11 + 15), each row with its exact text and file path, one native MSA voice, verified clip by clip by a named listener. Three real photographs — a shop sign with a person's name, a school or building door sign, a street name plate — with provenance. None supplied; both marked **not delivered**. SC-028 (no synthesised shipped audio) and SC-020 (no mock realia) unchanged.

## 6 · Owner decisions

None required for this pass. Two things only you can arrange: the panel sitting (which closes Unit 1 under Route A) and, when you choose, a learner sitting (which is the only thing that can fill the learner rows). One standing policy point, unchanged: whether synthesised speech may stand in for a pilot is a change to SC-028 and is not assumed.

## 7 · Exactly what still closes Unit 1

1. The 72 clips recorded, verified by a named listener, bound in the unit data, rebuilt and gated.
2. The three photographs placed with provenance, picture–task fit checked, rebuilt and gated.
3. The expert panel runs the check (protocol v2) and the design review is recorded in the evidence record §D.
4. A closing register entry. Learner performance, retention and transfer remain *not observed* until learners are observed; no learning claim is made before then.
