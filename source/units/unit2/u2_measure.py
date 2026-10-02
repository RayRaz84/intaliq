import re, sys
from collections import Counter

s1 = open("u2r4_s1.txt", encoding="utf8").read()
s2 = open("u2r4_s2.txt", encoding="utf8").read()

NAMES = {"رزان","سارة","كريم","بدر","نور"}
def strip(w):
    w = re.sub(r"[ً-ْٰـ]", "", w)   # harakat, dagger alif, tatweel
    w = w.replace("ٰ","")
    return w
def toks(t):
    t = re.sub(r"[«»\"،.!؟:\-…\(\)]", " ", t)
    return [strip(w) for w in t.split() if strip(w)]

# host lemma after removing proclitic و and definite article; keep possessive ي
def host(w):
    h = w
    if h.startswith("و") and len(h) > 2 and h[1:] not in ("لد",):  # وَلَد stays
        h = h[1:]
    if h.startswith("ال") and len(h) > 3: h = h[2:]
    return h

U1 = {  # Unit 1 carded items (lemma-hosts and their printed forms), names excluded
 "السلام":"U1","عليكم":"U1","اهلا":"U1","أهلا":"U1","انا":"U1","أنا":"U1","ولد":"U1","بنت":"U1","صديق":"U1","صديقة":"U1","صديقات":"U1",
 "قائمة":"U1","فصل":"U1","قلم":"U1","قلمي":"U1","عند":"U1","عندي":"U1","عندها":"U1","لي":"U1","اريد":"U1","أريد":"U1","تريد":"U1","يريد":"U1",
 "ليس":"U1","دخل":"U1","دخلت":"U1","تدخل":"U1","يدخل":"U1","رأى":"U1","رأت":"U1","رأتِ":"U1","ترى":"U1","يرى":"U1","قال":"U1","قالت":"U1","تقول":"U1","يقول":"U1",
 "تحب":"U1","يحب":"U1","هناك":"U1","من":"U1","اسم":"U1","اسمي":"U1","لا":"U1","نعم":"U1","انت":"U1","أنت":"U1","هذا":"U1","هذه":"U1","يا":"U1","هي":"U1",
}
NEW_CORE = {"اين":"C","أين":"C","في":"C","على":"C","تحت":"C","هنا":"C"}
SUPPORT  = {"كتاب":"S","كتابي":"S","باب":"S","حقيبة":"S","حقيبتي":"S","صورة":"S","صورتي":"S","بيت":"S","بيتي":"S","غرفة":"S","مفتاح":"S"}

def classify(w):
    if w in NAMES: return "NAME"
    h = host(w)
    for d,lab in ((U1,"U1"),(NEW_CORE,"C"),(SUPPORT,"S")):
        if h in d or w in d: return lab
    return "??"

for name, text in (("Story 1", s1), ("Story 2", s2)):
    tk = toks(text)
    running = len(tk)
    cls = [classify(w) for w in tk]
    names = cls.count("NAME")
    denom = running - names
    rec = cls.count("U1"); new = cls.count("C") + cls.count("S"); unk = cls.count("??")
    print(f"\n== {name}: running words {running} (names {names}) | denominator {denom} | recycled {rec} ({100*rec/denom:.1f}%) | new {new} | unclassified {unk}")
    if unk: print("   UNCLASSIFIED:", [w for w,c in zip(tk,cls) if c=="??"])
    c = Counter(host(w) for w in tk if classify(w)!="NAME")
    print("   new-core encounters:", {k:c.get(k,0) for k in ("اين","أين","في","على","تحت","هنا")})
    print("   support encounters:", {k:c.get(k,0) for k in ("كتاب","كتابي","باب","حقيبة","حقيبتي","صورة","بيت","غرفة","مفتاح")})
    print("   top:", c.most_common(15))
    print("   sentences:", len(re.findall(r"[.!؟]", text)))
