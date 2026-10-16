# Intaliq 1 — Unit 1 audio intake and verification (Batch 2, not yet delivered)

*Editor (Text role) · 2026-10-11 · SC-121. The listening machinery is built and tested against fixture bindings; it goes live the day verified recordings are bound. **No recording exists yet, and none is claimed.** What follows is what has to be supplied, by whom, and how it is verified — so that the hand-over is a folder of files and a filled table, not a conversation.*

## 1 · What is needed

**72 clips for Unit 1**, listed row by row in `source/units/unit1/audio/clips_manifest.json` (generated from the engine; never hand-typed): the 24 sentences of «قَائِمَةُ رَزَان» and the 11 of «مَنْ أَنْتَ يَا قَلَم؟», plus one clip per core-item phrase (22 + 15). Each row carries the **exact text to record** — the printed sentence or the item's phrase as the engine prints it — and the file path the engine will expect.

| Property | Requirement |
|---|---|
| Voice | **one voice for the whole unit** — a native MSA speaker **or, since SC-129, a speech synthesiser's fixed voice** (named in the manifest as `human: <speaker>` or `synthesised: <engine / voice id>`); a second voice may be used for the character lines only if the owner rules so |
| Delivery | read exactly as printed, fully vocalised, at a child-directed pace; dialogue read as speech, narration as narration; no words added, dropped or paraphrased — the recording must match the canon word for word, because the learner's response set is the printed text |
| Format | mono, 44.1 kHz, MP3 ≥128 kbps (or OGG); one file per row; leading/trailing silence ≤ 0.3 s; peak-normalised |
| Naming | exactly the `src` path in the manifest: `assets/audio/unit-01/m07.mp3`, `assets/audio/unit-01/item_urid.mp3`, `assets/audio/unit-01p/r04.mp3`, … |
| Not acceptable | the browser's live preview voice as a shipped clip (SC-028, as narrowed by SC-129); **any clip — human or synthesised — not verified by ear by a named listener**; a clip whose text differs from the canon; a clip that covers two rows; a failing clip patched rather than regenerated or re-recorded |

## 2 · How a clip becomes "verified"

Verification is a person, not a process. For each clip a named listener who reads Arabic plays the file while reading the manifest row's text and confirms every word, every ending and the sentence melody match the printed line; a clip with any deviation is re-recorded, never patched. The listener writes their name and the date into the row (`verified_by`, `verified_on`). The build then computes `sha256` for each file and the rows are copied into the unit data as `audio.clips` with `audio.verified: true`.

**What the engine then enforces** (already built, `audioCheck`): every sentence and every core item must be bound; refs must resolve; paths must sit under `assets/audio/`; hashes must be 64-hex and, at build and at the release gate, must match the file on disk; `verified_by` and `verified_on` must be present. Any failure withholds the whole unit — a half-bound unit never ships.

## 3 · What switches on when the bindings are valid

Three listening families (F9), all input-only: **hear a phrase → tap its picture** (`listen_tap`, 9 + 5 tasks at Unit 1), **hear a sentence → choose the printed line** (`listen_which`, 24 + 11), **hear a quotation → choose who says it** (`listen_who`, 5 + 3). The vocabulary pathway becomes **sound-first** (every pictured core item is heard and tapped before it is read — the station's A1), the reading pathway hears its opening sentences before the text, and the post-reading tail adds hear-who-says. The hub's audio line changes from "no verified recordings" to the bound count. The teacher's page wording ("no listening tasks") is lifted by the same build.

## 4 · Who decides what

- **Supplying the clips** is production work: a speaker and a microphone, or — since SC-129 — a synthesiser run against the manifest texts. **Verification is a person's work in every case**: a named Arabic-reading listener plays each clip against the printed text and signs the row. The Text role neither verifies clips itself nor simulates verification.
- ~~**One policy point is the owner's, if he wants the gap closed sooner:** SC-028 rules synthesised speech out as shipped audio …~~ **Ruled — SC-129 (2026-10-15):** synthesised production audio is permitted after clip-by-clip human verification; the human-speaker requirement is replaced, the quality control kept.
- **Verification** needs a named Arabic-reading listener; the Editor can be that listener for clips supplied to the session, and says so in the rows.

## 5 · Status

| | |
|---|---|
| Machinery | built, tested (`source/pipeline/test_listening.js`; the release gate re-runs it against the deployed engine) |
| Manifest | generated, 72 rows, every `src`/`sha256`/`verified_by` empty |
| Recordings | **none** |
| Unit 1 listening | **not delivered**; the unit is not complete until it is |
