# Intaliq 1 — Question-Word Posters

*Created 2026-10-10 under **SC-114** · Editor (Text role) · owned by the Art role for production (SC-112/SC-113) · a classroom instrument, not a product*

```
Owner's ruling (SC-114): "USE هَلْ and any question word freely. the classroom posters
should support and scafold them."
Posters scaffold what the readings expose. They never teach, never explain, never test.
```

---

## 1 · What a poster is for

Under SC-114 a question word may be printed in a reading before the unit that teaches it (`هَلْ` is taught at Unit 4 and printed from Unit 2; `مَاذَا` at Unit 6, printed from Unit 3). The poster is the standing support for that early exposure: the word, large, on the wall of the room where the book is read, with one question the class has already read under it. A learner who meets «هَلْ عِنْدَكِ الْكُرَةُ؟» on the page has met the same `هَلْ` on the wall over a question they already understood. The wall says nothing the page did not.

The posters are **cumulative**: a classroom working in Unit 3 has the Unit 1 and Unit 2 posters up. They are never taken down within the level.

## 2 · What is on a poster — and what is not

| On it | Not on it |
|---|---|
| **The question word**, fully vocalised, as the largest element | any English (P-6; the student book's single English element is the pop-up, SC-018) |
| **One model question**, quoted **verbatim** from a reading the class has read by the time the poster goes up, with its harakat exactly as printed in the canon | a grammatical term, a label, a translation, a rule |
| **One picture** in the course style (rich cartoon, SC-113), text-free, produced through the producer; where the model question has a frame in the reading's strip, the poster reuses that frame's scene | the **answer** to the model question (the poster asks; the room answers) |
| the Intaliq word-mark and the unit number, small, at the foot | digits other than the unit number, which is Western (SC-022) |

**One word, one poster.** `مَنْ أَنْتَ؟` and `مَنْ عِنْدَهُ قَلَمٌ؟` are two questions, not two posters; the `مَنْ` poster carries one of them.

## 3 · Rules

1. **Verbatim or nothing.** The model question is a substring of a frozen reading's `canon` (or, where no reading prints the word yet, of a frozen apparatus text, and the spec says so). The build asserts the substring the way `canonCheck()` asserts a sentence (SC-064). A poster whose question is not in a frozen text is not built.
2. **No spoiler.** The picture must not reveal a turn, a holder or a hiding place the reading withholds (criterion 27 binds the drawings, SC-034/SC-113). The `أَيْنَ` poster shows someone looking, not where the key is.
3. **No answer.** Not printed, not drawn: the poster for «مَنْ عِنْدَهُ الْكُرَةُ؟» does not show who has the ball.
4. **Sensitivity law** (SC-027 / SC-036) binds the picture as it binds every frame.
5. **No teaching.** No English, no term, no arrow between the word and anything, no "= ?". The poster is input, not instruction (SC-073 item 4's distinction applies: *appearance in comprehensible input*, nothing further).
6. **Due at the freeze of the first unit that prints the word.** Units 1 and 2 are frozen; their posters are due now. A word first printed in an apparatus text rather than a reading gets its poster then too, from the apparatus text, and is marked as such in §4.
7. **Not a product and not a drill.** The SC-096 shape (Student · Digital · Notebook) is unchanged. Posters are generated at freeze beside the teacher's page (SC-104) and are reached **only from the teacher's page**, never from the student Studio — they are for a wall, not a screen. Zero preparation beyond printing and hanging (P-4). No activity references a poster; no C-format uses one as a prop.
8. **Never assessed; nothing on it becomes assessable** before the unit that teaches the word (function-word progression §3 and §6).

## 4 · The set and its schedule

| Word | Poster | First printed | Model question (candidate; **verified as a canon substring at build**) | Source | Due | Status |
|---|---|---|---|---|---|---|
| `مَنْ` | `poster-man` | Unit 1 (core) | «مَنْ أَنْتَ؟» — the unit's own title, printed in Reading 2 («مَنْ... مَنْ أَنْتَ؟»); alternative «مَنْ عِنْدَهُ قَلَمٌ؟» | Unit 1 Reading 2, frozen | **now** | owed — Art role |
| `أَيْنَ` | `poster-ayna` | Unit 2 (core) | «أَيْنَ مِفْتَاحِي؟» — the title of Story 1 | Unit 2 Story 1, frozen (SC-105) | **now** | owed — Art role |
| `هَلْ` | `poster-hal` | Unit 2 Story 1 ×3 (owner's text, SC-095) | one of the three `هَلْ` questions of «أَيْنَ مِفْتَاحِي؟», chosen at build for the shortest line that stands alone | Unit 2 Story 1, frozen | **now** | owed — Art role |
| `مَاذَا` | `poster-madha` | Unit 3 CH-22 (SC-109 item 4) | «مَاذَا تُرِيدُ؟» (in Story 1 as «وَأَنْتَ، مَاذَا تُرِيدُ؟») | Unit 3 Story 1 — **not frozen** | after Unit 3's Gate B | waits |
| `مَا` | `poster-ma` | Unit 3 apparatus only (invent question) | «مَا اسْمُ الْقِطِّ؟» — **apparatus text, not a reading**; if a reading prints `مَا` before Unit 3 freezes, the reading's line replaces it | Unit 3 short-answer set — not frozen | after Unit 3's Gate B | waits |
| `لِمَاذَا` | `poster-limadha` | not yet printed (scheduled U7) | — | — | at the freeze of the first unit that prints it | — |
| `كَيْفَ` · `مَتَى` · `كَمْ` · `لِمَنْ` | — | not yet printed | — | — | at the freeze of the first unit that prints it | — |

A word that is never printed in Intaliq 1 never gets a poster. The set is not completed for completeness's sake — that would be the thematic padding the rules forbid.

## 5 · Production (Art role, through the producer — SC-113)

- **Slot ids** as in §4 (`poster-man`, `poster-ayna`, `poster-hal`, `poster-madha`, `poster-ma`, …), one text-free PNG per slot, true-white outside the scene is not required (SC-113 supersedes SC-037 inside the frame; the poster's own margins are white), **no text in the image** — the word and the question are typeset by the build, not drawn, so a correction to a harakah never costs a redraw (art package spec §2 and §4 apply).
- **Size:** square **2000 × 2000 px** PNG, the scene composed so that the top third can carry the word and the bottom band the question when the build lays out an A3 portrait sheet at 300 dpi. If the owner wants another sheet size, the image is unchanged and the layout changes.
- **Reuse before redraw:** where the model question has a frame in the unit's strip (`u2-s1-*` for «أَيْنَ مِفْتَاحِي؟»), the poster scene is **derived from that frame's composition** — same room, same figure, same colours — so the wall and the page agree. The producer's unlock loop handles corrections as for any slot.
- **Characters:** the figures in a poster are the reading's own (Unit 2: كَرِيم at the door; Unit 3: يُوسُف and لَيْلَى), drawn to the identities already accepted (SC-111/SC-113 reservation rows). رَزَان appears on a poster only if the model question is hers.
- **Build:** the poster sheets are generated at freeze by the same step that generates the teacher's page (runbook stage 14; `build_teacher_pages.py` gains a posters section or a sibling script), from a manifest `art_manifest_posters.json` in the art exchange folder, and the teacher's page lists *"Posters this unit adds: …"*. The release gate (TF-9, `verify_release.py`) checks that no student route links to a poster sheet, exactly as it checks for the teacher's page.

## 6 · Classroom use (what the teacher's page says, three lines or fewer)

Hang the unit's posters before Phase 1 and leave every earlier unit's up. When a question word comes up in a reading or a C-format, point to the poster — don't explain it. Never drill from the wall.

## 7 · QC at build

| Check | Rule |
|---|---|
| Word is fully vocalised and matches the function-word progression's licensed printed form | §6 table |
| Model question is a verbatim substring of a frozen canon (or frozen apparatus text, marked) | §3 rule 1 |
| No Latin letter, no Eastern digit (U+0660–0669), no digit except the unit number | P-6, SC-022 |
| Picture shows no withheld fact and no answer | §3 rules 2–3 |
| Picture passes the sensitivity law | SC-027 / SC-036 |
| Poster sheet reachable only from the teacher's page; TF-9 confirms no student route links it | §3 rule 7 |
| Status table §4 updated the day a poster ships (SC-050: a stated status is re-run when stated) | — |

## 8 · What this file does not decide

The ranks of `هَلْ · مَاذَا · مَا · مَنْ` and the Alhawary subsections marked *to locate* in the progression §6 are **owed**, not estimated here. Whether a poster set should also exist for words outside the question class (connectors, `عِنْدَ / لِـ`) is not raised by SC-114 and is not proposed. The sheet size in §5 is an implementation default, changeable without a ruling.
