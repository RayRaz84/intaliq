const fs = require('node:fs');
const path = require('node:path');
const crypto = require('node:crypto');
const root = path.resolve(__dirname, '../..');
const [id, source, prompt, reason, method = 'built-in image_gen'] = process.argv.slice(2);
if (!id || !source || !prompt || !reason) throw Error('Expected slot, source PNG, prompt, and correction reason');
const manifestPath = path.join(root, 'assets/art/unit2-rich/manifest.json');
const manifest = JSON.parse(fs.readFileSync(manifestPath));
const slot = manifest.slots.find(slot => slot.id === id);
if (!slot) throw Error('Unknown slot');
const bytes = fs.readFileSync(source);
if (bytes.subarray(0, 8).toString('hex') !== '89504e470d0a1a0a') throw Error('Expected PNG');
const sitePath = 'assets/art/unit2-rich/' + id + '-v43.png';
const candidate = 'rich-cartoon-candidates/unit2/' + id + '/v43/' + id + '.png';
const acceptedPath = 'accepted-rich/unit2/assets/art/' + slot.file.replace('.png', '-v43.png');
for (const file of [sitePath, 'art-production/' + candidate, 'art-production/' + acceptedPath]) {
  const target = path.join(root, file);
  fs.mkdirSync(path.dirname(target), { recursive: true });
  if (fs.existsSync(target) && !fs.readFileSync(target).equals(bytes)) throw Error('Refusing to overwrite correction ' + file);
  fs.writeFileSync(target, bytes);
}
slot.superseded = [...(slot.superseded || []), { ...slot.accepted, reason }];
slot.accepted = {
  file: slot.file.replace('.png', '-v43.png'), path: acceptedPath,
  site_path: sitePath, source_candidate: candidate,
  sha256: crypto.createHash('sha256').update(bytes).digest('hex'),
  size: bytes.readUInt32BE(16) + 'x' + bytes.readUInt32BE(20),
  accepted_at: '2026-10-10', by: 'Codex visual review after owner correction request',
  method, prompt, correction_reason: reason
};
slot.delivered = sitePath;
fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2) + '\n');
const mapPath = path.join(root, 'art_assets_map.json');
const map = JSON.parse(fs.readFileSync(mapPath));
map[id] = sitePath;
fs.writeFileSync(mapPath, JSON.stringify(map, null, 2) + '\n');
const statePath = path.join(root, 'art-production/state/unit2-rich-cartoon.json');
const state = JSON.parse(fs.readFileSync(statePath));
state.slots[id] = { status: 'accepted', accepted: slot.accepted, superseded: slot.superseded };
fs.writeFileSync(statePath, JSON.stringify(state, null, 2) + '\n');
console.log(id + ': exact corrected PNG preserved at ' + sitePath);
