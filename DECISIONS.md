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
    keeps only quantiles of model distributions (confirmed 2026-10-06);
  - one-sided alternatives: superseded on 2026-10-06, see below (optional
    box in Lecture 10, not examined).
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

## 2026-10-06 — Freeze round (Claude's review, Gabriela's review, Valentina's decisions)

These points supersede earlier entries where they differ.

- **Exam aids (QM Basic)**: formula sheet attached, every probability or
  multiplier a question needs is printed in the question or is on the sheet
  (one row of t values, "use the closest df"). No reading of z or t tables
  anywhere in the course.
- **Chapter structure**: Before class, **Lecture material** (was "In
  class"), After class. Tutorials: "In the tutorial". The lecture covers the
  core of a chapter, the chapter is the full reference. Slides are not
  published. The text never describes the classroom session and never shows
  the lecturer's intentions. Student-facing wording only.
- **After class** always starts with "Read the lecture material (15
  minutes)". Minimum path: read, recall questions, then 10 minutes on the
  tasks that follow (about 35 minutes). Headings in plain words: "Recall
  questions", "Finish a half-worked example", "Review: ...".
- **Formal content**: core terms in short Definition boxes (examinable).
  Formal versions, derivations, and side topics in collapsed "Optional: ..."
  boxes (not examined). The older `.optional-box` div is no longer used.
- **Binomial**: one short section in Basic Lecture 8 (number of successes,
  mean and variance, one figure for the success-failure rule). No binomial
  probability calculations.
- **Success-failure rule**: np >= 10 and n(1-p) >= 10 (OpenIntro, Moore and
  McCabe, AP Statistics). The text says once that some books use 5.
- **One-sided tests**: one collapsed optional box at the end of Basic
  Lecture 10. Not covered in the lecture, not examined. All tests two-sided.
  (Supersedes "taught fully in Lecture 10".)
- **Data quantiles and IQR**: defined in Basic Lecture 1 (definition box,
  anchor `#b01-quartiles`). Lecture 6 refers back.
- **Lecture 9 / Lecture 10 split**: Lecture 9 ("The t distribution and
  confidence intervals") ends with the t statistic. The p-value, the
  decision, and the link between interval and test are in Lecture 10.
- **Rules for expectation and variance**: shifting and rescaling in Basic
  Lecture 3, sums of two variables in Basic Lecture 5, both on the formula
  sheet under those lectures. Lecture 8 only uses them.
- **Quantile notation** stays cumulative and matches R. "Percentile" and
  "quantile" are defined once in Basic Lecture 6.
- **Sampling convention**: samples in the book are drawn without
  replacement and treated as independent when n is at most 10% of N.
- **Robust standard errors** (Intermediate Lecture 3) are a normal section,
  "enough to recognise", because the mock exam and Tutorial 1 ask what they
  fix. The chunk runs, so the build needs `lmtest` and `sandwich`.
- **Regression tables in paper layout**: Intermediate Lecture 4 and
  Tutorial 2 show specification tables (one column per model, standard
  errors in parentheses, `.reg-table` style) typed from the R output, with a
  non-evaluated `modelsummary` snippet for thesis use.
- **Mock exams stay unseen**: no lecture or tutorial task reuses the numbers
  of a mock exam question.
- **Language**: plain English for non-native readers, short sentences, no
  long dashes, no semicolons in prose, British spelling, estimates with
  hats, variables and data named at every data reference.
- Not adopted from the old slides, on purpose: tail notation z_alpha, a
  fixed "n = 30" rule, inference with known sigma, reading quartiles from a
  CDF by the midpoint rule, the full set-algebra list in the main text.

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
