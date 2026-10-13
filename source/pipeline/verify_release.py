#!/usr/bin/env python3
"""Rendered-page verification before any push (charter §8: rendered-page verification and presence
inventory before any release; runbook TF-9). Serves the deploy folder exactly as GitHub Pages would,
opens every route in a real browser, WALKS EVERY DIGITAL PATHWAY TO ITS END, checks the print-style
tasks have their response resources, and proves the deployed engine withholds a failing unit.

usage: python3 verify_release.py deploy/ [expected_version]
writes: verify_report.md and verify_shots/*.png (one per route) + verify_sheet.png
exit 1 on any blocker.

Added 2026-10-10 (audit batches 1–3): pathway walkthroughs (B1, I7), resource checks (B4, I7),
unresolved <use href="#…"> references, learner-view check (I6), and mutation tests against the
embedded engine (B2) — a canon, form, membership or audio-flag mutation must leave the unit undeliverable.
Added 2026-10-13 (SC-122): a status-only read of the Unit 1 evidence record (exists; names the version; carries its
five status fields). The gate never writes an evidence status."""
import sys, os, json, threading, http.server, socketserver, functools, re, subprocess, tempfile
from pathlib import Path
from playwright.sync_api import sync_playwright

deploy = Path(sys.argv[1]).resolve()
expected_version = sys.argv[2] if len(sys.argv) > 2 else None
out = deploy.parent / "verify_shots"; out.mkdir(exist_ok=True)

# --- serve the folder like Pages (relative asset paths resolve the same way)
PORT = int(os.environ.get('INTALIQ_VERIFY_PORT', '8765'))
handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(deploy))
class Q(socketserver.TCPServer): allow_reuse_address = True
Q.log_message = lambda *a, **k: None
srv = Q(("127.0.0.1", PORT), handler)
threading.Thread(target=srv.serve_forever, daemon=True).start()
base = f"http://127.0.0.1:{srv.server_address[1]}/"

html = (deploy / "index.html").read_text(encoding="utf-8")
routes = [""] + re.findall(r"'([a-z0-9\-/]+)':'v-", html)
routes = list(dict.fromkeys(routes))

blockers, warnings, rows, pathways, resources = [], [], [], [], []

# --- the engine as deployed (extracted from index.html, not from the source tree)
eng_start = html.find('(function(root){\n"use strict";')
eng_end = html.find('})(typeof window!=="undefined"?window:globalThis);', eng_start)
engine_js = html[eng_start:eng_end + len('})(typeof window!=="undefined"?window:globalThis);')] if eng_start >= 0 and eng_end > 0 else None
if not engine_js: blockers.append("embedded engine not found in index.html")

# --- B2: mutation tests — every mutation must leave the unit undeliverable, the control must deliver
MUTATION_JS = r'''
const fs=require("fs");const src=fs.readFileSync(process.argv[1],"utf8");
const g={};(new Function("globalThis","window",src+";return globalThis;"))(g,undefined);const E=g.SC_ENGINE;
const clone=o=>JSON.parse(JSON.stringify(o));const res=[];
for(const k of Object.keys(E.UNITS)){
  const tests={
    control:u=>{},
    canon_word_added:u=>{u.sentences[0].ar=u.sentences[0].ar+" زِيَادَة";},
    unprinted_form_on_card:u=>{u.items[0].forms=[...(u.items[0].forms||[]),"قُلْتُ"];},
    reading_lists_unknown_id:u=>{u.readings[0].sentence_ids.push("zz_missing");},
    reading_omits_first_sentence:u=>{u.readings[0].sentence_ids.shift();},
    audio_flag_without_clips:u=>{u.audio={verified:true};}
  };
  for(const [name,mut] of Object.entries(tests)){const u=clone(E.UNITS[k]);mut(u);const d=E.deliverable(u);
    res.push({unit:k,test:name,delivers:d.ok,seq:E.sequenceFor(u,(u.readings[0]||{}).id,3,true).length,path:E.pathway(u,"reading",0).length,why:d.failed.map(f=>f.id).join(",")});}
}
process.stdout.write(JSON.stringify(res));
'''
if engine_js:
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8") as f: f.write(engine_js); eng_path = f.name
    try:
        mut = json.loads(subprocess.check_output(["node", "-e", MUTATION_JS, eng_path], text=True))
    except Exception as e:
        mut = []; blockers.append(f"mutation tests could not run: {e}")
    for r in mut:
        if r["test"] == "control":
            if not r["delivers"] or r["seq"] == 0 or r["path"] == 0: blockers.append(f"{r['unit']}: the unmodified unit is not deliverable ({r['why']})")
        elif r["delivers"] or r["seq"] != 0 or r["path"] != 0:
            blockers.append(f"{r['unit']}: mutation '{r['test']}' still delivers (seq {r['seq']}, pathway {r['path']}) — QC does not stop delivery")

# --- F9: the listening machinery must hold against the deployed engine (fixture bindings only; no recording is shipped)
listening_test = None
if engine_js:
    here = Path(__file__).resolve().parent
    tl = here / "test_listening.js"
    if tl.exists():
        rr = subprocess.run(["node", str(tl), eng_path], capture_output=True, text=True)
        listening_test = rr.stdout.strip().splitlines()[-1] if rr.stdout.strip() else rr.stderr.strip()[:200]
        if rr.returncode != 0: blockers.append("listening fixture test failed against the deployed engine: " + listening_test)
    else:
        warnings.append("test_listening.js not beside verify_release.py — listening machinery not re-tested")

with sync_playwright() as p:
    b = p.chromium.launch(channel=os.environ.get('INTALIQ_BROWSER_CHANNEL') or None)
    pg = b.new_page(viewport={"width": 1180, "height": 900})
    console, failed, external = [], [], []
    pg.on("console", lambda m: console.append((m.type, m.text)) if m.type in ("error", "warning") else None)
    pg.on("pageerror", lambda e: console.append(("error", "pageerror: " + str(e))))
    pg.on("requestfailed", lambda r: failed.append(r.url) if "127.0.0.1" in r.url else external.append(r.url))
    pg.on("response", lambda r: failed.append(r.url) if (r.status >= 400 and "127.0.0.1" in r.url) else None)

    for r in routes:
        url = base + ("#" + r if r else "")
        pg.goto(url, wait_until="networkidle")
        pg.wait_for_timeout(300)
        info = pg.evaluate("""() => {
          const on=document.querySelector('.view.on');
          const imgs=[...document.images];
          const unresolved=on?[...on.querySelectorAll('use')].map(u=>u.getAttribute('href')||u.getAttribute('xlink:href')).filter(h=>h&&h.startsWith('#')&&!document.getElementById(h.slice(1))):[];
          return {
            view: on ? on.id : null,
            chip: (document.querySelector('.chip,.badge,[class*=chip]')||{}).textContent || '',
            brokenImgs: imgs.filter(i=>i.complete && i.naturalWidth===0).map(i=>i.getAttribute('src')),
            emptyFrames: on ? on.querySelectorAll('.picfr.empty').length : 0,
            frames: on ? on.querySelectorAll('.picfr').length : 0,
            teacherLinks: [...document.querySelectorAll('a[href]')].filter(a=>/teacher/i.test(a.getAttribute('href'))).length,
            unresolvedUse: [...new Set(unresolved)],
            learner: document.body.classList.contains('learner'),
            revVisible: on ? [...on.querySelectorAll('.rev')].filter(e=>getComputedStyle(e).display!=='none').length : 0,
            revTotal: on ? on.querySelectorAll('.rev').length : 0
          };
        }""")
        shot = out / f"{(r or 'home').replace('/', '_')}.png"
        pg.screenshot(path=str(shot), full_page=True)
        rows.append((r or "home", info, shot.name))
        if info["view"] is None: blockers.append(f"route #{r}: no view mounted")
        for s in info["brokenImgs"]: blockers.append(f"route #{r}: broken image {s}")
        for h in info["unresolvedUse"]: blockers.append(f"route #{r}: <use href=\"{h}\"> points at no symbol")
        if info["teacherLinks"]: blockers.append(f"route #{r}: {info['teacherLinks']} link(s) to the teacher page (SC-104)")
        if info["revTotal"] and info["learner"] and info["revVisible"]: blockers.append(f"route #{r}: {info['revVisible']} review note(s) visible in learner view (I6)")

    # --- B4 / I7: response resources on the Unit 1 print-style tasks
    pg.goto(base + "#unit-01/student", wait_until="networkidle"); pg.wait_for_timeout(200)
    res = pg.evaluate("""() => {
      const on=document.getElementById('v-student'); const acts=[...on.querySelectorAll('.act')];
      const find=t=>acts.filter(a=>(a.querySelector('.rubric span[lang=ar]')||{}).textContent.includes(t));
      const row=a=>a.querySelector('.picseq')?a.querySelector('.picseq').querySelectorAll('.picfr').length:0;
      const items=a=>a.querySelectorAll('ul[lang=ar] li').length;
      const out=[];
      for(const a of find('اِقْرَأْ وَصِلْ')) out.push({task:'read-match', pictures:row(a), items:items(a)});
      for(const a of find('مَنْ يَقُولُ')) out.push({task:'who-says', faces:row(a), items:items(a), circles:(a.textContent.match(/○/g)||[]).length});
      for(const a of find('رَتِّبْ')) out.push({task:'sequence', items:items(a), boxes:(a.textContent.match(/⬜/g)||[]).length});
      return out;
    }""")
    resources = res
    rm = [x for x in res if x["task"] == "read-match"]
    if not rm or rm[0]["pictures"] < rm[0]["items"]: blockers.append("Unit 1 read-match: response pictures missing or fewer than its sentences (B4)")
    for x in [x for x in res if x["task"] == "who-says"]:
        if x["faces"] < 2 or x["items"] < 1 or x["circles"] < x["items"]: blockers.append(f"Unit 1 who-says: faces {x['faces']}, quotes {x['items']}, answer slots {x['circles']} (B4)")
    for x in [x for x in res if x["task"] == "sequence"]:
        if x["items"] < 3 or x["boxes"] < x["items"]: blockers.append(f"Unit 1 sequence: {x['items']} lines, {x['boxes']} boxes (B4)")
    # I2: every printed who-says quote must be a substring of the printed story on the same page
    drift = pg.evaluate("""() => {
      const on=document.getElementById('v-student'); const norm=s=>s.replace(/\\s+/g,' ').replace(/&quot;/g,'"');
      const story=norm([...on.querySelectorAll('.storyprose')].map(e=>e.textContent).join(' '));
      const bad=[];
      for(const a of on.querySelectorAll('.act')){ const rub=(a.querySelector('.rubric span[lang=ar]')||{}).textContent||'';
        if(!/مَنْ يَقُولُ|رَتِّبْ/.test(rub)) continue;
        for(const li of a.querySelectorAll('ul[lang=ar] li')){ const t=norm(li.textContent).replace(/[○⬜]/g,'').trim().replace(/^«|»$/g,''); if(t && !story.includes(t)) bad.push(t); } }
      return bad; }""")
    for t in drift: blockers.append(f"Unit 1 printed quotation not in the story on its page: «{t}» (I2)")

    # --- SC-121: every learner-visible Arabic token on the Unit 1 pages is a canon word or a licensed/chrome token
    lic_path = Path(__file__).resolve().parent.parent / "units" / "unit1" / "apparatus_licence_u1.json"
    sweep = {"unknown": [], "checked": 0}
    if lic_path.exists() and engine_js:
        lic = json.loads(lic_path.read_text(encoding="utf-8"))
        allowed = set(lic["names"]["tokens"]) | set(lic["letters"]["tokens"]) | set(lic["licensed_forms"]["tokens"].keys()) | set(lic["chrome"]["tokens"])
        canon = subprocess.check_output(["node", "-e", 'const E=require(process.argv[1]);console.log(Object.values(E.UNITS).filter(u=>/unit-01/.test(u.unit_id)).map(u=>u.canon).join(" "))', eng_path], text=True)
        arabic_runs = lambda t: re.findall(r"[\u0621-\u064A\u064B-\u0652\u0670\u0640]+", t)   # letters, harakat, dagger alif, tatweel
        canon_words = set(arabic_runs(canon))
        for view in ("v-student", "v-note"):
            pg.goto(base + ("#unit-01/student" if view == "v-student" else "#unit-01/notebook"), wait_until="networkidle"); pg.wait_for_timeout(150)
            text = pg.evaluate("""(v) => { const on=document.getElementById(v).cloneNode(true); on.querySelectorAll('.rev,script,style,svg').forEach(e=>e.remove());
              const parts=[]; const walk=n=>{ for(const c of n.childNodes){ if(c.nodeType===3) parts.push(c.textContent); else if(c.nodeType===1) walk(c); } }; walk(on); return parts.join(' '); }""", view)
            toks = arabic_runs(text)
            sweep["checked"] += len(toks)
            for w in sorted(set(toks)):
                if w not in canon_words and w not in allowed: sweep["unknown"].append((view, w))
        for view, w in sweep["unknown"]: blockers.append(f"{view}: Arabic token «{w}» is neither in the canons nor in apparatus_licence_u1.json (SC-121)")
    else:
        warnings.append("apparatus licence not found — language sweep skipped")
    # --- SC-121: every print task has an Arabic rubric and at least one item; every notebook page has its rubric
    forms = pg.evaluate("""() => {
      const st=document.getElementById('v-student'); const nb=document.getElementById('v-note');
      const acts=[...st.querySelectorAll('.act')].map(a=>({rubric:!!a.querySelector('.rubric [lang=ar]'), items:a.querySelectorAll('ul[lang=ar] li').length, english:[...a.querySelectorAll('p.note:not(.rev)')].length}));
      const pages=[...nb.querySelectorAll('.sheet')].map(s=>({tag:!!s.querySelector('.sheet-tag [lang=ar]'), hasNb:!!s.querySelector('.nb')}));
      const corner=document.getElementById('authentic-corner'); const slots=corner?[...corner.querySelectorAll('.photo')].map(p=>!!p.querySelector('img')):[];
      return {acts, pages, corner: corner?{status:corner.dataset.status, slots}:null};
    }""")
    for i, a in enumerate(forms["acts"]):
        if not a["rubric"] or a["items"] < 1: blockers.append(f"Unit 1 print task #{i+1}: missing Arabic rubric or items")
        if a["english"]: blockers.append(f"Unit 1 print task #{i+1}: English instruction visible in learner view")
    for i, pgc in enumerate(forms["pages"]):
        if not pgc["tag"]: blockers.append(f"Unit 1 notebook sheet #{i+1}: no Arabic rubric tag")
    corner = forms["corner"]
    if corner is None or not all(corner["slots"]): warnings.append("Unit 1 authentic corner: NOT DELIVERED — " + (f"{sum(1 for s in (corner or {}).get('slots', []) if s)} of 3 photographs present" if corner else "block missing") + " (Batch 2; the unit is not complete)")

    # --- B1 / I7: walk every digital pathway to its end
    ANSWER_JS = r"""() => {
      const S=SCP.current(); const a=S.item; if(!a) return 'none';
      const E=window.SC_ENGINE, U=E.UNITS[S.unit];
      const click=sel=>{const el=document.querySelector(sel); if(!el) return false; el.click(); return true;};
      if(a==='POST') return 'post';
      switch(a.type){
        case 'explore': return click('#x-next')?'explore':'explore-missing';
        case 'read': { if(document.getElementById('rd-more')){click('#rd-more');return 'read-more';} return click('#rd-done')?'read-done':'read-missing'; }
        case 'arabic_to_picture': case 'picture_to_arabic': case 'meaning_in_context': return click(`[data-c="${a.correct}"]`)?a.type:'missing-choice';
        case 'either_or': { const c=U.contrasts.find(x=>x.id===a.contrast); return click(`[data-c="${c.correct}"]`)?a.type:'missing-choice'; }
        case 'true_false': { const f=U.facts.find(x=>x.id===a.fact); return click(`[data-c="${f.truth?'t':'f'}"]`)?a.type:'missing-choice'; }
        case 'who_says': { const w=U.whosays.find(x=>x.id===a.quote); const n=document.querySelectorAll('[data-c]').length; return (n>=2&&click(`[data-c="${w.speaker}"]`))?a.type:'who-says-faces-'+n; }
        case 'find_it': { const f=U.findit.find(x=>x.id===a.findit); return click(`[data-c="${f.answer}"]`)?a.type:'missing-choice'; }
        case 'retrieval': { const r=U.retrieval.find(x=>x.id===a.retrieval); return click(`[data-c="${r.blank}"]`)?a.type:'missing-choice'; }
        case 'sequence': { const rows=[...document.querySelectorAll('.seqrow')]; const texts=rows.map(r=>r.querySelector('.seqar').textContent.trim());
          const want=[...U.events].sort((x,y)=>x.order-y.order).map(e=>U.sentences.find(s=>s.id===e.sentence).ar.trim());
          const idx=want.map(t=>texts.indexOf(t)); if(idx.includes(-1)) return 'sequence-text-mismatch';
          // bubble the first out-of-place row up one step; the gate re-evaluates until the order is right
          for(let i=0;i<texts.length;i++){ if(texts[i]!==want[i]){ const j=texts.indexOf(want[i]); document.querySelector(`[data-up="${j}"]`).click(); return 'sequence-step'; } }
          return click('#seq-check')?'sequence-check':'sequence-missing'; }
        default: return 'unknown-'+a.type;
      }
    }"""
    for unit_base, pair in (("unit-01", "unit-01p"), ("unit-02", "unit-02p"), ("unit-03", "unit-03p")):
        for card in ("vocab", "reading", "reading2"):
            pg.goto(base, wait_until="networkidle"); pg.goto(base + f"#{unit_base}/practice", wait_until="networkidle"); pg.wait_for_timeout(200)
            disabled = pg.evaluate(f"() => {{const b=document.querySelector('[data-h=\"{card}\"]'); return b?b.disabled:null;}}")
            if disabled is None: blockers.append(f"{unit_base}: pathway card '{card}' missing"); continue
            if disabled: blockers.append(f"{unit_base}: pathway card '{card}' is disabled — unit withheld on the live build"); continue
            pg.click(f'[data-h="{card}"]'); pg.wait_for_timeout(150)
            planned = pg.evaluate("() => SCP.current().length")
            steps, kinds, done, last = 0, {}, False, None
            for _ in range(600):
                if pg.evaluate("() => !!document.querySelector('.donebig')"): done = True; break
                k = pg.evaluate(ANSWER_JS); kinds[k] = kinds.get(k, 0) + 1; steps += 1
                if k.startswith(("missing", "who-says-faces", "unknown", "sequence-text", "explore-missing", "read-missing")): last = k; break
                pg.wait_for_timeout(720 if k not in ("read-more", "sequence-step") else 120)
            completed = pg.evaluate("() => SCP.current().index")
            pathways.append((unit_base, card, planned, completed, done, dict(sorted(kinds.items())), last))
            if not done: blockers.append(f"{unit_base}/{card}: pathway did not reach its end (stopped at {last or 'step limit'} after {steps} actions; {completed} of {planned} tasks)")
    b.close()
srv.shutdown()

# --- static checks
if expected_version and f"VERSION {expected_version}" not in html:
    blockers.append(f"version chip is not VERSION {expected_version}")
if "teacher.html" in html: blockers.append("index.html mentions teacher.html (SC-104)")
for m in re.findall(r'src="(assets/[^"]+)"', html):
    if not (deploy / m).exists(): blockers.append(f"asset referenced but missing: {m}")
srcs = re.findall(r'src="(assets/art/[^"]+)"', html)
dups = {s for s in srcs if srcs.count(s) > 1}
if dups: warnings.append("art files used more than once (check each is a legitimate reuse): " + ", ".join(sorted(dups)))
for ph in ("illustration pending", "not yet commissioned", "PROPOSED"):
    n = html.count(ph)
    if n: warnings.append(f'"{ph}" appears {n}× — confirm each is intended')
for k in ("answer key", "Answer key", "ANSWER KEY"):
    if k in html: blockers.append("the word 'answer key' appears in the Studio (SC-048)")
if re.search(r"أَنَا وَلَدٌ|أَنَا بِنْتٌ", html): blockers.append("first-person gender self-categorisation printed (SC-021)")
if (deploy / "index.html").read_bytes() != (deploy / "404.html").read_bytes(): blockers.append("index.html and 404.html differ")
if not (deploy / "teacher.html").exists(): blockers.append("teacher.html missing from the deploy folder")

# --- evidence record: STATUS-ONLY check (SC-122; Learning Effectiveness Standard §9). The gate reads the Unit 1
# evidence record, requires that it exists, names the deployed version and carries its five status fields.
# It never writes a status, never infers one from a build result, and treats "not run / not observed" as valid.
rec = deploy / "source/units/unit1/INTALIQ1_UNIT1_LEARNING_EVIDENCE_RECORD.md"
if not rec.exists():
    blockers.append("Unit 1 evidence record missing (source/units/unit1/INTALIQ1_UNIT1_LEARNING_EVIDENCE_RECORD.md, SC-122)")
else:
    rtxt = rec.read_text(encoding="utf-8")
    fsec = rtxt.split("## F · Status", 1)[1] if "## F · Status" in rtxt else ""
    if expected_version and f"VERSION {expected_version}" not in fsec:
        blockers.append(f"Unit 1 evidence record §F does not name VERSION {expected_version} (SC-122) — re-state the record against the deployed build; statuses are not changed by this")
    for field in ("Technical:", "Design review:", "Learner evidence", "Listening and corner:"):
        if field not in fsec: blockers.append(f"Unit 1 evidence record §F lacks the field '{field}' (SC-122)")
    if "not observed" in fsec: warnings.append("Unit 1 learner evidence: NOT OBSERVED — the record says so; the unit carries no learning claim (SC-122)")
    if "Design review: not run" in fsec: warnings.append("Unit 1 design review: NOT RUN (SC-009 panel sitting not yet recorded; SC-122)")
errs = [c for c in console if c[0] == "error" and "ERR_TUNNEL" not in c[1] and "net::" not in c[1]]
for u in sorted(set(external)): warnings.append(f"external resource not reachable from this workspace (fine on Pages): {u[:90]}")
for e in errs: blockers.append(f"console error: {e[1][:160]}")
for f in failed: blockers.append(f"request failed: {f}")

# --- report
rep = ["# Release verification", f"folder: `{deploy}`", ""]
rep.append("| route | view | frames (empty) | broken imgs | unresolved use | shot |")
rep.append("|---|---|---|---|---|---|")
for r, i, s in rows:
    rep.append(f"| {r} | {i['view']} | {i['frames']} ({i['emptyFrames']}) | {len(i['brokenImgs'])} | {len(i['unresolvedUse'])} | {s} |")
rep += ["", "## Digital pathways walked to the end", "| unit | pathway | planned tasks | completed | reached end | actions by kind |", "|---|---|---:|---:|---|---|"]
for u, c, planned, completed, done, kinds, last in pathways:
    rep.append(f"| {u} | {c} | {planned} | {completed} | {'yes' if done else 'NO — ' + str(last)} | {', '.join(f'{k} {v}' for k, v in kinds.items())} |")
rep += ["", "## Unit 1 print-task response resources", "```", json.dumps(resources, ensure_ascii=False), "```"]
rep += ["", "## Unit 1 language sweep (learner view)", f"{sweep['checked']} Arabic tokens checked on the student and notebook pages; unknown: {len(sweep['unknown'])}" if 'sweep' in dir() else "not run"]
rep += ["", "## Unit 1 task forms", "```", json.dumps(forms, ensure_ascii=False) if 'forms' in dir() else "not run", "```"]
rep += ["", "## Listening machinery (fixture test against the deployed engine)", str(listening_test)]
rep += ["", "## Mutation tests (deployed engine)", "| unit | mutation | delivers | sequence | pathway |", "|---|---|---|---:|---:|"]
for r in (mut if engine_js else []):
    rep.append(f"| {r['unit']} | {r['test']} | {'YES' if r['delivers'] else 'blocked'} | {r['seq']} | {r['path']} |")
rep += ["", "## Blockers", *([f"- {b}" for b in blockers] or ["- none"]),
        "", "## Warnings", *([f"- {w}" for w in warnings] or ["- none"])]
(deploy.parent / "verify_report.md").write_text("\n".join(rep), encoding="utf-8")

# contact sheet
try:
    from PIL import Image
    shots = [Image.open(out / s) for _, _, s in rows]
    W = 400; thumbs = []
    for im in shots:
        h = int(im.height * W / im.width); thumbs.append(im.resize((W, min(h, 1200))))
    cols = 4; rowsN = (len(thumbs) + cols - 1) // cols; H = max(t.height for t in thumbs)
    sheet = Image.new("RGB", (W * cols, H * rowsN), "white")
    for k, t in enumerate(thumbs): sheet.paste(t, ((k % cols) * W, (k // cols) * H))
    sheet.save(deploy.parent / "verify_sheet.png")
except Exception as e:
    warnings.append(f"contact sheet not made: {e}")

print("\n".join(rep))
sys.exit(1 if blockers else 0)
