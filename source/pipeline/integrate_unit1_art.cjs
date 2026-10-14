/* Build-time Unit 1 PNG assignment. Accepted image bytes are never transformed. */
module.exports = function integrateUnit1Art(html, manifest) {
  const bySymbol = Object.fromEntries(manifest.slots.map(s => [s.engine_symbol, s.delivered]));
  const esc = s => String(s).replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;');
  const img = (symbol, attrs = '') => `<img class="rich-art" src="${bySymbol[symbol]}" alt="" ${attrs}>`;
  for (const view of ['v-student', 'v-note', 'v-note2']) {
    const re = new RegExp('(<section class="view" id="' + view + '">)([\\s\\S]*?)(</section>)');
    if (!re.test(html)) throw Error('Missing Unit 1 view: ' + view);
    html = html.replace(re, (all, start, body, end) => {
      if (view === 'v-student') {
        /* Move the exact existing Arabic labels outside the art, without generating typography. */
        body = body.replace(/<svg viewBox="0 0 900 290"[\s\S]*?<\/svg>/, old => {
          const labels = [...old.matchAll(/<text\b[^>]*>([\s\S]*?)<\/text>/g)].map(m => m[1]);
          if (labels.length !== 7) throw Error('Unexpected Unit 1 B1 label inventory: ' + labels.length);
          const people = ['av-omar', 'av-sara', 'av-huda', 'obj-list'];
          return `<div class="u1-b1" data-u1-art-release="30d90e8"><p class="arabic" lang="ar">${labels[0]}</p>` +
            img('b1-spread', 'style="width:100%;height:auto;display:block"') +
            '<div class="picseq u1-b1-labels">' + people.map((id, i) =>
              `<span class="picfr">${img(id)}<span class="arabic" lang="ar">${labels[i + 1]}</span></span>`).join('') + '</div>' +
            labels.slice(5).map(s => `<p class="arabic" lang="ar">${s}</p>`).join('') + '</div>';
        });
        body = body.replace('In-house stick-figure art (SC-034); the rich-cartoon redraw (SC-113) is queued behind the owner\'s Unit 1 slot list.',
          'Accepted Unit 2 rich-cartoon PNG style adopted for Unit 1 by the owner; the book, notebook and digital practice reuse the exact accepted files.');
        /* The legacy SVG greeting escaped the old sweep. Use Unit 1's licensed CH-01. */
        body = body.replace('<p class="arabic" lang="ar">مَرْحَبًا</p>',
          '<p class="arabic" lang="ar">السَّلَامُ عَلَيْكُمْ!</p>');
      }
      body = body.replace(/<svg\b([^>]*)>([\s\S]*?)<\/svg>/g, (old, attrs, contents) => {
        const uses = [...contents.matchAll(/<use\b[^>]*href="#([^"]+)"/g)];
        if (uses.length !== 1 || !bySymbol[uses[0][1]]) return old;
        const id = uses[0][1];
        if (id === 'av-tariq') throw Error('Production-only Tariq portrait exposed to learners');
        const label = attrs.match(/aria-label="([^"]*)"/)?.[1];
        const style = attrs.match(/style="([^"]*)"/)?.[1];
        return img(id, [label ? `aria-label="${esc(label)}"` : '', style ? `style="${esc(style)}"` : ''].filter(Boolean).join(' '));
      });
      if (body.includes(bySymbol['av-tariq'])) throw Error('Production-only Tariq portrait exposed to learners');
      if (view === 'v-student') {
        const intro = body.match(/<div class="picseq">([\s\S]*?)<\/div>/)?.[1];
        const expected = manifest.main_strip.map(id => manifest.slots.find(s => s.id === id).delivered);
        const actual = [...(intro || '').matchAll(/<img[^>]*src="([^"]+)"/g)].map(m => m[1]);
        if (JSON.stringify(actual) !== JSON.stringify(expected)) throw Error('Unit 1 main strip assignment changed');
      } else if (view === 'v-note') {
        const actual = [...body.matchAll(/<div class="nbpics">([\s\S]*?)<\/div>/g)].map(row =>
          [...row[1].matchAll(/<img[^>]*src="([^"]+)"/g)].map(m => m[1]));
        const expected = [manifest.main_strip, manifest.second_strip].map(ids =>
          ids.map(id => manifest.slots.find(s => s.id === id).delivered));
        if (JSON.stringify(actual) !== JSON.stringify(expected)) throw Error('Unit 1 notebook strip does not reuse student PNGs');
      } else {
        /* SC-100: Unit 2 N4 reuses Unit 1 faces, including Karim's pen-bearing portrait. */
        const retrieval = body.slice(body.indexOf('<span class="code">N4</span>'));
        const row = retrieval.match(/<div class="nbpics">([\s\S]*?)<\/div>/)?.[1] || '';
        const actual = [...row.matchAll(/<img[^>]*src="([^"]+)"/g)].map(m => m[1]);
        const expected = ['av-razan', 'av-omar', 'av-huda', 'av-karim-pen'].map(id => bySymbol[id]);
        if (JSON.stringify(actual) !== JSON.stringify(expected) || /<svg\b/.test(row))
          throw Error('Unit 2 N4 must reuse the four accepted Unit 1 portrait PNGs');
      }
      return start + body + end;
    });
  }
  html = html.replace('function setU(unitId){U=E.UNITS[unitId];N=E.normalize(U);',
    'function setU(unitId){document.getElementById("v-practice").dataset.artUnit=unitId;U=E.UNITS[unitId];N=E.normalize(U);');
  /* The named portrait and phrase supports need the same sizing as the existing SVG consumers. */
  if (!html.includes('/* Unit 1 exact PNG layout */')) html = html.replace('</style>', `
/* Unit 1 exact PNG layout */
.u1-b1-labels .picfr{width:160px;text-align:center}
.u1-b1-labels img{margin:auto}
#v-practice[data-art-unit^="unit-01"] .face img{width:74px;height:74px;object-fit:contain}
#v-practice[data-art-unit^="unit-01"] .mini img{width:90px;height:74px;object-fit:contain}
#v-practice[data-art-unit^="unit-01"] .vcard img{width:126px;height:96px;object-fit:contain}
#v-student .stpanel .art img{width:100%;max-width:280px;height:130px;object-fit:contain}
#v-student img[aria-label="the class picture: seven of the eight children on the list"]{height:auto}
</style>`);
  return html;
};
