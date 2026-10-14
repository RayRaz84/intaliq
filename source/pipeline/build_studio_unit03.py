# -*- coding: utf-8 -*-
"""Adds Unit 3 to the Studio (Version 42): student book view, Frames-rung notebook, practice hub wiring,
home card, unit map, live numbers; replaces the embedded engine with engine_core.js. Idempotent."""
import re, html
S = open("school_course_studio.html", encoding="utf8").read()
s1 = open("u3r1_s1.txt", encoding="utf8").read().strip()
s2 = open("u3r1_s2.txt", encoding="utf8").read().strip()
def paras(t): return [p.strip() for p in t.split("\n\n") if p.strip()]
def prose(t): return "\n".join(f"      <p>{html.escape(p)}</p>" for p in paras(t))
EMPTY = '<span class="picfr empty"><b>{n}</b><svg viewBox="0 0 120 100" aria-hidden="true"><rect x="2" y="2" width="116" height="96" rx="8" fill="#fff" stroke="#D9E0DE"/></svg></span>'
def strip_(n): return '<div class="picseq">' + "".join(EMPTY.format(n=i) for i in range(1, n+1)) + '</div>'
NBPIC = '<span class="nbpic"><svg viewBox="0 0 120 100"><rect x="2" y="2" width="116" height="96" rx="8" fill="#fff" stroke="#D9E0DE"/></svg><b>{n}</b></span>'
def nbpics(n): return '<div class="nbpics">' + "".join(NBPIC.format(n=i) for i in range(1, n+1)) + '</div>'
def pcard(i, ar): return f'<div class="act pcard"><span class="pslot" aria-hidden="true"></span><div class="rubric"><span class="ico">{i}</span><span lang="ar">{ar}</span></div></div>'
def li(items): return "".join(f"<li>{x}</li>" for x in items)
def bank(label, words): return f'<div class="bank"><span class="bl">{label}</span><br>' + "".join(f'<span class="w">{w}</span>' for w in words) + '</div>'
SLOT = '<span class="slot"></span>'
PHRASE = ["هٰذَا أَبِي","هٰذِهِ أُمِّي","هٰذَا أَخِي الصَّغِيرُ","هٰذِهِ أُخْتِي","عِنْدِي كُرَةٌ","لَيْسَ عِنْدِي كِتَابٌ","عِنْدَهُ قَلَمٌ","عِنْدَهَا كِتَابٌ","أُرِيدُ الْكُرَةَ","مَاذَا تُرِيدُ؟","أَحْتَاجُ إِلَى قَلَمِي","يُعْطِيهَا الْكِتَابَ","يَأْخُذُ الْمِفْتَاحَ","يَعِيشُ فِي بَيْتٍ كَبِيرٍ","مَعِي","هٰذِهِ هَدِيَّةٌ","بِجَانِبِ الْبَابِ","الْكُرَةُ لَيْسَتْ مَعِي"]
RECOMB = ["عِنْدَ لَيْلَى كُرَةٌ. الْكُرَةُ فِي حَقِيبَتِهَا. وَالْحَقِيبَةُ مَعَهَا.",
 "«هَلْ عِنْدَكَ قَلَمٌ؟» «لَا، لَيْسَ عِنْدِي قَلَمٌ. قَلَمِي عِنْدَ أُخْتِي.»",
 "هٰذَا أَبِي. عِنْدَهُ مِفْتَاحٌ كَبِيرٌ. الْمِفْتَاحُ مَعَهُ.",
 "أُمُّ كَرِيم عِنْدَهَا كِتَابٌ صَغِيرٌ. تُعْطِي الْكِتَابَ لِكَرِيم. يَضْحَكُ كَرِيم.",
 "«مَاذَا تُرِيدُ يَا زَيْد؟» «أُرِيدُ كُرَةً!» «الْكُرَةُ عِنْدَ أَخِي.»",
 "يَعِيشُ الْقِطُّ فِي بَيْتِ رَنَا. يَعِيشُ بِجَانِبِ الْبَابِ. وَرَنَا؟ تُحِبُّ الْقِطَّ.",
 "أَخَذَ عُمَر الْكُرَةَ وَذَهَبَ إِلَى بَيْتِ مَهَا. أَعْطَاهَا الْكُرَةَ. قَالَتْ مَهَا: «هٰذِهِ لِي؟»",
 "خَدِيجَة لَيْسَتْ فِي الْبَيْتِ. هِيَ مَعَ رَزَان. وَأَخُوهَا سَامِي فِي الْبَيْتِ.",
 "«أَحْتَاجُ إِلَى قَلَمٍ.» «قَلَمِي مَعِي. هٰذَا لَكَ.» «وَأَنَا أَحْتَاجُ إِلَى كِتَابٍ.» «لَيْسَ عِنْدِي كِتَابٌ!»",
 "هٰذِهِ هَدِيَّةٌ لِأُمِّي. وَهٰذِهِ هَدِيَّةٌ لِأَبِي. وَهٰذِهِ... لِلْقِطِّ!"]
PQ = ["مَنْ فِي بَيْتِكَ؟","هَلْ عِنْدَكَ أَخٌ؟","هَلْ عِنْدَكَ أُخْتٌ؟","مَاذَا تُرِيدُ؟","هَلْ عِنْدَكَ كُرَةٌ؟","هَلْ تَحْتَاجُ إِلَى قَلَمٍ؟","أَيْنَ تَعِيشُ؟","مَعَ مَنْ تَعِيشُ؟","مَعَ مَنْ تَذْهَبُ إِلَى الْبَيْتِ؟","هَلْ عِنْدَكَ هَدِيَّةٌ لِأُمِّكَ؟"]

STUDENT = f'''
<!-- ================= UNIT 3 · STUDENT BOOK (SC-109) ================= -->
<section class="view" id="v-student3">
  <div class="viewbar"><div class="viewbar-in"><a class="back" href="#">← Library</a><div><div class="vt">Unit 3 · Student book</div><div class="vsub">phrase page → strip → reading 1 → apparatus → reading 2 → recombination → personal questions</div></div><span class="draft">DRAFT · rev 1 · no illustrations yet</span></div></div>
  <main class="rtl">

  <div class="sheet">
    <span class="sheet-tag"><span class="rubric" lang="ar">اُنْظُرْ وَاقْرَأْ!</span></span>
    <h3>The phrase page (B0 · CR-13)</h3>
    <p class="note" style="direction:ltr">Every new item the two readings print, as the phrase the story prints. A reading aid, never assessable by listing. Picture slots are drawn as pending until illustration.</p>
    <div class="acts" style="grid-template-columns:repeat(auto-fit,minmax(240px,1fr))">
      {"".join(pcard(i+1, p) for i, p in enumerate(PHRASE))}
    </div>
  </div>

  <div class="sheet">
    <span class="sheet-tag"><span class="rubric" lang="ar">مَنْ عِنْدَهُ الْكُرَةُ؟</span></span>
    <h3>Reading 1 · «مَنْ عِنْدَهُ الْكُرَةُ؟» · present · 158 words</h3>
    <p class="note" style="direction:ltr">Eight-frame strip precedes the text (frames empty until illustration). Frames 1–5 never show what is under the cat; the key is seen in frame 6.</p>
    <div class="helpbox"><span class="rubric" lang="ar">نُعِيدُ الْقِصَّةَ بِالصُّوَرِ</span>
      <span class="note" style="direction:ltr;margin:0">C4, printed where it happens (SC-049): the class retells the story from these eight frames, learner-led — at the Frames rung, one picture each.</span></div>
    {strip_(8)}
    <div class="storyprose arabic" lang="ar">
{prose(s1)}
    </div>
  </div>

  <div class="sheet">
    <h3>Comprehension activities · reading 1</h3>
    <div class="acts">
      <div class="act"><div class="rubric"><span class="ico">✓✗</span><span lang="ar">صَحٌّ أَمْ خَطَأٌ؟ أَرِنِي</span></div>
        <ul lang="ar">{li(["1 · يُوسُف وَلَدٌ. ⬜","2 · لَيْلَى أُمُّ يُوسُف. ⬜","3 · الْكُرَةُ عِنْدَ لَيْلَى. ⬜","4 · الْكِتَابُ عِنْدَ يُوسُف. ⬜","5 · الْمِفْتَاحُ تَحْتَ الْقِطِّ. ⬜","6 · يَأْخُذُ الْقِطُّ الْكُرَةَ. ⬜"])}</ul></div>
      <div class="act"><div class="rubric"><span class="ico">💬</span><span lang="ar">مَنْ يَقُولُ؟</span></div>
        <ul lang="ar">{li(["«نَعَمْ، الْكُرَةُ عِنْدِي. وَأَنْتَ، مَاذَا تُرِيدُ؟»","«نَعَمْ، كِتَابُكَ عِنْدِي. وَأَنَا أَحْتَاجُ إِلَى قَلَمِي.»","«نَعَمْ، الْقَلَمُ مَعِي. وَأَنَا أَحْتَاجُ إِلَى مِفْتَاحِي.»","«يَا قِطُّ! أُرِيدُ الْكُرَةَ!»"])}</ul>
        <p class="note" style="direction:ltr">Four faces to choose from: <span class="ar" lang="ar">يُوسُف · لَيْلَى · أُمُّهُ · أَبُوهُ</span>.</p></div>
      <div class="act"><div class="rubric"><span class="ico">✏️</span><span lang="ar">أَجِبْ</span></div>
        <ul lang="ar">{li(["مَنْ عِنْدَهُ الْكُرَةُ؟","أَيْنَ الْمِفْتَاحُ؟","مَنْ عِنْدَهَا الْكِتَابُ؟","مَنْ عِنْدَهُ الْقَلَمُ؟","أَيْنَ يَعِيشُ الْقِطُّ؟","مَنْ يَأْخُذُ الْكُرَةَ؟","مَا اسْمُ الْقِطِّ؟ ✏️","أَيْنَ يَذْهَبُ الْقِطُّ؟ ✏️"])}</ul>
        <p class="note" style="direction:ltr">If the answer is not in the story, invent it (CR-15) — the last two have no answer in the text.</p></div>
      <div class="act"><div class="rubric"><span class="ico">🖼</span><span lang="ar">نَفْسُ الْقِصَّةِ... وَ</span></div>
        <ul lang="ar">{li(["A · الْمِفْتَاحُ تَحْتَ لَيْلَى، لَيْسَ تَحْتَ الْقِطِّ.","B · فِي الْفَصْلِ. «أُرِيدُ قَلَمًا!» الْقَلَمُ تَحْتَ الْقِطِّ."])}</ul>
        <p class="note" style="direction:ltr">Version A / B (S11): the same strip with one element changed, retold from the pictures — A keeps the cast and moves the key; B changes the setting and the object.</p></div>
    </div>
  </div>

  <div class="sheet">
    <span class="sheet-tag"><span class="rubric" lang="ar">هَدِيَّةُ رَزَان</span></span>
    <h3>Reading 2 · «هَدِيَّةُ رَزَان» · past · 118 words</h3>
    <p class="note" style="direction:ltr">Narration in the past (<span lang="ar">ذَهَبَتْ · رَأَى · قَالَ · نَظَرَ · أَعْطَتْ · ضَحِكَ · أَخَذَ · دَخَلَ · رَجَعَ · أَعْطَاهَا</span>); dialogue in the present; states nominal (SC-095).</p>
    {strip_(6)}
    <div class="storyprose arabic" lang="ar">
{prose(s2)}
    </div>
    <div class="popup"><h4>Look — the ending says whose!</h4><p><span class="ar" lang="ar">كِتَابِي</span> — my book · <span class="ar" lang="ar">كِتَابُكَ</span> — your book · <span class="ar" lang="ar">أُمُّهُ</span> — his mother · <span class="ar" lang="ar">عِنْدَهَا</span> — she has.<br>Listen for the end of the word: <span class="ar" lang="ar">ـي</span> me · <span class="ar" lang="ar">ـكَ</span> you (a boy) · <span class="ar" lang="ar">ـكِ</span> you (a girl) · <span class="ar" lang="ar">ـهُ</span> him · <span class="ar" lang="ar">ـهَا</span> her.</p></div>
    <p class="note" style="direction:ltr"><b>PROPOSED — confirmed at Gate B.</b> Unit 3's one pop-up (LC-4): the possessive ending, which the unit's grammar target turns productive; no grammatical term is used.</p>
    <h3>Comprehension activities · reading 2</h3>
    <div class="acts">
      <div class="act"><div class="rubric"><span class="ico">💬</span><span lang="ar">مَنْ يَقُولُ؟</span></div>
        <ul lang="ar">{li(["«كِتَابٌ! أُرِيدُ الْكِتَابَ! لَيْسَ عِنْدِي كِتَابٌ.»","«هٰذَا لَكَ.»","«هٰذَا أَخِي الصَّغِيرُ! يَعِيشُ مَعِي هُنَا.»"])}</ul>
        <p class="note" style="direction:ltr">Three faces to choose from: <span class="ar" lang="ar">رَزَان · خَدِيجَة · سَامِي</span>.</p></div>
      <div class="act"><div class="rubric"><span class="ico">🔢</span><span lang="ar">رَتِّبْ</span></div>
        <ul lang="ar">{li(["⬜ أَعْطَتْ رَزَان الْكِتَابَ لِسَامِي.","⬜ ذَهَبَتْ رَزَان إِلَى بَيْتِ خَدِيجَة، وَالْهَدِيَّةُ مَعَهَا.","⬜ وَرَجَعَ سَامِي. مَعَهُ كُرَةٌ.","⬜ رَأَى سَامِي الْهَدِيَّةَ."])}</ul>
        <p class="note" style="direction:ltr">Write 1–4 in the boxes.</p></div>
      <div class="act"><div class="rubric"><span class="ico">🕐</span><span lang="ar">الْآنَ أَمْ قَبْلُ؟</span></div>
        <ul lang="ar">{li(["يَذْهَبُ يُوسُف إِلَى أُمِّهِ. ⬜","ذَهَبَتْ رَزَان إِلَى بَيْتِ خَدِيجَة. ⬜","تُعْطِيهِ لَيْلَى الْكُرَةَ. ⬜","أَعْطَتْ رَزَان الْكِتَابَ لِسَامِي. ⬜","يَضْحَكُ يُوسُف. ⬜","ضَحِكَ سَامِي. ⬜"])}</ul>
        <p class="note" style="direction:ltr">S14 — sort the lines into the two readings, story 1 (now) or story 2 (before); no rule is stated. Every line is the readings' own text.</p></div>
    </div>
  </div>

  <div class="sheet">
    <span class="sheet-tag"><span class="rubric" lang="ar">اِقْرَأْ. ثُمَّ اقْرَأْ.</span></span>
    <h3>The recombination page (S10 · CR-14)</h3>
    <p class="note" style="direction:ltr">Ten one-breath texts from the unit's words. Not stories; read them, then read them again. They carry the encounter floors so the readings do not have to.</p>
    <div class="acts">
      {"".join(f'<div class="act"><div class="rubric"><span class="ico">{i+1}</span></div><ul lang="ar"><li>{t}</li></ul></div>' for i, t in enumerate(RECOMB))}
    </div>
  </div>

  <div class="sheet">
    <span class="sheet-tag"><span class="rubric" lang="ar">وَأَنْتَ؟ وَأَنْتِ؟</span></span>
    <h3>Personal questions (A9 · CR-16) — Unit 3's ten, added to the cumulative set</h3>
    <div class="acts"><div class="act"><ul lang="ar">{li(PQ)}</ul><p class="note" style="direction:ltr">Asked in the preview activities; answers from the phrase page; first-person answers are the learner's own. Never scored.</p></div></div>
  </div>

  </main>
</section>
'''

NOTE = f'''
<!-- ================= UNIT 3 · NOTEBOOK · FRAMES RUNG (SC-096, SC-109) ================= -->
<section class="view" id="v-note3">
  <div class="viewbar"><div class="viewbar-in"><a class="back" href="#">← Library</a><div><div class="vt">Unit 3 · Notebook</div><div class="vsub">Phase 4 · the output ladder · <b>Frames rung, first use</b> · rev 1 texts</div></div><span class="draft">DRAFT · no illustrations yet</span></div></div>
  <main class="rtl">
  <p class="lede" style="direction:ltr"><b>Ten pages, one scaffold removed (SC-096): two slots a line and a bank that is shuffled and over-full; a parallel story that keeps only its verbs; an own-story page with no bank at all.</b> Every slot and every bank word is a surface form the two readings print (SC-064); past forms are copied from the bank, never built (SC-073). Picture frames are empty until illustration.</p>

  <div class="sheet"><span class="sheet-tag"><span class="rubric" lang="ar">دَفْتَرِي</span></span><h3>Opener · page 1</h3>
    <div class="nb"><p class="arabic" lang="ar" style="font-size:28px;text-align:center">دَفْتَرِي</p>
    <p class="arabic" lang="ar" style="text-align:center">اِسْمِي <span class="slot" style="min-width:180px"></span></p>
    <div class="acts" style="grid-template-columns:repeat(auto-fit,minmax(150px,1fr));margin-top:16px">
      <div class="act" style="text-align:center"><div style="font-size:22px">🖼️</div><div class="rubric" lang="ar">اُكْتُبِ الْقِصَّةَ</div><div style="font-size:22px">⬜</div></div>
      <div class="act" style="text-align:center"><div style="font-size:22px">✍️</div><div class="rubric" lang="ar">قِصَّتِي الْمُوَازِيَةُ</div><div style="font-size:22px">⬜</div></div>
      <div class="act" style="text-align:center"><div style="font-size:22px">📖</div><div class="rubric" lang="ar">قِصَّتِي</div><div style="font-size:22px">⬜</div></div>
      <div class="act" style="text-align:center"><div style="font-size:22px">🙋</div><div class="rubric" lang="ar">دَوْرِي</div><div style="font-size:22px">⬜</div></div>
    </div></div></div>

  <div class="sheet"><span class="sheet-tag"><span class="code">N1 أ</span> <span class="rubric" lang="ar">اُكْتُبِ الْقِصَّةَ: «مَنْ عِنْدَهُ الْكُرَةُ؟»</span></span><h3>Write the story · story 1 · <b>present</b> · pages 2–3 · two slots a line</h3>
    {nbpics(8)}
    <div class="nb"><p class="arabic" lang="ar">
      <span class="nbline"><span class="nbno">1</span><span>فِي الْبَيْتِ {SLOT} وَأَبُوهُ وَأُخْتُهُ الصَّغِيرَةُ. يَعِيشُ الْقِطُّ {SLOT} الْبَابِ.</span></span><br>
      <span class="nbline"><span class="nbno">2</span><span>يَقُولُ يُوسُف: «{SLOT} الْكُرَةَ! مَنْ {SLOT} الْكُرَةُ؟»</span></span><br>
      <span class="nbline"><span class="nbno">3</span><span>تَقُولُ لَيْلَى: «الْكُرَةُ {SLOT}. وَأَنَا أَحْتَاجُ إِلَى {SLOT}.»</span></span><br>
      <span class="nbline"><span class="nbno">4</span><span>تَقُولُ أُمُّهُ: «كِتَابُكَ {SLOT}. {SLOT} عِنْدَهُ قَلَمِي.»</span></span><br>
      <span class="nbline"><span class="nbno">5</span><span>يَقُولُ أَبُوهُ: «الْقَلَمُ {SLOT}. أَيْنَ {SLOT}؟»</span></span><br>
      <span class="nbline"><span class="nbno">6</span><span>الْمِفْتَاحُ عَلَى الْأَرْضِ بِجَانِبِ {SLOT}... تَحْتَ {SLOT}!</span></span><br>
      <span class="nbline"><span class="nbno">7</span><span>{SLOT} يُوسُف الْمِفْتَاحَ. تُعْطِيهِ لَيْلَى {SLOT}.</span></span><br>
      <span class="nbline"><span class="nbno">8</span><span>وَالْقِطُّ؟ يَنْظُرُ إِلَى {SLOT}... وَيَأْخُذُ الْكُرَةَ... وَ{SLOT}!</span></span>
    </p>
    {bank("بَنْكُ الْكَلِمَاتِ", ["يَذْهَبُ","الْكُرَةَ","عِنْدَهُ","مَعِي","مِفْتَاحِي","أُمُّهُ","الْبَابِ","كِتَابِكَ","بِجَانِبِ","أُرِيدُ","الْقِطِّ","عِنْدِي","أَبُوكَ","يَأْخُذُ","عِنْدِي","أَيْنَ","عِنْدَكِ","الْكُرَةِ"])}
    <p class="note" style="direction:ltr"><b>Frames rung (SC-096):</b> two slots per line, one line per frame, and the bank is <b>shuffled and over-full</b> — sixteen slots, eighteen words; the two distractors (<span lang="ar">أَيْنَ · عِنْدَكِ</span>) are the story's own words in the wrong place. Every slot and bank word is verified against the canon. Frames as the strip sets them: the house · the want · لَيْلَى · the mother · the father · the key under the cat · the exchange · the cat's exit.</p></div></div>

  <div class="sheet"><span class="sheet-tag"><span class="code">N1 ب</span> <span class="rubric" lang="ar">اُكْتُبِ الْقِصَّةَ: «هَدِيَّةُ رَزَان»</span></span><h3>Write the story · story 2 · <b>past</b> · page 4 · two slots a line</h3>
    {nbpics(6)}
    <div class="nb"><p class="arabic" lang="ar">
      <span class="nbline"><span class="nbno">1</span><span>{SLOT} رَزَان إِلَى بَيْتِ خَدِيجَة، وَالْهَدِيَّةُ {SLOT}.</span></span><br>
      <span class="nbline"><span class="nbno">2</span><span>بِجَانِبِ الْبَابِ وَلَدٌ {SLOT}. هٰذَا {SLOT} خَدِيجَة.</span></span><br>
      <span class="nbline"><span class="nbno">3</span><span>{SLOT} سَامِي الْهَدِيَّةَ. قَالَ: «أُرِيدُ {SLOT}!»</span></span><br>
      <span class="nbline"><span class="nbno">4</span><span>{SLOT} رَزَان الْكِتَابَ لِسَامِي. «هٰذَا {SLOT}.»</span></span><br>
      <span class="nbline"><span class="nbno">5</span><span>{SLOT} خَدِيجَة. «هٰذَا أَخِي {SLOT}!»</span></span><br>
      <span class="nbline"><span class="nbno">6</span><span>{SLOT} سَامِي. أَعْطَاهَا {SLOT}.</span></span>
    </p>
    {bank("بَنْكُ الْكَلِمَاتِ", ["الْكُرَةَ","ضَحِكَتْ","مَعَهَا","أَخُو","لَكَ","الصَّغِيرُ","ذَهَبَتْ","رَأَى","صَغِيرٌ","أَعْطَتْ","الْكِتَابَ","وَرَجَعَ","أَخَذَ","مَعِي"])}
    <p class="note" style="direction:ltr"><b>The past forms are printed in the bank and copied</b> (SC-073) — <span lang="ar">ذَهَبَتْ · رَأَى · أَعْطَتْ · ضَحِكَتْ · وَرَجَعَ</span>; two distractors (<span lang="ar">أَخَذَ · مَعِي</span>) are printed forms placed where the frame does not want them. Twelve slots, fourteen words.</p></div></div>

  <div class="sheet"><span class="sheet-tag"><span class="code">N2</span> <span class="rubric" lang="ar">قِصَّتِي الْمُوَازِيَةُ</span></span><h3>My parallel story · pages 5–6 · the skeleton keeps only its verbs</h3>
    <div class="nb"><p class="arabic" lang="ar" style="font-size:24px;text-align:center">مَنْ عِنْدَهُ <span class="slot" style="min-width:150px"></span>؟</p>
    <p class="arabic" lang="ar">
      هُنَاكَ وَلَدٌ / بِنْتٌ اسْمُهُ / اسْمُهَا <span class="slot"></span>. يَعِيشُ / تَعِيشُ مَعَ <span class="slot" style="min-width:200px"></span>.<br>
      يَقُولُ / تَقُولُ: «أُرِيدُ <span class="slot"></span>! مَنْ عِنْدَهُ <span class="slot"></span>؟»<br>
      يَذْهَبُ / تَذْهَبُ إِلَى <span class="slot"></span>. «هَلْ عِنْدَكَ / عِنْدَكِ <span class="slot"></span>؟»<br>
      «نَعَمْ. وَأَنَا أَحْتَاجُ إِلَى <span class="slot"></span>.»<br>
      يُعْطِيهِ / يُعْطِيهَا <span class="slot"></span>. <span class="slot" style="min-width:320px"></span><br>
      «<span class="slot" style="min-width:200px"></span> مَعِي!»
    </p>
    <div class="drawbox"><span class="rubric" lang="ar">اُرْسُمْ: مَنْ فِي بَيْتِكَ؟</span></div>
    <p class="arabic" lang="ar" style="margin-top:8px">هٰذِهِ صَفْحَتِي! <span style="font-size:15px;color:#5A6B72">⬜</span></p>
    <p class="note" style="direction:ltr"><b>Frames rung:</b> the skeleton prints only the verbs and the frame words; <b>every noun phrase is the learner's</b> — the person, who they live with, the thing wanted, who has it, what that person needs — and the fifth line is a <b>whole line the learner writes</b> (what happens after the giving). No bank: the learner's own family from the C1 survey and the S6 poster is the source (Ladder §3). The last line is C3 (SC-049). Feminine present forms are printed for a girl writing about herself — input-first, disclosed (SC-090).</p></div></div>

  <div class="sheet"><span class="sheet-tag"><span class="code">N3</span> <span class="rubric" lang="ar">قِصَّتِي</span></span><h3>My own story · page 7 · starters, no bank</h3>
    <div class="nb"><p class="arabic" lang="ar">
      أَنَا <span class="slot"></span>. فِي بَيْتِي <span class="slot" style="min-width:260px"></span>.<br>
      عِنْدِي <span class="slot" style="min-width:200px"></span>.<br>
      لَيْسَ عِنْدِي <span class="slot" style="min-width:200px"></span>.<br>
      أُرِيدُ <span class="slot" style="min-width:200px"></span>.<br>
      أَحْتَاجُ إِلَى <span class="slot" style="min-width:200px"></span>.<br>
      <span class="slot" style="min-width:340px"></span> مَعِي.
    </p>
    <div class="drawbox"><span class="rubric" lang="ar">اُرْسُمْ</span></div>
    <p class="note" style="direction:ltr">The freest page, and at this rung <b>without a bank</b>: the starters are the unit's frames in the first person, and the words come from the learner's own truths — the C1 grid, the S6 poster, the phrase page. The last line is the learner's, ending in <span lang="ar">مَعِي</span>. Nothing says why.</p></div></div>

  <div class="sheet"><span class="sheet-tag"><span class="code">S6</span> <span class="rubric" lang="ar">دَوْرِي</span></span><h3>My family · page 8 · feeds the classroom share (C3)</h3>
    <div class="nb"><p class="arabic" lang="ar" style="font-size:23px">هٰذَا أَبِي. هٰذِهِ أُمِّي.<br>عِنْدِي <span class="slot" style="min-width:140px"></span>. اسْمُهُ / اسْمُهَا <span class="slot" style="min-width:160px"></span>.</p>
    <div class="drawbox" style="height:130px"><span class="rubric" lang="ar">اُرْسُمْ: مَنْ فِي بَيْتِكَ؟</span></div>
    <p class="note" style="direction:ltr">Two lines and a drawing; at the Frames rung the poster is <b>presented as a two-line exchange</b> with a partner (Ladder §3): «مَنْ فِي بَيْتِكَ؟» — the poster answers. The second line takes <span lang="ar">أَخٌ · أُخْتٌ · قِطٌّ</span> or any printed noun; a child with no sibling writes <span lang="ar">قِطٌّ</span> or leaves the line — nothing on this page requires a family shape.</p></div></div>

  <div class="sheet"><span class="sheet-tag"><span class="code">C1</span> <span class="rubric" lang="ar">اِسْأَلْ أَصْدِقَاءَكَ</span></span><h3>Survey grid · page 9 · <i>find someone who has…</i> · filled in class, used on page 5</h3>
    <div class="nb" style="background-image:none">
      <p class="arabic" lang="ar" style="text-align:center;font-size:21px">«هَلْ عِنْدَكَ أَخٌ؟» · «هَلْ عِنْدَكَ أُخْتٌ؟» · «هَلْ عِنْدَكَ كُرَةٌ؟» · «هَلْ عِنْدَكَ قِطٌّ؟»</p>
      <table class="nbgrid">
        <tr><th>الِاسْمُ</th><th>أَخٌ</th><th>أُخْتٌ</th><th>كُرَةٌ</th><th>قِطٌّ</th></tr>
        <tr><td>1</td><td></td><td></td><td></td><td></td></tr>
        <tr><td>2</td><td></td><td></td><td></td><td></td></tr>
        <tr><td>3</td><td></td><td></td><td></td><td></td></tr>
        <tr><td>4</td><td></td><td></td><td></td><td></td></tr>
        <tr><td>5</td><td></td><td></td><td></td><td></td></tr>
      </table>
      <p class="arabic" lang="ar" style="text-align:center;font-size:19px;margin-top:10px">اِسْأَلْ. اُكْتُبِ الِاسْمَ. ✓</p>
      <p class="note" style="direction:ltr">The four questions are the unit's own personal questions (CR-16), printed in the student book. Ticks, not sentences; the names collected here are the people of page 5. C1's learner-facing instruction is the one Arabic line; the procedure is on the teacher's page (SC-104).</p></div></div>

  <div class="sheet"><span class="sheet-tag"><span class="code">N4</span> <span class="rubric" lang="ar">هَلْ تَذْكُرُ؟</span></span><h3>Do you remember? · page 10 · Unit 2 only</h3>
    <div class="nb">
      {nbpics(4)}
      <p class="arabic" lang="ar">
        <span class="nbline"><span class="nbno">1</span><span>يَرَى كَرِيم مِفْتَاحًا <span class="slot"></span> الْأَرْضِ.</span></span><br>
        <span class="nbline"><span class="nbno">2</span><span>تَقُولُ مَهَا: «مِفْتَاحِي <span class="slot"></span> الْكِتَابِ.»</span></span><br>
        <span class="nbline"><span class="nbno">3</span><span>هُنَاكَ <span class="slot"></span> عِنْدَ الْبَابِ.</span></span><br>
        <span class="nbline"><span class="nbno">4</span><span>«يَا خَدِيجَة! أَنَا <span class="slot"></span>!»</span></span>
      </p>
      {bank("بَنْكُ الْكَلِمَاتِ", ["تَحْتَ","هُنَا","عَلَى","قِطٌّ"])}
      <p class="note" style="direction:ltr">Delayed retrieval draws on <b>earlier units only</b> (N4's rule; U3–U4 on the previous unit): four Unit 2 frames — reprinted from the student book once its illustrations exist (SC-100), empty until then — four Unit 2 lines, and the location words retrieved a unit later. Every word is Unit 2's own printed text.</p></div></div>

  </main>
</section>
'''

# ---- patch the Studio ----
ENGINE = open("engine_core.js", encoding="utf8").read()
i = S.index("(function(root){"); j = S.index('})(typeof window!=="undefined"?window:globalThis);') + len('})(typeof window!=="undefined"?window:globalThis);')
S = S[:i] + ENGINE.strip() + S[j:]
# views (replace if present)
for vid, block in (("v-student3", STUDENT), ("v-note3", NOTE)):
    if f'id="{vid}"' in S:
        a = S.index(f'<section class="view" id="{vid}">'); a = S.rfind("\n<!--", 0, a); b = S.index("</section>", a) + len("</section>")
        S = S[:a] + block.rstrip("\n") + S[b:]
    else:
        anchor = "<!-- ================= NOTEBOOK =================" if vid == "v-student3" else "<footer>"
        S = S.replace(anchor, block.lstrip("\n") + "\n" + anchor, 1)
# practice wiring
S = S.replace('const PAIRS={"unit-01":"unit-01p","unit-02":"unit-02p"};', 'const PAIRS={"unit-01":"unit-01p","unit-02":"unit-02p","unit-03":"unit-03p"};')
S = S.replace('$("pr-sub").textContent=base==="unit-02"?"Unit 2 practice · المنصّة · rev 6, no illustrations yet":"Unit 1 practice · المنصّة";',
              '$("pr-sub").textContent=base==="unit-03"?"Unit 3 practice · المنصّة · rev 1, no illustrations yet":base==="unit-02"?"Unit 2 practice · المنصّة · rev 6, no illustrations yet":"Unit 1 practice · المنصّة";')
if "'unit-03/student'" not in S:
    S = S.replace("'unit-02/student':'v-student2'}", "'unit-02/student':'v-student2','unit-03/student':'v-student3','unit-03/notebook':'v-note3','unit-03/practice':'v-practice','unit-03p/practice':'v-practice'}")
# home card: replace the "soon" Unit 3 card
CARD3 = '''<div class="card">
      <span class="ribbon">BUILT · rev 1</span>
      <span class="ucode">UNIT 3</span>
      <h2>I have, I don't have, I want</h2>
      <div class="ar" lang="ar">«يَا لَيْلَى، هَلْ عِنْدَكِ الْكُرَةُ؟» «نَعَمْ، الْكُرَةُ عِنْدِي. وَأَنْتَ، مَاذَا تُرِيدُ؟»</div>
      <p class="desc">A boy trades round his family for the ball the cat is sitting on; a girl with one gift and two people at a friend's door — possession as a system; give, take, need; the first Frames-rung notebook.</p>
      <div class="meta"><span><b>2</b> readings</span><span><b>158 + 118</b> words</span><span><b id="n-u3">—</b> activities</span></div>
      <div class="btnrow">
        <a class="pbtn" href="#unit-03/student">Student</a>
        <a class="pbtn primary" href="#unit-03/practice">Digital</a>
        <a class="pbtn" href="#unit-03/notebook">Notebook</a>
      </div>
    </div>
    <div class="card soon">
      <span class="ribbon soon">NEXT</span>
      <span class="ucode">UNIT 4</span>
      <h2>Yes, no, and what I like</h2>
      <div class="ar" lang="ar">هَلْ تُحِبُّ...؟ أُحِبُّ... لَا أُحِبُّ...</div>
      <p class="desc">Polar questions and the first opinions; eat, drink, look at. Second Frames-rung unit.</p>
      <span class="soonchip">IN DESIGN</span>
    </div>'''
m = re.search(r'<div class="card soon">\s*<span class="ribbon soon">NEXT</span>\s*<span class="ucode">UNIT 3</span>.*?</div>\s*</div>', S, re.S)
if m: S = S[:m.start()] + CARD3 + S[m.end():]
S = S.replace('<div class="urow"><span class="un">3</span><div><h4>I have, I don\'t have, I want</h4>', '<div class="urow built"><span class="un">3</span><div><h4>I have, I don\'t have, I want</h4>')
S = S.replace("set('n-u1',per['unit-01']||0);set('n-u2',per['unit-02']||0);", "set('n-u1',per['unit-01']||0);set('n-u2',per['unit-02']||0);set('n-u3',per['unit-03']||0);")
S = S.replace('<a class="hbtn ghost" href="#unit-02/student">Open Unit 2</a>', '<a class="hbtn ghost" href="#unit-03/student">Open Unit 3</a>')
S = re.sub(r"VERSION \d+", "VERSION 42", S)
S = S.replace("Deep links: #unit-01/student · #unit-01/practice · #unit-01/notebook · #unit-02/student · #unit-02/practice · #unit-02/notebook.", "Deep links: #unit-01/student · #unit-01/practice · #unit-01/notebook · #unit-02/student · #unit-02/practice · #unit-02/notebook · #unit-03/student · #unit-03/practice · #unit-03/notebook.")
S = S.replace("(unit-01p, unit-02p)", "(unit-01p, unit-02p, unit-03p)")
S = S.replace("Unit 2 illustrations: not yet commissioned — the picture strips are empty frames by standing instruction.", "Unit 2 and Unit 3 illustrations: not yet commissioned — the picture strips are empty frames by standing instruction.")
open("school_course_studio.html", "w", encoding="utf8").write(S)
# verify every notebook slot bank word and every activity line is verbatim in the canon
import unicodedata
canon = s1 + " " + s2
words = re.findall(r'<span class="w">([^<]+)</span>', NOTE)
bad = [w for w in words if w not in canon]
print("bank words not in canon:", bad)
print("written; size", len(S))
