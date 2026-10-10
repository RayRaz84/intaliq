> **Numbering note (SC-118, 2026-10-10).** The register entries this file cites by the repository copy's numbers are, in the governing project register: repository SC-114 → **SC-115** (Version 43 build), SC-115 → **SC-116** (Version A compositing), SC-116 → **SC-117** (brown bag, Version 44). The register is appended only in the project; this copy is an export.
>
> **Scope since Version 45 (SC-120).** `build_studio_art.cjs` is now the whole Text build: it also embeds `engine_core.js` into the Studio wholesale, regenerates the `<!-- gen:… -->` blocks from engine data, runs the teacher-page generator and writes `teacher.html`, and refuses on any undeliverable unit. See `INTALIQ_DEPLOYMENT.md` §Building. Build Version 45 with `INTALIQ_STUDIO_VERSION=45 node source/pipeline/build_studio_art.cjs`.

# Unit 2 Art Build

The final Text integration stage consumes `art_assets_map.json` and `source/cast-and-art/unit2_art_bindings.json`. It regenerates canonical Unit 2 data, copies its assignments into the engine, removes the earlier runtime assignment patch, and emits the Studio review version. Frozen prose is not edited.

From the repository root:

```sh
node source/pipeline/build_studio_art.cjs
node source/pipeline/build_studio_art.cjs art-production/release-43/deploy
```

The first command generates the source Studio, root `index.html` and identical `404.html`. The second stages a self-contained deploy directory with the same page bytes, teacher page, assets, and `.nojekyll`. Run this final stage after any earlier structural Studio build; do not publish the output of the historical Version 42 builder directly.

Install release dependencies in a local environment using `source/pipeline/requirements-release.txt`. With Python Playwright and Chrome available:

```sh
INTALIQ_BROWSER_CHANNEL=chrome INTALIQ_VERIFY_PORT=0 python source/pipeline/verify_release.py art-production/release-43/deploy 43
python source/pipeline/verify_unit2_art.py
```

The focused check expects a local preview at `http://127.0.0.1:8877/` (override with `--base-url`). TF-9 starts its own temporary server; port zero requests an available port. Neither check authorizes content approval. Read the official report and inspect its contact sheet before pushing; the focused check additionally blocks non-pixel-preserving Version A replacements, changed accepted hashes, missing canonical image fields, and incorrect notebook reuse.

The corrected raw PNGs are versioned siblings. Old production PNGs stay unchanged, with supersession reasons in the production manifest. Never run the historical ignored `art-production/sync-rich-integration.cjs` as a release stage: it is the runtime-patch approach superseded by this build.

SC-115 authorizes targeted compositing for Version A's two changed frames only. `python source/pipeline/derive_version_a.py` reproduces them from the original scenes and the tracked generated book insert (Pillow required). This is an Art-production operation, not part of the integration build; the build only consumes the accepted derived PNGs.

For the brown-bag follow-up build, issue Version 44 explicitly and verify it:

```sh
INTALIQ_STUDIO_VERSION=44 node source/pipeline/build_studio_art.cjs
node source/pipeline/build_studio_art.cjs art-production/release-44/deploy
INTALIQ_BROWSER_CHANNEL=chrome INTALIQ_VERIFY_PORT=0 python source/pipeline/verify_release.py art-production/release-44/deploy 44
python source/pipeline/verify_unit2_art.py --version 44
```

Without the version override, the build retains the source Studio's current version; it does not silently downgrade to 43. Art acceptance takes an optional final revision argument (for example `v44`) and retains old accepted PNGs.
