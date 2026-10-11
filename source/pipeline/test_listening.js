// test_listening.js — proves the listening machinery (F9) without any shipped recording.
// A FIXTURE binding set (fake hashes, fixture verifier) is built in memory for Unit 1 and never written anywhere:
//   1. with complete, well-formed bindings the unit is deliverable, F9 activities exist, and the pathways are sound-first;
//   2. every malformed binding (bad ref, bad src, bad hash, missing verifier, duplicate ref, missing sentence/item) WITHHOLDS the unit.
// The real bindings (assets/audio/… with true sha256 and a named verifier) are owed: see INTALIQ1_UNIT1_AUDIO_INTAKE.md.
// usage: node source/pipeline/test_listening.js [engine.js]   → exit 1 on any failed expectation (the gate passes the engine extracted from index.html)
const path = require("node:path");
const E = process.argv[2] ? require(path.resolve(process.argv[2])) : require(path.join(__dirname, "engine_core.js"));
const clone = o => JSON.parse(JSON.stringify(o));
const fakeHash = s => require("node:crypto").createHash("sha256").update("fixture:" + s).digest("hex");
function fixtureBindings(u) {
  const clips = [];
  u.sentences.forEach(s => clips.push({ id: "c_" + s.id, kind: "sentence", ref: s.id, src: `assets/audio/${u.unit_id}/${s.id}.mp3`, sha256: fakeHash(s.id), verified_by: "fixture (not a person)", verified_on: "2026-10-11" }));
  u.items.filter(i => /CORE_TARGET$/.test(i.status)).forEach(i => clips.push({ id: "c_" + i.id, kind: "item", ref: i.id, src: `assets/audio/${u.unit_id}/item_${i.id}.mp3`, sha256: fakeHash(i.id), verified_by: "fixture (not a person)", verified_on: "2026-10-11" }));
  return clips;
}
let failures = 0;
const expect = (cond, msg) => { console.log((cond ? "  ok   " : "  FAIL ") + msg); if (!cond) failures++; };
for (const k of ["unit-01", "unit-01p"]) {
  console.log(k);
  const base = E.UNITS[k];
  const u = clone(base); u.audio = { verified: true, clips: fixtureBindings(base) };
  const d = E.deliverable(u), acts = E.qc(u, E.gen(u)).ok;
  expect(d.ok, "complete fixture bindings → deliverable (" + d.failed.map(f => f.why).join("; ") + ")");
  expect(acts.some(a => a.type === "listen_tap"), "listen_tap generated: " + acts.filter(a => a.type === "listen_tap").length);
  expect(acts.some(a => a.type === "listen_which"), "listen_which generated: " + acts.filter(a => a.type === "listen_which").length);
  expect(acts.some(a => a.type === "listen_who"), "listen_who generated: " + acts.filter(a => a.type === "listen_who").length);
  const v = E.pathway(u, "vocab", 0), r = E.pathway(u, "reading", 0);
  expect(v[0] && v[0].type === "listen_tap", "vocabulary pathway is sound-first (first task " + (v[0] && v[0].type) + ")");
  expect(r.some(a => a.type === "listen_which"), "reading pathway hears sentences before the text");
  expect(E.postReading(u, 3, true).some(a => a.type === "listen_who"), "post-reading includes hear-the-speaker");
  const mutations = {
    "ref to a missing sentence": c => { c[0].ref = "zz"; },
    "src outside assets/audio": c => { c[0].src = "x.mp3"; },
    "malformed sha256": c => { c[0].sha256 = "abc"; },
    "no verifier": c => { c[0].verified_by = ""; },
    "no date": c => { c[0].verified_on = "yesterday"; },
    "duplicate ref": c => { c.push({ ...c[0], id: "dup" }); },
    "a sentence left unbound": c => { c.splice(0, 1); },
    "a core item left unbound": c => { c.splice(c.length - 1, 1); },
    "flag without clips": c => { c.length = 0; },
  };
  for (const [name, mut] of Object.entries(mutations)) {
    const m = clone(base); m.audio = { verified: true, clips: fixtureBindings(base) }; mut(m.audio.clips);
    const dm = E.deliverable(m);
    expect(!dm.ok && E.pathway(m, "vocab", 0).length === 0, "withheld on: " + name);
  }
  const off = clone(base); off.audio = { verified: false };
  expect(E.deliverable(off).ok && !E.qc(off, E.gen(off)).ok.some(a => /^listen/.test(a.type)), "verified:false → deliverable, no listening tasks");
}
console.log(failures ? `\n${failures} expectation(s) failed` : "\nall listening expectations hold (fixture only — no recording is shipped)");
process.exit(failures ? 1 : 0);
