# Editorial decisions — official textbook

Teaching-team file, not rendered into the student book.

## 2026-08-30 — New repo decisions

- **Authoritative sources for every chapter**: the per-lecture scenario files
  (`lecture-scenarios/`) plus `00-README-template.md`. Where they clash with
  the prototype's editorial log (below), **the scenarios supersede**.
  Confirmed points of supersession:
  - every lecture has a driving-question opener and closing answer
    (old "keep pages lean without driving-question sections" is superseded);
  - one named caveat box per lecture, styled navy/teal, never yellow
    (old "no note boxes" is superseded in form, kept in spirit: one box,
    scope caveats only, placed after consolidation);
  - data quantiles/IQR live in the L1–L2 descriptive material; Lecture 6
    keeps only quantiles of model distributions;
  - one-sided alternatives are taught fully in Lecture 10 (not "conceptual
    orientation in L9"); exams remain two-sided.
- **Build**: Quarto book (replaces bookdown/gitbook). Same R chunks; native
  callouts/cross-refs/search; per-page include for the planned analytics
  layer and widgets; renders to `docs/` for GitHub Pages exactly as before.
  `execute-dir: project` so all chapters read `data/…` from the repo root.
- **No hidden objects**: setup chunks contain chunk options only; every
  analysis object is constructed in visible code on the page where it is
  used. Display-only figure code may stay `echo: false` when self-contained.
- **Repo/URL**: `textbook-qm-ebi`, published at
  valentinamel.github.io/textbook-qm-ebi, linked from Canvas. The prototype
  URL stays live, internal use only, no redirect.
- Stable anchors kept (`#b02`, …); chapter codes kept in filenames.
- Agreed content redistribution (from the scenario set): variance & SD
  b04→b03; independence of events b05→b04; t distribution b08→b09;
  one-sided alternatives b09→b10; coefficient inference i02→i03.
- Intermediate running units: thousands of dollars, with one short worked
  note on rescaling (project-todo decision 2026-08-29).
- **Utility writing in every lecture** (2026-08-30): each chapter's
  After-class practice ends with a "Make it yours" two-sentence
  utility-value question anchored to the student's EiA venture with a
  business-they-know fallback, closing with a standing pointer that the
  task (and any other chapter task) can be discussed with the Tilly bot. Complements (does not replace) the
  per-tutorial utility prompts from the project todo.
- "Try it" faded tasks use the warm orange pencil style (callout-caution),
  never red/alarm styling; checks and model answers use quiet teal
  callouts.

## Prototype editorial log (carried forward for history)

The full prototype log lives in
`Prototype materials/textbook-prototype/INTERNAL_EDITORIAL_DECISIONS.md`.
Everything there remains in force **except** the superseded points listed
above. Highlights still in force: restrained navy/teal visual system;
three-phase colour language (blue/green/purple); collapsed model answers
after every substantive question; tutorials branded as exam preparation
sessions; broad source gender category only, never inferred from names;
Season 17 excluded; link, don't republish, copyrighted readings; positive
quantile notation matching `qnorm()`/`qt()`; formula sheet and exam PDF from
one shared source.
