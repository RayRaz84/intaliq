# -*- coding: utf-8 -*-
# Unit 3 engine data (SC-109) — built from the revision-1 texts; no illustrations (img:None) by standing instruction.
import re, json
s1=open("u3r1_s1.txt",encoding="utf8").read().strip()
s2=open("u3r1_s2.txt",encoding="utf8").read().strip()
PUNCT=r"[«»\"،.!؟:\-…]"
def toks(t): return [w for w in re.sub(PUNCT," ",t).split() if w]
def paras(t): return [p.strip() for p in t.split("\n\n") if p.strip()]

# id -> (lemma, status, kind, gloss, dim, img, candidate surface forms, extra)
# N=NEW_CORE_TARGET R=RECYCLED_CORE_TARGET S=COMPREHENSIBLE_SUPPORT G=RECOGNITION_ONLY
ITEMS = {
 # Unit 3 new core (band 5, SC-109)
 "umm":    ("أُمّ","N","lemma","mother","person",None,["أُمِّي","أُمُّهُ","أُمِّهِ","أُمُّ","لِأُمِّي","لِأُمِّكَ"],{"chunk_ref":"CH-24"}),
 "ab":     ("أَب","N","lemma","father","person",None,["أَبِي","أَبُوهُ","أَبُوكَ","لِأَبِي"],{"chunk_ref":"CH-24"}),
 "ukht":   ("أُخْت","N","lemma","sister","person",None,["أُخْتُهُ","أُخْتِهِ","أُخْتِي","أُخْتٌ"],{"chunk_ref":"CH-24"}),
 "akh":    ("أَخ","N","lemma","brother","person",None,["أَخُو","أَخُوكِ","أَخِي","أَخُوهَا","أَخٌ"],{"chunk_ref":"CH-24"}),
 "maa":    ("مَعَ","N","lemma","with","possession",None,["مَعِي","مَعَهَا","مَعَهُ","مَعَ"],{"chunk_ref":"CH-25"}),
 # possession system — productive from this unit (promotions, SC-109)
 "inda":   ("عِنْدَ","N","lemma","has / have","possession",None,["عِنْدِي","عِنْدَكَ","عِنْدَكِ","عِنْدَهُ","عِنْدَهَا","عِنْدَ"],{"chunk_ref":"CH-21"}),
 "laysa":  ("لَيْسَ","N","lemma","is not / has no","polarity",None,["لَيْسَ","لَيْسَتْ","وَلَيْسَ"],{"chunk_ref":"CH-05"}),
 "li":     ("لِـ","N","lemma","for (you / me)","possession",None,["لَكَ","لَكِ","لِي","لِخَدِيجَة","لِسَامِي","لِكَرِيم","لِلْقِطِّ"],{}),
 # target verbs (verb track)
 "aata":   ("أَعْطَى","N","lemma","gives / gave","action",None,["يُعْطِيهِ","وَيُعْطِيهِ","يُعْطِيهَا","وَيُعْطِيهَا","تُعْطِيهِ","تُعْطِي","أَعْطَتْ","أَعْطَاهَا"],{}),
 "akhadha":("أَخَذَ","N","lemma","takes / took","action",None,["يَأْخُذُ","وَيَأْخُذُ","أَخَذَ","وَأَخَذَ"],{}),
 "ihtaja": ("اِحْتَاجَ","N","lemma","needs","action",None,["أَحْتَاجُ","تَحْتَاجُ"],{"chunk_ref":"CH-23"}),
 "aasha":  ("عَاشَ","N","lemma","lives","action",None,["يَعِيشُ","تَعِيشُ"],{}),
 "arada":  ("أَرَادَ","R","lemma","wants","action",None,["أُرِيدُ","تُرِيدُ"],{"chunk_ref":"CH-22"}),
 # recycled core
 "ayna":   ("أَيْنَ","R","lemma","where?","question",None,["أَيْنَ"],{}),
 "fi":     ("فِي","R","lemma","in","place",None,["فِي","وَفِي"],{}),
 "ala":    ("عَلَى","R","lemma","on","place",None,["عَلَى"],{}),
 "tahta":  ("تَحْتَ","R","lemma","under","place",None,["تَحْتَ"],{}),
 "huna":   ("هُنَا","R","lemma","here","place",None,["هُنَا"],{}),
 "hunaka": ("هُنَاكَ","R","lemma","there is / there","existence",None,["هُنَاكَ"],{}),
 "dhahab": ("ذَهَبَ","R","lemma","goes / went","action",None,["يَذْهَبُ","وَيَذْهَبُ","ذَهَبَتْ"],{"chunk_ref":"CH-18"}),
 "ila":    ("إِلَى","R","lemma","to","place",None,["إِلَى"],{}),
 "rajaa":  ("رَجَعَ","R","lemma","comes back / came back","action",None,["يَرْجِعُ","رَجَعَ","وَرَجَعَ","رَجَعَتْ","وَرَجَعَتْ"],{}),
 "walad":  ("وَلَد","R","lemma","a boy","person",None,["وَلَدٌ"],{}),
 "ism":    ("اِسْم","R","lemma","a name","object",None,["اسْمُهُ","وَاسْمُهُ"],{}),
 "yara":   ("رَأَى","R","lemma","sees / saw","action","vg-see",["رَأَى"],{}),
 "yaqul":  ("قَالَ","R","lemma","says / said","action","vg-say",["يَقُولُ","تَقُولُ","قَالَ","قَالَتْ"],{}),
 "yadkhul":("دَخَلَ","R","lemma","enters / entered","action","vg-enter",["دَخَلَ","وَدَخَلَ","دَخَلَتْ"],{}),
 "la":     ("لَا","R","lemma","no","polarity",None,["لَا"],{}),
 "naam":   ("نَعَمْ","R","lemma","yes","polarity",None,["نَعَمْ"],{}),
 "anta":   ("أَنْتَ","R","lemma","you","person",None,["أَنْتَ","وَأَنْتَ"],{}),
 "hadha":  ("هٰذَا","R","lemma","this","deixis",None,["هٰذَا","هٰذِهِ"],{}),
 "ana":    ("أَنَا","R","lemma","I","person",None,["أَنَا","وَأَنَا"],{}),
 "man":    ("مَنْ","R","lemma","who?","question",None,["مَنْ"],{}),
 "qalam":  ("قَلَم","R","lemma","a pen","object","obj-pen",["قَلَمِي","قَلَمُ","الْقَلَمُ","الْقَلَمَ"],{}),
 "fasl":   ("فَصْل","R","lemma","class","place",None,["الْفَصْلِ"],{}),
 # support (recycled and new)
 "ya":     ("يَا","S","lemma","O (address)","address",None,["يَا"],{}),
 "kitab":  ("كِتَاب","S","lemma","a book","object",None,["كِتَابِي","كِتَابَكَ","كِتَابُكَ","الْكِتَابَ","الْكِتَابِ","كِتَابٌ","وَالْكِتَابُ"],{}),
 "bayt":   ("بَيْت","S","lemma","a house","place","obj-door",["بَيْتٍ","الْبَيْتِ","بَيْتِ","الْبَيْتَ","بَيْتِهَا"],{}),
 "bab":    ("بَاب","S","lemma","a door","object","obj-door",["الْبَابِ"],{}),
 "miftah": ("مِفْتَاح","S","lemma","a key","object",None,["مِفْتَاحِي","الْمِفْتَاحُ","الْمِفْتَاحَ"],{}),
 "ard":    ("أَرْض","S","lemma","the ground","place",None,["الْأَرْضِ"],{}),
 "qitt":   ("قِطّ","S","lemma","a cat","person",None,["قِطٌّ","الْقِطُّ","وَالْقِطُّ","الْقِطِّ","قِطُّ"],{}),
 "kabir":  ("كَبِير","S","lemma","big","description",None,["كَبِيرٍ","كَبِيرٌ"],{}),
 "saghir": ("صَغِير","S","lemma","small","description",None,["الصَّغِيرَةُ","صَغِيرٌ","الصَّغِيرُ"],{}),
 "kura":   ("كُرَة","S","lemma","a ball","object",None,["الْكُرَةَ","الْكُرَةُ","الْكُرَةِ","كُرَةٌ"],{}),
 "hadiya": ("هَدِيَّة","S","lemma","a gift","object",None,["هَدِيَّةٌ","الْهَدِيَّةُ","الْهَدِيَّةَ","وَالْهَدِيَّةُ"],{}),
 "bijanib":("بِجَانِبِ","S","lemma","beside","place",None,["بِجَانِبِ"],{}),
 "yanzur": ("نَظَرَ","S","lemma","looks / looked","action",None,["يَنْظُرُ","نَظَرَ","وَنَظَرَتْ"],{}),
 "yadhak": ("ضَحِكَ","S","lemma","laughs / laughed","action",None,["يَضْحَكُ","ضَحِكَ","ضَحِكَتْ"],{}),
 "aydan":  ("أَيْضًا","S","lemma","too","addition",None,["أَيْضًا"],{}),
 "madha":  ("مَاذَا","S","lemma","what?","question",None,["مَاذَا"],{"chunk_ref":"CH-22"}),
 "walakin":("وَلٰكِنْ","G","lemma","but","connector",None,["وَلٰكِنْ"],{}),
}
STAT={"N":"NEW_CORE_TARGET","R":"RECYCLED_CORE_TARGET","S":"COMPREHENSIBLE_SUPPORT","G":"RECOGNITION_ONLY"}
PHRASES={
 "umm":[("هٰذِهِ أُمِّي","أُمِّي"),("أُمُّهُ عِنْدَهَا الْكِتَابُ","أُمُّهُ")],
 "ab":[("هٰذَا أَبِي","أَبِي"),("أَبُوهُ عِنْدَهُ الْقَلَمُ","أَبُوهُ")],
 "ukht":[("هٰذِهِ أُخْتِي","أُخْتِي"),("أُخْتُهُ الصَّغِيرَةُ","أُخْتُهُ")],
 "akh":[("هٰذَا أَخِي الصَّغِيرُ","أَخِي"),("أَخُو خَدِيجَة","أَخُو")],
 "maa":[("الْكُرَةُ مَعِي","مَعِي"),("الْهَدِيَّةُ مَعَهَا","مَعَهَا")],
 "inda":[("عِنْدِي كُرَةٌ","عِنْدِي"),("عِنْدَكِ الْكُرَةُ؟","عِنْدَكِ"),("عِنْدَ رَزَان هَدِيَّةٌ","عِنْدَ")],
 "laysa":[("الْكُرَةُ لَيْسَتْ مَعِي","لَيْسَتْ"),("لَيْسَ عِنْدِي كِتَابٌ","لَيْسَ")],
 "li":[("هٰذَا لَكَ","لَكَ"),("هٰذِهِ لَكِ","لَكِ")],
 "aata":[("يُعْطِيهَا الْكِتَابَ","يُعْطِيهَا"),("أَعْطَتْ رَزَان الْكِتَابَ لِسَامِي","أَعْطَتْ")],
 "akhadha":[("يَأْخُذُ الْمِفْتَاحَ","يَأْخُذُ"),("أَخَذَ الْكِتَابَ","أَخَذَ")],
 "ihtaja":[("أَحْتَاجُ إِلَى قَلَمِي","أَحْتَاجُ")],
 "aasha":[("يَعِيشُ فِي بَيْتٍ كَبِيرٍ","يَعِيشُ")],
 "arada":[("أُرِيدُ الْكُرَةَ","أُرِيدُ")],
 "madha":[("مَاذَا تُرِيدُ؟","مَاذَا")],
 "kura":[("عِنْدِي كُرَةٌ","كُرَةٌ"),("أُرِيدُ الْكُرَةَ","الْكُرَةَ")],
 "hadiya":[("هٰذِهِ هَدِيَّةٌ","هَدِيَّةٌ")],
 "bijanib":[("بِجَانِبِ الْبَابِ","بِجَانِبِ")],
 "saghir":[("هٰذَا أَخِي الصَّغِيرُ","الصَّغِيرُ"),("كِتَابٌ صَغِيرٌ","صَغِيرٌ")],
}
def build(unit_id,title,text,castlist,stages,extras):
    P=paras(text); alltoks=set(toks(text))
    items=[]
    for iid,(lemma,st,kind,gloss,dim,img,forms,extra) in ITEMS.items():
        present=[f for f in forms if f in alltoks]
        if not present: continue
        carrier=None
        for p_ in P:
            for c in re.split(r"(?<=[.!؟])\s+", p_):
                ct=set(toks(c)); f_=next((f for f in present if f in ct),None)
                if f_: carrier=(c.strip(),f_); break
            if carrier: break
        clause,hlf=carrier
        for ph,hl in PHRASES.get(iid,[]):
            if hl in present: clause,hlf=ph,hl; break
        it={"id":iid,"ar":present[0],"status":STAT[st],"lemma":lemma,"kind":kind,"forms":present,"gloss":gloss,"img":img,"dim":dim,"phrase":clause,"hl":hlf}
        it.update(extra); items.append(it)
    sents=[]
    for k,p in enumerate(P):
        pt=set(toks(p)); refs=[i["id"] for i in items if any(f in pt for f in i["forms"])]
        sents.append({"id":f"s{k:02d}","ar":p,"stage":stages[k],"items":refs,"img":None})
    u={"unit_id":unit_id,"title":title,"audio":{"verified":False},"canon":text,"cast":castlist,"items":items,"sentences":sents,
       "readings":[{"id":extras["reading_id"],"role":extras["role"],"title":title,"sentence_ids":[s["id"] for s in sents]}]}
    u.update({k:v for k,v in extras.items() if k not in("reading_id","role")})
    return u

cast1=[{"id":"yusuf","ar":"يُوسُف","img":None},{"id":"layla","ar":"لَيْلَى","img":None},{"id":"umm","ar":"أُمُّهُ","img":None},{"id":"ab","ar":"أَبُوهُ","img":None},{"id":"qitt","ar":"الْقِطُّ","img":None}]
cast2=[{"id":"razan","ar":"رَزَان","img":"av-razan"},{"id":"khadija","ar":"خَدِيجَة","img":None},{"id":"sami","ar":"سَامِي","img":None}]
st1=[0,0, 1,1,1,1,1, 1,1, 2,2, 2, 3,3,3,3]
st2=[0,0, 1,1,1, 2,2, 2,2,2, 3,3]
ex1={"reading_id":"main","role":"main",
 "contrasts":[
  {"id":"c1","stage":0,"img":None,"a":"يَعِيشُ الْقِطُّ بِجَانِبِ الْبَابِ","b":"يَعِيشُ الْقِطُّ فِي الْحَقِيبَةِ","correct":"a","support":"s00","dim":"place"},
  {"id":"c2","stage":1,"img":None,"a":"الْكُرَةُ عِنْدَ لَيْلَى","b":"الْكُرَةُ عِنْدَ يُوسُف","correct":"a","support":"s03","dim":"possession"},
  {"id":"c3","stage":1,"img":None,"a":"أُمِّي عِنْدَهَا كِتَابِي","b":"أُمِّي عِنْدَهَا قَلَمِي","correct":"a","support":"s06","dim":"possession"},
  {"id":"c4","stage":2,"img":None,"a":"الْمِفْتَاحُ تَحْتَ الْقِطِّ","b":"الْمِفْتَاحُ تَحْتَ الْكِتَابِ","correct":"a","support":"s11","dim":"place"},
  {"id":"c5","stage":3,"img":None,"a":"يَأْخُذُ الْقِطُّ الْكُرَةَ","b":"يَأْخُذُ الْقِطُّ الْمِفْتَاحَ","correct":"a","support":"s14","dim":"object"}],
 "facts":[
  {"id":"f1","stage":0,"ar":"يُوسُف وَلَدٌ.","truth":True,"support":"s00","dim":"person"},
  {"id":"f2","stage":0,"ar":"لَيْلَى أُمُّ يُوسُف.","truth":False,"support":"s00","dim":"person"},
  {"id":"f3","stage":1,"ar":"الْكُرَةُ عِنْدَ لَيْلَى.","truth":True,"support":"s03","dim":"possession"},
  {"id":"f4","stage":1,"ar":"الْكِتَابُ عِنْدَ يُوسُف.","truth":False,"support":"s06","dim":"possession"},
  {"id":"f5","stage":2,"ar":"الْمِفْتَاحُ تَحْتَ الْقِطِّ.","truth":True,"support":"s11","dim":"place"},
  {"id":"f6","stage":3,"ar":"يَأْخُذُ الْقِطُّ الْكُرَةَ.","truth":True,"support":"s14","dim":"object"}],
 "whosays":[
  {"id":"w1","stage":1,"quote":"«نَعَمْ، الْكُرَةُ عِنْدِي. وَأَنْتَ، مَاذَا تُرِيدُ؟»","speaker":"layla","support":"s03"},
  {"id":"w2","stage":1,"quote":"«نَعَمْ، كِتَابُكَ عِنْدِي. وَأَنَا أَحْتَاجُ إِلَى قَلَمِي.»","speaker":"umm","support":"s08"},
  {"id":"w3","stage":2,"quote":"«نَعَمْ، الْقَلَمُ مَعِي. وَأَنَا أَحْتَاجُ إِلَى مِفْتَاحِي.»","speaker":"ab","support":"s10"},
  {"id":"w4","stage":3,"quote":"«يَا قِطُّ! أُرِيدُ الْكُرَةَ!»","speaker":"yusuf","support":"s15"}],
 "events":[
  {"id":"e1","order":1,"stage":1,"img":None,"sentence":"s02"},
  {"id":"e2","order":2,"stage":1,"img":None,"sentence":"s07"},
  {"id":"e3","order":3,"stage":2,"img":None,"sentence":"s11"},
  {"id":"e4","order":4,"stage":3,"img":None,"sentence":"s14"}],
 "findit":[
  {"id":"fi1","stage":1,"img":None,"prompt_gloss":"Which line says where the cat lives?","answer":"s00","pool":["s00","s01","s02","s03"]},
  {"id":"fi2","stage":1,"img":None,"prompt_gloss":"Which line says who has the book?","answer":"s06","pool":["s04","s05","s06","s07"]},
  {"id":"fi3","stage":2,"img":None,"prompt_gloss":"Which line says where the key is?","answer":"s11","pool":["s08","s09","s10","s11"]}],
 "retrieval":[
  {"id":"r1","stage":1,"sentence":"s03","blank":"عِنْدِي","choices":["عِنْدِي","عِنْدَكَ","عِنْدَهُ"],"img":None,"item":"inda"},
  {"id":"r2","stage":1,"sentence":"s06","blank":"أُمِّي","choices":["أُمِّي","أَبِي","أُخْتِي"],"img":None,"item":"umm"},
  {"id":"r3","stage":2,"sentence":"s10","blank":"مَعِي","choices":["مَعِي","مَعَهَا","مَعَهُ"],"img":None,"item":"maa"},
  {"id":"r4","stage":3,"sentence":"s12","blank":"يَأْخُذُ","choices":["يَأْخُذُ","يُعْطِيهَا","يَرْجِعُ"],"img":None,"item":"akhadha"}]}
ex2={"reading_id":"second","role":"second",
 "contrasts":[
  {"id":"c1","stage":0,"img":None,"a":"الْهَدِيَّةُ لِخَدِيجَة","b":"الْهَدِيَّةُ لِسَامِي","correct":"a","support":"s00","dim":"possession"},
  {"id":"c2","stage":1,"img":None,"a":"سَامِي أَخُو خَدِيجَة","b":"سَامِي أَخُو رَزَان","correct":"a","support":"s01","dim":"person"},
  {"id":"c3","stage":2,"img":None,"a":"أَعْطَتْ رَزَان الْكِتَابَ لِسَامِي","b":"أَعْطَتْ رَزَان الْكِتَابَ لِخَدِيجَة","correct":"a","support":"s05","dim":"possession"},
  {"id":"c4","stage":3,"img":None,"a":"مَعَ سَامِي كُرَةٌ","b":"مَعَ سَامِي قَلَمٌ","correct":"a","support":"s10","dim":"object"}],
 "facts":[
  {"id":"f1","stage":0,"ar":"الْهَدِيَّةُ كِتَابٌ صَغِيرٌ.","truth":True,"support":"s00","dim":"object"},
  {"id":"f2","stage":1,"ar":"سَامِي أَخُو خَدِيجَة.","truth":True,"support":"s01","dim":"person"},
  {"id":"f3","stage":1,"ar":"عِنْدَ سَامِي كِتَابٌ.","truth":False,"support":"s02","dim":"possession"},
  {"id":"f4","stage":2,"ar":"الْكِتَابُ مَعَ سَامِي.","truth":True,"support":"s07","dim":"possession"},
  {"id":"f5","stage":3,"ar":"أَعْطَاهَا سَامِي الْكُرَةَ.","truth":True,"support":"s10","dim":"possession"}],
 "whosays":[
  {"id":"w1","stage":1,"quote":"«كِتَابٌ! أُرِيدُ الْكِتَابَ! لَيْسَ عِنْدِي كِتَابٌ.»","speaker":"sami","support":"s02"},
  {"id":"w2","stage":2,"quote":"«هٰذَا لَكَ.»","speaker":"razan","support":"s05"},
  {"id":"w3","stage":3,"quote":"«هٰذَا أَخِي الصَّغِيرُ! يَعِيشُ مَعِي هُنَا.»","speaker":"khadija","support":"s09"}],
 "events":[
  {"id":"e1","order":1,"stage":0,"img":None,"sentence":"s00"},
  {"id":"e2","order":2,"stage":1,"img":None,"sentence":"s02"},
  {"id":"e3","order":3,"stage":2,"img":None,"sentence":"s05"},
  {"id":"e4","order":4,"stage":3,"img":None,"sentence":"s10"}],
 "findit":[
  {"id":"fi1","stage":1,"img":None,"prompt_gloss":"Which line says what the gift is?","answer":"s00","pool":["s00","s01","s02","s03"]},
  {"id":"fi2","stage":2,"img":None,"prompt_gloss":"Which line gives the book to سامي?","answer":"s05","pool":["s03","s04","s05","s06"]},
  {"id":"fi3","stage":3,"img":None,"prompt_gloss":"Which line brings the ball?","answer":"s10","pool":["s08","s09","s10","s11"]}],
 "retrieval":[
  {"id":"r1","stage":0,"sentence":"s00","blank":"مَعَهَا","choices":["مَعَهَا","مَعَهُ","مَعِي"],"img":None,"item":"maa"},
  {"id":"r2","stage":2,"sentence":"s05","blank":"أَعْطَتْ","choices":["أَعْطَتْ","أَخَذَ","ذَهَبَتْ"],"img":None,"item":"aata"},
  {"id":"r3","stage":3,"sentence":"s09","blank":"أَخِي","choices":["أَخِي","أُخْتِي","أَبِي"],"img":None,"item":"akh"}]}
U3=build("unit-03","مَنْ عِنْدَهُ الْكُرَةُ؟",s1,cast1,st1,ex1)
U3P=build("unit-03p","هَدِيَّةُ رَزَان",s2,cast2,st2,ex2)
js="\n/* ---- Unit 3 (SC-109) — revision-1 texts; no illustrations yet (img:null) ---- */\nconst UNIT_03 = "+json.dumps(U3,ensure_ascii=False)+";\nconst UNIT_03P = "+json.dumps(U3P,ensure_ascii=False)+";\n"
open("unit03_data.js","w",encoding="utf8").write(js)
print("items",len(U3["items"]),len(U3P["items"]),"sentences",len(U3["sentences"]),len(U3P["sentences"]))
