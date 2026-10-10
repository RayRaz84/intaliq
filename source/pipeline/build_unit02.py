import re, json, argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
parser = argparse.ArgumentParser()
parser.add_argument('--art-map', type=Path, default=ROOT / 'art_assets_map.json')
parser.add_argument('--output', type=Path, default=Path('unit02_data.js'))
args = parser.parse_args()
def canon(name):
    local = Path(name)
    return (local if local.exists() else ROOT / 'source/units/unit2/canon' / name).read_text(encoding='utf8').strip()
s1=canon('u2r7_s1.txt')
s2=canon('u2r7_s2.txt')
PUNCT=r"[«»\"،.!؟:\-…]"
def toks(t): return [w for w in re.sub(PUNCT," ",t).split() if w]
def paras(t): return [p.strip() for p in t.split("\n\n") if p.strip()]

# item definitions: id -> (lemma, status, kind, gloss, dim, img, candidate surface forms (exact tokens), extra)
# statuses: N=NEW_CORE_TARGET R=RECYCLED_CORE_TARGET S=COMPREHENSIBLE_SUPPORT G=RECOGNITION_ONLY
ITEMS = {
 # Unit 2 core
 "ayna":   ("أَيْنَ","N","lemma","where?","question",None,["أَيْنَ"],{"chunk_ref":"CH-14"}),
 "fi":     ("فِي","N","lemma","in","place",None,["فِي"],{"chunk_ref":"CH-15"}),
 "ala":    ("عَلَى","N","lemma","on","place",None,["عَلَى"],{"chunk_ref":"CH-15"}),
 "tahta":  ("تَحْتَ","N","lemma","under","place",None,["تَحْتَ"],{"chunk_ref":"CH-15"}),
 "huna":   ("هُنَا","N","lemma","here","place",None,["هُنَا"],{"chunk_ref":"CH-16"}),
 "dhahab": ("ذَهَبَ","N","lemma","goes / went","action",None,["يَذْهَبُ","أَذْهَبُ","ذَهَبَتْ","وَذَهَبَتْ"],{"chunk_ref":"CH-18"}),
 "ila":    ("إِلَى","N","lemma","to","place",None,["إِلَى"],{"chunk_ref":"CH-18"}),
 "rajaa":  ("رَجَعَ","N","lemma","comes back / came back","action",None,["يَرْجِعُ","رَجَعَتْ"],{}),
 "wadaa":  ("وَضَعَ","N","lemma","puts / put","action",None,["يَضَعُ","أَضَعُ","تَضَعُ","وَضَعَتْ"],{}),
 # recycled core (Unit 1)
 "hunaka": ("هُنَاكَ","R","lemma","there is","existence",None,["هُنَاكَ"],{}),
 "walad":  ("وَلَد","R","lemma","a boy","person","av-karim",["وَلَدٌ"],{}),
 "ism":    ("اِسْم","R","lemma","a name","object",None,["اسْمُهُ"],{}),
 "inda":   ("عِنْدَ","R","lemma","has / at","possession",None,["عِنْدَهُ","عِنْدَ","عِنْدِي"],{}),
 "yara":   ("رَأَى","R","lemma","sees / saw","action","vg-see",["يَرَى","رَأَتْ","وَرَأَتْ"],{}),
 "yaqul":  ("قَالَ","R","lemma","says / said","action","vg-say",["يَقُولُ","تَقُولُ","قَالَتْ","وَقَالَتْ"],{}),
 "yadkhul":("دَخَلَ","R","lemma","enters","action","vg-enter",["يَدْخُلُ","وَيَدْخُلُ"],{}),
 "la":     ("لَا","R","lemma","no","polarity",None,["لَا"],{}),
 "naam":   ("نَعَمْ","R","lemma","yes","polarity",None,["نَعَمْ"],{}),
 "anta":   ("أَنْتَ","R","lemma","you","person",None,["أَنْتَ","وَأَنْتَ"],{}),
 "hadha":  ("هٰذَا","R","lemma","this","deixis",None,["هٰذَا","وَهٰذَا","هٰذِهِ","وَهٰذِهِ"],{}),
 "ana":    ("أَنَا","R","lemma","I","person",None,["أَنَا","وَأَنَا"],{}),
 "ya":     ("يَا","S","lemma","O (address)","address",None,["يَا"],{}),
 "man":    ("مَنْ","R","lemma","who? (whose?)","question",None,["لِمَنْ"],{}),
 "qalam":  ("قَلَم","R","lemma","a pen","object","obj-pen",["وَقَلَمٌ"],{}),
 "sadiq":  ("صَدِيق","R","lemma","a friend","person","vg-sadiq",["صَدِيقَةُ"],{}),
 "laysa":  ("لَيْسَ","G","lemma","is not (f.)","polarity",None,["لَيْسَتْ"],{}),
 "li":     ("لِـ","G","lemma","for (you / Khadija)","possession",None,["لِخَدِيجَة","لَكِ"],{}),
 # support
 "miftah": ("مِفْتَاح","S","lemma","a key","object",None,["مِفْتَاحٌ","مِفْتَاحًا","الْمِفْتَاحُ","الْمِفْتَاحَ","الْمِفْتَاحِ","مِفْتَاحُ","وَمِفْتَاحُ","مِفْتَاحِي","مِفْتَاحُكَ","مِفْتَاحَكَ","مِفْتَاحُكِ"],{}),
 "haqiba": ("حَقِيبَة","S","lemma","a bag","object",None,["حَقِيبَةٌ","الْحَقِيبَةِ","حَقِيبَتِهِ","حَقِيبَتِي","حَقِيبَتِهَا"],{}),
 "kitab":  ("كِتَاب","S","lemma","a book","object",None,["كِتَابٌ","الْكِتَابِ"],{}),
 "bayt":   ("بَيْت","S","lemma","a house","place","obj-door",["الْبَيْتِ","الْبَيْتَ","بَيْتِ","بَيْتِهِ","بَيْتِهَا","بَيْتِكِ","بَيْتِي"],{}),
 "bab":    ("بَاب","S","lemma","a door","object","obj-door",["الْبَابِ"],{}),
 "ard":    ("أَرْض","S","lemma","the ground","place",None,["الْأَرْضِ"],{}),
 "yad":    ("يَد","S","lemma","hand","object",None,["يَدِهِ"],{}),
 "qitt":   ("قِطّ","S","lemma","a cat","person",None,["قِطٌّ","الْقِطُّ","وَالْقِطُّ"],{}),
 "kabira": ("كَبِير","S","lemma","big","description",None,["كَبِيرَةٌ"],{}),
 "sura":   ("صُورَة","S","lemma","a picture","object",None,["صُورَةٌ","الصُّورَةِ","الصُّورَةُ","الصُّورَةَ","صُورَةً"],{}),
 "hazina": ("حَزِين","S","lemma","sad","description",None,["حَزِينَةٌ"],{}),
 "yanzur": ("نَظَرَ","S","lemma","looks","action",None,["يَنْظُرُ"],{}),
 "yadhak": ("ضَحِكَ","S","lemma","laughs / laughed","action",None,["يَضْحَكُ","تَضْحَكُ","ضَحِكَتْ","وَضَحِكَتْ"],{}),
 "aata":   ("أَعْطَى","S","lemma","gave (her)","action",None,["أَعْطَتْهَا"],{}),
 "aydan":  ("أَيْضًا","S","lemma","too","addition",None,["أَيْضًا"],{}),
 "hal":    ("هَلْ","G","lemma","(question particle)","question",None,["هَلْ"],{}),
 "walakin":("وَلٰكِنْ","G","lemma","but","connector",None,["وَلٰكِنْ"],{}),
}
STAT={"N":"NEW_CORE_TARGET","R":"RECYCLED_CORE_TARGET","S":"COMPREHENSIBLE_SUPPORT","G":"RECOGNITION_ONLY"}

PHRASES={
 "ayna":[("أَيْنَ الْمِفْتَاحُ؟","أَيْنَ")],
 "fi":[("فِي الْحَقِيبَةِ","فِي")],
 "ala":[("عَلَى الْبَابِ","عَلَى")],
 "tahta":[("تَحْتَ الْكِتَابِ","تَحْتَ")],
 "huna":[("أَنَا هُنَا!","هُنَا")],
 "dhahab":[("يَذْهَبُ إِلَى الْبَيْتِ","يَذْهَبُ"),("ذَهَبَتْ إِلَى بَيْتِ خَدِيجَة","ذَهَبَتْ")],
 "ila":[("يَذْهَبُ إِلَى الْبَيْتِ","إِلَى")],
 "rajaa":[("يَرْجِعُ إِلَى بَيْتِهِ","يَرْجِعُ"),("رَجَعَتْ إِلَى بَيْتِهَا","رَجَعَتْ")],
 "wadaa":[("أَضَعُ مِفْتَاحِي فِي حَقِيبَتِي","أَضَعُ"),("وَضَعَتْ الصُّورَةَ فِي حَقِيبَتِهَا","وَضَعَتْ")],
}
def build(unit_id,title,text,castlist,stages,extras):
    P=paras(text); alltoks=set(toks(text))
    items=[]
    for iid,(lemma,st,kind,gloss,dim,img,forms,extra) in ITEMS.items():
        present=[f for f in forms if f in alltoks]
        if not present: continue
        # phrase carrier: the first clause (any paragraph) that contains one of the printed forms as a token; hl = that form
        carrier=None
        for p_ in P:
            for c in re.split(r"(?<=[.!؟])\s+", p_):
                ct=set(toks(c))
                f_=next((f for f in present if f in ct),None)
                if f_: carrier=(c.strip(),f_); break
            if carrier: break
        clause,hlf=carrier
        # phrase-page carriers (B0, CR-13): a core item is met inside the phrase the phrase page prints, when that form is printed in this reading
        for ph,hl in PHRASES.get(iid,[]):
            if hl in present: clause,hlf=ph,hl; break
        it={"id":iid,"ar":present[0],"status":STAT[st],"lemma":lemma,"kind":kind,"forms":present,"gloss":gloss,"img":img,"dim":dim,"phrase":clause,"hl":hlf}
        it.update(extra); items.append(it)
    ids={i["id"]:i for i in items}
    sents=[]
    for k,p in enumerate(P):
        pt=set(toks(p)); refs=[i["id"] for i in items if any(f in pt for f in i["forms"])]
        sents.append({"id":f"s{k:02d}","ar":p,"stage":stages[k],"items":refs,"img":None})
    u={"unit_id":unit_id,"title":title,"audio":{"verified":False},"canon":text,"cast":castlist,"items":items,"sentences":sents,
       "readings":[{"id":extras["reading_id"],"role":extras["role"],"title":title,"sentence_ids":[s["id"] for s in sents]}]}
    u.update({k:v for k,v in extras.items() if k not in("reading_id","role")})
    return u

cast1=[{"id":"karim","ar":"كَرِيم","img":"av-karim"},{"id":"zayd","ar":"زَيْد","img":"av-zayd"},{"id":"maha","ar":"مَهَا","img":"av-maha"},{"id":"omar","ar":"عُمَر","img":"av-omar"},{"id":"qitt","ar":"الْقِطُّ","img":None}]
cast2=[{"id":"razan","ar":"رَزَان","img":"av-razan"},{"id":"khadija","ar":"خَدِيجَة","img":None},{"id":"rana","ar":"رَنَا","img":"av-rana"}]
st1=[0,0,0,0,0, 1,1,1,1,1,1,1, 2,2,2,2, 3,3,3,3,3,3]
st2=[0,0,0,0,0, 1,1,1,1,1,1, 2,2,2, 3,3,3,3,3,3]
ex1={"reading_id":"main","role":"main",
 "contrasts":[
  {"id":"c1","stage":0,"img":None,"a":"الْمِفْتَاحُ عَلَى الْأَرْضِ","b":"الْمِفْتَاحُ فِي الْبَيْتِ","correct":"a","support":"s02","dim":"place"},
  {"id":"c2","stage":1,"img":None,"a":"مِفْتَاحِي فِي حَقِيبَتِي","b":"مِفْتَاحِي عَلَى الْبَابِ","correct":"a","support":"s06","dim":"place"},
  {"id":"c3","stage":1,"img":None,"a":"مِفْتَاحِي تَحْتَ الْكِتَابِ","b":"مِفْتَاحِي فِي حَقِيبَتِي","correct":"a","support":"s08","dim":"place"},
  {"id":"c4","stage":2,"img":None,"a":"هُنَاكَ قِطٌّ عِنْدَ الْبَابِ","b":"هُنَاكَ وَلَدٌ عِنْدَ الْبَابِ","correct":"a","support":"s12","dim":"person"},
  {"id":"c5","stage":3,"img":None,"a":"هٰذَا مِفْتَاحُكَ","b":"هٰذَا مِفْتَاحُ زَيْد","correct":"a","support":"s18","dim":"possession"}],
 "facts":[
  {"id":"f1","stage":0,"ar":"كَرِيم وَلَدٌ.","truth":True,"support":"s00","dim":"person"},
  {"id":"f2","stage":0,"ar":"الْمِفْتَاحُ عَلَى الْأَرْضِ.","truth":True,"support":"s02","dim":"place"},
  {"id":"f3","stage":1,"ar":"مِفْتَاحُ زَيْد عَلَى الْبَابِ.","truth":False,"support":"s06","dim":"place"},
  {"id":"f4","stage":1,"ar":"مِفْتَاحُ عُمَر عَلَى الْبَابِ.","truth":True,"support":"s10","dim":"place"},
  {"id":"f5","stage":2,"ar":"هُنَاكَ قِطٌّ عِنْدَ الْبَابِ.","truth":True,"support":"s12","dim":"person"},
  {"id":"f6","stage":3,"ar":"الْمِفْتَاحُ مِفْتَاحُ كَرِيم.","truth":True,"support":"s18","dim":"possession"}],
 "whosays":[
  {"id":"w1","stage":1,"quote":"«لَا. مِفْتَاحِي فِي حَقِيبَتِي. أَضَعُ مِفْتَاحِي فِي حَقِيبَتِي.»","speaker":"zayd","support":"s06"},
  {"id":"w2","stage":1,"quote":"«لَا. مِفْتَاحِي تَحْتَ الْكِتَابِ. أَضَعُ مِفْتَاحِي تَحْتَ الْكِتَابِ.»","speaker":"maha","support":"s08"},
  {"id":"w3","stage":1,"quote":"«أَنَا؟ أَضَعُ مِفْتَاحِي فِي حَقِيبَتِي.»","speaker":"karim","support":"s11"},
  {"id":"w4","stage":2,"quote":"«نَعَمْ. أَنَا قِطٌّ. وَهٰذَا مِفْتَاحُكَ.»","speaker":"qitt","support":"s15"}],
 "events":[
  {"id":"e1","order":1,"stage":0,"img":None,"sentence":"s02"},
  {"id":"e2","order":2,"stage":1,"img":None,"sentence":"s05"},
  {"id":"e3","order":3,"stage":2,"img":None,"sentence":"s12"},
  {"id":"e4","order":4,"stage":3,"img":None,"sentence":"s20"}],
 "findit":[
  {"id":"fi1","stage":0,"img":None,"prompt_gloss":"Which line says where the key is?","answer":"s02","pool":["s01","s02","s03","s04"]},
  {"id":"fi2","stage":1,"img":None,"prompt_gloss":"Which line puts a key UNDER a book?","answer":"s08","pool":["s06","s08","s10","s11"]},
  {"id":"fi3","stage":3,"img":None,"prompt_gloss":"Which line asks where the house key is?","answer":"s16","pool":["s13","s15","s16","s17"]}],
 "retrieval":[
  {"id":"r1","stage":0,"sentence":"s02","blank":"عَلَى","choices":["عَلَى","فِي","تَحْتَ"],"img":None,"item":"ala"},
  {"id":"r2","stage":1,"sentence":"s08","blank":"تَحْتَ","choices":["تَحْتَ","عَلَى","فِي"],"img":None,"item":"tahta"},
  {"id":"r3","stage":1,"sentence":"s05","blank":"إِلَى","choices":["إِلَى","فِي","عَلَى"],"img":None,"item":"ila"},
  {"id":"r4","stage":3,"sentence":"s20","blank":"يَضَعُ","choices":["يَضَعُ","يَذْهَبُ","يَرْجِعُ"],"img":None,"item":"wadaa"}]}
ex2={"reading_id":"second","role":"second",
 "contrasts":[
  {"id":"c1","stage":0,"img":None,"a":"الصُّورَةُ فِي الْحَقِيبَةِ","b":"الصُّورَةُ عَلَى الْبَابِ","correct":"a","support":"s03","dim":"place"},
  {"id":"c2","stage":1,"img":None,"a":"خَدِيجَة لَيْسَتْ فِي الْبَيْتِ","b":"خَدِيجَة فِي الْبَيْتِ","correct":"a","support":"s05","dim":"place"},
  {"id":"c3","stage":1,"img":None,"a":"ذَهَبَتْ خَدِيجَة إِلَى بَيْتِ رَزَان","b":"ذَهَبَتْ خَدِيجَة إِلَى بَيْتِ رَنَا","correct":"a","support":"s06","dim":"place"},
  {"id":"c4","stage":3,"img":None,"a":"عِنْدِي صُورَةٌ لَكِ","b":"لَيْسَ عِنْدِي صُورَةٌ","correct":"a","support":"s15","dim":"possession"}],
 "facts":[
  {"id":"f1","stage":0,"ar":"خَدِيجَة صَدِيقَةُ رَزَان.","truth":True,"support":"s01","dim":"person"},
  {"id":"f2","stage":0,"ar":"الصُّورَةُ لِخَدِيجَة.","truth":True,"support":"s02","dim":"possession"},
  {"id":"f3","stage":1,"ar":"خَدِيجَة فِي الْبَيْتِ.","truth":False,"support":"s05","dim":"place"},
  {"id":"f4","stage":1,"ar":"رَزَان حَزِينَةٌ.","truth":True,"support":"s10","dim":"description"},
  {"id":"f5","stage":3,"ar":"عِنْدَ خَدِيجَة صُورَةٌ أَيْضًا.","truth":True,"support":"s15","dim":"possession"}],
 "whosays":[
  {"id":"w1","stage":1,"quote":"«خَدِيجَة؟ ذَهَبَتْ خَدِيجَة إِلَى بَيْتِكِ!»","speaker":"rana","support":"s06"},
  {"id":"w2","stage":2,"quote":"«رَزَان! أَنَا أَذْهَبُ إِلَى بَيْتِكِ!»","speaker":"khadija","support":"s12"},
  {"id":"w3","stage":3,"quote":"«وَأَنَا... عِنْدِي صُورَةٌ لَكِ أَيْضًا!»","speaker":"khadija","support":"s15"},
  {"id":"w4","stage":3,"quote":"«هٰذِهِ لَكِ.»","speaker":"razan","support":"s14"}],
 "events":[
  {"id":"e1","order":1,"stage":0,"img":None,"sentence":"s03"},
  {"id":"e2","order":2,"stage":1,"img":None,"sentence":"s06"},
  {"id":"e3","order":3,"stage":2,"img":None,"sentence":"s12"},
  {"id":"e4","order":4,"stage":3,"img":None,"sentence":"s16"}],
 "findit":[
  {"id":"fi1","stage":0,"img":None,"prompt_gloss":"Which line says where رزان puts the picture?","answer":"s03","pool":["s00","s01","s02","s03"]},
  {"id":"fi2","stage":1,"img":None,"prompt_gloss":"Which line says where سارة went?","answer":"s06","pool":["s04","s05","s06","s07"]},
  {"id":"fi3","stage":3,"img":None,"prompt_gloss":"Which line gives the SECOND picture?","answer":"s16","pool":["s14","s15","s16","s17"]}],
 "retrieval":[
  {"id":"r1","stage":0,"sentence":"s03","blank":"فِي","choices":["فِي","عَلَى","تَحْتَ"],"img":None,"item":"fi"},
  {"id":"r2","stage":1,"sentence":"s08","blank":"رَجَعَتْ","choices":["رَجَعَتْ","ذَهَبَتْ","وَضَعَتْ"],"img":None,"item":"rajaa"},
  {"id":"r3","stage":1,"sentence":"s04","blank":"هُنَا","choices":["هُنَا","هُنَاكَ"],"img":None,"item":"huna"}]}
U2=build("unit-02","أَيْنَ مِفْتَاحِي؟",s1,cast1,st1,ex1)
U2P=build("unit-02p","صُورَةُ رَزَان وَخَدِيجَة",s2,cast2,st2,ex2)
assets=json.loads(args.art_map.read_text(encoding='utf8'))
bindings=json.loads((ROOT / 'source/cast-and-art/unit2_art_bindings.json').read_text(encoding='utf8'))
for unit in [U2,U2P]:
    assignments=bindings['units'][unit['unit_id']]
    for group, records in assignments.items():
        for record in unit[group]:
            slot=records.get(record['id'])
            if slot:
                filename=assets[slot]
                if not (ROOT / filename).is_file():
                    raise ValueError('Missing art: '+filename)
                record['img']=filename
js="\n/* ---- Unit 2 (SC-092 · SC-094 · SC-095) — frozen revision 6; art assigned by the build from art_assets_map.json ---- */\nconst UNIT_02 = "+json.dumps(U2,ensure_ascii=False)+";\nconst UNIT_02P = "+json.dumps(U2P,ensure_ascii=False)+";\n"
args.output.write_text(js,encoding='utf8')
print("items",len(U2["items"]),len(U2P["items"]),"sentences",len(U2["sentences"]),len(U2P["sentences"]))
