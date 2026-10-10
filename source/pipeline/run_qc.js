// run_qc.js — QC and delivery check against the REAL engine (source/pipeline/engine_core.js).
// (The old entry point ran against engine_test.js, a stale fixture; a pass there verified nothing — audit 2026-10-10 §11.)
// usage: node source/pipeline/run_qc.js        → exit 1 if any unit is undeliverable
const path = require("node:path");
const E = require(path.join(__dirname, "engine_core.js"));
let bad = 0;
for (const [k, u] of Object.entries(E.UNITS)) {
  const r = E.qc(u, E.gen(u)), d = E.deliverable(u), c = E.canonCheck(u);
  console.log(`${k.padEnd(9)} words ${String(c.words).padStart(3)} · generated ${String(d.acts).padStart(3)} · failed ${r.failed.length} · ${d.ok ? "DELIVERABLE" : "WITHHELD"} · pathways vocab ${E.pathway(u, "vocab", 0).length} / reading ${E.pathway(u, "reading", 0).length - 2 + 1 + E.postReading(u, 3, true).length}`);
  r.failed.forEach(f => console.log("   ✗", f.id, "—", f.why));
  r.notes.filter(n => /licence/.test(n.note)).forEach(n => console.log("   ·", n.note));
  if (!d.ok) bad++;
}
process.exit(bad ? 1 : 0);
