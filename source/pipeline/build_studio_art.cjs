const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const { execFileSync } = require('node:child_process');
const root = path.resolve(__dirname, '../..');
const output = process.argv[2] ? path.resolve(process.argv[2]) : root;
const read = file => fs.readFileSync(path.join(root, file), 'utf8');
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
execFileSync('python3', [path.join(__dirname, 'build_unit02.py'), '--output', path.join(root, 'source/units/unit2/unit02_data.js')], { cwd: root, stdio: 'inherit' });
let html = read('source/pipeline/school_course_studio.html');
const data = read('source/units/unit2/unit02_data.js');
let engine = read('source/pipeline/engine_core.js');
for (const name of ['UNIT_02', 'UNIT_02P']) {
  const declaration = data.match(new RegExp('^const ' + name + ' = .*;$', 'm'));
  if (!declaration || !new RegExp('^const ' + name + ' = .*;$', 'm').test(html)) throw Error('Missing unit declaration: ' + name);
  html = html.replace(new RegExp('^const ' + name + ' = .*;$', 'm'), declaration[0]);
  engine = engine.replace(new RegExp('^const ' + name + ' = .*;$', 'm'), declaration[0]);
}
html = html.replace(/\/\* ---- Unit 2[^\n]*\*\//, data.match(/\/\* ---- Unit 2[^\n]*\*\//)[0]);
engine = engine.replace(/\/\* ---- Unit 2[^\n]*\*\//, data.match(/\/\* ---- Unit 2[^\n]*\*\//)[0]);
fs.writeFileSync(path.join(__dirname, 'engine_core.js'), engine);
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
html = html.replace(/VERSION \d+/g, 'VERSION 43');
if (html.includes('withRichArt') || html.includes('RICH_UNIT2')) throw Error('Runtime assignment patch remains');
if (/teacher\.html/i.test(html)) throw Error('Teacher page linked in Studio');
const wrapper = '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><link rel="icon" href="data:,"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><style>[hidden]{display:none!important}</style>';
const document = wrapper + html;
fs.mkdirSync(output, { recursive: true });
for (const name of ['index.html', '404.html']) fs.writeFileSync(path.join(output, name), document);
if (output === root) fs.writeFileSync(path.join(__dirname, 'school_course_studio.html'), html);
else {
  fs.cpSync(path.join(root, 'assets'), path.join(output, 'assets'), { recursive: true });
  fs.copyFileSync(path.join(root, 'teacher.html'), path.join(output, 'teacher.html'));
  fs.copyFileSync(path.join(root, '.nojekyll'), path.join(output, '.nojekyll'));
}
const review = '<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>INTALIQ Unit 2 Art Review</title><style>body{font:14px Arial;margin:24px;color:#202426;background:#fff}h1{font-size:24px}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:20px}figure{margin:0;min-width:0}img{width:100%;height:180px;object-fit:contain}figcaption{overflow-wrap:anywhere;margin-top:8px}small{display:block;color:#555}</style><h1>INTALIQ Unit 2</h1><main>' + manifest.slots.map(slot => '<figure><img src="' + path.basename(slot.delivered) + '" alt="' + slot.id + '"><figcaption>' + slot.id + '<small>' + slot.kind + '</small></figcaption></figure>').join('') + '</main></html>';
fs.writeFileSync(path.join(output, 'assets/art/unit2-rich/review.html'), review);
const prompts = JSON.parse(read('assets/art/unit2-rich/production-prompts.json'));
prompts['version43-corrections'] = Object.fromEntries(manifest.slots.filter(slot => slot.accepted.prompt).map(slot => [slot.id, { method: slot.accepted.method, prompt: slot.accepted.prompt, reason: slot.accepted.correction_reason }]));
fs.writeFileSync(path.join(output, 'assets/art/unit2-rich/production-prompts.json'), JSON.stringify(prompts, null, 2) + '\n');
console.log('Text build: Version 43; canonical engine assignments; index and 404 generated from one source.');
