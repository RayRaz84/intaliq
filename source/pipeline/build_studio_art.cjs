/* build_studio_art.cjs — the Text build (SC-112 §5; TF-8; audit 2026-10-10 batches 1–3).
   One source, one engine, generated outputs:
     source/pipeline/engine_core.js          — the engine and ALL unit data (Units 2–3 declarations refreshed from their build scripts)
     source/pipeline/school_course_studio.html — the Studio source; its embedded engine is REPLACED by engine_core.js at build,
                                                 and its <!-- gen:… --> blocks are regenerated from the engine's data
     source/pipeline/build_teacher_pages.py   — the teacher's page (SC-104), built from the same engine
   Outputs: index.html, 404.html (identical), teacher.html, assets/art/unit2-rich/review.html + production-prompts.json.
   The build REFUSES when any unit is not deliverable (unit-level QC failure), when the Unit 2 art inventory or hashes
   disagree with the manifest, or when the Studio links the teacher page. Edits made only to index.html are overwritten. */
const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const { execFileSync } = require('node:child_process');
const root = path.resolve(__dirname, '../..');
const output = process.argv[2] ? path.resolve(process.argv[2]) : root;
const read = file => fs.readFileSync(path.join(root, file), 'utf8');
const version = Number(process.env.INTALIQ_STUDIO_VERSION || read('source/pipeline/school_course_studio.html').match(/VERSION (\d+)/)?.[1] || 43);
if (!Number.isInteger(version) || version < 43) throw Error('Invalid Studio version');

/* ---- 1 · Unit 2 art: inventory and accepted bytes (SC-113, SC-115–SC-117) ---- */
const assets = JSON.parse(read('art_assets_map.json'));
const bindings = JSON.parse(read('source/cast-and-art/unit2_art_bindings.json'));
const manifest = JSON.parse(read('assets/art/unit2-rich/manifest.json'));
if (manifest.slots.length !== 69 || Object.keys(assets).length !== 69) throw Error('Incomplete Unit 2 inventory');
for (const slot of manifest.slots) {
  const filename = assets[slot.id];
  if (filename !== slot.delivered) throw Error('Manifest/map disagreement: ' + slot.id);
  const bytes = fs.readFileSync(path.join(root, filename));
  if (crypto.createHash('sha256').update(bytes).digest('hex') !== slot.accepted.sha256) throw Error('Accepted bytes changed: ' + slot.id);
}

/* ---- 2 · the engine: Unit 2 declarations from its build script; Units 1 and 3 live in engine_core.js ---- */
execFileSync('python3', [path.join(__dirname, 'build_unit02.py'), '--output', path.join(root, 'source/units/unit2/unit02_data.js')], { cwd: root, stdio: 'inherit' });
const data = read('source/units/unit2/unit02_data.js');
let engine = read('source/pipeline/engine_core.js');
for (const name of ['UNIT_02', 'UNIT_02P']) {
  const declaration = data.match(new RegExp('^const ' + name + ' = .*;$', 'm'));
  if (!declaration || !new RegExp('^const ' + name + ' = .*;$', 'm').test(engine)) throw Error('Missing unit declaration: ' + name);
  engine = engine.replace(new RegExp('^const ' + name + ' = .*;$', 'm'), declaration[0]);
}
engine = engine.replace(/\/\* ---- Unit 2[^\n]*\*\//, data.match(/\/\* ---- Unit 2[^\n]*\*\//)[0]);
fs.writeFileSync(path.join(__dirname, 'engine_core.js'), engine);

/* evaluate the engine once, in isolation; refuse to build on any unit-level failure (B2) */
const g = {}; (new Function('globalThis', 'window', engine + ';return globalThis;'))(g, undefined); const E = g.SC_ENGINE;
const report = {};
for (const [k, u] of Object.entries(E.UNITS)) {
  const d = E.deliverable(u);
  report[k] = { words: E.canonCheck(u).words, generated: d.acts, blocked: !d.ok, vocab: E.pathway(u, 'vocab', 0).length, reading: E.pathway(u, 'reading', 0).length - 2 + 1 + E.postReading(u, 3, true).length };
  if (!d.ok) throw Error('Unit not deliverable — refusing to build: ' + k + ' — ' + d.failed.map(f => f.why).join(' · '));
  /* audio bindings (B6 closure): when a unit claims verified clips, every file must exist under assets/audio/ and hash as bound */
  if (u.audio && u.audio.verified) for (const c of u.audio.clips || []) {
    const f = path.join(root, c.src);
    if (!fs.existsSync(f) || fs.statSync(f).size === 0) throw Error('Audio binding without a file: ' + k + ' ' + c.id + ' → ' + c.src);
    const h = crypto.createHash('sha256').update(fs.readFileSync(f)).digest('hex');
    if (h !== c.sha256) throw Error('Audio file does not hash as bound: ' + k + ' ' + c.id);
    report[k].clips = (report[k].clips || 0) + 1;
  }
}

/* ---- 3 · the Studio: embed the engine wholesale, regenerate the generated blocks ---- */
let html = read('source/pipeline/school_course_studio.html');
/* the embedded engine is everything in its <script> block up to the end of the engine's IIFE — header comments
   included, so a rebuild replaces the previous embedding exactly (cleanup 2026-10-12: earlier builds kept the old
   header comments above the IIFE and stacked a new copy on every rebuild) */
const iife = html.indexOf('(function(root){\n"use strict";');
const engStart = iife < 0 ? -1 : html.lastIndexOf('<script>\n', iife) + '<script>\n'.length;
const engEnd = html.indexOf('})(typeof window!=="undefined"?window:globalThis);', iife);
if (iife < 0 || engStart < '<script>\n'.length || engEnd < 0) throw Error('Embedded engine not found in the Studio source');
const endLen = '})(typeof window!=="undefined"?window:globalThis);'.length;
html = html.slice(0, engStart) + engine.trimEnd() + html.slice(engEnd + endLen);

const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/"/g, '&quot;');
const svgOf = id => `<svg viewBox="0 0 120 100"><g transform="translate(10 4) scale(.95)"><use href="#${id}"/></g></svg>`;
const facesRow = (u, label) => '<div class="picseq" aria-label="' + label + '">' + u.cast.map((c, i) =>
  `<span class="picfr">${svgOf(c.img)}<b>${i + 1} · <bdi lang="ar">${esc(c.ar)}</bdi></b></span>`).join('') + '</div>';
const whoSays = (u, label) => {
  const S = Object.fromEntries(u.sentences.map(s => [s.id, s]));
  const ws = [...u.whosays].sort((a, b) => a.stage - b.stage || a.id.localeCompare(b.id));
  for (const w of ws) if (!S[w.support] || !S[w.support].ar.includes(w.quote.replace(/^«|»$/g, ''))) throw Error('who-says quote not verbatim: ' + w.id);
  return facesRow(u, label) + '<ul lang="ar">' + ws.map(w => `<li>${esc(w.quote)} ○</li>`).join('') + '</ul>';
};
const sequence = (u, order) => {
  const S = Object.fromEntries(u.sentences.map(s => [s.id, s]));
  const ev = Object.fromEntries(u.events.map(e => [e.id, e]));
  return '<ul lang="ar">' + order.map(id => { const e = ev[id]; if (!e || !S[e.sentence]) throw Error('event missing: ' + id); return `<li>⬜ ${esc(S[e.sentence].ar)}</li>`; }).join('') + '</ul>';
};
const GEN = {
  'u1-ws-main': () => whoSays(E.UNITS['unit-01'], 'who says — the five faces, numbered'),
  'u1p-ws': () => whoSays(E.UNITS['unit-01p'], 'who says — four faces and the pen, numbered'),
  'u1-seq-main': () => sequence(E.UNITS['unit-01'], ['e3', 'e1', 'e4', 'e2']),
  'u1p-seq': () => sequence(E.UNITS['unit-01p'], ['re3', 're1', 're2']),
};
for (const [key, fn] of Object.entries(GEN)) {
  const re = new RegExp('<!-- gen:' + key + ' -->[\\s\\S]*?<!-- /gen:' + key + ' -->');
  if (!re.test(html)) throw Error('Generated block missing in the Studio source: ' + key);
  html = html.replace(re, '<!-- gen:' + key + ' -->' + fn() + '<!-- /gen:' + key + ' -->');
}

/* ---- 4 · the Unit 2 art assignment (unchanged from Version 43/44) ---- */
html = html.replace(/^  const RICH_UNIT2 = .*;\n/m, '');
html = html.replace(/  function withRichArt\(unit\)\{[\s\S]*?\n  \}\n(?=  function setU)/, '');
html = html.replace('U=withRichArt(E.UNITS[unitId]);', 'U=E.UNITS[unitId];');
html = html.replace(/^  const img=.*;$/m, '  const img=(id,cls)=>id?(id.startsWith("assets/art/")?`<img class="${cls||\'timg\'} rich-art" src="${id}" alt="">`:`<svg class="${cls||\'timg\'}" viewBox="0 0 120 100" aria-hidden="true"><use href="#${id}"/></svg>`):"";');
const oldPathToSlot = new Map();
for (const slot of manifest.slots) {
  oldPathToSlot.set('assets/art/unit2-rich/' + slot.id + '.png', slot.id);
  oldPathToSlot.set(slot.delivered, slot.id);
  for (const old of slot.superseded || []) oldPathToSlot.set(old.site_path, slot.id);
}
html = html.replace(/src="(assets\/art\/unit2-rich\/[^" ]+\.png)"/g, (all, filename) => oldPathToSlot.has(filename) ? 'src="' + assets[oldPathToSlot.get(filename)] + '"' : all);
const strip = (ids, label) => '<div class="picseq" aria-label="' + label + '">' + ids.map((id, i) => '<span class="picfr"><b>' + (i + 1) + '</b><img src="' + assets[id] + '" alt=""></span>').join('') + '</div>';
html = html.replace(/<div class="picseq" aria-label="Version A">.*?<\/div>/, strip(bindings.version_a, 'Version A'));
const noteStart = html.indexOf('<section class="view" id="v-note2">');
const noteEnd = html.indexOf('</section>', noteStart);
if (noteStart < 0 || noteEnd < 0) throw Error('Missing Unit 2 notebook');
let note = html.slice(noteStart, noteEnd).replace('Picture frames are empty until illustration.', 'Picture frames reuse the student-book strips (SC-100).');
html = html.slice(0, noteStart) + note + html.slice(noteEnd);
const thirdStart = html.indexOf('<section class="view" id="v-note3">');
const thirdEnd = html.indexOf('</section>', thirdStart);
let third = html.slice(thirdStart, thirdEnd);
const retrievalStart = third.indexOf('<span class="code">N4</span>');
if (retrievalStart < 0) throw Error('Missing Unit 3 delayed retrieval');
const pictures = '<div class="nbpics">' + bindings.unit3_retrieval.map((id, i) => '<span class="nbpic"><img class="rich-art" src="' + assets[id] + '" alt=""><b>' + (i + 1) + '</b></span>').join('') + '</div>';
third = third.slice(0, retrievalStart) + third.slice(retrievalStart).replace(/<div class="nbpics">.*?<\/div>/, pictures);
third = third.replace('reprinted from the student book once its illustrations exist (SC-100), empty until then', 'reprinted byte-for-byte from the student-book strips (SC-100)');
html = html.slice(0, thirdStart) + third + html.slice(thirdEnd);
html = html.replace(/VERSION \d+/g, 'VERSION ' + version);
if (html.includes('withRichArt') || html.includes('RICH_UNIT2')) throw Error('Runtime assignment patch remains');
if (/teacher\.html/i.test(html)) throw Error('Teacher page linked in Studio');
if (/أَنَا وَلَدٌ|أَنَا بِنْتٌ/.test(html)) throw Error('First-person gender self-categorisation printed (SC-021)');

/* ---- 5 · outputs ---- */
const wrapper = '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><link rel="icon" href="data:,"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><style>[hidden]{display:none!important}</style>';
const document = wrapper + html;
fs.mkdirSync(output, { recursive: true });
for (const name of ['index.html', '404.html']) fs.writeFileSync(path.join(output, name), document);
fs.writeFileSync(path.join(__dirname, 'school_course_studio.html'), html);

/* the teacher's page is generated from the same engine (it refuses to build on a failing unit) and wrapped the same way */
execFileSync('python3', [path.join(__dirname, 'build_teacher_pages.py')], { cwd: root, stdio: 'inherit' });
const teacherBody = fs.readFileSync(path.join(__dirname, 'intaliq1_teacher_pages.artifact-body.html'), 'utf8');
fs.writeFileSync(path.join(output, 'teacher.html'), wrapper + teacherBody);
if (output !== root) {
  fs.cpSync(path.join(root, 'assets'), path.join(output, 'assets'), { recursive: true });
  fs.copyFileSync(path.join(root, '.nojekyll'), path.join(output, '.nojekyll'));
} else fs.writeFileSync(path.join(root, 'teacher.html'), wrapper + teacherBody);

const review = '<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>INTALIQ Unit 2 Art Review</title><style>body{font:14px Arial;margin:24px;color:#202426;background:#fff}h1{font-size:24px}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:20px}figure{margin:0;min-width:0}img{width:100%;height:180px;object-fit:contain}figcaption{overflow-wrap:anywhere;margin-top:8px}small{display:block;color:#555}</style><h1>INTALIQ Unit 2</h1><main>' + manifest.slots.map(slot => '<figure><img src="' + path.basename(slot.delivered) + '" alt="' + slot.id + '"><figcaption>' + slot.id + '<small>' + slot.kind + '</small></figcaption></figure>').join('') + '</main></html>';
fs.writeFileSync(path.join(output, 'assets/art/unit2-rich/review.html'), review);
const prompts = JSON.parse(read('assets/art/unit2-rich/production-prompts.json'));
const corrections = Object.fromEntries(manifest.slots.filter(slot => slot.accepted.prompt && slot.delivered.endsWith('-v' + version + '.png')).map(slot => [slot.id, { method: slot.accepted.method, prompt: slot.accepted.prompt, reason: slot.accepted.correction_reason }]));
if (Object.keys(corrections).length) prompts['version' + version + '-corrections'] = corrections;
fs.writeFileSync(path.join(output, 'assets/art/unit2-rich/production-prompts.json'), JSON.stringify(prompts, null, 2) + '\n');
fs.writeFileSync(path.join(__dirname, 'build_report.json'), JSON.stringify({ version, units: report }, null, 2) + '\n');
console.log('Text build: Version ' + version + '; engine embedded from engine_core.js; generated blocks refreshed; teacher.html built; index and 404 generated from one source.');
console.log(JSON.stringify(report));
