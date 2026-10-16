#!/bin/bash
# Unit 1 clips.command — double-click in Finder. A menu around source/pipeline/generate_clips.py (SC-129).
# Nothing here changes the book, the manifest's texts or any licence; it only runs the generator's modes in order.
cd "$(dirname "$0")" || exit 1
GEN="source/pipeline/generate_clips.py"
UNIT=1
TRACKER="source/units/unit1/INTALIQ1_UNIT1_CLIP_TRACKER.csv"
SHEET="audio_work/listening_sheet_unit1.html"

bold() { printf '\n\033[1m%s\033[0m\n' "$1"; }
pause() { printf '\nPress Return to go back to the menu. '; read -r _; }

# ---- 0 · the API key (kept in .secrets/, which git ignores; never in the chat, never in the repository) ----
if [ -z "$ELEVENLABS_API_KEY" ] && [ ! -s .secrets/elevenlabs.key ]; then
  bold "ElevenLabs API key"
  echo "Paste the key you copied from elevenlabs.io (nothing appears while you paste), then press Return:"
  read -rs KEY
  if [ -z "$KEY" ]; then echo "No key entered. Closing."; exit 1; fi
  mkdir -p .secrets && printf '%s' "$KEY" > .secrets/elevenlabs.key && chmod 600 .secrets/elevenlabs.key
  echo "Saved to .secrets/elevenlabs.key — a git-ignored file. You will not be asked again."
fi

# ---- 0 · ffmpeg (trims silence and evens the volume; without it clips are stored as ElevenLabs returns them) ----
if ! command -v ffmpeg >/dev/null 2>&1; then
  if command -v brew >/dev/null 2>&1; then
    bold "Installing ffmpeg (one time; a few minutes)"; brew install ffmpeg
  else
    bold "ffmpeg is not installed"
    echo "Clips will be stored untrimmed until it is. To fix later: install Homebrew from https://brew.sh, then run:  brew install ffmpeg"
  fi
fi

# ---- 0 · certificates: a python.org Python on macOS has no root store; certifi gives it one (one time, quiet) ----
python3 -c "import certifi" >/dev/null 2>&1 || python3 -m pip install --quiet --user certifi >/dev/null 2>&1 || true

# ---- helper: ask which ElevenLabs model (the web studio shows its model in a drop-down next to the voice) ----
ask_model() {
  echo; echo "  Model (as shown in the ElevenLabs web studio):"
  echo "    1  Eleven v3                — most natural; what the website usually uses now"
  echo "    2  Eleven Multilingual v2   — the earlier default"
  echo "    3  Eleven Flash v2.5"
  printf '  Choose 1–3 [1]: '; read -r mm
  case "$mm" in 2) MODEL=v2;; 3) MODEL=flash;; *) MODEL=v3;; esac
}

# ---- helper: numbered voice list → VOICE_IDS[] / VOICE_NAMES[] ----
load_voices() {
  VOICE_IDS=(); VOICE_NAMES=()
  local line
  while IFS= read -r line; do
    case "$line" in voice_id*|""|Audition*) continue;; esac
    VOICE_IDS+=("${line:0:24}"); VOICE_NAMES+=("$(echo "${line:25}" | sed 's/  */ /g')")
  done < <(python3 "$GEN" voices)
  VOICE_IDS=("${VOICE_IDS[@]// /}")
  if [ "${#VOICE_IDS[@]}" -eq 0 ]; then echo "No voices came back — check the key and the internet connection."; return 1; fi
  local i; for i in "${!VOICE_IDS[@]}"; do printf '  %2d  %s\n' "$((i+1))" "${VOICE_NAMES[$i]}"; done
}

while true; do
  bold "Intaliq · Unit 1 clips"
  cat <<'MENU'
  1  Audition voices       — five Unit 1 lines in each voice, side by side in your browser
  2  Generate Unit 1       — all 72 clips in the voice you chose; opens the listener's sheet and the tracker
  3  Record verification   — copy the listener's accepted / retake decisions into the manifest
  4  Retakes               — regenerate named clips (e.g. c_m07,c_r03), then verify them again
  5  Quit
MENU
  printf '\nChoose 1–5: '; read -r CHOICE
  case "$CHOICE" in
    1)
      bold "Voices on your account"
      load_voices || { pause; continue; }
      printf '\nType the numbers to audition, separated by spaces (e.g. 2 5 9), or "all": '
      read -r PICK
      IDS=""
      if [ "$PICK" = "all" ]; then IDS=$(IFS=,; echo "${VOICE_IDS[*]}")
      else for n in $PICK; do i=$((n-1)); [ -n "${VOICE_IDS[$i]}" ] && IDS="$IDS,${VOICE_IDS[$i]}"; done; IDS="${IDS#,}"; fi
      [ -z "$IDS" ] && { echo "Nothing chosen."; pause; continue; }
      ask_model
      python3 "$GEN" audition --unit "$UNIT" --voices "$IDS" --model "$MODEL" && open audio_work/audition/audition.html
      echo; echo "Listen, choose ONE voice for the whole unit, then run option 2. If a word is said wrong in every voice, tell Claude the word."
      pause;;
    2)
      bold "Which voice for which reading? (SC-130: one voice per reading)"
      load_voices || { pause; continue; }
      printf '\nNumber of the voice for READING 1 «قَائِمَةُ رَزَان» (46 clips): '; read -r n1; i1=$((n1-1)); V1="${VOICE_IDS[$i1]}"
      printf 'Number of the voice for READING 2 «مَنْ أَنْتَ يَا قَلَم؟» (26 clips) [same as reading 1 if blank]: '; read -r n2
      if [ -z "$n2" ]; then i2=$i1; else i2=$((n2-1)); fi; V2="${VOICE_IDS[$i2]}"
      [ -z "$V1" ] || [ -z "$V2" ] && { echo "No such number."; pause; continue; }
      ask_model
      echo "Reading 1 → ${VOICE_NAMES[$i1]} · Reading 2 → ${VOICE_NAMES[$i2]} · model $MODEL"
      python3 "$GEN" generate --unit "$UNIT" --reading 1 --voice "$V1" --model "$MODEL" \
        && python3 "$GEN" generate --unit "$UNIT" --reading 2 --voice "$V2" --model "$MODEL" \
        && { open "$SHEET"; open "$TRACKER"; }
      echo; echo "Listener: play each clip against its line on the sheet; in the tracker enter accepted or retake, your full name and today's date. Then run option 3."
      pause;;
    3)
      python3 "$GEN" record --unit "$UNIT" --tracker "$TRACKER"
      echo; echo "If no retakes are listed, tell Claude: \"clips are verified\"."
      pause;;
    4)
      load_voices || { pause; continue; }
      printf '\nNumber of the unit'"'"'s voice: '; read -r n; i=$((n-1)); VID="${VOICE_IDS[$i]}"
      printf 'Clip ids to redo, comma-separated (as listed by option 3): '; read -r ONLY
      ask_model
      python3 "$GEN" generate --unit "$UNIT" --voice "$VID" --only "$ONLY" --model "$MODEL" && open "$SHEET"
      echo; echo "Verify the redone clips in the tracker, then run option 3 again."
      pause;;
    5|q|Q) exit 0;;
    *) echo "Choose 1–5.";;
  esac
done
