# Unit 1 — what is still missing (audit re-run 2026-09-12, after SC-050…054)

*The School Course · Level 1 · Unit 1 «مَنْ أَنْتَ؟» · every count below is machine-generated from the canonical data and from a sweep of the rendered products. Nothing here is estimated.*

---

## 0. What the sweep confirms is sound

| check | result |
|---|---|
| Engine + QC | **106 + 65 activities, 0 suppressed** |
| Drift (engine data vs printed story) | **0** — every canonical sentence and quote verbatim |
| Roll check (SC-054) | all 8 roster names resolve to a Cast Bible character |
| Marker check (SC-053) | 25 figures defined, every base figure recorded in the bible |
| Notebook | 8 sheets covering 10 pages |
| Student book | 6 sheets, can-do page last |
| Page errors on render | 0 |

Language, data integrity and cast are in good order. **Everything below is either new or previously known.**

---

## 1. NEW — two core items get no in-context activity at all

**وَلَدٌ and بِنْتٌ generate zero `meaning_in_context` activities.** The platform carries them with an explore card and two picture-matching tasks, and nothing else.

The cause is a data-format accident, not a design choice. Item surfaces are stored **sometimes as citation forms and sometimes as text surfaces**, with nothing marking which is which:

- `walad` = **وَلَدٌ**, but the story only ever says **وَلَدًا** and **الْوَلَدُ**
- `bint` = **بِنْتٌ**, but the story says **بِنْتًا** and **الْبِنْتُ**

The generator's eligibility test is a whole-word match of the item's surface against the sentence (SC-047), so these two never match anything and their whole activity family is silently skipped. Nothing fails; the activities simply never exist.

This matters more than two items would suggest: **the boy/girl pair is what the هٰذَا/هٰذِهِ contrast and the صَدِيق/صَدِيقَة gender rule both rest on.**

## 2. NEW — the encounter table cannot be mechanically re-derived

The same citation-form ambiguity means the story document's encounter table counts **families** (the لِـ family, the عِنْدَ family, يَقُول/قَالَ together) while the data stores **single surfaces**. A fresh machine count of the stored surfaces does not reproduce the recorded table, and cannot.

The table is not wrong — the families really are there. It is **unverifiable**, which under SC-050 (*a stated count is re-run at the moment it is stated*) is its own defect. The fix is to give each item an explicit `forms: []` list so one script can count what the table claims.

## 3. NEW — the pictures and the text tell different stories

The story data references **eight** frames. The printed six-picture strip shows **six**.

The two that exist as finished art and are **not on the page**:

- **`sc-alone`** — رزان alone between two empty circles: the «لَيْسَ لَهَا صَدِيقٌ» low point, *added to the text under SC-047* and never added to the strip.
- **`sc-tariq`** — عمر with the list, «لِي صَدِيقٌ: طَارِق!»: the unit's signature frame, also from SC-047.

So the strip still tells the **pre-SC-047 story** while the text tells the current one, and a child who retells from the pictures cannot reach the two sentences those insertions were made to teach. The notebook's N1 retell inherits the same six. This is the SC-052 failure shape exactly — two artefacts that must agree, drifting — and the guard added then covers sentences and quotes, **not illustrations**.

**Decision needed:** eight frames in the strip and eight retell lines in N1, or keep six and accept that two taught sentences have no picture.

## 4. NEW — five verb vignettes are drawn and orphaned, and B1 shows text instead

`vg-enter` · `vg-see` · `vg-say` · `vg-like` · `vg-sadiq` are finished and used nowhere. The build document's B1 spec calls for exactly these — *"the verbs as small vignette panels captioned in phrases"* — but the rendered spread carries **two lines of running Arabic** in their place.

That inverts the rule the spread exists to serve: **a Novice Low reader cannot read the caption that is supposed to teach them the verb.** Pictures were built for this and are sitting unused.

## 5. NEW — one two-value breach, and dead art from a retired story

- **B1's spread still carries teal** — the board fill and both caption lines. SC-053's purge covered the figure definitions; B1 is inline page markup and was missed. Mine.
- **`sc-party` · `sc-mix` · `sc-zayd`** belong to the **birthday-party story retired by SC-040**. They should be struck or explicitly parked, not left where a later build can pick them up by accident.
- The illustrations sheet still says *"Stick-figure art per SC-034"*, which SC-053 superseded.

## 6. Open decisions

- **The art style.** The pushed sample (D) is drawn and unapproved; the Studio still renders the SC-053 stick figures, and Cast Bible §2 describes those, not D. **Everything in §3–5 above is cheaper to fix after the style is settled, not before** — the frames would be drawn twice.
- **نُور's gender** — assigned girl, awaiting confirmation. هٰذَا/هٰذِهِ and صَدِيق/صَدِيقَة in every future unit turn on it.
- **A deeper roster** — the functional text spends 12 of its 30 words; room for about a dozen more reserved names.

## 7. Still not produced (unchanged, and all of it is production, not writing)

Recorded audio — the whole listening family stays suppressed by rule, so a four-skill course currently ships three · the authentic corner's **three photographs**, still empty slots · typeset print pages: no trim size, no spreads, no page count for either product · the book's unit opener · **B2, the preview panel** — one line of spec, never drafted · platform **A3/A5** (verb animations, animated story preview), Phase 2 per SC-028.

## 8. Cascade debt, mine (unchanged)

- **`SCHOOL_COURSE_U1_STATION.md`** — v1, predates eleven rulings: four cast portraits not five, bare words against SC-038, previews the v2 story, old possessive.
- **`SCHOOL_COURSE_UNIT1_BRIEF.md`** — still states a 22-item core (now 23) and still records approval of the retired birthday-party story.

## 9. QC never run

Native-ear collocation pass · B&P frequency eye-pass on the core · panel calibration · rendered-page verification of **actual typeset pages** (only the HTML preview has ever been checked).

---

## Where the unit stands

**The language is sound and the data is clean.** What this pass found is a different class of problem from the last three: not errors in the Arabic, but **three places where two artefacts that should agree don't** — items versus their text forms, pictures versus text, and built art versus the pages that were supposed to use it. Every one was found the same way, by comparing two things mechanically rather than reading either one.

**No outstanding writing.** Three outstanding decisions: the art style, the six-versus-eight frames, and نُور. The rest is production.
