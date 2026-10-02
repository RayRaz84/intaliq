#!/usr/bin/env python3
"""Rendered-page verification before any push (charter §8: rendered-page verification
and presence inventory before any release). Serves the deploy folder exactly as GitHub
Pages would, opens every route in a real browser, and reports what a reader would hit.

usage: python3 verify_release.py deploy/ [expected_version]
writes: verify_report.md and verify_shots/*.png (one per route) + verify_sheet.png
exit 1 on any blocker."""
import sys, os, json, threading, http.server, socketserver, functools, re
from pathlib import Path
from playwright.sync_api import sync_playwright

deploy = Path(sys.argv[1]).resolve()
expected_version = sys.argv[2] if len(sys.argv) > 2 else None
out = deploy.parent / "verify_shots"; out.mkdir(exist_ok=True)

# --- serve the folder like Pages (relative asset paths resolve the same way)
PORT = 8765
handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(deploy))
class Q(socketserver.TCPServer): allow_reuse_address = True
srv = Q(("127.0.0.1", PORT), handler)
threading.Thread(target=srv.serve_forever, daemon=True).start()
base = f"http://127.0.0.1:{PORT}/"

html = (deploy / "index.html").read_text(encoding="utf-8")
routes = [""] + re.findall(r"'([a-z0-9\-/]+)':'v-", html)
routes = list(dict.fromkeys(routes))

blockers, warnings, rows = [], [], []

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1180, "height": 900})
    console, failed, external = [], [], []
    pg.on("console", lambda m: console.append((m.type, m.text)) if m.type in ("error", "warning") else None)
    pg.on("requestfailed", lambda r: failed.append(r.url) if "127.0.0.1" in r.url else external.append(r.url))
    pg.on("response", lambda r: failed.append(r.url) if (r.status >= 400 and "127.0.0.1" in r.url) else None)

    for r in routes:
        url = base + ("#" + r if r else "")
        pg.goto(url, wait_until="networkidle")
        pg.wait_for_timeout(300)
        info = pg.evaluate("""() => {
          const on=document.querySelector('.view.on');
          const imgs=[...document.images];
          return {
            view: on ? on.id : null,
            chip: (document.querySelector('.chip,.badge,[class*=chip]')||{}).textContent || '',
            title: document.title,
            brokenImgs: imgs.filter(i=>i.complete && i.naturalWidth===0).map(i=>i.getAttribute('src')),
            emptyFrames: on ? on.querySelectorAll('.picfr.empty').length : 0,
            frames: on ? on.querySelectorAll('.picfr').length : 0,
            teacherLinks: [...document.querySelectorAll('a[href]')].filter(a=>/teacher/i.test(a.getAttribute('href'))).length,
            textOverflow: on ? [...on.querySelectorAll('*')].filter(e=>e.scrollWidth>e.clientWidth+4 && getComputedStyle(e).overflowX==='visible' && e.children.length===0).length : 0
          };
        }""")
        shot = out / f"{(r or 'home').replace('/', '_')}.png"
        pg.screenshot(path=str(shot), full_page=True)
        rows.append((r or "home", info, shot.name))
        if info["view"] is None: blockers.append(f"route #{r}: no view mounted")
        for s in info["brokenImgs"]: blockers.append(f"route #{r}: broken image {s}")
        if info["teacherLinks"]: blockers.append(f"route #{r}: {info['teacherLinks']} link(s) to the teacher page (SC-104)")
    b.close()
srv.shutdown()

# --- static checks
if expected_version and f"VERSION {expected_version}" not in html:
    blockers.append(f"version chip is not VERSION {expected_version}")
if "teacher.html" in html: blockers.append("index.html mentions teacher.html (SC-104)")
for m in re.findall(r'src="(assets/[^"]+)"', html):
    if not (deploy / m).exists(): blockers.append(f"asset referenced but missing: {m}")
srcs = re.findall(r'src="(assets/art/[^"]+)"', html)
dups = {s for s in srcs if srcs.count(s) > 1}
if dups: warnings.append("art files used more than once (check each is a legitimate reuse): " + ", ".join(sorted(dups)))
for ph in ("illustration pending", "not yet commissioned", "PROPOSED"):
    n = html.count(ph)
    if n: warnings.append(f'"{ph}" appears {n}× — confirm each is intended')
for k in ("answer key", "Answer key", "ANSWER KEY"):
    if k in html: blockers.append("the word 'answer key' appears in the Studio (SC-048)")
errs = [c for c in console if c[0] == "error" and "ERR_TUNNEL" not in c[1] and "net::" not in c[1]]
for u in external: warnings.append(f"external resource not reachable from this workspace (fine on Pages): {u[:90]}")
for e in errs: blockers.append(f"console error: {e[1][:160]}")
for f in failed: blockers.append(f"request failed: {f}")

# --- report
rep = ["# Release verification", f"folder: `{deploy}`", ""]
rep.append("| route | view | frames (empty) | broken imgs | shot |")
rep.append("|---|---|---|---|---|")
for r, i, s in rows:
    rep.append(f"| {r} | {i['view']} | {i['frames']} ({i['emptyFrames']}) | {len(i['brokenImgs'])} | {s} |")
rep += ["", "## Blockers", *([f"- {b}" for b in blockers] or ["- none"]),
        "", "## Warnings", *([f"- {w}" for w in warnings] or ["- none"])]
(deploy.parent / "verify_report.md").write_text("\n".join(rep), encoding="utf-8")

# contact sheet
try:
    from PIL import Image
    shots = [Image.open(out / s) for _, _, s in rows]
    W = 400; thumbs = []
    for im in shots:
        h = int(im.height * W / im.width); thumbs.append(im.resize((W, min(h, 1200))))
    cols = 4; rowsN = (len(thumbs) + cols - 1) // cols; H = max(t.height for t in thumbs)
    sheet = Image.new("RGB", (W * cols, H * rowsN), "white")
    for k, t in enumerate(thumbs): sheet.paste(t, ((k % cols) * W, (k // cols) * H))
    sheet.save(deploy.parent / "verify_sheet.png")
except Exception as e:
    warnings.append(f"contact sheet not made: {e}")

print("\n".join(rep))
sys.exit(1 if blockers else 0)
