# Intaliq 1 — Unit 3 Visual Plan and Slot List

*Issued 2026-11-04 by the Art role, after the SC-135 freeze; **amended 2026-11-08 for Story 1 revision 4 (SC-138)** — frames 3, 4, 5 and 8 and phrase 10. **A plan, not an illustration — plan approval is not image authorization.** Machine-readable twin: `source/cast-and-art/art_manifest_unit3.json` (the producer reads that file; where the two differ, the JSON governs). Style: SC-113 rich-cartoon, Art Package Spec sizes (frames 590 × 490). Sentence ids are the engine's (`s00`…), as in the Unit 3 clip manifest.*

## 0 · Three owner questions before portraits are drawn

- **Q1** Is Unit 3's big cat a new cat (proposed) or Unit 2's orange-and-white cat? R-1 forbids carrying plot history, and Unit 2's cat lives at Karim's door.
- **Q2** Confirm or replace the five proposed people markers (and whether any SC-111 Unit 3 drawings should be transcribed instead).
- **Q3** Version A/B for Unit 3: the Studio line ('A keeps the cast and moves the key; B changes the setting and the object') was carried from Unit 2 and has no Unit 3 strips — draw Version A/B for Unit 3, or drop the line?

Frames and phrase pictures can be planned now; nothing is generated until Q1–Q2 are answered, because every frame depends on the cast sheets.

## 1 · Spoiler rules

- **Story 1 «مَنْ عِنْدَهُ الْكُرَةُ؟»:** the key is never visible before frame 6 — not under, near or behind the cat. The cat sits beside the door in frames 1 and 5 looking at nothing in particular; its interest in the ball shows only in frame 8, where Yusuf shares the ball and it ends up under the cat. Frame 1 shows nobody holding anything.
- **Story 2 «هَدِيَّةُ رَزَان»:** the ball does not exist in any frame before 6; خَدِيجَة does not appear before frame 4.
- **Phrase page** (read before the strip): phrase 13 takes the key from a bare floor — no cat, no door; phrase 17 puts the *ball* beside the door, not the cat or the key.

## 2 · Cast and objects

Reused unchanged (Unit 2 accepted files): `av-razan` · `av-razan-happy` · `av-razan-talk` · `av-razan-q` · `av-khadija` · `av-khadija-happy` · `obj-book` · `obj-pen` · `obj-key` · `obj-door` · `obj-house` · `u2-ph-01` · `u2-ph-02` · `u2-ph-03` · `u2-ph-04` · `u2-ph-05` · `u2-ph-06` · `u2-ph-08` · `u2-ph-16`.

| slot | character | identity (PROPOSED until confirmed) |
|---|---|---|
| `av-yusuf` | يُوسُف | boy; PROPOSED marker: short black hair with one swirl at the crown; fixed green top |
| `av-yusuf-q` | يُوسُف |  |
| `av-yusuf-talk` | يُوسُف |  |
| `av-yusuf-laugh` | يُوسُف |  |
| `av-layla` | لَيْلَى | girl, his little sister (smaller than Yusuf); PROPOSED marker: two short high pigtails with yellow bobbles; fixed yellow dress |
| `av-layla-talk` | لَيْلَى |  |
| `av-umm` | أُمُّهُ | adult woman, tall; PROPOSED marker: long dark hair in a low side ponytail over one shoulder; fixed plum top |
| `av-umm-talk` | أُمُّهُ |  |
| `av-ab` | أَبُوهُ | adult man, tall; PROPOSED marker: short dark beard and moustache; fixed grey shirt |
| `av-ab-q` | أَبُوهُ |  |
| `av-sami` | سَامِي | small boy, Khadija's little brother (clearly smaller than Razan); PROPOSED marker: round short hair with a front tuft; fixed red striped top |
| `av-sami-want` | سَامِي |  |
| `av-sami-happy` | سَامِي |  |
| `av-qitt3` | الْقِطُّ (Unit 3) | a BIG cat, distinct from Unit 2's orange-and-white cat (owner question Q1); PROPOSED: grey tabby with white socks |
| `av-qitt3-walk` | الْقِطُّ (Unit 3) |  |

Collision check against the Cast Bible reservation table: none of the proposed markers is taken (swirl at the crown ≠ Karim's three curls or Omar's spikes; high pigtails ≠ Razan's low side bundles or Maha's topknot; the mother's low side ponytail ≠ Nur's single plait — **closest pair, check at 48 px**; beard is new; Sami's front tuft ≠ Badr's side-swept fringe). Gender convention holds (gathered hair → girl).

| object | drawing |
|---|---|
| `obj-kura` | one ball, a single fixed drawing (PROPOSED: red-and-white panelled ball), no text |
| `obj-hadiya` | the gift: obj-book drawn smaller with a ribbon tied round it, book still recognisable |
| `obj-house-big` | a visibly bigger house than obj-house, same door drawing, same roof line |

## 3 · Story 1 — «مَنْ عِنْدَهُ الْكُرَةُ؟» — eight frames

| slot | text | event | show | must NOT show | risk |
|---|---|---|---|---|---|
| `u3-s1-1` | s00 | يُوسُف lives in a big house with his mother, father, little sister لَيْلَى and a big cat; the cat lives beside the door | the big house (av-yusuf, av-umm, av-ab, av-layla all neutral, standing apart); the big cat (av-qitt3) sitting beside the door | the ball, the book, the pen, the key — nobody holds anything | four people + cat in one frame: keep everyone small and separated; the cat must read as big (about a child's waist height) |
| `u3-s1-2` | s01 | Yusuf wants the ball and does not have it | Yusuf (-q) alone, both hands open and empty | the ball anywhere; Layla | the empty hands are the whole meaning |
| `u3-s1-3` | s02–s04 | Layla has the ball and asks what he will give her — she wants his book; his book is with their mother | Yusuf (-talk) facing Layla (-talk) who holds obj-kura against her chest, her free palm held out | the book (it is elsewhere); the mother | the ball must be held by Layla, not between them |
| `u3-s1-4` | s05–s07 | The mother has his book; she needs her pen to write; the father has it; Yusuf: «the pen too?!» and she laughs | the mother (av-umm-talk, laughing) at a table with a blank sheet of paper and NO pen, holding obj-book out; Yusuf facing her | the pen; the father; the ball | the empty paper is the mother's reason for the pen — it must read at strip size |
| `u3-s1-5` | s08–s10 | At the door: the father, ready to go out, has the pen and needs his key; Yusuf sums up everyone's wants and the father laughs | the father (av-ab, laughing) dressed to go out (jacket on) at the door holding obj-pen, free hand open; Yusuf beside him; the big cat sitting beside the door, neutral | the key — not under, behind or near the cat; the cat looking at anything in particular | the jacket and the door are the father's reason for the key; the cat gives nothing away |
| `u3-s1-6` | s11 | The reveal: the key is on the floor beside the door — under the cat | Yusuf (-q) looking down; the cat sitting; obj-key's bow and teeth visible under the cat | — | the key must be legible at strip size under the cat: show bow + teeth |
| `u3-s1-7` | s12–s13 | The chain runs back: key to father, pen to mother, book to Layla, ball to Yusuf — he laughs | Yusuf (-laugh) holding obj-kura; behind him, small: the father with obj-key, the mother with obj-pen, Layla with obj-book | the cat near the ball | each of the four objects in exactly one pair of hands; nothing else in frame |
| `u3-s1-8` | s14–s17 | The cat looks at the ball; Yusuf gives it the ball and they play; the ball ends under the cat; Layla asks who has it | Yusuf (-laugh) and the big cat playing by the door, obj-kura under the cat's paws; Layla (-talk) in the doorway | the cat running off with the ball (revision 3's ending) | the ball under the cat must echo frame 6's key under the cat |

## 4 · Story 2 — «هَدِيَّةُ رَزَان» — six frames

| slot | text | event | show | must NOT show | risk |
|---|---|---|---|---|---|
| `u3-s2-1` | s00 | Razan has a gift for Khadija — a small book — and goes to her house with it | av-razan-happy walking toward obj-house holding obj-hadiya | Sami; Khadija; the ball | the gift must read as a small book (ribbon round obj-book, smaller) |
| `u3-s2-2` | s01–s03 | By the door, Khadija's little brother Sami sees the gift and wants it; Razan says it is for Khadija | av-sami (-want) by the open door, reaching; av-razan-talk holding obj-hadiya back a little | Khadija; the ball; Sami holding anything | Sami must read as clearly smaller and younger than Razan |
| `u3-s2-3` | s04–s05 | Razan looks at Sami — small, no book — and gives him the book | av-razan handing obj-hadiya to av-sami | Khadija; the ball | the hand-over is the beat: the book between their hands |
| `u3-s2-4` | s06–s07 | Sami laughs, takes the book inside; Razan goes in too; Khadija is there; the book is with Sami | inside: av-sami-happy holding the book; av-khadija (neutral); av-razan entering | the ball | first frame with Khadija |
| `u3-s2-5` | s08–s09 | Razan explains, unsure; Khadija laughs: this is my little brother — I have a book, he doesn't | av-razan-q facing av-khadija-happy; Sami small in the background with the book | the ball | Razan's -q face is the only uncertain face in the strip |
| `u3-s2-6` | s10–s11 | Sami comes back with a ball and gives it to Razan; she goes home with it | av-sami-happy holding obj-kura out to av-razan-happy; Khadija behind | — | the ball is obj-kura, the same drawing as Story 1's |

## 5 · Phrase page — eighteen pictures

| slot | phrase | picture |
|---|---|---|
| `u3-ph-01` | هٰذَا أَبِي | the father alone (av-ab), neutral |
| `u3-ph-02` | هٰذِهِ أُمِّي | the mother alone (av-umm), neutral |
| `u3-ph-03` | هٰذَا أَخِي الصَّغِيرُ | Sami alone (av-sami), neutral |
| `u3-ph-04` | هٰذِهِ أُخْتِي | Layla alone (av-layla), neutral |
| `u3-ph-05` | عِنْدِي كُرَةٌ | a child's hands holding obj-kura, no face (first person is the reader) |
| `u3-ph-06` | لَيْسَ عِنْدِي كِتَابٌ | a child's two empty open hands; no book in frame |
| `u3-ph-07` | عِنْدَهُ قَلَمٌ | the father holding obj-pen |
| `u3-ph-08` | عِنْدَهَا كِتَابٌ | the mother holding obj-book |
| `u3-ph-09` | أُرِيدُ الْكُرَةَ | two hands reaching toward obj-kura, no face |
| `u3-ph-10` | مَاذَا تُعْطِينِي؟ | Layla (-talk) holding obj-kura, her other palm held out, asking |
| `u3-ph-11` | أَحْتَاجُ إِلَى قَلَمِي | an open hand held out toward obj-pen just out of reach, no face |
| `u3-ph-12` | يُعْطِيهَا الْكِتَابَ | Yusuf handing obj-book to Layla |
| `u3-ph-13` | يَأْخُذُ الْمِفْتَاحَ | a hand picking obj-key up from the floor line — no cat, no door |
| `u3-ph-14` | يَعِيشُ فِي بَيْتٍ كَبِيرٍ | obj-house-big alone |
| `u3-ph-15` | مَعِي | a child's hands holding obj-kura close to the chest, no face |
| `u3-ph-16` | هٰذِهِ هَدِيَّةٌ | obj-hadiya alone |
| `u3-ph-17` | بِجَانِبِ الْبَابِ | obj-kura on the floor beside obj-door — no cat, no key |
| `u3-ph-18` | الْكُرَةُ لَيْسَتْ مَعِي | Yusuf (-q) alone, empty hands, no ball in frame |

## 6 · Engine and notebook assignments

- **unit-03** items: `umm`→`av-umm` · `ab`→`av-ab` · `ukht`→`av-layla` · `inda`→`u3-ph-07` · `laysa`→`u3-ph-06` · `maa`→`u3-ph-15` · `aata`→`u3-ph-12` · `akhadha`→`u3-ph-13` · `ihtaja`→`u3-ph-11` · `aasha`→`u3-ph-14` · `arada`→`u3-ph-09` · `walad`→`av-yusuf` · `kitab`→`obj-book` · `miftah`→`obj-key` · `qitt`→`av-qitt3` · `kabir`→`obj-house-big` · `kura`→`obj-kura` · `bijanib`→`u3-ph-17` · `madha`→`u3-ph-10` · `bayt`→`obj-house` · `ayna`→`u2-ph-01` · `fi`→`u2-ph-02` · `ala`→`u2-ph-03` · `tahta`→`u2-ph-04` · `dhahab`→`u2-ph-06` · `rajaa`→`u2-ph-08` · `ard`→`u2-ph-16` · `saghir`→`av-layla` · `yadhak`→`av-yusuf-laugh`
  cast: `yusuf`→`av-yusuf` · `layla`→`av-layla` · `umm`→`av-umm` · `ab`→`av-ab` · `qitt`→`av-qitt3`; sentences: s00→u3-s1-1 · s01→2 · s02–s04→3 · s05–s07→4 · s08–s10→5 · s11→6 · s12–s13→7 · s14–s17→8
- **unit-03p** items: `akh`→`u3-ph-03` · `inda`→`u3-ph-07` · `laysa`→`u3-ph-06` · `maa`→`u3-ph-15` · `aata`→`u3-ph-12` · `akhadha`→`u3-ph-13` · `kitab`→`obj-book` · `saghir`→`av-sami` · `kura`→`obj-kura` · `hadiya`→`obj-hadiya` · `bijanib`→`u3-ph-17` · `huna`→`u2-ph-05` · `dhahab`→`u2-ph-06` · `rajaa`→`u2-ph-08` · `walad`→`av-sami` · `yadhak`→`av-sami-happy`
  cast: `razan`→`av-razan` · `khadija`→`av-khadija` · `sami`→`av-sami`; sentences: s00→u3-s2-1 · s01–s03→2 · s04–s05→3 · s06–s07→4 · s08–s09→5 · s10–s11→6
- Picture-free: function words with no faithful single picture (ism, naam, anta, ana, man, ya, hunaka, hadha, li, aydan, walakin, yanzur, aasha/arada in 03p) stay picture-free, as in Units 1–2.
- Notebook: N1 strip pages take u3-s1-1…8 and u3-s2-1…6 byte-identical (SC-100); p.10 retrieval keeps its four bound Unit 2 frames.
- Once bound: re-run QC, re-state the activity count (SC-050), new Version from the Text role.

## 7 · Acceptance checklist (per image)

- one fixed identity per character, identical across frames and to its portrait
- each object is its single drawing; Story 2's ball is Story 1's `obj-kura`
- the row's *must not show* is absent; nothing unlisted is added
- no text, letters, numerals or glyph-like marks inside the image
- SC-027/SC-036: no hearts, no embrace; children stand apart; the mother and father are drawn as parents, not a couple scene
- Sami is visibly younger and smaller than Razan; Layla smaller than Yusuf; the Unit 3 cat visibly big
- legible reduced to strip size (118 × 98 px): the key under the cat in frame 6, the ribbon on the gift
- one file per slot; no frame reused for two story moments

## 8 · Order of work

Owner answers Q1–Q3 → cast sheets (15 portraits) and three objects → the two strips → the phrase page → binding, QC, Version → Unit 3 closing entry after its clips are verified.
