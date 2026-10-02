import re, json, subprocess, sys
from collections import Counter
P=r"[«»\"،.!؟:\-…\(\)]"
def strip(w): return re.sub(r"[ً-ْٰـ]","",w)
def toks(t): return [strip(w) for w in re.sub(P," ",t).split() if strip(w)]
# prior-unit lemmas from the engine (forms + lemmas), stripped
NODE='''const fs=require("fs");const src=fs.readFileSync("engine_core.js","utf8");const g={};(new Function("globalThis",src+";return globalThis;"))(g);
const out={};for(const [k,u] of Object.entries(g.SC_ENGINE.UNITS)){out[k]=u.items.map(i=>[i.lemma,i.forms||[],i.status]);}process.stdout.write(JSON.stringify(out));'''
eng=json.loads(subprocess.check_output(["node","-e",NODE],text=True))
KNOWN=set(); 
for k,items in eng.items():
    if k.startswith("unit-03"): continue
    for lemma,forms,st in items:
        KNOWN.add(strip(lemma)); KNOWN.update(strip(f) for f in forms)
# Unit 1 lemma map forms
import importlib.util
spec=importlib.util.spec_from_file_location("lem","ledger/lemmas.py"); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
for _id,lemma,gloss,kind,forms in m.LEMMAS: KNOWN.add(strip(lemma)); KNOWN.update(strip(f) for f in forms)
# add stems for suffix stripping
STEMS={strip(x) for x in ["كِتَاب","قَلَم","مِفْتَاح","بَيْت","حَقِيبَة","صُورَة","اِسْم","صَدِيق","عِنْدَ","مَعَ","لِـ","أُمّ","أَب","أَخ","أُخْت","كُرَة","هَدِيَّة","يُعْطِي","تُعْطِي","أَعْطَى","أَعْطَتْ"]}
NAMES={strip(x) for x in ["يُوسُف","لَيْلَى","رَزَان","خَدِيجَة","سَامِي"]}
NEWCORE={strip(x) for x in ["أُمّ","أُمِّي","أُمُّهُ","أُمِّهِ","أَب","أَبِي","أَبُوهُ","أَبُوكَ","أَخ","أَخِي","أَخُو","أَخُوكِ","أُخْت","أُخْتِهِ","أُخْتُهُ","مَعَ","مَعِي","مَعَهَا","مَعَهُ"]}
TARGETV={strip(x) for x in ["يَعِيشُ","يَأْخُذُ","أَخَذَ","أَحْتَاجُ","يُعْطِيهِ","يُعْطِيهَا","تُعْطِيهِ","أَعْطَتْ","أَعْطَاهَا","تُرِيدُ"]}
SUPPORT={strip(x) for x in ["كُرَة","الْكُرَةُ","الْكُرَةَ","الْكُرَةِ","كُرَةٌ","هَدِيَّة","هَدِيَّةٌ","الْهَدِيَّةُ","الْهَدِيَّةَ","صَغِير","صَغِيرٌ","الصَّغِيرَةُ","الصَّغِيرُ","بِجَانِبِ","مَاذَا","نَظَرَ","نَظَرَتْ","لِسَامِي","لَكَ"]}
def host(w):
    cands=[w]
    if w.startswith("و") and len(w)>2: cands.append(w[1:])
    out=[]
    for c in cands:
        out.append(c)
        if c.startswith("ال") and len(c)>3: out.append(c[2:])
        if c.startswith("ل") and len(c)>2: out.append(c[1:]); 
        if c.startswith("لل"): out.append(c[2:])
        for suf in ("ها","ه","ك","ي","ني"):
            if c.endswith(suf) and len(c)>len(suf)+1:
                base=c[:-len(suf)]; out.append(base); out.append(base+"ة") if base.endswith("ت") and False else None
                if base.endswith("ت"): out.append(base[:-1]+"ة")
                if base.startswith("ال"): out.append(base[2:])
    return out
def classify(w):
    if w in NAMES: return "NAME"
    hs=host(w)
    if any(h in NEWCORE for h in hs): return "NEW"
    if any(h in TARGETV for h in hs): return "NEW"
    if any(h in KNOWN for h in hs): return "KNOWN"
    if any(h in SUPPORT for h in hs): return "SUP"
    return "??"
def measure(name,text,extra_known=set()):
    tk=toks(text); cls=[]
    for w in tk:
        c=classify(w)
        if c in("NEW","SUP","??") and any(h in extra_known for h in host(w)): c="KNOWN"
        cls.append(c)
    names=cls.count("NAME"); den=len(tk)-names; kn=cls.count("KNOWN")
    print(f"== {name}: {len(tk)} words ({names} names) | known {kn}/{den} = {100*kn/den:.1f}% | new-core+verbs {cls.count('NEW')} | support {cls.count('SUP')} | ?? {[w for w,c in zip(tk,cls) if c=='??']}")
    return tk,cls
s1=open("u3r1_s1.txt",encoding="utf8").read(); s2=open("u3r1_s2.txt",encoding="utf8").read()
tk1,c1=measure("Story 1 vs Units 1–2 (report)",s1)
# Story 2 vs Units 1–2 + Story 1 + phrase page (phrase page = every new item the readings print → by CR-1 all Story-1 printed lemmas count as known)
s1known={h for w in tk1 for h in host(w)}
tk2,c2=measure("Story 2 vs Units 1–2 + Story 1 + phrase page (GATE ≥80%)",s2,s1known|NEWCORE|TARGETV|SUPPORT)
tk2b,c2b=measure("Story 2 vs Units 1–2 only (info)",s2)
cnt=Counter(); 
for w in tk1+tk2:
    for key,grp in (("عند",{"عند"}),("مع",{"مع"}),("أم",{"أم"}),("أب",{"أب","أبو"}),("أخ",{"أخ","أخو"}),("أخت",{"أخت"}),("ليس",{"ليس","ليست"}),("أريد",{"أريد","تريد"}),("أعطى",{"يعطي","تعطي","أعطت","أعطا","أعطى"}),("أخذ",{"يأخذ","أخذ"}),("احتاج",{"أحتاج"}),("عاش",{"يعيش"}),("كرة",{"كرة"}),("هدية",{"هدية"}),("صغير",{"صغير","صغيرة"}),("بجانب",{"بجانب"}),("ماذا",{"ماذا"})):
        if any(h in grp for h in host(w)): cnt[key]+=1
print("encounters both readings:",dict(cnt))
