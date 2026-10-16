# Unit 1 clips — how they are generated and verified (SC-129)

*One voice per reading ⟨SC-130⟩ — narration and dialogue alike, so every listening task, which draws on one reading, turns on the words and not the timbre; Unit 1 casts a female voice for Reading 1 and a male voice for Reading 2. Pronunciation is locked by respelling the generator's input, never the book (`pronunciation_map.json`). Verification is a named person's work, clip by clip; the generator never fills it in.*

**Easiest route (2026-10-16):** double-click `Unit 1 clips.command` at the repository root in Finder. It asks for the API key once (stored in the git-ignored `.secrets/`), installs `ffmpeg` if Homebrew is present, and offers the steps below as a numbered menu: audition → generate → record → retakes. The commands below are what it runs.

Run from the repository root, in a Terminal that can reach `api.elevenlabs.io` (the sandboxed shells cannot). The key stays out of the repository and the chat: `export ELEVENLABS_API_KEY=…` for the session, or a file `.secrets/elevenlabs.key` (git-ignored). `ffmpeg` on PATH (`brew install ffmpeg`).

| Step | Command | Result |
|---|---|---|
| 1 · candidates | `python3 source/pipeline/generate_clips.py voices` | the account's voices and labels |
| 2 · audition | `… audition --unit 1 --voices ID1,ID2,ID3 [--model v3]` (model: `v2` = eleven_multilingual_v2 · `v3` = eleven_v3 · `flash`; settings: the voice's own saved settings by default — what the web studio uses — or `--settings house`) | five lines per voice → `audio_work/audition/audition.html`; listen side by side, choose one |
| 3 · lock | edit `pronunciation_map.json` only where a word is consistently mis-said; re-run step 2 on that line | the map is recorded per clip (`tts_input`) and in the generation log |
| 4 · generate | `… generate --unit 1 --reading 1 --voice ID` then `… --reading 2 --voice ID2` (`--model v3`; omit `--reading` to voice both with one) | 72 files at their manifest paths, trimmed (silence ≤ 0.3 s), peak-normalised, mono 44.1 kHz MP3 128k; SHA-256 and the unit's `voice` written to the manifest; `audio_work/listening_sheet_unit1.html` |
| 5 · verify | the listener opens the sheet, plays each clip against its printed text, and enters `accepted` / `retake` + full name + date in `INTALIQ1_UNIT1_CLIP_TRACKER.csv` | the only human step, and the one that makes a clip shippable |
| 6 · record | `… record --unit 1 --tracker source/units/unit1/INTALIQ1_UNIT1_CLIP_TRACKER.csv` | accepted rows' `verified_by` / `verified_on` copied into the manifest; retake ids listed |
| 7 · retakes | `… generate --unit 1 --voice ID --only c_m07,c_r03` → step 5 again | regenerated, never edited |
| 8 · bind | the Text session copies the manifest rows into the engine's `audio.clips` with `audio.verified = true`, builds, runs the gate (hashes, bindings, listening fixture, pathways), pushes | listening families switch on; new Studio Version |

If generation is done in the ElevenLabs web studio instead, export each clip as `<clip_id>.mp3` into `audio_work/raw/` and run `… post --unit 1 --from audio_work/raw --voice-label "synthesised: ElevenLabs · <voice name> · <model>"`; steps 5–8 are the same.

A regenerated or changed file clears its verification automatically (the hash no longer matches); `hash` warns when it finds this.
