# Intaliq 1 — Working in parallel sessions

*Written 2026-10-02 on the owner's direction to run text production and illustration in separate chats. Binding on every session attached to this project. The project's documents are the only shared memory; a chat's own history is private to it and counts for nothing in the others.*

---

## 1 · The sessions and what each owns

| session | name the owner uses | owns (may create and rewrite) | never touches |
|---|---|---|---|
| **Text** | *Intaliq Text* | Gate A briefs, story drafts, measurements, the thirty-line audits, the ledgers (vocabulary, grammar, chunks, recycling, verb inventory), outcomes sheets, scope and curriculum maps, teacher's pages, engine content, **the Studio build** (`build_*.py`, `engine_core.js`, `school_course_studio.html`, `deploy/`), the production records, the Author's Page | art files, art manifests, art reviews, the Cast Bible reservation rows for drawn figures |
| **Art** | *Intaliq Art* | `INTALIQ1_ART_PACKAGE_SPEC.md`, the art manifests, round reviews, the style reference set, the Cast Bible §2 style rows and reservation-table rows for drawn figures, visual plans, the accepted asset set and `art_assets_map.json` | story texts, ledgers, engine content, the Studio build, deploy files |
| **Publisher** | *Intaliq Publisher* (Claude Code on the Mac) | `git add / commit / push` of the clone | the content of any file |

**Illustration enters the Studio in one place:** the Art session delivers *accepted* files under `assets/art/` plus `art_assets_map.json` (slot id → file) into the project and the exchange folder; the Text session's build consumes the map (TF-8) and produces the Studio version. Neither session edits `index.html` by hand.

## 2 · The register

The decision register stays **one file, one sequence**. Either session may append an entry, under these rules: (a) `project_read` the register immediately before appending — never append from memory of its last number; (b) take the next free SC number at that moment; (c) write the entry with the session's name in its first line (*Recorded by Intaliq Art*); (d) `project_write` immediately. A ruling the owner gives in one chat is recorded by **that** chat. The other chat learns it **from the register, not from the owner's paraphrase** — charter §8, *no approval by relay*, applies between sessions exactly as it applies between people. If two sessions appended the same number (both wrote before either read), the later writer renumbers its own entry and notes the collision; nothing is deleted.

**Where the register lives ⟨SC-118, 2026-10-10⟩.** The register is appended **only in the project** (`claude/SCHOOL_COURSE_DECISION_REGISTER.md`). The copy under the repository's `source/governance/` is an **export for the auditor**, re-made from the project copy by the Publisher; it is never appended to. A session that cannot reach the project — a Codex or Claude Code task on the Mac, say — records the owner's ruling in its status-board section as **pending transcription**, quoting the owner's words, and **takes no number**; the next session with project access transcribes it verbatim into the register and gives it the next free number. This is how the 2026-10-10 fork (two SC-114s, two Version 44s) was closed and how it is not repeated. Versions, likewise, are issued only against the project register's sequence (§5).

## 3 · Read before you write

Every session starts a work turn by reading, in this order: `INTALIQ1_SESSION_STATUS.md` (what the others did last) · the register's last three entries · `SCHOOL_COURSE_AUTHORS_PAGE.md`. Before rewriting **any** project document, `project_read` it first — the other session may have changed it since. A document in the other session's column is read-only; a needed change is requested through `INTALIQ1_SESSION_STATUS.md` under *asks*, not made.

## 4 · The status file

`INTALIQ1_SESSION_STATUS.md` has one section per session. At the end of every working turn a session rewrites **its own section only**: what it changed (file names), what it is waiting on, what it asks of the other session, and the owner rulings it recorded (SC numbers). Three lines are enough; a stale section is a defect.

## 5 · Versions and builds

Studio versions are issued by the Text session only, in sequence. The Art session never claims a version. The release gate (`tools/verify_release.py`, TF-9) runs in the Text session before any files go to the clone; the Publisher pushes only what the Text session wrote into the clone and says nothing about content.

## 6 · The owner's part

Say which chat you are in when it matters (a ruling, a hand-over). Give a ruling in the chat whose work it concerns; it reaches the other through the register. Carry files between ChatGPT and the exchange folder as before. Nothing else.
