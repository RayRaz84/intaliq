# -*- coding: utf-8 -*-
"""
build_teacher_pages.py — generates the per-unit TEACHER'S PAGE (SC-104).

Rules this generator enforces, by construction:
  * one page per frozen unit; contents = unit flow (five phases → the unit's actual pages),
    C1 · C3 · C4 procedures (three lines or fewer each); ⟨SC-124: the pilot observation notes were removed — no pilot,
    observation or evaluation survey is part of the course⟩;
  * NO answer keys of any kind (SC-048 item 3) — the data below carries no answers, and the
    assertion at the bottom of this file refuses to build if any bank/answer field is ever added;
  * NOT linked from the student Studio — this script never touches school_course_studio.html;
  * counts (words, activities) are read from the engine, never typed by hand.

Output: intaliq1_teacher_pages.artifact-body.html (body, no skeleton — the Text build wraps it into the
        repo's teacher.html, which is the file to open). The former second output, a standalone wrapped copy,
        was dropped in the 2026-10-12 cleanup: nothing read it, and teacher.html is the same page.
        (Name chosen to differ by more than letter case — audit 2026-10-10 §11: the old pair collided on a
         case-insensitive filesystem.)
Phase order (owner's decision, SC-119): input → reading → consolidation AND scaffolded interaction (C1) →
notebook output → fuller communication and transfer (C3, C4). SC-128 adds, inside the same phases: one noticing
task (S15) before the unit's pop-up, a genre label on the functional text, and a shared use for S6 → C3.
"""
import json, subprocess, html, datetime, pathlib, sys, re

HERE = pathlib.Path(__file__).resolve().parent
ENGINE = HERE / "engine_core.js"

# ---------- 1 · counts from the engine (never hand-typed) ----------
NODE = r'''
const fs=require("fs");const src=fs.readFileSync(process.argv[1],"utf8");
const g={};(new Function("globalThis",src+";return globalThis;"))(g);const E=g.SC_ENGINE;const out={};
for(const [k,u] of Object.entries(E.UNITS)){const acts=E.gen(u);const q=E.qc(u,acts);const c=E.canonCheck(u);const d=E.deliverable(u);
 const vocab=E.pathway(u,"vocab",0).length, reading=E.pathway(u,"reading",0).length-2+1+E.postReading(u,3,true).length;
 out[k]={title:u.title,words:c.words,canon_ok:c.ok,ok:q.ok.length,failed:q.failed.length,blocked:!d.ok,vocab,reading};}
process.stdout.write(JSON.stringify(out));
'''
meta = json.loads(subprocess.check_output(["node", "-e", NODE, str(ENGINE)], text=True))
for k, v in meta.items():
    assert v["canon_ok"] and v["failed"] == 0 and not v["blocked"], f"{k}: engine not clean — refuse to build a teacher's page on a failing unit"

# ---------- 2 · per-unit data (no answers anywhere) ----------
UNITS = [
 dict(
  n=1, label="Unit 1", ar="الْوَحْدَةُ ١", status="COMPLETE (SC-132) · Unit 1 is the pre-calibration unit (SC-093)",
  r1=dict(key="unit-01", title="قَائِمَةُ رَزَان", tense="present", frames=6),
  r2=dict(key="unit-01p", title="مَنْ أَنْتَ يَا قَلَم؟", tense="past", frames=3),
  pictures="Accepted rich-cartoon PNGs (owner adoption 2026-10-14; `data-u1-art-release` 30d90e8) in the book, notebook and digital practice. Audio: 72 clips, synthesised (ElevenLabs; Reading 1 one child voice, Reading 2 another — SC-129, SC-130) and verified clip by clip by a named listener (2026-10-17); the listening tasks are live.",
  flow=[
   ("Input", "The learner, alone",
    ["Digital · الْمُفْرَدَات — every core item met, recognised and met again in a sentence ({v1} tasks, planned sequence).",
     "Textbook · اُنْظُرْ! — the labelled phrase scene (B1) and the six-frame strip."],
    "Shared devices at the top of class, or the picture spread where there are none. Do not explain the words; the pictures and phrases do that. The vocabulary pathway now opens sound-first: the learner hears the verified clip and taps the picture before reading the word. The listening tasks (hear-and-tap, hear-which-line, hear-who-says) play the verified clips; the 🔊 beside a printed line plays the verified clip when that line has one, otherwise the browser's preview voice — a reading aid, not a listening task."),
   ("Reading", "The learner (the class may read together)",
    ["Reading 1 «قَائِمَةُ رَزَان» — {w1} words, present narration — then its sets: اِقْرَأْ وَصِلْ · صَحٌّ أَمْ خَطَأٌ؟ أَرِنِي · مَنْ يَقُولُ؟ · اِخْتَرْ وَاكْتُبْ · رَتِّبْ · اِبْحَثْ فِي النَّصِّ. Digital · الْقِرَاءَة ١ ({p1} tasks selected from {a1} generated).",
     "Reading 2 «مَنْ أَنْتَ يَا قَلَم؟» — {w2} words, past narration, dialogue in the present — then its sets, ending with الْآنَ أَمْ قَبْلُ؟ (sort each line into story 1 or story 2 — the titles are the categories). Digital · الْقِرَاءَة ٢ ({p2} tasks selected from {a2} generated)."],
    "Readings are read cold — there is no oral pre-telling in this course. Every set is self-checking against the page it sits on; nothing to mark."),
   ("Consolidation and scaffolded interaction", "The learner; then the class, with you facilitating",
    ["اُنْظُرْ مَرَّةً أُخْرَى — the noticing task (S15, SC-128), printed between Reading 1 and the pop-up: two examples with their people («هٰذَا عُمَر.» · «هٰذِهِ سَارَة.»); the learner underlines the word that changes, then rings هٰذَا or هٰذِهِ for three story people, and reads the confirmation box. Let them find it; do not pre-teach it.",
     "The pop-up «Look — no “is”!» — the book's only English (LC-4: one per unit, no rule drilled). It is the explanation that follows the noticing, not a substitute for it.",
     "قَائِمَةُ الصَّفِّ — the class roll as functional text (اِسْتَعْمِلِ النَّصَّ), with the named row of faces. Label it rightly if asked: a class roll written for this book (a genre model), not a real school's list; the real Arabic is the corner's. عَرَبِيَّةٌ حَوْلَنَا — the learner-sourced corner (SC-131): in the week of the unit, each child finds one piece of real Arabic writing around them — a package at home, a sign at the mosque or the Arabic school, a book cover — and draws it or pastes a photo into a box; then the three tasks apply to what they brought: ring a name you know · person or place? · ring a letter from your own name. Bring two or three examples yourself for children who find none; a half-filled page is fine — nothing is faked. أَسْتَطِيعُ! — the can-do page the learner ticks by saying the lines.",
     "C1 · اِسْأَلْ أَصْدِقَاءَكَ — notebook p. 9: «مَنْ أَنْتَ؟ / مَنْ أَنْتِ؟» · «هَلْ عِنْدَكَ / عِنْدَكِ قَلَمٌ؟» · «هَلْ عِنْدَكَ / عِنْدَكِ قَائِمَةٌ؟» — rehearsed from the printed line, then asked of five real classmates. Its names feed p. 5."],
    "Scaffolded interaction comes BEFORE notebook writing (owner's decision, SC-119): run C1 here, not after the notebook. A learner who missed it completes p. 5 from the printed class list instead."),
   ("Output", "The learner, alone — begun in class, finishable at home",
    ["Notebook p. 2–3 · اُكْتُبِ الْقِصَّةَ: «قَائِمَةُ رَزَان» — six frames, one line per frame, bank printed (Captions rung, SC-096).",
     "Notebook p. 4 · اُكْتُبِ الْقِصَّةَ: «مَنْ أَنْتَ يَا قَلَم؟» — three frames; the past forms are copied from the bank, never built.",
     "Notebook p. 5–6 · قِصَّتِي الْمُوَازِيَةُ — the same story about the learner's real class, using the names collected in C1.",
     "Notebook p. 7 · قِصَّتِي — starters, printed models for every choice, a split bank (things / people / a line to say). p. 8 · دَوْرِي — the class card («هٰذَا أَنَا. اسْمِي ___.»), which prepares the newcomer exchange of Phase 5; the two exchanges it will serve are printed on the page.",
     "Notebook p. 10 · هَلْ تَذْكُرُ؟ — blank at Unit 1 by design (it draws on earlier units only)."],
    "Every page here is completable alone (P-3). Do not mark; the pages are shown, not graded."),
   ("Fuller communication and transfer", "The teacher facilitates — zero prep, no props",
    ["C3 · هٰذِهِ صَفْحَتِي! — the newcomer exchange (SC-128): cards (p. 8) laid out; a partner plays the new student, holds the class list, reads a name and asks «مَنْ ___؟»; the class answers by pointing at the card «هٰذَا ___. / هٰذِهِ ___.»; the newcomer confirms «أَنْتَ ___! / أَنْتِ ___!» → «نَعَمْ! أَنَا ___!». Then p. 5–6 is shown and one question asked, as before.",
     "C4 · نُعِيدُ الْقِصَّةَ بِالصُّوَرِ — printed under the six-frame strip in the book; run it here, after both readings, not when the strip is first met.",
     "Transfer — the same language in a new small situation: a classmate's pen, a list of another class."],
    "Everything here runs on pages the unit has already produced. Nothing is made, cut or printed. At the Captions rung you cue each frame of C4 and the class supplies the language."),
  ],
  c3_example="«مَنْ عُمَر؟» · «هَلْ عِنْدَكَ قَلَمٌ؟»",
  c3_procedure=[
   "Model it first, with the book: hold the class roll (p. 9's five names, or the printed قَائِمَةُ الصَّفِّ), read one name — «مَنْ سَارَة؟» — and let the class point at a card and answer «هٰذِهِ سَارَة.»; then «أَنْتِ سَارَة!» → «نَعَمْ! أَنَا سَارَة!». Once each way, a boy and a girl. Do not translate.",
   "In pairs or small groups, cards (p. 8) on the desks. One learner is the newcomer with the list; the others answer by pointing at cards. Every name on the list is found and ticked. Swap the newcomer. This is Razan's problem from the story, done for real.",
   "Then the finished page (p. 5–6) is held up with «هٰذِهِ صَفْحَتِي!» and the partner asks one question from the unit's own set, e.g. {c3ex}. If there is a wall, the cards go on it afterwards; nothing is marked. Another class or a family member may play the newcomer as an extension — never required."],
  notes=[]),
 dict(
  n=2, label="Unit 2", ar="الْوَحْدَةُ ٢", status="Frozen (revision 6) · Gate B closed (SC-105, pop-up SC-134) · rich-cartoon illustrations live (SC-113, SC-117) · clips owed",
  r1=dict(key="unit-02", title="أَيْنَ مِفْتَاحِي؟", tense="present", frames=8),
  r2=dict(key="unit-02p", title="صُورَةُ رَزَان وَخَدِيجَة", tense="past", frames=6),
  pictures="Rich-cartoon illustrations, 69 accepted files (SC-113; bag corrected SC-117). No verified audio: there are no listening tasks.",
  flow=[
   ("Input", "The learner, alone",
    ["Digital · الْمُفْرَدَات — every core item met, recognised and met again in a sentence ({v1} tasks, planned sequence).",
     "Textbook · اُنْظُرْ وَاقْرَأْ! — the phrase page (B0): nineteen numbered phrases, each as the story prints it.",
     "The strips (8 + 6 frames) and the preview panel — rich-cartoon frames live."],
    "Shared devices at the top of class, or the phrase page and strips where there are none. Sound is the browser's preview voice on request only — no verified audio, so no listening tasks."),
   ("Reading", "The learner (the class may read together)",
    ["Reading 1 «أَيْنَ مِفْتَاحِي؟» — {w1} words, present narration — then: صَحٌّ أَمْ خَطَأٌ؟ أَرِنِي · مَنْ يَقُولُ؟ · أَجِبْ (the last two questions have no answer in the text: the learner invents one) · نَفْسُ الْقِصَّةِ... وَ (Version A / B, retold from the pictures). Digital · الْقِرَاءَة ١ ({p1} tasks selected from {a1} generated).",
     "Reading 2 «صُورَةُ رَزَان وَخَدِيجَة» — {w2} words, past narration, dialogue in the present — then: مَنْ يَقُولُ؟ · رَتِّبْ · الْآنَ أَمْ قَبْلُ؟ (sort each line into story 1 or story 2 — the titles are the categories). Digital · الْقِرَاءَة ٢ ({p2} tasks selected from {a2} generated)."],
    "Read cold, as in Unit 1. The «invent it» answers are the learner's own — there is nothing to correct."),
   ("Consolidation and scaffolded interaction", "The learner; then the class, with you facilitating",
    ["اِقْرَأْ. ثُمَّ اقْرَأْ. — the recombination page: ten one-breath texts from the unit's words; read, then read again.",
     "وَأَنْتَ؟ وَأَنْتِ؟ — Unit 2's ten personal questions, added to Unit 1's set; answered from the phrase page, never scored.",
     "The pop-up «Look — now, or before?» — proposed (SC-105), awaiting the owner's word; the book's only English.",
     "C1 · اِسْأَلْ أَصْدِقَاءَكَ — notebook p. 9: «أَيْنَ تَضَعُ مِفْتَاحَكَ؟» · «إِلَى أَيْنَ تَذْهَبُ؟» — asked of real classmates; its answers feed p. 5."],
    "Ask the personal questions aloud, in Arabic, one at a time; accept one-word answers from the phrase page. Scaffolded interaction comes before the notebook (SC-119): run C1 here."),
   ("Output", "The learner, alone — begun in class, finishable at home",
    ["Notebook p. 2–3 · اُكْتُبِ الْقِصَّةَ: «أَيْنَ مِفْتَاحِي؟» — eight frames, one line per frame, bank printed (Captions rung).",
     "Notebook p. 4 · اُكْتُبِ الْقِصَّةَ: «صُورَةُ رَزَان وَخَدِيجَة» — six frames; the three past forms are in the bank and copied.",
     "Notebook p. 5–6 · قِصَّتِي الْمُوَازِيَةُ — four swaps: the finder, the friend visited (from the p. 9 survey), where the key is kept, and who is at the door (drawn).",
     "Notebook p. 7 · قِصَّتِي — the location sentence produced: thing · preposition · place from a split bank. p. 8 · دَوْرِي — my key.",
     "Notebook p. 10 · هَلْ تَذْكُرُ؟ — the first real one: four Unit 1 faces and lines."],
    "The p. 9 survey was run in the previous phase; p. 5 uses its answers. A learner who missed it writes p. 5 from the phrase page's people."),
   ("Fuller communication and transfer", "The teacher facilitates — zero prep, no props",
    ["C3 · هٰذِهِ صَفْحَتِي! — the last line of p. 6, and the key poster on p. 8: show a partner, who asks one question.",
     "C4 · نُعِيدُ الْقِصَّةَ بِالصُّوَرِ — under the eight-frame strip (rich-cartoon frames live since Version 43); run it after both readings.",
     "Transfer — the same language in a new small situation: where a classmate keeps a thing; the way to another room."],
    "Everything here runs on pages the unit has already produced. At the Captions rung you cue each frame of C4 and the class supplies the language."),
  ],
  c3_example="«أَيْنَ مِفْتَاحُكَ؟» · «مَنْ عِنْدَ الْبَابِ؟»",
  notes=[]),
 dict(
  n=3, label="Unit 3", ar="الْوَحْدَةُ ٣", status="Frozen (revision 3, SC-135) · Gate B closed · illustrations and clips owed",
  r1=dict(key="unit-03", title="مَنْ عِنْدَهُ الْكُرَةُ؟", tense="present", frames=8),
  r2=dict(key="unit-03p", title="هَدِيَّةُ رَزَان", tense="past", frames=6),
  pictures="Not yet illustrated — strips print as empty numbered frames until Gate B freezes the texts (SC-113). No verified audio: there are no listening tasks.",
  flow=[
   ("Input", "The learner, alone",
    ["Digital · الْمُفْرَدَات — every core item met, recognised and met again in a sentence ({v1} tasks, planned sequence).",
     "Textbook · اُنْظُرْ وَاقْرَأْ! — the phrase page (B0): eighteen numbered phrases, each as the story prints it.",
     "The strips (8 + 6 frames) — pictures follow the Gate B freeze."],
    "Until the pictures land (after Gate B), phase 1 rests on the phrase page and the digital practice alone. No verified audio, so no listening tasks."),
   ("Reading", "The learner (the class may read together)",
    ["Reading 1 «مَنْ عِنْدَهُ الْكُرَةُ؟» — {w1} words, present narration — then: صَحٌّ أَمْ خَطَأٌ؟ أَرِنِي · مَنْ يَقُولُ؟ · أَجِبْ (the last two questions are invented) · نَفْسُ الْقِصَّةِ... وَ (Version A / B). Digital · الْقِرَاءَة ١ ({p1} tasks selected from {a1} generated).",
     "Reading 2 «هَدِيَّةُ رَزَان» — {w2} words, past narration, dialogue in the present — then: مَنْ يَقُولُ؟ · رَتِّبْ · الْآنَ أَمْ قَبْلُ؟. Digital · الْقِرَاءَة ٢ ({p2} tasks selected from {a2} generated)."],
    "Read cold. The family words are met inside the story before anyone names them; do not pre-teach the list."),
   ("Consolidation and scaffolded interaction", "The learner; then the class, with you facilitating",
    ["اِقْرَأْ. ثُمَّ اقْرَأْ. — the recombination page, ten texts.",
     "وَأَنْتَ؟ وَأَنْتِ؟ — Unit 3's ten personal questions, added to the cumulative set.",
     "The pop-up «Look — the ending says whose!» — the book's only English; proposed, confirmed at Gate B.",
     "C1 · اِسْأَلْ أَصْدِقَاءَكَ — notebook p. 9, find someone who has: «هَلْ عِنْدَكَ أَخٌ؟ · أُخْتٌ؟ · كُرَةٌ؟ · قِطٌّ؟» — asked of real classmates; its answers feed p. 5."],
    "Ask the personal questions in Arabic, one at a time. «مَنْ فِي بَيْتِكَ؟» takes any true answer, including «أَنَا وَأُمِّي» or «قِطٌّ» — nothing on any page requires a family shape. Scaffolded interaction comes before the notebook (SC-119): run C1 here."),
   ("Output", "The learner, alone — begun in class, finishable at home",
    ["Notebook p. 2–3 · اُكْتُبِ الْقِصَّةَ: «مَنْ عِنْدَهُ الْكُرَةُ؟» — eight frames, two slots per line, bank shuffled and over-full (Frames rung, first use).",
     "Notebook p. 4 · اُكْتُبِ الْقِصَّةَ: «هَدِيَّةُ رَزَان» — six frames; the past forms are in the bank and copied.",
     "Notebook p. 5–6 · قِصَّتِي الْمُوَازِيَةُ — the skeleton keeps only its verbs; the learner writes every noun phrase and one whole line, from the p. 9 survey and the p. 8 poster.",
     "Notebook p. 7 · قِصَّتِي — starters, no bank. p. 8 · دَوْرِي — my family, two lines and a drawing.",
     "Notebook p. 10 · هَلْ تَذْكُرُ؟ — four Unit 2 lines."],
    "This is the first unit with no bank on p. 5–7. Expect it to be slower; give the planned supports (the models row and the learner's own C1 grid) and let learners finish; the rung is set by design (Ladder §3), not by a sheet."),
   ("Fuller communication and transfer", "The teacher facilitates — zero prep, no props",
    ["C3 · هٰذِهِ صَفْحَتِي! — p. 6, and the family poster on p. 8 presented as a two-line exchange.",
     "C4 · نُعِيدُ الْقِصَّةَ بِالصُّوَرِ — under the eight-frame strip; learner-led, one picture each (Frames rung); after both readings.",
     "Transfer — the same language in a new small situation: who has what in another family; a gift for someone at school."],
    "The survey ran in phase 3, before p. 5. The poster is shared with a partner, not the whole class, unless the child wants to."),
  ],
  c3_example="«مَنْ هٰذَا؟» · «هَلْ عِنْدَكَ أَخٌ؟»",
  notes=[]),
]

PROCEDURES = {
 "C1": ("اِسْأَلْ أَصْدِقَاءَكَ", "Ask your friends — the survey (Phase 3, before the notebook)", [
   "Prepare first (SC-124): notebook open at p. 9. Ask the printed questions yourself, in Arabic, to three or four learners — holding up a real pen or list where it fits — and let each answer from the printed answers; then the class says each question with you. Do not translate.",
   "In pairs, learners ask each other every printed question once and answer from the printed answers. Then they stand, ask five classmates, write each name and tick ✓ or ✗ in each column.",
   "Stop when every grid has five names. Those names are used on p. 5, so this runs before the parallel story; a learner who missed it uses the printed class list on p. 5."]),
 "C3": ("هٰذِهِ صَفْحَتِي", "Share your page", [
   "In pairs. The learner holds up the finished page (p. 5–6 or the poster on p. 8) and says the printed line: «هٰذِهِ صَفْحَتِي!»",
   "The partner points to one thing on the page and asks one question from the unit's own set — for this unit, e.g. {c3ex}.",
   "Swap roles. If there is a wall, the pages go on it; nothing is marked."]),
 "C4": ("نُعِيدُ الْقِصَّةَ", "Story circle — the retell (Phase 5, after both readings)", [
   "Books open at the strip. Point to frame 1 and wait; the class says what happens — at the Captions rung you cue the frames, the class supplies the language.",
   "Write on the board only what the class says, as they say it. Do not supply or correct toward the printed text.",
   "Move to the next frame once a sentence has been said for this one. The story ends when the strip does."]),
}

# PILOT notes removed by SC-124 (2026-10-13): no pilot, observation or evaluation survey is part of the course.

# ---------- 3 · render ----------
_AR = re.compile(r'«?[\u0600-\u06FF][\u0600-\u06FF\s؟!،:\.]*[\u0600-\u06FF؟!\.]»?|«?[\u0600-\u06FF]»?')
def esc(s):
    """escape, then isolate every Arabic run so numbers and punctuation beside it keep their place"""
    return _AR.sub(lambda m: f'<bdi lang="ar" class="ar">{m.group(0)}</bdi>', html.escape(s))
def ar(s): return f'<bdi lang="ar" class="ar">{html.escape(s)}</bdi>'

def render_unit(u):
    m1, m2 = meta[u["r1"]["key"]], meta[u["r2"]["key"]]
    fill = dict(w1=m1["words"], w2=m2["words"], a1=m1["ok"], a2=m2["ok"], v1=m1["vocab"], p1=m1["reading"], p2=m2["reading"])
    out = [f'''
<section class="unit" id="unit-{u["n"]:02d}">
 <header class="uhead">
  <div class="eyebrow">Teacher · {esc(u["label"])} · {ar(u["ar"])}</div>
  <h2 dir="ltr">{ar(u["r1"]["title"])} <span class="sep">·</span> {ar(u["r2"]["title"])}</h2>
  <dl class="facts">
   <div><dt>Reading 1</dt><dd>{ar(u["r1"]["title"])} — {m1["words"]} words, {u["r1"]["tense"]} · {u["r1"]["frames"]} frames</dd></div>
   <div><dt>Reading 2</dt><dd>{ar(u["r2"]["title"])} — {m2["words"]} words, {u["r2"]["tense"]} · {u["r2"]["frames"]} frames</dd></div>
   <div><dt>Digital</dt><dd>{m1["ok"]} + {m2["ok"]} generated (QC clean); a learner's planned pathways select {m1["vocab"]} vocabulary + {m1["reading"]} reading-1 + {m2["reading"]} reading-2 tasks</dd></div>
   <div><dt>Pictures</dt><dd>{esc(u["pictures"])}</dd></div>
   <div><dt>Status</dt><dd>{esc(u["status"])}</dd></div>
  </dl>
 </header>

 <h3>The unit flow <small>five phases, in the order the course requires (meaning → reading → consolidation and scaffolded interaction → output → fuller communication and transfer; SC-119)</small></h3>
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
        if code == "C3" and u.get("c3_procedure"):           # SC-128: a unit may carry its own C3 use (Unit 1: the newcomer exchange)
            lines = u["c3_procedure"]; en = "Share your page — the newcomer exchange (Phase 5)"
        ls = "".join(f"<li>{esc(l.format(c3ex=u['c3_example']))}</li>" for l in lines)
        out.append(f'''
  <article class="proc"><header><span class="code">{code}</span><span class="rub">{ar(rub)}</span><span class="en">{esc(en)}</span></header><ol>{ls}</ol></article>''')
    out.append('</div>\n</section>')   # SC-124: the pilot-notes section is removed; nothing on this page records learners
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
.lines{height:54px;background:repeating-linear-gradient(to bottom,transparent 0 26px,var(--line) 26px 27px)}
footer{color:var(--mute);font-size:13px;margin-top:10px}
@media (max-width:560px){.phase{grid-template-columns:1fr}.tnote{grid-column:1}.facts dt{min-width:64px}}
@media print{body{background:#fff;color:#000;padding-inline:0}.unit{border:0;padding:0;page-break-after:always}.toc{display:none}.lines{height:72px}}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
</style>'''

body = [CSS, f'''
<div class="wrap">
 <header class="top"><span class="badge">Teacher</span><h1>Intaliq 1 · Teacher's pages</h1><span style="color:var(--mute)">Level 1 · MSA · ages 8–13</span></header>
 <p class="disc"><b>Not part of the student materials.</b> This page is for the person running the class. It is not linked from the student site and does not need to be hidden from learners: it holds no answers to anything (SC-048) — only the order of the unit and the three classroom procedures. Nothing on it asks you to prepare, print, cut or make anything.</p>
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

(HERE / "intaliq1_teacher_pages.artifact-body.html").write_text(page, encoding="utf-8")
print("built:", {k: (v["words"], v["ok"]) for k, v in meta.items()}, "bytes:", len(page.encode("utf-8")))
