"""Focused Unit 2 art checks, supplementary to the mandatory TF-9 release gate."""
import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path
from PIL import Image, ImageChops
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
parser = argparse.ArgumentParser()
parser.add_argument('--base-url', default='http://127.0.0.1:8877/')
parser.add_argument('--version', type=int, default=43)
parser.add_argument('--out', type=Path)
args = parser.parse_args()
args.out = args.out or ROOT / f'art-production/v{args.version}-checks'
args.out.mkdir(parents=True, exist_ok=True)
assets = json.loads((ROOT / 'art_assets_map.json').read_text())
manifest = json.loads((ROOT / 'assets/art/unit2-rich/manifest.json').read_text())
bindings = json.loads((ROOT / 'source/cast-and-art/unit2_art_bindings.json').read_text())
html = (ROOT / 'index.html').read_text()
assert (ROOT / '404.html').read_bytes() == (ROOT / 'index.html').read_bytes(), '404 differs from index'
assert f'VERSION {args.version}' in html and 'RICH_UNIT2' not in html and 'withRichArt' not in html
assert len(assets) == len(manifest['slots']) == 69
report = {'version': args.version, 'accepted_hashes': 0, 'version_a': [], 'viewports': [], 'errors': []}
for slot in manifest['slots']:
    assert assets[slot['id']] == slot['delivered']
    assert hashlib.sha256((ROOT / slot['delivered']).read_bytes()).hexdigest() == slot['accepted']['sha256']
    for file in [slot['accepted']['path'], slot['accepted']['source_candidate']]:
        assert hashlib.sha256((ROOT / 'art-production' / file).read_bytes()).hexdigest() == slot['accepted']['sha256'], 'Accepted archive differs'
    for old in slot.get('superseded', []):
        assert hashlib.sha256((ROOT / old['site_path']).read_bytes()).hexdigest() == old['sha256'], 'Superseded asset altered'
    report['accepted_hashes'] += 1
    if slot['id'] in ('u2-va-2', 'u2-va-7'):
        derivation = slot.get('derivation')
        assert derivation, slot['id'] + ': no pixel-preserving derivation record'
        original = Image.open(ROOT / assets[derivation['source_slot']]).convert('RGBA')
        assert hashlib.sha256((ROOT / assets[derivation['source_slot']]).read_bytes()).hexdigest() == derivation['source_sha256']
        insert = ROOT / 'source/cast-and-art/references/rich-cartoon/version-a-generated-book.png'
        assert hashlib.sha256(insert.read_bytes()).hexdigest() == derivation['generated_book_sha256']
        revised = Image.open(ROOT / slot['delivered']).convert('RGBA')
        assert original.size == revised.size
        difference = ImageChops.difference(original, revised).convert('RGB')
        bbox = difference.getbbox()
        assert bbox, 'Version A has no change'
        x, y, width, height = derivation['changed_rect']
        assert bbox[0] >= x and bbox[1] >= y and bbox[2] <= x + width and bbox[3] <= y + height, 'Changes outside authorized region'
        report['version_a'].append({'slot': slot['id'], 'changed_bbox': bbox, 'outside_pixels_identical': True})

engine_check = """const E=require('./source/pipeline/engine_core.js');const result={};for(const id of ['unit-02','unit-02p']){const u=E.UNITS[id],q=E.qc(u,E.gen(u));if(q.failed.length)throw Error(JSON.stringify(q.failed));for(const group of ['items','cast','sentences','contrasts','facts','events','findit','retrieval'])if(u[group].some(x=>!x.img||!x.img.startsWith('assets/art/')))throw Error(id+' unassigned '+group);result[id]={activities:q.ok.length,words:E.canonCheck(u).words,pictureActivities:q.ok.filter(a=>['arabic_to_picture','picture_to_arabic'].includes(a.type)).length};}console.log(JSON.stringify(result));"""
report['engine'] = json.loads(subprocess.check_output(['node', '-e', engine_check], cwd=ROOT, text=True))
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(channel='chrome')
    page = browser.new_page()
    page.on('pageerror', lambda error: report['errors'].append(str(error)))
    for width in [1180, 390]:
        page.set_viewport_size({'width': width, 'height': 900})
        for route in ['unit-02/student', 'unit-02/notebook', 'unit-03/notebook']:
            page.goto(args.base_url + 'index.html#' + route)
            page.locator('.view.on img[src*="unit2-rich"]').first.wait_for()
            images = page.locator('.view.on img[src*="unit2-rich"]')
            images.evaluate_all('async elements => { await Promise.all(elements.map(e => e.decode())); }')
            if route == 'unit-02/student':
                a = page.locator('[aria-label="Version A"] img').evaluate_all('elements=>elements.map(e=>e.getAttribute("src"))')
                assert a == [assets[slot] for slot in bindings['version_a']]
            if route == 'unit-02/notebook':
                notebook = images.evaluate_all('elements=>elements.map(e=>e.getAttribute("src"))')
                expected = [assets['u2-s1-' + str(i)] for i in range(1, 9)] + [assets['u2-s2-' + str(i)] for i in range(1, 7)]
                assert notebook == expected, 'Notebook is not exact student-strip reuse'
            if route == 'unit-03/notebook':
                assert images.evaluate_all('elements=>elements.map(e=>e.getAttribute("src"))') == [assets[slot] for slot in bindings['unit3_retrieval']]
            page.screenshot(path=str(args.out / (route.replace('/', '-') + '-' + str(width) + '.png')), full_page=True)
        for pathway in ['vocab', 'reading', 'reading2']:
            page.goto(args.base_url + 'index.html#unit-02/practice')
            page.reload()
            page.locator('[data-h="' + pathway + '"]').click()
            for step in range(4):
                art = page.locator('#pr-stage img.rich-art')
                assert art.count(), 'Missing practice image'
                art.evaluate_all('async elements => { await Promise.all(elements.map(e => e.decode())); }')
                if not step:
                    page.screenshot(path=str(args.out / ('practice-' + pathway + '-' + str(width) + '.png')))
                page.locator('#x-next').click()
            assert page.locator('#pr-stage img.rich-art').count()
        if args.version >= 44:
            page.goto(args.base_url + 'index.html#unit-02/practice')
            page.reload()
            for unit in ['unit-02', 'unit-02p']:
                assert page.evaluate('id => window.SC_ENGINE.UNITS[id].items.find(i => i.id === "haqiba").img', unit) == assets['obj-bag']
            queue = page.evaluate('''() => {
                const E = window.SC_ENGINE, u = E.UNITS['unit-02'];
                const {ok} = E.qc(u, E.gen(u));
                return [...ok.filter(a => a.type === 'explore').slice(0, 6),
                        ...ok.filter(a => a.type === 'arabic_to_picture'),
                        ...ok.filter(a => a.type === 'picture_to_arabic')];
            }''')
            page.locator('[data-h="vocab"]').click()
            found = []
            for index, activity in enumerate(queue):
                if activity.get('item') == 'haqiba' and activity['type'] in ['arabic_to_picture', 'picture_to_arabic']:
                    art = page.locator('#pr-stage img[src="' + assets['obj-bag'] + '"]')
                    assert art.count(), 'Brown bag missing in live picture task'
                    art.evaluate_all('async elements => { await Promise.all(elements.map(e => e.decode())); }')
                    page.screenshot(path=str(args.out / ('brown-bag-' + activity['type'] + '-' + str(width) + '.png')))
                    found.append(activity['type'])
                    if len(found) == 2:
                        break
                if activity['type'] == 'explore':
                    page.locator('#x-next').click()
                else:
                    page.locator('[data-c="' + activity['correct'] + '"]').click()
                page.wait_for_function('expected => document.getElementById("pr-count").textContent.startsWith("TASK " + expected + " OF")', arg=index + 2)
            assert len(found) == 2, 'Both bag picture-recognition families must render'
            report.setdefault('brown_bag', []).append({'viewport': width, 'path': assets['obj-bag'], 'families': found})
        report['viewports'].append(width)
    page.set_viewport_size({'width': 800, 'height': 400})
    slots = ['u2-s1-3', 'u2-s1-5', 'u2-s1-6', 'u2-s2-4', 'u2-va-2', 'u2-va-7']
    page.set_content('<style>body{font:14px Arial}main{display:flex;gap:12px;flex-wrap:wrap}figure{margin:0}img{width:118px;height:98px;object-fit:contain}figcaption{font-size:12px}</style><main>' + ''.join('<figure><img src="' + args.base_url + assets[slot] + '"><figcaption>' + slot + '</figcaption></figure>' for slot in slots) + '</main>')
    page.locator('img').evaluate_all('async elements => { await Promise.all(elements.map(e => e.decode())); }')
    page.screenshot(path=str(args.out / 'strip-size-corrections.png'))
    for slot in manifest['slots']:
        response = page.request.get(args.base_url + slot['delivered'])
        assert response.ok and hashlib.sha256(response.body()).hexdigest() == slot['accepted']['sha256']
    browser.close()
assert not report['errors'], report['errors']
(args.out / 'unit2-report.json').write_text(json.dumps(report, indent=2) + '\n')
print(json.dumps(report, indent=2))
