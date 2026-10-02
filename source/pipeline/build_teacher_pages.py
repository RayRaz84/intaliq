# -*- coding: utf-8 -*-
"""
build_teacher_pages.py — generates the per-unit TEACHER'S PAGE (SC-104).

Rules this generator enforces, by construction:
  * one page per frozen unit; contents = unit flow (five phases → the unit's actual pages),
    C1 · C3 · C4 procedures (three lines or fewer each), pilot observation notes (Activity Architecture §8);
  * NO answer keys of any kind (SC-048 item 3) — the data below carries no answers, and the
    assertion at the bottom of this file refuses to build if any bank/answer field is ever added;
  * NOT linked from the student Studio — this script never touches school_course_studio.html;
  * counts (words, activities) are read from the engine, never typed by hand.

Outputs: intaliq1_teacher_pages.html (artifact body, no skeleton) and
         Intaliq1_Teacher_Pages.html (standalone, wrapped).
"""
import json, subprocess, html, datetime, pathlib, sys, re

HERE = pathlib.Path(__file__).resolve().parent
ENGINE = HERE / "engine_core.js"

# ---------- 1 · counts from the engine (never hand-typed) ----------
NODE = r'''
const fs=require("fs");const src=fs.readFileSync(process.argv[1],"utf8");
const g={};(new Function("globalThis",src+";return globalThis;"))(g);const E=g.SC_ENGINE;const out={};
for(const [k,u] of Object.entries(E.UNITS)){const acts=E.gen(u);const q=E.qc(u,acts);const c=E.canonCheck(u);
 out[k]={title:u.title,words:c.words,canon_ok:c.ok,ok:q.ok.length,failed:q.failed.length};}
process.stdout.write(JSON.stringify(out));
'''
meta = json.loads(subprocess.check_output(["node", "-e", NODE, str(ENGINE)], text=True))
for k, v in meta.items():
    assert v["canon_ok"] and v["failed"] == 0, f"{k}: engine not clean — refuse to build a teacher's page on a failing unit"

# ---------- 2 · per-unit data (no answers anywhere) ----------
UNITS = [
 dict(
  n=1, label="Unit 1", ar="الْوَحْدَةُ ١", status="Frozen · Unit 1 is the pre-calibration unit (SC-093)",
  r1=dict(key="unit-01", title="قَائِمَةُ رَزَان", tense="present", frames=6),
  r2=dict(key="unit-01p", title="مَنْ أَنْتَ يَا قَلَم؟", tense="past", frames=3),
  pictures="Illustrated (house style, SC-034).",
  flow=[
   ("Input", "The learner, alone",
    ["Digital · الْمُفْرَدَات — hear-and-tap practice on the unit's words, verbs and possession (A1–A4).",
     "Textbook · اُنْظُرْ! — the labelled phrase scene (B1) and the six-frame strip."],
    "Shared devices at the top of class, or the picture spread where there are none. Do not explain the words; the pictures and audio do that."),
   ("Reading", "The learner (the class may read together)",
    ["Reading 1 «قَائِمَةُ رَزَان» — {w1} words, present narration — then its sets: اِقْرَأْ وَصِلْ · صَحٌّ أَمْ خَطَأٌ؟ أَرِنِي · مَنْ يَقُولُ؟ · اِخْتَرْ وَاكْتُبْ · رَتِّبْ · اِبْحَثْ فِي النَّصِّ. Digital · الْقِرَاءَة ١ ({a1} activities).",
     "Reading 2 «مَنْ أَنْتَ يَا قَلَم؟» — {w2} words, past narration, dialogue in the present — then its sets, ending with الْآنَ أَمْ قَبْلُ؟ (sort lines into the present story or the past story, by ear). Digital · الْقِرَاءَة ٢ ({a2} activities)."],
    "Readings are read cold — there is no oral pre-telling in this course. Every set is self-checking against the page it sits on; nothing to mark."),
   ("Consolidation", "The learner",
    ["The pop-up «Look — no “is”!» — the book's only English (LC-4: one per unit, no rule drilled).",
     "قَائِمَةُ الصَّفِّ — the class roll as functional text (اِسْتَعْمِلِ النَّصَّ); عَرَبِيَّةٌ حَوْلَنَا — the authentic-print corner.",
     "أَسْتَطِيعُ! — the unit's last page: can-do lines the learner ticks by saying them."],
    "Read the pop-up once with the class if asked; do not extend it into a grammar lesson."),
   ("Output", "The learner, alone — begun in class, finishable at home",
    ["Notebook p. 2–3 · اُكْتُبِ الْقِصَّةَ: «قَائِمَةُ رَزَان» — six frames, one line per frame, bank printed (Captions rung, SC-096).",
     "Notebook p. 4 · اُكْتُبِ الْقِصَّةَ: «مَنْ أَنْتَ يَا قَلَم؟» — three frames; the past forms are copied from the bank, never built.",
     "Notebook p. 5–6 · قِصَّتِي الْمُوَازِيَةُ — the same story about the learner's real class, using the names from the survey on p. 9.",
     "Notebook p. 7 · قِصَّتِي — starters and a split bank (things / people). p. 8 · دَوْرِي — the name poster.",
     "Notebook p. 10 · هَلْ تَذْكُرُ؟ — blank at Unit 1 by design (it draws on earlier units only)."],
    "Sequence note: p. 5 needs the names collected on p. 9 — run the C1 survey before learners start the parallel story."),
   ("Communication", "The teacher facilitates — zero prep, no props",
    ["C4 · نُعِيدُ الْقِصَّةَ بِالصُّوَرِ — printed under the six-frame strip in the book.",
     "C1 · اِسْأَلْ أَصْدِقَاءَكَ — notebook p. 9: «مَنْ أَنْتَ؟» · «مَنْ عِنْدَهُ قَلَمٌ؟»",
     "C3 · هٰذِهِ صَفْحَتِي! — the last line of p. 6, and the poster on p. 8."],
    "Everything here runs on pages the unit has already produced. Nothing is made, cut or printed."),
  ],
  c3_example="«مَنْ هٰذَا؟» · «عِنْدَكَ قَلَمٌ؟»",
  notes=[]),
 dict(
  n=2, label="Unit 2", ar="الْوَحْدَةُ ٢", status="Frozen (revision 6) · texts signed off (SC-105) · Gate B closes on the pop-up · illustrations held",
  r1=dict(key="unit-02", title="أَيْنَ مِفْتَاحِي؟", tense="present", frames=8),
  r2=dict(key="unit-02p", title="صُورَةُ رَزَان وَخَدِيجَة", tense="past", frames=6),
  pictures="Not yet illustrated — strips print as empty numbered frames until the hold is lifted.",
  flow=[
   ("Input", "The learner, alone",
    ["Digital · الْمُفْرَدَات — hear-and-tap practice on the unit's items.",
     "Textbook · اُنْظُرْ وَاقْرَأْ! — the phrase page (B0): nineteen numbered phrases, each as the story prints it.",
     "The strips (8 + 6 frames) and the preview panel — pictures pending."],
    "Until the pictures land, phase 1 rests on the phrase page and the digital practice alone. Do not draw the frames yourself; the illustration plan governs them."),
   ("Reading", "The learner (the class may read together)",
    ["Reading 1 «أَيْنَ مِفْتَاحِي؟» — {w1} words, present narration — then: صَحٌّ أَمْ خَطَأٌ؟ أَرِنِي · مَنْ يَقُولُ؟ · أَجِبْ (the last two questions have no answer in the text: the learner invents one) · نَفْسُ الْقِصَّةِ... وَ (Version A / B, retold from the pictures). Digital · الْقِرَاءَة ١ ({a1} activities).",
     "Reading 2 «صُورَةُ رَزَان وَخَدِيجَة» — {w2} words, past narration, dialogue in the present — then: مَنْ يَقُولُ؟ · رَتِّبْ · الْآنَ أَمْ قَبْلُ؟ (sort lines into the now-story or the before-story, by ear). Digital · الْقِرَاءَة ٢ ({a2} activities)."],
    "Read cold, as in Unit 1. The «invent it» answers are the learner's own — there is nothing to correct."),
   ("Consolidation", "The learner",
    ["اِقْرَأْ. ثُمَّ اقْرَأْ. — the recombination page: ten one-breath texts from the unit's words; read, then read again.",
     "وَأَنْتَ؟ وَأَنْتِ؟ — Unit 2's ten personal questions, added to Unit 1's set; answered from the phrase page, never scored.",
     "The pop-up «Look — now, or before?» — proposed (SC-105), awaiting the owner's word; the book's only English."],
    "Ask the personal questions aloud, in Arabic, one at a time; accept one-word answers from the phrase page."),
   ("Output", "The learner, alone — begun in class, finishable at home",
    ["Notebook p. 2–3 · اُكْتُبِ الْقِصَّةَ: «أَيْنَ مِفْتَاحِي؟» — eight frames, one line per frame, bank printed (Captions rung).",
     "Notebook p. 4 · اُكْتُبِ الْقِصَّةَ: «صُورَةُ رَزَان وَخَدِيجَة» — six frames; the three past forms are in the bank and copied.",
     "Notebook p. 5–6 · قِصَّتِي الْمُوَازِيَةُ — four swaps: the finder, the friend visited (from the p. 9 survey), where the key is kept, and who is at the door (drawn).",
     "Notebook p. 7 · قِصَّتِي — the location sentence produced: thing · preposition · place from a split bank. p. 8 · دَوْرِي — my key.",
     "Notebook p. 10 · هَلْ تَذْكُرُ؟ — the first real one: four Unit 1 faces and lines."],
    "Same sequence note as Unit 1: run the p. 9 survey before p. 5."),
   ("Communication", "The teacher facilitates — zero prep, no props",
    ["C4 · نُعِيدُ الْقِصَّةَ بِالصُّوَرِ — under the eight-frame strip (rubric added in Studio Version 39; the frames are still empty).",
     "C1 · اِسْأَلْ أَصْدِقَاءَكَ — notebook p. 9: «أَيْنَ تَضَعُ مِفْتَاحَكَ؟» · «إِلَى أَيْنَ تَذْهَبُ؟»",
     "C3 · هٰذِهِ صَفْحَتِي! — the last line of p. 6, and the key poster on p. 8."],
    "Until the strip is illustrated, C4 can run from the phrase-page pictures' order of events only if the class has read the story; otherwise hold C4 for the pictures."),
  ],
  c3_example="«أَيْنَ مِفْتَاحُكَ؟» · «مَنْ عِنْدَ الْبَابِ؟»",
  notes=[]),
 dict(
  n=3, label="Unit 3", ar="الْوَحْدَةُ ٣", status="Revision 1 · Gate A approved (SC-109) · Gate B pending · illustrations held",
  r1=dict(key="unit-03", title="مَنْ عِنْدَهُ الْكُرَةُ؟", tense="present", frames=8),
  r2=dict(key="unit-03p", title="هَدِيَّةُ رَزَان", tense="past", frames=6),
  pictures="Not yet illustrated — strips print as empty numbered frames until the hold is lifted.",
  flow=[
   ("Input", "The learner, alone",
    ["Digital · الْمُفْرَدَات — hear-and-tap practice on the unit's items.",
     "Textbook · اُنْظُرْ وَاقْرَأْ! — the phrase page (B0): eighteen numbered phrases, each as the story prints it.",
     "The strips (8 + 6 frames) — pictures pending."],
    "Until the pictures land, phase 1 rests on the phrase page and the digital practice alone."),
   ("Reading", "The learner (the class may read together)",
    ["Reading 1 «مَنْ عِنْدَهُ الْكُرَةُ؟» — {w1} words, present narration — then: صَحٌّ أَمْ خَطَأٌ؟ أَرِنِي · مَنْ يَقُولُ؟ · أَجِبْ (the last two questions are invented) · نَفْسُ الْقِصَّةِ... وَ (Version A / B). Digital · الْقِرَاءَة ١ ({a1} activities).",
     "Reading 2 «هَدِيَّةُ رَزَان» — {w2} words, past narration, dialogue in the present — then: مَنْ يَقُولُ؟ · رَتِّبْ · الْآنَ أَمْ قَبْلُ؟. Digital · الْقِرَاءَة ٢ ({a2} activities)."],
    "Read cold. The family words are met inside the story before anyone names them; do not pre-teach the list."),
   ("Consolidation", "The learner",
    ["اِقْرَأْ. ثُمَّ اقْرَأْ. — the recombination page, ten texts.",
     "وَأَنْتَ؟ وَأَنْتِ؟ — Unit 3's ten personal questions, added to the cumulative set.",
     "The pop-up «Look — the ending says whose!» — the book's only English; proposed, confirmed at Gate B."],
    "Ask the personal questions in Arabic, one at a time. «مَنْ فِي بَيْتِكَ؟» takes any true answer, including «أَنَا وَأُمِّي» or «قِطٌّ» — nothing on any page requires a family shape."),
   ("Output", "The learner, alone — begun in class, finishable at home",
    ["Notebook p. 2–3 · اُكْتُبِ الْقِصَّةَ: «مَنْ عِنْدَهُ الْكُرَةُ؟» — eight frames, two slots per line, bank shuffled and over-full (Frames rung, first use).",
     "Notebook p. 4 · اُكْتُبِ الْقِصَّةَ: «هَدِيَّةُ رَزَان» — six frames; the past forms are in the bank and copied.",
     "Notebook p. 5–6 · قِصَّتِي الْمُوَازِيَةُ — the skeleton keeps only its verbs; the learner writes every noun phrase and one whole line, from the p. 9 survey and the p. 8 poster.",
     "Notebook p. 7 · قِصَّتِي — starters, no bank. p. 8 · دَوْرِي — my family, two lines and a drawing.",
     "Notebook p. 10 · هَلْ تَذْكُرُ؟ — four Unit 2 lines."],
    "This is the first unit with no bank on p. 5–7. Expect it to be slower; if learners cannot supply a whole line unassisted, note it on the pilot sheet — the ladder moves the rung to Unit 5 on that evidence, not on impression."),
   ("Communication", "The teacher facilitates — zero prep, no props",
    ["C4 · نُعِيدُ الْقِصَّةَ بِالصُّوَرِ — under the eight-frame strip; learner-led, one picture each (Frames rung).",
     "C1 · اِسْأَلْ أَصْدِقَاءَكَ — notebook p. 9, find someone who has: «عِنْدَكَ أَخٌ؟ · أُخْتٌ؟ · كُرَةٌ؟ · قِطٌّ؟»",
     "C3 · هٰذِهِ صَفْحَتِي! — p. 6, and the family poster on p. 8 presented as a two-line exchange."],
    "Run p. 9 before p. 5, as always. The poster is shared with a partner, not the whole class, unless the child wants to."),
  ],
  c3_example="«مَنْ هٰذَا؟» · «عِنْدَكَ أَخٌ؟»",
  notes=[]),
]

PROCEDURES = {
 "C1": ("اِسْأَلْ أَصْدِقَاءَكَ", "Ask your friends — the survey", [
   "Notebook open at p. 9. Read the two printed questions aloud once, in Arabic; do not translate them.",
   "Learners stand, ask five classmates, write each name and tick the column that fits the answer.",
   "Stop when every grid has five names. Those names are used on p. 5 — so this runs before the parallel story."]),
 "C3": ("هٰذِهِ صَفْحَتِي", "Share your page", [
   "In pairs. The learner holds up the finished page (p. 5–6 or the poster on p. 8) and says the printed line: «هٰذِهِ صَفْحَتِي!»",
   "The partner points to one thing on the page and asks one question from the unit's own set — for this unit, e.g. {c3ex}.",
   "Swap roles. If there is a wall, the pages go on it; nothing is marked."]),
 "C4": ("نُعِيدُ الْقِصَّةَ", "Story circle — the retell", [
   "Books open at the strip. Point to frame 1 and wait; the class says what happens.",
   "Write on the board only what the class says, as they say it. Do not supply or correct toward the printed text.",
   "Move to the next frame once a sentence has been said for this one. The story ends when the strip does."]),
}

PILOT = [
 "Of the two readings, how much could learners retell from the strip without the text? (a rough share, and which frames stalled)",
 "First cold read of Reading 1: what did the class understand before the phrase page and strip, and what changed after them?",
 "Were the personal questions (وَأَنْتَ؟ وَأَنْتِ؟) answered without you? Which ones needed you?",
 "Was the recombination page read, skipped, or read once? (Unit 2 onward)",
 "On the notebook: did learners complete p. 5–6 and p. 7 unassisted? Where did they stop and ask?",
 "Anything a learner said in Arabic that the unit did not teach — write it down exactly.",
]

# ---------- 3 · render ----------
_AR = re.compile(r'«?[\u0600-\u06FF][\u0600-\u06FF\s؟!،:\.]*[\u0600-\u06FF؟!\.]»?|«?[\u0600-\u06FF]»?')
def esc(s):
    """escape, then isolate every Arabic run so numbers and punctuation beside it keep their place"""
    return _AR.sub(lambda m: f'<bdi lang="ar" class="ar">{m.group(0)}</bdi>', html.escape(s))
def ar(s): return f'<bdi lang="ar" class="ar">{html.escape(s)}</bdi>'

def render_unit(u):
    m1, m2 = meta[u["r1"]["key"]], meta[u["r2"]["key"]]
    fill = dict(w1=m1["words"], w2=m2["words"], a1=m1["ok"], a2=m2["ok"])
    out = [f'''
<section class="unit" id="unit-{u["n"]:02d}">
 <header class="uhead">
  <div class="eyebrow">Teacher · {esc(u["label"])} · {ar(u["ar"])}</div>
  <h2 dir="ltr">{ar(u["r1"]["title"])} <span class="sep">·</span> {ar(u["r2"]["title"])}</h2>
  <dl class="facts">
   <div><dt>Reading 1</dt><dd>{ar(u["r1"]["title"])} — {m1["words"]} words, {u["r1"]["tense"]} · {u["r1"]["frames"]} frames</dd></div>
   <div><dt>Reading 2</dt><dd>{ar(u["r2"]["title"])} — {m2["words"]} words, {u["r2"]["tense"]} · {u["r2"]["frames"]} frames</dd></div>
   <div><dt>Digital</dt><dd>{m1["ok"]} + {m2["ok"]} generated activities, QC clean</dd></div>
   <div><dt>Pictures</dt><dd>{esc(u["pictures"])}</dd></div>
   <div><dt>Status</dt><dd>{esc(u["status"])}</dd></div>
  </dl>
 </header>

 <h3>The unit flow <small>five phases, in the order the course requires (meaning → reading → output → talk)</small></h3>
 <ol class="flow">''']
    for i, (name, who, pages, note) in enumerate(u["flow"], 1):
        items = "".join(f"<li>{esc(p.format(**fill))}</li>" for p in pages)
        out.append(f'''
  <li class="phase">
   <div class="ph"><span class="pnum">{i}</span><div><b>{esc(name)}</b><span class="who">{esc(who)}</span></div></div>
   <ul class="pages">{items}</ul>
   <p class="tnote">{esc(note)}</p>
  </li>''')
    out.append('</ol>\n <h3>Procedures <small>the three teacher-run formats; three lines each</small></h3>\n <div class="procs">')
    for code, (rub, en, lines) in PROCEDURES.items():
        ls = "".join(f"<li>{esc(l.format(c3ex=u['c3_example']))}</li>" for l in lines)
        out.append(f'''
  <article class="proc"><header><span class="code">{code}</span><span class="rub">{ar(rub)}</span><span class="en">{esc(en)}</span></header><ol>{ls}</ol></article>''')
    out.append('</div>\n <h3>Pilot notes <small>what the classroom pilot must report (Activity Architecture §8) — write here, or on paper</small></h3>\n <ol class="pilot">')
    for q in PILOT:
        out.append(f'<li><p>{esc(q)}</p><div class="lines" aria-hidden="true"></div></li>')
    out.append('</ol>\n</section>')
    return "".join(out)

today = datetime.date.today().isoformat()
CSS = r'''
<title>Intaliq Teacher Pages</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Naskh+Arabic:wght@400;700&family=Source+Serif+4:opsz,wght@8..60,500;8..60,700&family=Source+Sans+3:wght@400;600&display=swap">
<style>
:root{--ink:#1d2a2c;--mute:#5b6b6e;--ground:#f6f4ee;--paper:#fffdf8;--line:#d6d9d2;--acc:#2e6b70;--acc-ink:#fff;--warn:#8a5a12;--warn-bg:#f5e9d3;--chip:#e8efee}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--ink:#e8ebe6;--mute:#a4b0ae;--ground:#161d1e;--paper:#1f2829;--line:#37464a;--acc:#7cc4c8;--acc-ink:#0f1a1b;--warn:#e7c27a;--warn-bg:#3a2e14;--chip:#26393b}}
:root[data-theme="dark"]{--ink:#e8ebe6;--mute:#a4b0ae;--ground:#161d1e;--paper:#1f2829;--line:#37464a;--acc:#7cc4c8;--acc-ink:#0f1a1b;--warn:#e7c27a;--warn-bg:#3a2e14;--chip:#26393b}
body{background:var(--ground);color:var(--ink);font:16px/1.5 "Source Sans 3",system-ui,sans-serif;margin:0;padding-block:0 48px;padding-inline:16px}
.ar{font-family:"Noto Naskh Arabic","Amiri","Scheherazade New",serif;font-size:1.12em;unicode-bidi:isolate;direction:rtl}
.wrap{max-width:860px;margin:0 auto}
.top{border-bottom:2px solid var(--acc);padding:22px 0 14px;display:flex;flex-wrap:wrap;gap:8px 18px;align-items:baseline}
.top h1{font:700 30px/1.15 "Source Serif 4",Georgia,serif;margin:0;text-wrap:balance}
.badge{display:inline-block;background:var(--acc);color:var(--acc-ink);font-weight:600;letter-spacing:.08em;text-transform:uppercase;font-size:12px;padding:3px 9px;border-radius:3px}
.disc{background:var(--warn-bg);color:var(--warn);border-left:4px solid var(--warn);padding:10px 14px;margin:16px 0 8px;font-size:15px}
.disc b{font-weight:600}
.toc{display:flex;gap:10px;flex-wrap:wrap;margin:14px 0 26px;font-size:15px}
.toc a{color:var(--acc);text-decoration:none;border:1px solid var(--line);padding:4px 10px;border-radius:3px}
.toc a:focus-visible,a:focus-visible{outline:2px solid var(--acc);outline-offset:2px}
.unit{background:var(--paper);border:1px solid var(--line);padding:22px clamp(14px,3vw,30px) 26px;margin:0 0 34px}
.uhead .eyebrow{font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--mute)}
.uhead .eyebrow .ar{text-transform:none;letter-spacing:0;font-size:1.25em}
.uhead h2{font:700 26px/1.3 "Source Serif 4",Georgia,serif;margin:4px 0 12px;text-wrap:balance}
.sep{color:var(--mute);margin:0 8px}
.facts{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:6px 22px;margin:0;font-size:15px}
.facts div{display:flex;gap:10px;align-items:baseline}
.facts dt{color:var(--mute);min-width:74px;font-size:12px;letter-spacing:.08em;text-transform:uppercase}
.facts dd{margin:0}
h3{font:700 20px/1.3 "Source Serif 4",Georgia,serif;margin:30px 0 12px;border-top:1px solid var(--line);padding-top:16px}
h3 small{display:block;font:400 14px/1.4 "Source Sans 3",system-ui,sans-serif;color:var(--mute)}
.flow{list-style:none;margin:0;padding:0;display:grid;gap:14px}
.phase{display:grid;grid-template-columns:176px 1fr;gap:6px 16px}
.ph{display:flex;gap:10px;align-items:flex-start}
.pnum{flex:none;width:28px;height:28px;border-radius:50%;background:var(--acc);color:var(--acc-ink);font-weight:600;display:grid;place-items:center;font-variant-numeric:tabular-nums}
.ph b{display:block;font-size:16px}
.who{display:block;font-size:13px;color:var(--mute);line-height:1.3}
.pages{margin:0;padding-left:18px}
.pages li{margin:2px 0}
.tnote{grid-column:2;margin:2px 0 0;padding:6px 10px;background:var(--chip);border-radius:3px;font-size:15px}
.tnote::before{content:"Teacher — ";font-weight:600;color:var(--acc)}
.procs{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px}
.proc{border:1px solid var(--line);border-radius:4px;padding:12px 14px;background:var(--ground)}
.proc header{display:flex;flex-wrap:wrap;gap:6px 10px;align-items:baseline;margin-bottom:6px}
.proc .code{background:var(--acc);color:var(--acc-ink);font-weight:600;padding:1px 7px;border-radius:3px;font-size:13px}
.proc .rub{font-weight:700;font-size:1.05em}
.proc .en{color:var(--mute);font-size:14px}
.proc ol{margin:0;padding-left:20px;font-size:15px}
.proc li{margin:4px 0}
.pilot{margin:0;padding-left:22px;display:grid;gap:12px}
.pilot p{margin:0 0 4px}
.lines{height:54px;background:repeating-linear-gradient(to bottom,transparent 0 26px,var(--line) 26px 27px)}
footer{color:var(--mute);font-size:13px;margin-top:10px}
@media (max-width:560px){.phase{grid-template-columns:1fr}.tnote{grid-column:1}.facts dt{min-width:64px}}
@media print{body{background:#fff;color:#000;padding-inline:0}.unit{border:0;padding:0;page-break-after:always}.toc{display:none}.lines{height:72px}}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
</style>'''

body = [CSS, f'''
<div class="wrap">
 <header class="top"><span class="badge">Teacher</span><h1>Intaliq 1 · Teacher's pages</h1><span style="color:var(--mute)">Level 1 · MSA · ages 8–13</span></header>
 <p class="disc"><b>Not part of the student materials.</b> This page is for the person running the class. It is not linked from the student site and does not need to be hidden from learners: it holds no answers to anything (SC-048) — only the order of the unit, the three classroom procedures, and the questions the pilot must answer. Nothing on it asks you to prepare, print, cut or make anything.</p>
 <nav class="toc">''' + "".join(f'<a href="#unit-{u["n"]:02d}">{esc(u["label"])}</a>' for u in UNITS) + '</nav>']
for u in UNITS:
    body.append(render_unit(u))
body.append(f'''
 <footer>Generated at freeze from the unit instruments and the engine (SC-104) · Intaliq 1 · {today} · the three products are Digital · Textbook · Notebook; this page is not a fourth.</footer>
</div>''')
page = "".join(body)

# ---------- 4 · guards ----------
for forbidden in ("answer key", "Answer key", "مِفْتَاحُ الْإِجَابَاتِ", "correct answer"):
    assert forbidden not in page, f"teacher's page must carry no keys: found {forbidden!r}"
studio = (HERE / "school_course_studio.html")
if studio.exists():
    assert "teacher_pages" not in studio.read_text(encoding="utf-8"), "the Studio must not link the teacher's page (SC-104)"

(HERE / "intaliq1_teacher_pages.html").write_text(page, encoding="utf-8")
(HERE / "Intaliq1_Teacher_Pages.html").write_text(
    '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body>'
    + page + "</body></html>", encoding="utf-8")
print("built:", {k: (v["words"], v["ok"]) for k, v in meta.items()}, "bytes:", len(page.encode("utf-8")))
