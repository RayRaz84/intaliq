# Intaliq 1 — Unit 1 consolidated supply list (what is still owed from outside the Text session)

*Editor (Text role) · 2026-10-13 · under SC-121/SC-122. One list, nothing else to read: the 72 recordings and the 3 photographs Unit 1 needs before it can be called complete, each with its exact text or specification, the filename the build expects, how it is verified, and the task it serves. **None of it exists yet.** Synthesised speech is not acceptable as a shipped clip (SC-028); mock or generated "authentic" realia are not acceptable in the corner (SC-020); neither can be changed by the Text role. All independent source work is done: the listening families, sound-first pathways, corner tasks and slots are built and switch on by themselves when these inputs are bound.*

## A · Recordings — 72 clips

**Voice:** one native MSA speaker for the whole unit. **Delivery:** exactly as printed, fully vocalised, child-directed pace; dialogue as speech, narration as narration; no word added, dropped or paraphrased. **Format:** mono, 44.1 kHz, MP3 ≥ 128 kbps (or OGG); one file per row; leading/trailing silence ≤ 0.3 s; peak-normalised. **Naming:** exactly the path in the table, under `assets/audio/`. **Verification (per clip, a person):** a named Arabic-reading listener plays the file while reading the row's text, confirms every word, ending and sentence melody; any deviation → re-record, never patch; the listener's name and the ISO date go into `clips_manifest.json` (`verified_by`, `verified_on`); the build computes the hash and refuses any file that does not match. **Task fit:** a *sentence* clip serves hear-which-line (`listen_which`), hear-who-says (`listen_who`, quoted lines) and the reading pathway's opening lines; an *item* clip serves hear-and-tap (`listen_tap`) and the sound-first vocabulary pathway (every pictured core item heard before it is read).


### unit-01 · «قَائِمَةُ رَزَان» — 46 clips

| # | id | kind | ref | text to record (exact) | file |
|---|---|---|---|---|---|
| 1 | `c_m00` | sentence | `m00` | هُنَاكَ بِنْتٌ اسْمُهَا رَزَان. | `assets/audio/unit-01/m00.mp3` |
| 2 | `c_m01` | sentence | `m01` | تَدْخُلُ الْفَصْلَ. | `assets/audio/unit-01/m01.mp3` |
| 3 | `c_m02` | sentence | `m02` | رَزَان لَيْسَ لَهَا صَدِيقٌ... وَعِنْدَهَا قَائِمَةٌ. | `assets/audio/unit-01/m02.mp3` |
| 4 | `c_m03` | sentence | `m03` | تَقُولُ: «السَّلَامُ عَلَيْكُمْ! أَنَا رَزَان.» | `assets/audio/unit-01/m03.mp3` |
| 5 | `c_m04` | sentence | `m04` | يَقُولُ عُمَر وَسَارَة وَرَنَا: «وَعَلَيْكُمُ السَّلَامُ!» | `assets/audio/unit-01/m04.mp3` |
| 6 | `c_m05` | sentence | `m05` | تَرَى رَزَان الْقَائِمَةَ. | `assets/audio/unit-01/m05.mp3` |
| 7 | `c_m06` | sentence | `m06` | هُنَاكَ اسْمٌ: «عُمَر». وَهُنَاكَ اسْمٌ: «سَارَة». | `assets/audio/unit-01/m06.mp3` |
| 8 | `c_m07` | sentence | `m07` | تَقُولُ: «مَنْ عُمَر؟ وَمَنْ سَارَة؟ أُرِيدُ صَدِيقًا!» | `assets/audio/unit-01/m07.mp3` |
| 9 | `c_m08` | sentence | `m08` | تَرَى رَزَان هُدَى وَتَقُولُ: «هٰذِهِ سَارَة!» | `assets/audio/unit-01/m08.mp3` |
| 10 | `c_m09` | sentence | `m09` | تَقُولُ هُدَى: «لَا! لَا! لَيْسَ اسْمِي سَارَة! أَنَا هُدَى!» | `assets/audio/unit-01/m09.mp3` |
| 11 | `c_m10` | sentence | `m10` | تَقُولُ رَزَان: «أَهْلًا يَا هُدَى!» | `assets/audio/unit-01/m10.mp3` |
| 12 | `c_m11` | sentence | `m11` | تَرَى رَزَان وَلَدًا. تَقُولُ: «أَنْتَ عُمَر!» | `assets/audio/unit-01/m11.mp3` |
| 13 | `c_m12` | sentence | `m12` | يَقُولُ الْوَلَدُ: «نَعَمْ! أَنَا عُمَر! وَمَنْ أَنْتِ؟» | `assets/audio/unit-01/m12.mp3` |
| 14 | `c_m13` | sentence | `m13` | تَقُولُ رَزَان: «أَنَا رَزَان.» | `assets/audio/unit-01/m13.mp3` |
| 15 | `c_m13b` | sentence | `m13b` | يَقُولُ عُمَر: «أَهْلًا يَا رَزَان!» | `assets/audio/unit-01/m13b.mp3` |
| 16 | `c_m14` | sentence | `m14` | تَرَى رَزَان بِنْتًا. تَقُولُ: «وَأَنْتِ سَارَة!» | `assets/audio/unit-01/m14.mp3` |
| 17 | `c_m15` | sentence | `m15` | تَقُولُ الْبِنْتُ: «نَعَمْ! أَنَا سَارَة!» | `assets/audio/unit-01/m15.mp3` |
| 18 | `c_m15b` | sentence | `m15b` | يَرَى عُمَر الْقَائِمَةَ وَيَقُولُ: «هُنَاكَ اسْمٌ: "طَارِق"! لِي صَدِيقٌ: طَارِق!» | `assets/audio/unit-01/m15b.mp3` |
| 19 | `c_m16` | sentence | `m16` | تَرَى سَارَة الْقَائِمَةَ وَتَقُولُ: «هُنَاكَ اسْمٌ: "رَزَان"! مَنْ هِيَ؟» | `assets/audio/unit-01/m16.mp3` |
| 20 | `c_m17` | sentence | `m17` | تَقُولُ رَزَان: «أَنَا! أَنَا رَزَان!» | `assets/audio/unit-01/m17.mp3` |
| 21 | `c_m18` | sentence | `m18` | تَقُولُ سَارَة: «أَهْلًا يَا رَزَان! لِي صَدِيقَةٌ: رَزَان!» | `assets/audio/unit-01/m18.mp3` |
| 22 | `c_m18b` | sentence | `m18b` | وَتَقُولُ رَنَا: «وَأَنَا! لِي صَدِيقَةٌ!» | `assets/audio/unit-01/m18b.mp3` |
| 23 | `c_m19` | sentence | `m19` | تُحِبُّ رَزَان... الْقَائِمَةَ! | `assets/audio/unit-01/m19.mp3` |
| 24 | `c_m20` | sentence | `m20` | تَقُولُ رَزَان: «أَنَا رَزَان... وَلِي صَدِيقَاتٌ!» | `assets/audio/unit-01/m20.mp3` |
| 25 | `c_salam` | item | `salam` | السَّلَامُ عَلَيْكُمْ! | `assets/audio/unit-01/item_salam.mp3` |
| 26 | `c_ahlan` | item | `ahlan` | أَهْلًا يَا رَزَان! | `assets/audio/unit-01/item_ahlan.mp3` |
| 27 | `c_ana` | item | `ana` | أَنَا رَزَان. | `assets/audio/unit-01/item_ana.mp3` |
| 28 | `c_walad` | item | `walad` | هٰذَا وَلَدٌ. | `assets/audio/unit-01/item_walad.mp3` |
| 29 | `c_bint` | item | `bint` | هٰذِهِ بِنْتٌ. | `assets/audio/unit-01/item_bint.mp3` |
| 30 | `c_sadiq` | item | `sadiq` | رَزَان صَدِيقَتِي! | `assets/audio/unit-01/item_sadiq.mp3` |
| 31 | `c_inda` | item | `inda` | عِنْدَهَا قَائِمَةٌ. | `assets/audio/unit-01/item_inda.mp3` |
| 32 | `c_li` | item | `li` | لِي صَدِيقَاتٌ! | `assets/audio/unit-01/item_li.mp3` |
| 33 | `c_urid` | item | `urid` | أُرِيدُ صَدِيقًا! | `assets/audio/unit-01/item_urid.mp3` |
| 34 | `c_laysa` | item | `laysa` | لَيْسَ لَهَا صَدِيقٌ. | `assets/audio/unit-01/item_laysa.mp3` |
| 35 | `c_laha` | item | `laha` | لَهَا صَدِيقَةٌ. | `assets/audio/unit-01/item_laha.mp3` |
| 36 | `c_yadkhul` | item | `yadkhul` | تَدْخُلُ الْفَصْلَ. | `assets/audio/unit-01/item_yadkhul.mp3` |
| 37 | `c_yara` | item | `yara` | تَرَى رَزَان الْقَائِمَةَ. | `assets/audio/unit-01/item_yara.mp3` |
| 38 | `c_yaqul` | item | `yaqul` | تَقُولُ رَزَان: «أَهْلًا!» | `assets/audio/unit-01/item_yaqul.mp3` |
| 39 | `c_yuhibb` | item | `yuhibb` | تُحِبُّ رَزَان الْقَائِمَةَ. | `assets/audio/unit-01/item_yuhibb.mp3` |
| 40 | `c_hunaka` | item | `hunaka` | هُنَاكَ قَائِمَةٌ. | `assets/audio/unit-01/item_hunaka.mp3` |
| 41 | `c_man` | item | `man` | مَنْ عُمَر؟ | `assets/audio/unit-01/item_man.mp3` |
| 42 | `c_ism` | item | `ism` | هُنَاكَ اسْمٌ: «عُمَر». | `assets/audio/unit-01/item_ism.mp3` |
| 43 | `c_la` | item | `la` | لَا! لَيْسَ اسْمِي سَارَة! | `assets/audio/unit-01/item_la.mp3` |
| 44 | `c_naam` | item | `naam` | نَعَمْ! أَنَا عُمَر! | `assets/audio/unit-01/item_naam.mp3` |
| 45 | `c_anta` | item | `anta` | أَنْتَ عُمَر! | `assets/audio/unit-01/item_anta.mp3` |
| 46 | `c_hadha` | item | `hadha` | هٰذِهِ سَارَة! | `assets/audio/unit-01/item_hadha.mp3` |

### unit-01p · «مَنْ أَنْتَ يَا قَلَم؟» — 26 clips

| # | id | kind | ref | text to record (exact) | file |
|---|---|---|---|---|---|
| 1 | `c_r01` | sentence | `r01` | دَخَلَ كَرِيم وَقَالَ: «السَّلَامُ عَلَيْكُمْ!» | `assets/audio/unit-01p/r01.mp3` |
| 2 | `c_r02` | sentence | `r02` | قَالَتْ فَرِيدَة وَمَهَا وَزَيْد: «وَعَلَيْكُمُ السَّلَامُ!» | `assets/audio/unit-01p/r02.mp3` |
| 3 | `c_r03` | sentence | `r03` | قَالَ كَرِيم: «أُرِيدُ قَلَمًا. مَنْ عِنْدَهُ قَلَمٌ؟» | `assets/audio/unit-01p/r03.mp3` |
| 4 | `c_r04` | sentence | `r04` | قَالَتْ مَهَا: «لَا! لَيْسَ عِنْدِي قَلَمٌ!» | `assets/audio/unit-01p/r04.mp3` |
| 5 | `c_r05` | sentence | `r05` | قَالَ زَيْد: «أَنَا؟ لَا! لَيْسَ عِنْدِي قَلَمٌ.» | `assets/audio/unit-01p/r05.mp3` |
| 6 | `c_r06` | sentence | `r06` | قَالَتْ فَرِيدَة: «لَا يَا كَرِيم! لَيْسَ عِنْدِي قَلَمٌ.» | `assets/audio/unit-01p/r06.mp3` |
| 7 | `c_r07` | sentence | `r07` | كَرِيم... لَيْسَ عِنْدَهُ قَلَمٌ. | `assets/audio/unit-01p/r07.mp3` |
| 8 | `c_r08` | sentence | `r08` | قَالَ قَلَمٌ: «أَنَا! أَنَا قَلَمٌ!» | `assets/audio/unit-01p/r08.mp3` |
| 9 | `c_r09` | sentence | `r09` | رَأَى كَرِيم الْقَلَمَ وَقَالَ: «مَنْ... مَنْ أَنْتَ؟» | `assets/audio/unit-01p/r09.mp3` |
| 10 | `c_r10` | sentence | `r10` | قَالَ الْقَلَمُ: «أَنَا قَلَمُ كَرِيم! وَلِي صَدِيقٌ: كَرِيم!» | `assets/audio/unit-01p/r10.mp3` |
| 11 | `c_r11` | sentence | `r11` | قَالَتْ فَرِيدَة: «نَعَمْ يَا كَرِيم... هُنَاكَ قَلَمٌ يَتَكَلَّمُ!» | `assets/audio/unit-01p/r11.mp3` |
| 12 | `c_salam` | item | `salam` | السَّلَامُ عَلَيْكُمْ! | `assets/audio/unit-01p/item_salam.mp3` |
| 13 | `c_dakhala` | item | `dakhala` | دَخَلَ كَرِيم. | `assets/audio/unit-01p/item_dakhala.mp3` |
| 14 | `c_qala` | item | `qala` | قَالَ كَرِيم: «أَنَا!» | `assets/audio/unit-01p/item_qala.mp3` |
| 15 | `c_raa` | item | `raa` | رَأَى كَرِيم الْقَلَمَ. | `assets/audio/unit-01p/item_raa.mp3` |
| 16 | `c_inda` | item | `inda` | عِنْدَهُ قَلَمٌ. | `assets/audio/unit-01p/item_inda.mp3` |
| 17 | `c_man` | item | `man` | مَنْ عِنْدَهُ قَلَمٌ؟ | `assets/audio/unit-01p/item_man.mp3` |
| 18 | `c_hunaka` | item | `hunaka` | هُنَاكَ قَلَمٌ! | `assets/audio/unit-01p/item_hunaka.mp3` |
| 19 | `c_ana` | item | `ana` | أَنَا قَلَمٌ! | `assets/audio/unit-01p/item_ana.mp3` |
| 20 | `c_sadiq` | item | `sadiq` | لِي صَدِيقٌ: كَرِيم! | `assets/audio/unit-01p/item_sadiq.mp3` |
| 21 | `c_urid` | item | `urid` | أُرِيدُ قَلَمًا. | `assets/audio/unit-01p/item_urid.mp3` |
| 22 | `c_laysa` | item | `laysa` | لَيْسَ عِنْدِي قَلَمٌ! | `assets/audio/unit-01p/item_laysa.mp3` |
| 23 | `c_li` | item | `li` | لِي صَدِيقٌ: كَرِيم! | `assets/audio/unit-01p/item_li.mp3` |
| 24 | `c_la` | item | `la` | لَا! لَيْسَ عِنْدِي قَلَمٌ! | `assets/audio/unit-01p/item_la.mp3` |
| 25 | `c_naam` | item | `naam` | نَعَمْ يَا كَرِيم | `assets/audio/unit-01p/item_naam.mp3` |
| 26 | `c_anta` | item | `anta` | مَنْ... مَنْ أَنْتَ؟ | `assets/audio/unit-01p/item_anta.mp3` |

Delivered recordings come back as the folder `assets/audio/` plus the filled manifest; the Text role then copies the rows into the unit data as `audio.clips` with `audio.verified: true`, rebuilds (the build verifies every file and hash), runs the gate (the listening fixture test and the pathway walkthroughs now include the F9 tasks) and pushes; the teacher's page wording "no listening tasks" is lifted by the same build.

## B · Photographs — 3 real photographs for «عَرَبِيَّةٌ حَوْلَنَا»

**Format:** JPEG or PNG, landscape, ≥ 1200 px on the long side; delivered as `assets/photos/unit1-authentic/ac-1.jpg … ac-3.jpg` with `PROVENANCE.md` beside them (where · when · by whom · licence, one line each). **Authenticity:** photographs of real objects in the world, taken or licensed by the owner; faces, licence plates and house numbers tied to a person out of frame or cropped. **Verification (before the build):** the Editor checks picture–task fit at page size (SC-100 applied to the corner) and records it in the record §C.

| Slot | Photograph of | Must show | Must not | Serves task |
|---|---|---|---|---|
| `ac-1` | a real **shop sign carrying a person's name** (pharmacy, bakery, shop named for someone) | at least one name a Unit 1 learner can know — ideally a roster name: آدَم · رَنَا · سَارَة · طَارِق · عُمَر · رَزَان · نُور · بَدْر, or هُدَى · كَرِيم · مَهَا · زَيْد · فَرِيدَة — in clear Arabic lettering, legible at ~60 mm wide on the page | mock-ups, composites, AI-generated or edited signage; a sign dominated by long unrelated text | **1 · ○ أَيْنَ الِاسْمُ؟** — find and circle the name you know |
| `ac-2` | a real **school or building door sign** | a short label a child treats as "a place" (مَدْرَسَة, a room name, a number) | a poster or notice with running text | **2 · 👤 / 🏠 ؟** — person or place, answered by pointing at the icon |
| `ac-3` | a real **street name plate** | a street name in Arabic script with a letter or two a learner may find in their own name | a plate dominated by Latin script | **3 · ○ حَرْفٌ — اسْمِي** — circle one letter from your own name |

## C · Status

| Component | Owed | Status |
|---|---|---|
| Recordings | 72 clips (46 + 26) per §A, verified by a named listener | **none exist** |
| Photographs | 3 per §B with provenance | **none exist** |
| The sitting that closes the unit under SC-122 | the expert panel's design review (Route A), recorded in `INTALIQ1_UNIT1_LEARNING_EVIDENCE_RECORD.md`; learner sittings per the observation kit when the owner arranges them | **not run** |
