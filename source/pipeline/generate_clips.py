#!/usr/bin/env python3
"""
Intaliq 1 — clip generator for synthesised production audio (SC-129).

Produces the unit's clips from `source/units/unit<N>/audio/clips_manifest.json` with the ElevenLabs
text-to-speech API, post-processes them to the recording-package format, hashes them into the manifest,
and prepares the listener's sheet. It never fills `verified_by` / `verified_on` itself: those come from a
named person's listening, recorded in the clip tracker CSV and copied in by `record`.

What is sent to the API is the printed text, optionally respelled per `pronunciation_map.json`
(whole-word substitutions, recorded per clip as `tts_input` when they differ). The manifest `text`
and the printed book never change.

Modes (run from the repository root):

  python3 source/pipeline/generate_clips.py voices
      list the account's voices with their labels (to pick candidates for an audition)

  python3 source/pipeline/generate_clips.py audition --unit 1 --voices ID1,ID2,ID3
      five sample lines per voice → audio_work/audition/<voice>/… + audition.html to listen side by side

  python3 source/pipeline/generate_clips.py generate --unit 1 --voice ID [--only c_m07,c_r03] [--force]
      every clip of the unit (both readings) → its manifest `src` path, post-processed, hashed;
      skips rows that already have a file unless --only / --force

  python3 source/pipeline/generate_clips.py post --unit 1 [--from audio_work/raw]
      post-process files already generated elsewhere (e.g. the web studio), named <clip_id>.mp3
      or by their manifest basename, into their `src` paths; then hash

  python3 source/pipeline/generate_clips.py hash --unit 1
      recompute every SHA-256 and the per-unit `voice` field; write the listener's sheet

  python3 source/pipeline/generate_clips.py record --unit 1 --tracker source/units/unit1/INTALIQ1_UNIT1_CLIP_TRACKER.csv
      copy accepted rows' listener name and date from the tracker into the manifest; list retakes

Environment: ELEVENLABS_API_KEY (or a file `.secrets/elevenlabs.key` at the repository root, git-excluded).
Requires `ffmpeg` on PATH for post-processing (macOS: `brew install ffmpeg`); without it the raw API
output is kept and the manifest row is marked `post: "none"`, which the record must then explain.
Standard library only; no third-party Python packages.
"""
import argparse, csv, datetime, hashlib, html, json, os, re, shutil, subprocess, sys, time, urllib.request, urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
API = "https://api.elevenlabs.io/v1"
MODEL = "eleven_multilingual_v2"
OUTPUT_FORMAT = "mp3_44100_128"            # the recording package's format: mono-ready 44.1 kHz MP3 at 128 kbps
VOICE_SETTINGS = {"stability": 0.62, "similarity_boost": 0.8, "style": 0.15, "use_speaker_boost": True, "speed": 0.92}
AUDITION_LINES = {  # one narration, one question, one dialogue with exclamation, one name-heavy line, one Reading-2 line
    1: ["c_m00", "c_m07", "c_m09", "c_m16", "c_r11"],
}

# ---------------------------------------------------------------- helpers
def unit_dir(n): return ROOT / "source" / "units" / f"unit{n}" / "audio"
def manifest_path(n): return unit_dir(n) / "clips_manifest.json"
def pmap_path(n): return unit_dir(n) / "pronunciation_map.json"

def load_json(p):
    with open(p, encoding="utf-8") as f: return json.load(f)

def save_json(p, d):
    with open(p, "w", encoding="utf-8") as f: json.dump(d, f, ensure_ascii=False, indent=2); f.write("\n")

def api_key():
    k = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if not k:
        f = ROOT / ".secrets" / "elevenlabs.key"
        if f.exists(): k = f.read_text(encoding="utf-8").strip()
    if not k: sys.exit("No API key: set ELEVENLABS_API_KEY or put the key in .secrets/elevenlabs.key (git-excluded).")
    return k

def api(path, method="GET", body=None, accept="application/json"):
    req = urllib.request.Request(API + path, method=method)
    req.add_header("xi-api-key", api_key()); req.add_header("Accept", accept)
    data = None
    if body is not None:
        req.add_header("Content-Type", "application/json"); data = json.dumps(body).encode("utf-8")
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, data=data, timeout=120) as r: return r.read()
        except urllib.error.HTTPError as e:
            msg = e.read().decode("utf-8", "replace")[:300]
            if e.code in (429, 500, 502, 503) and attempt < 3: time.sleep(3 * (attempt + 1)); continue
            sys.exit(f"API error {e.code} on {path}: {msg}")
        except urllib.error.URLError as e:
            sys.exit(f"Cannot reach the ElevenLabs API ({e.reason}). Run this where api.elevenlabs.io is reachable — your own Terminal, not a sandboxed shell.")

def all_clips(m):
    for ukey, u in m["units"].items():
        for c in u["clips"]: yield ukey, u, c

def find_clip(m, cid):
    for ukey, u, c in all_clips(m):
        if c["id"] == cid: return ukey, u, c
    sys.exit(f"no clip {cid} in the manifest")

def respell(text, pmap):
    """whole-word substitutions, longest key first; returns (api_input, applied list)"""
    applied = []
    out = text
    for k in sorted(pmap.get("map", {}), key=len, reverse=True):
        v = pmap["map"][k]
        pat = re.compile(r"(?<![؀-ۿ])" + re.escape(k) + r"(?![؀-ۿ])")
        if pat.search(out): out = pat.sub(v, out); applied.append([k, v])
    return out, applied

def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""): h.update(chunk)
    return h.hexdigest()

def have_ffmpeg(): return shutil.which("ffmpeg") is not None

def post_process(src, dst):
    """trim leading/trailing silence to ≤0.3 s (then a small even margin), peak-normalise to −1 dBFS, mono 44.1 kHz MP3 128k"""
    if not have_ffmpeg():
        shutil.copyfile(src, dst); return "none"
    trim = ("silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.05,"
            "areverse,silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.05,areverse,"
            "adelay=120|120,apad=pad_dur=0.18")
    tmp = Path(str(dst) + ".tmp.wav")
    run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(src), "-af", trim, "-ac", "1", "-ar", "44100", str(tmp)])
    det = subprocess.run(["ffmpeg", "-i", str(tmp), "-af", "volumedetect", "-f", "null", "-"], capture_output=True, text=True).stderr
    mx = re.search(r"max_volume:\s*(-?[\d.]+) dB", det)
    gain = (-1.0 - float(mx.group(1))) if mx else 0.0
    run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(tmp), "-af", f"volume={gain:.2f}dB", "-ac", "1", "-ar", "44100",
         "-codec:a", "libmp3lame", "-b:a", "128k", str(dst)])
    tmp.unlink(missing_ok=True)
    return "trim≤0.3s · peak −1 dBFS · mono 44.1 kHz · mp3 128k"

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode: sys.exit("ffmpeg failed: " + r.stderr[-400:])

def tts(voice_id, text):
    body = {"text": text, "model_id": MODEL, "voice_settings": VOICE_SETTINGS}
    return api(f"/text-to-speech/{voice_id}?output_format={OUTPUT_FORMAT}", "POST", body, accept="audio/mpeg")

def voice_name(voice_id):
    try:
        v = json.loads(api(f"/voices/{voice_id}"))
        return v.get("name", voice_id)
    except SystemExit:
        return voice_id

# ---------------------------------------------------------------- modes
def mode_voices(a):
    vs = json.loads(api("/voices")).get("voices", [])
    print(f"{'voice_id':24} {'name':22} labels")
    for v in sorted(vs, key=lambda x: x.get("name", "")):
        lab = ", ".join(f"{k}={val}" for k, val in (v.get("labels") or {}).items())
        print(f"{v['voice_id']:24} {v.get('name',''):22} {lab}")
    print("\nAudition three or four with:  generate_clips.py audition --unit 1 --voices ID1,ID2,ID3")

def mode_audition(a):
    m, pmap = load_json(manifest_path(a.unit)), load_json(pmap_path(a.unit))
    out = ROOT / "audio_work" / "audition"; out.mkdir(parents=True, exist_ok=True)
    rows = []
    for vid in a.voices.split(","):
        vid = vid.strip(); name = voice_name(vid); d = out / vid; d.mkdir(exist_ok=True)
        for cid in AUDITION_LINES[a.unit]:
            _, _, c = find_clip(m, cid)
            txt, applied = respell(c["text"], pmap)
            raw = d / f"{cid}.raw.mp3"; raw.write_bytes(tts(vid, txt))
            post_process(raw, d / f"{cid}.mp3"); raw.unlink()
            rows.append((vid, name, cid, c["text"], applied))
            print(f"  {name:20} {cid}")
    sheet = ["<!doctype html><meta charset=utf-8><title>Intaliq 1 — voice audition</title>",
             "<style>body{font-family:system-ui;max-width:1000px;margin:24px auto;padding:0 16px}td{padding:8px 10px;vertical-align:top;border-top:1px solid #ddd}"
             ".ar{font-family:'Noto Naskh Arabic','Amiri',serif;font-size:24px;direction:rtl;text-align:right}th{text-align:left}</style>",
             "<h1>Voice audition · Unit %d</h1><p>Same five lines, each candidate voice. Listen for: every printed vowel respected, no invented word-final vowels, "
             "question melody, names said as Arabic, a pace a nine-year-old can follow. One voice will do the whole unit.</p>" % a.unit]
    for vid in a.voices.split(","):
        vid = vid.strip(); name = next(r[1] for r in rows if r[0] == vid)
        sheet.append(f"<h2>{html.escape(name)} <small>({vid})</small></h2><table>")
        for r in [r for r in rows if r[0] == vid]:
            note = (" <small>(sent as: " + html.escape(respell(r[3], pmap)[0]) + ")</small>") if r[4] else ""
            sheet.append(f"<tr><td style='width:90px'>{r[2]}</td><td class=ar>{html.escape(r[3])}{note}</td><td><audio controls preload=none src='{vid}/{r[2]}.mp3'></audio></td></tr>")
        sheet.append("</table>")
    (out / "audition.html").write_text("\n".join(sheet), encoding="utf-8")
    print(f"\nOpen {out/'audition.html'} and choose. Then: generate --unit {a.unit} --voice <ID>")

def mode_generate(a):
    m, pmap = load_json(manifest_path(a.unit)), load_json(pmap_path(a.unit))
    only = set(a.only.split(",")) if a.only else None
    vname = voice_name(a.voice)
    log_p = ROOT / "audio_work" / f"generation_log_unit{a.unit}.json"; log_p.parent.mkdir(exist_ok=True)
    log = load_json(log_p) if log_p.exists() else {"runs": []}
    run_rec = {"when": datetime.datetime.now().isoformat(timespec="seconds"), "voice_id": a.voice, "voice": vname,
               "model": MODEL, "settings": VOICE_SETTINGS, "clips": []}
    n = 0
    for ukey, u, c in all_clips(m):
        if only and c["id"] not in only: continue
        dst = ROOT / c["src"]
        if dst.exists() and not a.force and not only: continue
        if c.get("verified_by") and not a.force:
            print(f"  skip {c['id']}: already verified by {c['verified_by']} — use --force to regenerate (verification will be cleared)"); continue
        txt, applied = respell(c["text"], pmap)
        dst.parent.mkdir(parents=True, exist_ok=True)
        raw = Path(str(dst) + ".raw.mp3"); raw.write_bytes(tts(a.voice, txt))
        post = post_process(raw, dst); raw.unlink()
        c["sha256"] = sha256(dst); c["post"] = post
        if applied: c["tts_input"] = txt
        else: c.pop("tts_input", None)
        c["verified_by"] = ""; c["verified_on"] = ""          # a new file is an unverified file
        u["voice"] = f"synthesised: ElevenLabs · {vname} ({a.voice}) · {MODEL}"
        run_rec["clips"].append({"id": c["id"], "src": c["src"], "sha256": c["sha256"], "respelled": applied})
        n += 1; print(f"  {c['id']:10} → {c['src']}  {'(respelled: ' + ', '.join(k for k, _ in applied) + ')' if applied else ''}")
    log["runs"].append(run_rec); save_json(log_p, log); save_json(manifest_path(a.unit), m)
    write_sheet(a.unit, m)
    print(f"\n{n} clip(s) generated. Listener's sheet: audio_work/listening_sheet_unit{a.unit}.html · tracker: source/units/unit{a.unit}/INTALIQ1_UNIT{a.unit}_CLIP_TRACKER.csv")
    if not have_ffmpeg(): print("NOTE: ffmpeg not found — files kept as the API returned them (post: none). Install ffmpeg and run `post` to finish.")

def mode_post(a):
    m = load_json(manifest_path(a.unit)); src_dir = ROOT / (a.src or "audio_work/raw")
    n = 0
    for ukey, u, c in all_clips(m):
        cand = [src_dir / f"{c['id']}.mp3", src_dir / Path(c["src"]).name, src_dir / f"{c['id']}.wav", src_dir / Path(c["src"]).with_suffix(".wav").name]
        f = next((p for p in cand if p.exists()), None)
        if not f: continue
        dst = ROOT / c["src"]; dst.parent.mkdir(parents=True, exist_ok=True)
        c["post"] = post_process(f, dst); c["sha256"] = sha256(dst); c["verified_by"] = ""; c["verified_on"] = ""
        if a.voice_label: u["voice"] = a.voice_label
        n += 1; print(f"  {c['id']:10} ← {f.name}")
    save_json(manifest_path(a.unit), m); write_sheet(a.unit, m); print(f"\n{n} file(s) post-processed and hashed.")

def mode_hash(a):
    m = load_json(manifest_path(a.unit)); n = 0
    for ukey, u, c in all_clips(m):
        p = ROOT / c["src"]
        if p.exists():
            h = sha256(p)
            if c.get("sha256") and c["sha256"] != h and c.get("verified_by"):
                print(f"  WARNING {c['id']}: file changed since it was verified — verification cleared"); c["verified_by"] = ""; c["verified_on"] = ""
            c["sha256"] = h; n += 1
    save_json(manifest_path(a.unit), m); write_sheet(a.unit, m); print(f"{n} file(s) hashed.")

def mode_record(a):
    m = load_json(manifest_path(a.unit)); accepted = retakes = 0; missing = []
    with open(a.tracker, encoding="utf-8-sig", newline="") as f:
        rd = csv.DictReader(f)
        cols = {k.split(" ")[0]: k for k in rd.fieldnames}
        for row in rd:
            cid = row.get(cols.get("clip_id", "clip_id"), "").strip()
            if not cid: continue
            status = row.get(cols.get("status", "status"), "").strip().lower()
            who = row.get(cols.get("verified_by", "verified_by"), "").strip()
            when = row.get(cols.get("verified_on", "verified_on"), "").strip()
            _, u, c = find_clip(m, cid)
            if status.startswith("accept"):
                if not (who and re.match(r"^\d{4}-\d{2}-\d{2}$", when)): missing.append(cid); continue
                if not (ROOT / c["src"]).exists() or sha256(ROOT / c["src"]) != c.get("sha256"):
                    print(f"  {cid}: file missing or changed since hashing — not recorded"); continue
                c["verified_by"], c["verified_on"] = who, when; accepted += 1
            elif status.startswith("retake"):
                c["verified_by"] = c["verified_on"] = ""; retakes += 1; print(f"  retake {cid}: {row.get(cols.get('retake_reason','retake_reason'),'')}")
    save_json(manifest_path(a.unit), m); write_sheet(a.unit, m)
    total = sum(len(u["clips"]) for u in m["units"].values())
    done = sum(1 for _, _, c in all_clips(m) if c.get("verified_by"))
    print(f"\naccepted this pass: {accepted} · retakes: {retakes} · verified in manifest: {done}/{total}")
    if missing: print("accepted rows missing listener name or ISO date (not recorded): " + ", ".join(missing))
    if retakes: print("regenerate retakes with:  generate --unit %d --voice <ID> --only %s" % (a.unit, ",".join(c["id"] for _, _, c in all_clips(m) if not c.get("verified_by") and (ROOT / c["src"]).exists())))
    if done == total: print("All clips verified. Next: bind audio.clips into the engine (audio.verified = true), build, gate, push.")

def write_sheet(n, m):
    out = ROOT / "audio_work" / f"listening_sheet_unit{n}.html"; out.parent.mkdir(exist_ok=True)
    rows = ["<!doctype html><meta charset=utf-8><title>Intaliq 1 — listener's sheet · Unit %d</title>" % n,
            "<style>body{font-family:system-ui;max-width:1100px;margin:24px auto;padding:0 16px}table{border-collapse:collapse;width:100%}td,th{padding:8px 10px;border-top:1px solid #ddd;vertical-align:top}"
            ".ar{font-family:'Noto Naskh Arabic','Amiri',serif;font-size:26px;direction:rtl;text-align:right;line-height:1.7}.ok{color:#2a7}.no{color:#a33}small{color:#666}</style>",
            "<h1>Listener's sheet · Unit %d</h1>" % n,
            "<p><b>How to verify (SC-129):</b> play each clip while reading its printed text. Accept only if <b>every word, every ending and the sentence melody</b> match the text exactly, "
            "at a child-directed pace, with no word added, dropped or paraphrased. Anything else is a <b>retake</b> (the clip is regenerated, never edited). "
            "Enter your decision, your full name and today's date (YYYY-MM-DD) in the clip tracker CSV, then run <code>generate_clips.py record</code>. "
            "The file name of the sheet's audio is the file that ships; the hash in the manifest is the one checked at build.</p>"]
    for ukey, u in m["units"].items():
        rows.append(f"<h2>{ukey} · <span class=ar style='font-size:22px'>{html.escape(u['title'])}</span> <small>{html.escape(u.get('voice','') or 'voice not yet named')}</small></h2><table><tr><th>#</th><th>id</th><th>printed text</th><th>clip</th><th>status</th></tr>")
        for i, c in enumerate(u["clips"], 1):
            p = ROOT / c["src"]; rel = os.path.relpath(p, out.parent)
            st = f"<span class=ok>verified · {html.escape(c['verified_by'])} · {c['verified_on']}</span>" if c.get("verified_by") else ("<span class=no>awaiting verification</span>" if p.exists() else "<small>no file</small>")
            sent = f"<br><small>sent to the synthesiser as: <span class=ar style='font-size:16px'>{html.escape(c['tts_input'])}</span></small>" if c.get("tts_input") else ""
            audio = f"<audio controls preload=none src='{html.escape(rel)}'></audio>" if p.exists() else ""
            rows.append(f"<tr><td>{i}</td><td><code>{c['id']}</code><br><small>{c['kind']} · {c['ref']}</small></td><td class=ar>{html.escape(c['text'])}{sent}</td><td>{audio}</td><td>{st}</td></tr>")
        rows.append("</table>")
    out.write_text("\n".join(rows), encoding="utf-8")

# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="mode", required=True)
    sub.add_parser("voices")
    p = sub.add_parser("audition"); p.add_argument("--unit", type=int, default=1); p.add_argument("--voices", required=True)
    p = sub.add_parser("generate"); p.add_argument("--unit", type=int, default=1); p.add_argument("--voice", required=True); p.add_argument("--only"); p.add_argument("--force", action="store_true")
    p = sub.add_parser("post"); p.add_argument("--unit", type=int, default=1); p.add_argument("--from", dest="src"); p.add_argument("--voice-label")
    p = sub.add_parser("hash"); p.add_argument("--unit", type=int, default=1)
    p = sub.add_parser("record"); p.add_argument("--unit", type=int, default=1); p.add_argument("--tracker", required=True)
    a = ap.parse_args()
    {"voices": mode_voices, "audition": mode_audition, "generate": mode_generate, "post": mode_post, "hash": mode_hash, "record": mode_record}[a.mode](a)

if __name__ == "__main__":
    main()
