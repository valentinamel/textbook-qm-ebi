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

## 2026-10-07 — Exam sheets and internal information

- **Exam sheets are dry.** The formula sheet and the code sheet contain
  notation, formulas with their conditions, R commands with a short comment,
  and labels of R output. No interpretation, no advice, no workflow, so that
  the exam can test understanding. The introduction above the sheet body is
  for the web page only.
- **One source for web page and exam PDF.** `scripts/build_exam_sheets.py`
  builds `assets/downloads/qm-basic-formula-sheet.pdf` (two pages) and
  `assets/downloads/qm-intermediate-code-sheet.pdf` from the sheet body.
  Rebuild after every change to a sheet.
- **No internal information on student pages.** Nothing about how the
  course, the book, a lecture, an example, a dataset, or the exam was
  planned or built, and no reasons for design choices. Students see what
  they need to understand the material or to act.
- **Simulated practice data.** Students never simulate. Simulation code is
  shown in a closed optional box for transparency only.
- **Mock exam pointers.** Chapters do not name mock exam question numbers.

## 2026-10-08 — Exams and mock exams

- **Open questions only.** All parts of all exams and of both mock exams are
  open questions, in the style of the exams of earlier years: a short case,
  parts with their points, and a complete solution. No multiple choice, no
  output with blanks, no list of statements to mark.
- **New content in open form.** Students interpret supplied R output and
  assess an answer of an AI assistant. The AI answer is a short text, and
  each part asks about one of its sentences.
- **Blueprint.** Each course has a specification table (course learning
  goals from OSIRIS by cognitive level). The mock exam, the exam, and the
  resit follow it. The table and the scoring instructions are in the
  assessment dossier of each course, outside this repository.
- **QM Intermediate needs R.** Learning goal 3 names R, so parts that start
  with "In R:" stay in the exam. Stand-in values keep later parts
  answerable.
- **Mock exams are unseen.** Cases and numbers of a mock exam do not repeat
  a worked example or practice task of a chapter.
- **Parts labelled (a), (b).** At the start of a list line the opening
  bracket is written as `&#40;`, so that the page does not turn the label
  into a nested list.

## 2026-10-08 — Gabriela's second review (Lectures 6 to 10, tutorials, exam format)

- **Lectures 9 and 10 follow Gabriela's structure.** Her order and examples
  are kept, rewritten in the plain style of the book. Figures are rebuilt in
  R. Longer derivations sit in collapsed optional boxes.
- **D1 Strict wording for SD and SE.** $\sigma/\sqrt n$ is the standard
  deviation of the sample mean, $\sqrt{p(1-p)/n}$ the standard deviation of
  $\widehat P$. "Standard error" is used only for the estimated versions
  $S/\sqrt n$ and $\sqrt{\hat p(1-\hat p)/n}$. Under $H_0$ the book writes
  $\operatorname{SD}_0(\widehat P)$, "the standard deviation of $\widehat P$
  under $H_0$". No hat on SE, no "estimated standard error".
- **D2 Sigma known is a first step only.** Lecture 9 shows the interval with
  known $\sigma$ once, as a starting point. Exams ask for t intervals and t
  tests for a mean, and z intervals and z tests for a proportion.
  Probabilities for $\bar X$ with a given $\sigma$ and sample size with a
  planning value of $\sigma$ stay examinable.
- **D3 One procedure.** The gap parameter, "zero contrast", "universal
  benchmark", and the seven-step workflow are retired. A test has five
  steps. The critical value comes first, the p-value second.
- **D4 Cumulative notation.** $z_{1-\alpha/2}$, $t_{1-\alpha/2,\,n-1}$,
  $z_{obs}$, $t_{obs}$. Reject if $|t_{obs}|$ is at least the critical
  value. The formula sheet lists $z$ and $t$ values for $1-\alpha$ = 0.90,
  0.95, 0.99 and df 5 to 120. A df that is not listed uses the closest
  listed value.
- **D5 One running example.** The Shark Tank sample of 100 (seed 123) is
  used for all worked intervals and tests in Lectures 8 to 10.
- **D6 Exam-procedure boxes.** Four boxes (`.exam-procedure`): interval for
  a mean in five parts, interval for a proportion in five parts (Lecture
  9), test in five steps, and a test question answered with an interval
  (Lecture 10). Worked examples, tutorials, mock exam, and marking guides
  use the same numbering, as in the exam of December 2025.
- **Scope of tutorials.** Tutorial 3 covers Lectures 6 to 9, Tutorial 4
  covers Lecture 10. Every tutorial has more calculation practice with times
  per task and a verification chunk per task.
- **Moved and dropped.** Sample size moved from Lecture 8 to Lecture 9. The
  law of large numbers is dropped from Lecture 8. Lecture 7 has new sections
  on simple random samples (iid, 10% condition) and the shortcut variance.
- **Book exercises stay on Canvas.** The exercises of the textbook by
  Nieuwenhuis that Gabriela compiled are set as homework on Canvas, not in
  this repository (copyright).
- **Sigma known on Canvas.** The Canvas homework may contain intervals and
  tests for a mean with known $\sigma$, marked as a first step (as in
  Lectures 9 and 10). They are not examined.

## 2026-10-09 — Fourth review round (seven reviewers, coordinator decisions)

- **Format names, book-wide.** The before-class check in lectures is
  "Check your preparation". The worked exam item after class is "Worked exam
  interpretation: <topic>" (replaces "Exam-style item", "Exam-style:",
  "Exam practice:"). Invented examples start with "An invented example.",
  exam-style lead-ins with "**Exam-style question.** An invented example."
  Every page ends with "[Continue to <next item in `_quarto.yml`>: <its
  title>](<file>)".
- **Tutorial format.** All tasks at heading level 3, each with its minutes.
  Tasks outside the core carry "(N minutes, extra practice for home)". One
  total for the core tasks under "In the tutorial", and time-budget lines for
  Before class and After class as in the lectures.
- **Extra practice through Tilly** (9 October, Valentina). The homework
  exercises with solutions (compiled from Nieuwenhuis) go to the Tilly bot,
  not into the public book. Every Basic lecture and tutorial ends its after
  class part with "More practice": ask Tilly for an extra exercise, with the
  solution shown only after the student's answer.
- **Margin of error.** One symbol, $m$, as on the formula sheet. The symbol
  $h$ is retired.
- **Critical values in QM Intermediate.** With R the critical value is
  `qt(0.975, df)`, written $t_{0.975,\,df}$. Intermediate Lecture 3 gets one
  exam-procedure box ("Exam procedure: a test and an interval for a
  coefficient").
- **Sample standard deviation in Lecture 3.** Calculating $s$ (divide by
  $n-1$) from a small data set is a "Be able to do yourself" item of
  Lecture 3, so Tutorial 1 and the homework may ask it.
- **Lecture 1 and 5 additions.** The quartile definition (at least a quarter
  at or below $Q_1$ and at least three quarters at or above it, and the
  mirror for $Q_3$) is used in Lecture 1, the tutorials, and the formula
  sheet. A guide to correlation strength goes into Lecture 5. The subsection
  "How the course works" stays in Lecture 1.
- **One-sided tests** leave the main text of Lecture 9. They remain optional
  reading in Lecture 10 and are not examined.
- **Videos.** No swap before the discussion of 10 October. Clear mapping
  errors are fixed, and the prep boxes of Lectures 7 to 9 warn that the
  video writes $M_n$ for $\bar X$ and $\hat\Theta$ for an estimator.
- **Formula sheet.** Section titles equal the lecture titles. The
  percentage-change block is removed (no Basic lecture teaches it). New: the
  row $\operatorname{SD}_0(\widehat P)$, the proportion test written with
  it, $P(\text{Type I error})\le\alpha$, and a df label in the
  critical-value table. Still two pages.
- **QM Intermediate exam.** 120 minutes in TestVision, as the past exams.
  Aids: RStudio, Excel, the TestVision calculator, a simple pocket
  calculator, scrap paper, and the code sheet. The mock exam is resized with
  the plan of review R7, including the `predict()` fix in old part 1.5. 100
  points.
- **Grade and pass rule, both exams** (R&R TiSEM 2026-2027, articles 6.2 to
  6.4, and the Osiris change of 2026-2027: only component grades are
  registered, Osiris calculates and rounds the final grade). The test score
  is points / 10 with two decimals on a scale of 1.00 to 10.00 (minimum
  1.00). It is entered in Osiris as the component grade of the 100% exam.
  Osiris rounds it to a whole or half grade, and 5.50 to 5.74 becomes 6.0,
  5.25 to 5.49 becomes 5.0. Pass with 6.0 or higher, that is with 55
  points or more.
- **QM Basic mock exam.** The changes of review R6 are adopted: a new sample
  for the R output of Question 5, the five-step proportion test in Question
  6 (paid for by R6's cuts), a correlation calculation in 3.7, one summary
  calculation for CLG3 in Question 1, and the marking-rule fixes. Seven
  questions, 100 points, suggested minutes adding to at most 170.

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
