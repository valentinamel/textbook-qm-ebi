# Changelog

Running log of what changes per chapter relative to the prototype
(valentinamel.github.io/textbook-prototype). One entry per chapter, updated
when the chapter is rewritten.

## 2026-08-30 — Repo created

- New official repository `textbook-qm-ebi`, Quarto book, publishing to
  `docs/` for GitHub Pages at valentinamel.github.io/textbook-qm-ebi.
  Prototype stays untouched as internal reference.
- Data pipeline carried over verbatim: `data-raw/` snapshot →
  `scripts/build_teaching_data.R` → `data/shark_tank_teaching.csv`
  (1,441 rows, 19 variables, Seasons 1–16, SHA-256 checks in data/README.md).
- Standing template implemented in `assets/styles.scss`: three-phase
  containers (pale blue / green / purple), outcomes box, driving-question
  block, one navy/teal caveat box per lecture (never yellow), optional-box
  for demoted formal material, stated time budgets.
- Standing rule: **no hidden objects** — every object used in a chapter's
  code is constructed in visible code on the same page; setup chunks hold
  chunk options only.

## b02 — Probability foundations and random variables (pilot)

Source: prototype `B02-typical-pitch.Rmd` rewritten per `basic-L02.md`
scenario + template. Changes:

- **Fixed season support error**: body said support of season is {1,…,8};
  now {1,…,16} (practice answer was already correct).
- **Finite additivity in the main text**; countable additivity demoted to an
  optional box (course uses finite sample spaces only).
- **Formal random-variable definition (X: Ω→ℝ) demoted to an optional box**;
  informal definition first (numerical measurement determined by chance via
  a fixed rule), per scenario.
- **Empirical-distribution material removed from prep** (frequency /
  relative-frequency tables, season bar chart, description-words histogram).
  Per scenario it is taught in the L1 descriptive block — ⚠ b01 must receive
  it when b01 is rewritten (see basic-L01.md notes: hand-read histogram +
  median-interval location). Prep now: 3 videos, one-line season table
  reactivation, Mentimeter PREDICT, refresher pointer. Outcomes list updated
  accordingly.
- **D and L construction now visible** in every code block that uses them
  (was hidden in an include=FALSE setup chunk); added the explicit 2×2
  counts table with margins as the anchor object of the lecture.
- **Worked example ladder added**: worked (D^c, D∩L, D∪L in words/symbols
  from the table) → worked by hand (P(D∪L) = (882+734−505)/1441, each number
  pointed to; resolves the prep prediction) → faded in class (P(no deal and
  early) = 330/1441, steps 1 given / 2–3 student) → faded after class with
  new numbers (P(D∪E) = 1212/1441) → unassisted practice (kept from
  prototype).
- **Added driving question** opener and closing answer section (new template
  element).
- **Added caveat box** "What these numbers can and cannot say" consolidating
  the empirical-proportion-vs-forecast subsection + on-air-deal ≠ investment
  (previously a standalone section; now the single per-lecture box).
- **Added checks** as collapsed callouts: pitch_id 7 outcome-vs-event; season
  events as a partition (and D, L as a non-example).
- **Added business version of event combination** (industries F, T disjoint)
  after the 12-outcome diagram, per scenario segment 3.
- **Added spaced-review item** (L1: sampling variability vs selection bias)
  and stated time budgets on Before/After class.
- Cross-reference fixed: independence of events now points to Lecture 4
  (moved from L5 in the redistribution).
- Figures numbered and referenced (@fig-b02-events, @fig-b02-partition);
  figure code unchanged from prototype.
- Kept: whole-to-part table, die example, derived rules, partition figure,
  retrieval set, practice set, worked exam interpretation, Nieuwenhuis
  pointer.

### 2026-08-30, revision after first review

- Design pass: richer but restrained styling (phase containers, checklist
  outcomes box, driving-question card, sand/gold worked-example blocks,
  teal check callouts, navy caveat chip, styled tables and code).
- Second design pass (decrowding): near-white phase backgrounds with the
  colour carried by border and marker; more whitespace throughout (wider
  padding, larger block margins, higher line-height); lighter borders.
- Third design pass (consulting-style minimalism, final direction): back to
  the prototype's system font stack (SF Pro on macOS, Segoe UI on Windows)
  at 16.5px, no web fonts ($web-font-path: false — never add a separate
  @import, it breaks the compiled CSS); sharp 6px corners, flat surfaces,
  no shadows or gradients; small-caps letter-spaced kicker labels instead
  of pill chips (outcomes, driving question, caveat, utility); square
  phase markers; thin rules on tables. Pencil kept on "Try it".
- "Try it" faded tasks restyled from red/exclamation (callout-important) to
  a warm orange pencil style (callout-caution) — standing convention for
  all chapters.
- **New standing element**: a utility-writing question ("Make it yours",
  two sentences, EiA venture or a business the student knows) closes the
  After-class practice of every lecture. Added to b02; After-class budget
  now ~55 minutes.

## 2026-08-30 — Full book migration (after pilot approval)

Everything below was produced in one migration pass: all remaining
lectures, tutorials, exam resources, supplementary pages, welcome and
course gateways, the how-to-succeed page with printable weekly
checklists, and the new sampling-distribution widget. Per-chapter
details follow.

### b01 — Introduction to data analysis (vs old B01-question-to-evidence.Rmd)

- Retitled per scenario; kept anchor {#b01}. Driving question opener and
  closing answer added; entry-quiz opener line added.
- ADDED the empirical-distribution block moved from b02's prep (frequency
  and relative-frequency tables, season bar chart, description-words
  histogram) into the descriptive section, taught in the body.
- ADDED the hand-read histogram section: the five-step reading sequence
  applied to the equity histogram, then locating the median interval from
  cumulative bar counts (58, then 58+88, …), with a FADED quartile-interval
  task — previously untaught but examined (Mock Exam Q1).
- ADDED the note that description_words describes the source text, not the
  pitch itself.
- In-class data collection (risk choice/scale/founder probability), sample
  vs target population, sampling variability vs selection bias kept and
  restructured per scenario segments; caveat box consolidates the
  what-these-records-cannot-say material.
- After class: reproduce-the-workflow, retrieval, graph explanation, FADED
  histogram reading, AI-answer audit (Attempt-Ask-Verify-Explain),
  exam-style items; Make it yours utility question with Tilly pointer added.

### b03 — Discrete distributions, expectation, and variance (vs old B03-relationships.Rmd)

- Variance and SD MOVED IN from old b04, including the same-mean/different-
  spread figure, four-step reading of the formula, definition and
  computational forms, and Bernoulli p(1−p).
- ADDED the tiny-PMF worked ladder (values 0/1/2, masses 0.2/0.5/0.3):
  expectation with every product written, FADED E[Y²], variance both ways —
  all before any Shark Tank computation.
- season_pmf and p_hat construction now visible (was hidden in setup).
- CDF as running total with F(3) hand-computed from three bars, full table
  in LIVE R, CHECK reading F(8) off the step graph.
- Expectation of season (8.8) resolves the prep prediction (an expectation
  need not be a possible value); E[X]=p for the deal indicator.
- Model-vs-sample distinction section with the n−1 remark deferred to L7.
- Caveat box: expectation is not a guarantee for one pitch; file-based
  values are not forecasts. Utility question + Tilly added.

### b04 — Conditioning, total probability, Bayes, independence (vs old B04-conditional-probability.Rmd)

- Variance section MOVED OUT (to b03); independence of events MOVED IN
  (from b05): definition via P(A|B)=P(A), product form, D-and-L check with
  the numbers, one-minute disjoint-vs-independent contrast.
- ADDED the natural-frequency Bayes tree as a numbered figure and worked
  example (1000 pitches: 100 deals of which 80 flagged, 900 non-deals of
  which 180 flagged, 80/260 ≈ 31%) BEFORE the formula, each count then
  matched to a term.
- Denominator-pointing exercise promoted into the in-class opening;
  conditional probability worked with the column/row physically highlighted
  (same numerator, different denominator, different question).
- Total probability rebuilt from the two period-specific rates with the L2
  partition figure; multiplication rule as the rearranged definition with a
  FADED two-way verification.
- D, L, p_hat construction visible in every code block.
- Caveat box: reversing the condition does not reverse cause; selected
  televised records. Utility question + Tilly added.

### b05 — Joint distributions, covariance, and correlation (vs old B05-random-variables.Rmd)

- Event independence MOVED OUT (to b04); chapter keeps independence of
  random variables via the product rule in every joint-PMF entry, with the
  (1,1) check (0.350 vs 0.312) — one mismatch proves dependence.
- ADDED the hand-worked conditional (505/734 with the column highlighted)
  connecting joint tables back to L4.
- ADDED the signed-products covariance worked example on the small practice
  table (masses 0.30/0.20/0.10/0.40): four signed deviation products written
  out, averaged, then the computational form verified; sign logic before
  formula manipulation.
- Marginals by summing rows/columns worked by hand with arrows; correlation
  as standardised covariance with the units argument and the linear-vs-
  curved two-panel figure (CHECK: near-zero correlation is not "no
  relationship").
- Inspect-first-summarise-second: season-equity scatter, LIVE R
  correlations, prep prediction resolved (r ≈ −0.42).
- Point-biserial remark demoted per scenario. X, Y construction visible.
- Caveat box includes the forward pointer to multiple regression
  (Intermediate L4) on why the marginal equity-deal association may
  mislead. Utility question + Tilly added.

### b06 — Continuous distributions and the normal model (vs old B06-continuous-distributions.Rmd)

- Data-quantile/IQR section SHRUNK to quantiles of model distributions
  (data quantiles now live in the L1–L2 descriptive material), per the
  supersession decision.
- ADDED the supplied-Z-values worked example in the exam's format: given
  P(Z≤1.5)=0.9332, P(Z≤1.0)=0.8413, P(Z≤−1.0)=0.1587 on the page, compute
  P(Y≤65) and P(40<Y<60) for N(50,100) by hand, then pnorm verification —
  the hand path is primary because the closed-book exam supplies values.
- ADDED the reverse-percentile worked example (90th percentile back to a
  raw value, x = μ + zσ, qnorm as verification).
- Density-is-height/probability-is-area opening with the density-can-exceed-
  1 CHECK; uniform session-timing worked example (18/90 = 0.20) with FADED
  second interval.
- Model check against data: equity histogram with fitted normal curve read
  with the five-step sequence — the model is a choice and here it fails;
  forward pointer that the normal returns for sampling distributions.
- ADDED a second business uniform example in practice; unit-change item
  kept. Caveat box: normality is a model claim. Utility + Tilly added.

### b07 — Samples, parameters, and estimators (vs old B07-samples-estimators.Rmd)

- ADDED the live sampling activity as a described in-class activity with
  reproducible code: five seed-varied samples of 100, mean equity computed
  each time, five means plotted as dots on a fixed axis (the experiential
  anchor b08 builds on), prep prediction resolved.
- Notation-discipline section kept unchanged (parameters/estimators/
  estimates, capital and lower-case, sample proportion as a sample mean).
- Sample variance and n−1: the three-deviation worked example (2, −5,
  forced 3), constraint argument, downward-bias statement.
- Sampling-method table kept with the FADED classify-four-recruitment-
  stories task.
- All sampling code shows set.seed visibly; pitch_sample construction on
  the page.
- After class includes the draw-your-own-sample shared-plot activity.
- Caveat box: random sampling supports generalisation to the frame, random
  assignment supports causal comparison, neither repairs the show's
  selection. Utility + Tilly added.

### b08 — Sampling distributions and the CLT (vs old B08-sampling-distributions.Rmd)

- t distribution MOVED OUT (to b09). Chapter is sampling distribution, SE,
  and CLT only.
- ADDED the sampling-distribution WIDGET (new, assets/widgets/
  sampling-lab.html, embedded via iframe): n slider, draw buttons, histogram
  of sample means forming live next to the skewed equity population
  histogram on a shared x-axis, with mean-of-means and SD-of-means compared
  to the square-root-rule prediction. Widget homework (three specified
  settings, one sentence each) in After class.
- PROMOTED the σ=12, n=36 practice item to a worked example (E, Var, SE of
  the sample mean), with the linearity rules shown and referenced to the
  formula sheet's Lecture 8 block (E[aX+b], Var(aX+b), Var(X+Y) under
  independence — added there).
- Square-root rule resolves the prep prediction (4×); FADED how-large-must-
  n-be task.
- CLT stated for the course's conditions with the two-panel simulation
  figure (seed 208) read with the five-step sequence; no universal n=30
  rule; skew and dependence caveats. LLN vs CLT contrast with CHECK.
- Proportions as means: SE of the deal proportion at n=100 with the
  success-failure condition checked.
- sigma_equity and p_deal construction visible.
- Caveat box: more observations shrink random error, never selection bias.
  Utility + Tilly added.

### b09-t-confidence-intervals.qmd — changes vs old B09-confidence-intervals.Rmd

- Retitled to "The t distribution, confidence intervals, and the two-sided
  test"; kept anchor {#b09}.
- MOVED IN from old B08: the entire t-distribution section (why estimating
  sigma adds uncertainty, heavier tails, df = n−1 recalled from L7,
  convergence to normal) now OPENS the technical content, with the old
  t-curves figure kept verbatim as `fig-b09-t-curves`. Added collapsed
  CHECK: t(0.975,11) ≈ 2.20 vs t(0.975,99) ≈ 1.98 (verified).
- MOVED OUT to b10: the whole "One-sided alternatives: overview" section
  including the three-panel rejection-region figure and the three p-values
  list. Left a one-line forward pointer in the null-hypothesis section
  ("Directional, one-sided alternatives exist; Lecture 10 treats them").
- NO HIDDEN OBJECTS: the old setup chunk built sharks/pitch_sample/
  gap objects invisibly. All construction is now visible in the body
  (`b09-gap-objects`): set.seed(123), sample_rows, pitch_sample,
  benchmark, equity_gap_pp, gap_bar, gap_sd, n, df, gap_se. Sample drawn
  with b07's exact idiom (`sample(seq_len(nrow(sharks)), size = 100,
  replace = FALSE)`) — identical rows to old `sample(..., 100)`, verified:
  mean equity 12.76, gap −2.24, sd 7.7079, SE 0.7708, df 99.
- ADDED fully hand-worked interval BEFORE the Shark Tank R block
  (`exm-b09-hand-interval`): n=64, x̄=80, s=16, benchmark 75 → gap 5,
  SE 16/8=2, t≈2.00 (qt(0.975,63)=1.998), margin 4, interval (1, 9);
  every arithmetic step voiced. (These numbers were the old chapter's
  Practice item 1 — practice got fresh numbers, see below.)
- ADDED the gap-device section up front: benchmark questions become
  zero-contrast questions; framing flagged as carrying to regression.
- Conditions section recast as an explicit numbered checklist placed
  before the calculation.
- Shark Tank interval reproduced and verified: gap (−3.769, −0.711) →
  mean (11.231, 14.289); critical_t 1.9842.
- Two-sided test: added the hand arithmetic once before the R block
  (−2.24/0.77 ≈ −2.91); R gives t = −2.9061, p = 0.004515 (old chapter
  said 0.0046; prose now says ≈0.0045). p-value figure kept, now
  `fig-b09-two-sided-p` with caption and the five-step reading sequence
  in prose; chunk made self-contained (echo: false).
- Interval–test agreement section kept; ADDED the FADED task (interval
  (−1.4, 3.8) given → state decision without computing), with nested
  collapsed answer, per scenario item 7.
- KEPT the coverage simulation figure verbatim with set.seed(209), now
  `fig-b09-coverage`, self-contained; inline `r sum(covered)` replaced by
  the verified literal 96 (of 100) in caption and prose.
- Kept the one forbidden 95% sentence and its correct replacement, now
  typeset as quote blocks.
- Consolidated caveats into ONE caveat-box (significance ≠ importance,
  ≠ causation, narrow interval repairs nothing about selection) placed
  late in In class, per template.
- Added "Answering the driving question" section with the actual numbers
  and a one-line preview of Lecture 10.
- Before class rebuilt to template: 30-minute budget, video-prep box with
  the three old videos + External Video Guide link, reactivation task
  (the old D = X − 15 hypotheses prep, kept, with collapsed check),
  PREDICT Mentimeter item (s-for-sigma: wider/narrower/unchanged, from
  scenario), refresher pointer; prediction resolved in the t section.
- After class rebuilt to scenario (55 + 5 = 60 min): Retrieval 6 (added
  "why t rather than normal"); From worked to faded with new numbers
  (n=25, x̄=42, s=10, benchmark 40 → SE 2, interval (−2.13, 6.13),
  includes zero, t=1.00, p≈0.33 — verified); unassisted Practice with
  fresh numbers replacing the promoted (1,9) item (n=49, x̄=110, s=14,
  benchmark 100 → interval (5.98, 14.02), t=5.00 — verified; kept old
  items on the 0.42/0.18/df=120 coefficient (t=2.33, p≈0.021, interval
  (0.064, 0.776) — verified) and significance-vs-importance); forbidden-
  sentence rewrite as its own 5-minute section; spaced review one L8 SE
  item (24/√64=3) and one L4 conditional item (P(D|L)=505/734=0.688 vs
  P(L|D)=505/882=0.573); worked exam interpretation on the Mock Exam Q4
  pattern (t=2.400, df=63, SE 8/√64=1 — matches mock exam); Make it yours
  utility prompt (venture metric vs industry benchmark framed as a gap)
  with lecture-specific Tilly line.
- Component conversions: \( \) → $ $, <details> → collapsed callouts,
  outcomes/driving-question divs to exemplar syntax, figure labels +
  captions added, closing references kept (Nieuwenhuis Ch. 15–16).

### b10-testing-errors-power.qmd — changes vs old B10-hypothesis-testing.Rmd

- Retitled to "Testing decisions, errors, power, and the road to
  regression"; kept anchor {#b10}.
- MOVED IN from old B09: the one-sided-alternatives section (three-
  alternatives table, three-panel rejection figure now
  `fig-b10-one-sided`, pre-specification rule, invalid tail-picking,
  course convention two-sided), placed directly after the Type I/II/power
  section so it sits beside the rejection-region figure it needs. The
  figure chunk is self-contained with `tail_df <- 99` set explicitly;
  the t=−2.91 three-p-value list kept (two-sided 0.0045, left 0.0023,
  right 0.9977 — verified) and explicitly credited to Lecture 9. Added
  the explicit "tail-picking doubles the true Type I rate to ~10%"
  argument connecting it to the power discussion.
- NO HIDDEN OBJECTS: old setup chunk built pitch_sample/phat/p0/deal_gap
  invisibly; all now constructed visibly in `b10-proportion-objects`
  (set.seed(123), b07 sampling idiom — same rows as old chapter,
  verified: phat 0.64, deal_gap 0.14, null SE 0.05, z 2.80, p 0.00511).
- ADDED the hand-worked proportion test BEFORE the R block
  (`exm-b10-launch-test`): 232 of 400 launches vs p0 = 0.50 → p̂ 0.58,
  gap 0.08, null SE √0.000625 = 0.025, z 3.20, two-sided p ≈ 0.0014
  (verified) — the Mock Exam Q5 numbers, every step voiced, null-counts
  condition check included.
- Estimated-vs-null SE subtlety DEMOTED to an optional-box (per
  scenario), with the added note that the L9 mean-gap procedures use the
  same SE in both, so there the interval/test match is exact.
- The four wrong p-value sentences recast as a FADED pairs task
  (callout-caution with four "(you)" sentences in launch-test context and
  nested collapsed corrections) replacing the old bullet list; framed as
  the handed-out before-break pair task per scenario.
- Type I/II/power: kept table, formulas, and the two-panel figure (now
  `fig-b10-errors-power`, self-contained, captioned); ADDED both errors
  named in context for the launch test (worked, in prose); four levers of
  power kept with the alpha trade-off spelled out as "not a free gain."
- Seven-step workflow kept as the standing recipe, with "do not reject ≠
  accept" moved here and used to resolve the new prep PREDICT item.
- Regression preview KEPT UNCHANGED (live `lm(equity_offered_pct ~
  season)` on all 1,441 rows; slope −0.824, SE 0.048, t −17.3, interval
  (−0.92, −0.73) — verified); prose now reads the row explicitly with the
  estimate/SE/t/p/interval vocabulary and forward-points to Intermediate.
- Consolidated caveats into ONE caveat-box (significance ≠ magnitude ≠
  causation + the standing five-item reporting list).
- "Answering the driving question" added; closes the course arc ("from
  one pitch to a defensible claim about a frame") per scenario item 10.
- Before class: 25-minute budget; videos kept + External Video Guide
  link; the coefficient-row exercise kept as reactivation with collapsed
  check. ⚠ QUESTION: the L10 scenario lists no PREDICT item, but the
  standing template requires one — I added a 2-minute one-click item
  ("p = 0.20 at α = 0.05: has the study shown the null is true?"),
  resolved in the workflow section, keeping the 25-minute budget. Drop it
  if the scenario's omission was deliberate.
- After class rebuilt to scenario (60 + 5 = 65 min): Retrieval 7 (old
  list kept); worked→faded (120 of 200, z ≈ 2.83, p ≈ 0.005 — verified)
  then unassisted set covering mean (n=49, t=1.50, p≈0.14 — verified) and
  proportion errors, the −0.290/0.058 coefficient (t=−5.00, interval
  (−0.404, −0.176) — verified), significance-vs-negligible, causal
  limits; NEW one-sided reasoning section (t=−2.91: all three p-values,
  which alternatives were legitimate to pre-specify, what tail-switching
  breaks); spaced review one L9 interval item (interval (0.4, 5.2) →
  decision) and one L5 correlation item (r ≈ −0.42 season–equity,
  verified in file); exam-style Mock Exam Q5 pattern including the
  mentoring_hours regression row (0.80, SE 0.25, t 3.20, CI [0.31,1.29])
  and the proportion CI (0.532, 0.628) — verified 0.5316–0.6284; Make it
  yours utility prompt + Tilly line.
- Old after-class Practice items were redistributed rather than dropped:
  120/200 → faded task; n=49 item, coefficient item, errors item,
  negligible-but-significant item, causal-reasons item → unassisted set.
- Component conversions as in b09; closing references kept (Nieuwenhuis
  Ch. 15–16); "Continue to Tutorial 4" retained.

### t01 — Basic Tutorial 1 (vs old B-EP01.Rmd)

- Scope now Lectures 1–3 INCLUDING variance and SD (moved into L3);
  variance items added to the set.
- Exam-preparation-session branding; standing pair-first-with-AI-then-
  plenary format stated; collapsed model answers throughout; closing
  utility prompt (EiA-anchored, business-you-know fallback) with Tilly
  line. p_hat and all objects constructed visibly.

### t02 — Basic Tutorial 2 (vs old B-EP02.Rmd)

- Scope now Lectures 4–5 with independence of EVENTS under L4 and
  independence of random variables under L5; Bayes natural-frequency items
  aligned with the new b04 treatment.
- Same standing tutorial format, collapsed answers, utility prompt + Tilly.
  D, L constructed visibly.

### t03-exam-prep.qmd — changes vs old B-EP03.Rmd

- Retitled "Tutorial 3: Normal models, sampling, and standard errors"
  (scope is now Lectures 6–8); kept anchor {#b-ep03}.
- Adopted the t01/t02 exam-preparation-session pattern: branding paragraph
  (pairs first with AI allowed, then plenary), Before/In class/After
  phases, collapsed callout answers everywhere, closing utility prompt
  with Tilly line. Added an explicit scope note: "The t distribution
  belongs to Lecture 9 and is rehearsed in Tutorial 4."
- t REMOVED throughout (t now taught in Lecture 9, after this tutorial):
  - Outcome "explain why a one-sample t procedure has n−1 degrees of
    freedom" dropped; replaced by a normal/CLT outcome.
  - Old Task 5 ("Degrees of freedom and the t reference", qt(0.975,11) vs
    qt(0.975,99)) removed — the qt comparison moved to b09's in-class
    CHECK. Replaced by a new Task 5 "A proportion through the CLT":
    p=0.612, n=100 → SE 0.0487, success–failure 61.2/38.8,
    P(P̂ ≤ 0.50) ≈ Φ(−2.30) ≈ 0.011 (verified), closing with a one-line
    bridge to L9 testing logic.
  - The n−1 idea survives only in its L7 form: new Task 3 item 5 asks for
    the divisor used by sd() (99) with the deviations-sum-to-zero reason.
  - Timed-practice item 5 (df of a one-sample t procedure) replaced by a
    CLT probability: P(X̄>85) with μ=82, σ=24, n=64 → z=1, ≈0.16
    (verified).
- NO HIDDEN OBJECTS: old setup chunk drew pitch_sample invisibly; the
  sample is now constructed once, visibly, in Task 2's chunk with
  set.seed(123) and b07's sampling idiom (verified identical output:
  mean 12.76, sd 7.7079, Q1 8, median 10, Q3 17.75, p̂ 0.64).
- Task 4 expanded from a pure CLT item into "One pitch versus one mean"
  to carry the Lecture 6 content now in scope: P(X̄>15) ≈ 0.017 (verified)
  contrasted with the single-pitch normal-model value P(X>15) ≈ 0.42
  (verified), plus the explicit reminder that L6 rejected the normal
  model for pitch-level equity while the CLT justifies the mean version.
- Tasks 1–3 migrated essentially intact (population/frame/claim;
  parameter–estimator–estimate + IQR; SEs and sample size); all numbers
  re-verified (SE mean 0.7708, SE prop 0.0480, IQR 9.75).
- Before class: definitions list now opens with standardisation
  (L6 content); "parameter/estimator/SE/CLT" kept; formula-sheet and
  refresher pointers converted to ../resources/ links.
- After class: timed redo explicitly framed as unassisted exam-conditions
  work per the tutorial protocol; added a "Check your understanding"
  from-memory block (t01 pattern); added Make it yours utility prompt
  (expected SE and the "what would surprise you" instinct, EiA-anchored
  with fallback) with Tilly line.
- Closing pointer: "Continue to Lecture 9: The t distribution, confidence
  intervals, and the two-sided test."
- ⚠ QUESTION: the quartile/IQR sub-items (old Task 2.3) were kept even
  though data quantiles now live in L1–L2 descriptives — tutorials mirror
  the cumulative exam, so review seemed right. Cut Task 2.3 if Tutorial 3
  should be strictly L6–L8.

### t04-exam-prep.qmd — changes vs old B-EP04.Rmd

- Title and anchor kept: "Tutorial 4: Inference and tests against zero"
  {#b-ep04}; scope confirmed as Lectures 9–10 as now taught (t in L9,
  one-sided in L10, exams two-sided — stated in the intro).
- Adopted the t01/t03 exam-preparation-session pattern: branding
  paragraph (pairs first with AI allowed, then plenary), collapsed
  callout answers, After-class timed unassisted redo, Check your
  understanding block, Make it yours utility prompt with Tilly line.
- NO HIDDEN OBJECTS: old setup chunk built pitch_sample and
  equity_gap_pp invisibly; both now constructed visibly in the in-class
  load chunk (`bep04-load`) with set.seed(123) and b07's sampling idiom.
  All Task 1/2 numbers re-verified against the old chapter: d̄ −2.24,
  s_d 7.7079, SE 0.7708, df 99, interval (−3.77, −0.71), t −2.906,
  p 0.0045; p̂ 0.64, z 2.80, p 0.0051, proportion CI (0.546, 0.734), gap
  CI (0.046, 0.234).
- Task 1 gained item 5: why the critical value is qt(0.975, 99) rather
  than qnorm(0.975) — rehearses the t distribution at its new L9 home;
  answer notes 1.984 vs 1.96.
- NEW Task 5 "One-sided alternatives and the exam convention" (L10 now
  owns one-sided): compute both one-sided p-values for t = −2.906, df 99
  (left 0.0023, right 0.9977 — verified), explain why tail-choice after
  seeing the estimate is invalid (Type I doubling), state the two-sided
  exam convention. Old Task 5 ("Repair the conclusion") became Task 6,
  unchanged.
- Tasks 2–4 migrated essentially intact (proportion contrast; regression
  coefficient row −0.290/0.058/−5.00; errors and power), with the
  alpha-trade-off answer sharpened ("wider rejection region catches more
  of everything").
- Before-class memory list item 3 extended: not just df = n−1 but also
  WHY the critical value is t rather than normal (L9's opening idea).
- Prep-check p-value wording updated to 0.0045 (old said "about 0.0046";
  exact value 0.004515).
- After class: timed practice (n=81 spending/renewal set) kept verbatim
  — all numbers re-verified (gap interval (0.01, 3.99), t 2.00, p 0.049;
  p̂ 0.667, proportion CI (0.564, 0.769), z 1.22, p 0.22); model answer
  gained one sentence explaining the borderline mean result via
  two-SEs-from-zero; framed as unassisted exam-conditions work. Added
  the Check your understanding block (interval meaning, decision link,
  errors/power, one-sided legitimacy, coefficient row) and the utility
  prompt (investor claim as zero-contrast test, which error costs more).
- Closing kept: formula sheet + Basic Mock Exam pointer + Intermediate.

### formula-sheet.qmd — changes vs old formula-sheet.Rmd + formula-sheet-content.Rmd

- Merged the two-file bookdown structure (wrapper + child) into one Quarto page
  at `/home/claude/work/textbook-qm-ebi/basic/formula-sheet.qmd`; kept the
  `::: {.formula-sheet}` wrapper div (same class the intermediate code sheet uses).
- Kept ALL old anchors: `{#formula-sheet}`, `{#formula-notation}`,
  `{#formula-l1}` … `{#formula-l10}`.
- Converted all `\[ \]` display math to `$$ $$` and inline `\( \)` to `$ $`;
  markdown pipe tables unchanged; dropped the `\newpage` (PDF-only pagination,
  handled at PDF-generation time — noted in the HTML comment).
- **Moved (new lecture allocation):**
  - Population variance/SD, Bernoulli variance, and sample variance/SD:
    Lecture 4 block → Lecture 3 block. Bernoulli variance merged into the
    single "Bernoulli distribution" entry (E[X]=p and Var(X)=p(1-p) together).
  - One-sample t statistic: Lecture 8 block → opens the Lecture 9 block.
  - Independence of events P(A∩B)=P(A)P(B): Lecture 5 block → Lecture 4 block,
    matching b04 (which now teaches independence of events) so tutorial-2
    cumulative use stays consistent. Lecture 5 keeps independence of random
    variables via the joint PMF.
- **Added to Lecture 8:** "Linearity rules for expectation and variance" —
  E[aX+b]=aE[X]+b, E[X+Y]=E[X]+E[Y], Var(aX+b)=a²Var(X), and
  Var(X+Y)=Var(X)+Var(Y) for independent X, Y (placed before the sampling
  distribution of the mean, which b08 derives from them).
- **Added to Lecture 10:** one-line note that a pre-specified one-sided
  alternative uses a single tail for its p-value and that course exams are
  two-sided only (old sheet had no one-sided material; nothing was cut).
- Renamed block titles to match new chapter titles: L3 "Discrete
  distributions, expectation, and variance"; L4 "Conditioning, Bayes' rule,
  and independence"; L5 "Joint PMFs, covariance, and correlation"; L8
  "Linearity rules, sampling distributions, and SEs"; L9 "The t distribution,
  confidence intervals, and tests". L1, L2, L6, L7, L10 titles unchanged.
- Kept positive quantile notation (z_{1-α/2}, t_{1-α/2,n-1}); added one short
  line in L9 mapping it to `qnorm(1 - alpha/2)` / `qt(1 - alpha/2, df)`.
- Kept the tutorial-usage table (T1: L1–3, T2: L1–5, T3: L1–8, T4: L1–10,
  exam: complete sheet) and the "definitions remain examinable" sentence.
- Replaced the old "Download the print-ready PDF" link (pointed at
  `output/pdf/basic-course-formula-sheet.pdf`, which does not exist in the new
  book) with the sentence that the complete two-page PDF is attached to the
  exam, plus an HTML comment stating the exam PDF must be generated from this
  same content using the old `exam-materials/formula-sheet-basic.Rmd` layout
  (PDF not built, per instructions).
- ⚠ QUESTION: b08 (line ~164) cites the linearity rules as being on the
  formula sheet under "Lecture 3"; the sheet now carries them under Lecture 8
  per the migration instruction. b08's parenthetical "(Lecture 3, and the
  Refresher's linearity rules)" should probably be edited to say Lecture 8.
- ⚠ QUESTION: independence-of-events move L5→L4 was inferred from the
  content-redistribution conventions (b05→b04), not explicitly listed in the
  formula-sheet instruction — confirm.
- ⚠ QUESTION: should a download link for the exam PDF be reinstated once the
  PDF exists, and at which site path?

### basic/mock-exam.qmd — changes vs old mock-exam-basic.Rmd

- Faithful migration to `/home/claude/work/textbook-qm-ebi/basic/mock-exam.qmd`:
  all 5 questions, 26 subparts, tasks, numbers, points, and marking guides
  UNCHANGED (verbatim apart from format conversion).
- Kept the page anchor `{#basic-mock-exam}` and the internal link to
  `[QM Basic Formula Sheet](#formula-sheet)` (anchor exists in the new
  formula-sheet.qmd).
- Converted `\[ \]` / `\( \)` math to `$$` / `$`; tables untouched.
- Converted the five `<details><summary>Model answer and marking guide</summary>`
  blocks to `::: {.callout-note collapse="true"}` with
  `## Model answer and marking guide` titles (book-wide convention).
- Added the standard setup chunk (`bmock-setup`, chunk options only, no
  objects) matching the exemplar chapters.
- Histogram chunk: converted to `#|` options, labelled `fig-bmock-histogram`
  with a fig-cap, kept `echo: false` (fully self-contained: builds
  mock_breaks/mock_counts inside the chunk — satisfies the no-hidden-objects
  rule). Plot code itself unchanged.
- Lecture-number references: the old exam contains NO references to content by
  lecture number, so nothing needed fixing for the moved topics (variance→L3,
  t distribution→L9, one-sided→L10). All tests in the exam are already
  two-sided.
- Verified: all R chunks extracted with knitr::purl and run without error from
  the project root (R 4.3.3); the histogram renders.
- No ⚠ QUESTION items.

### i01 — Simple linear regression (vs old I01-simple-linear-regression.Rmd)

- RUNNING UNITS SWITCHED to thousands of dollars (ask_1k, deal_1k); all
  coefficients, axes, fitted values, and answers re-verified by refitting.
- ADDED the rescaling worked note (what the slope means in $1,000s and how
  the same relationship reads in other units) before the model.
- ADDED the errors-vs-residuals two-panel figure (population line with ε,
  fitted line with e; CHECK which object is observable).
- ADDED the three-point toy hand-calculation of b1 = s_XY/s_X² and b0, with
  the line through (x̄, ȳ) shown on the toy plot.
- SSE drag-lab widget migrated verbatim (inline SVG+JS, self-contained),
  with the target-SSE-to-beat framing; least squares motivated (why
  vertical, why squared).
- Zoom-honesty paragraph kept (records outside the display, kept in the
  fit); observed = fitted + residual verified on one row; prediction inside
  the evidence boundary.
- deals subset and derived unit columns constructed visibly. Caveat box:
  association, selection into deals, no causal ask-changing claim.
  Utility (EiA3) + Tilly added.

### i02 — What the model assumes and how residuals betray it (vs old I02-regression-inference.Rmd)

- SEs, intervals, and the coefficient t-test MOVED OUT (to i03); chapter is
  assumptions and diagnostics only, retitled accordingly.
- Assumptions table kept ("best single table in the course"), one row at a
  time, tied to what each supports; outcome-need-not-be-normal stated early.
- Linearity-is-about-the-average four-panel figure with pattern-matching
  CHECK; constant-variance fan shapes with FADED annotate-a-printed-plot
  pairs task.
- What plots cannot show: zero conditional mean and independence from
  design knowledge, two Shark Tank stories (repeat pitchers, network ties)
  classified.
- ADDED the influence section promoted from the code sheet: summary()
  residual line read as a red flag, rstandard and Cook's distance in LIVE
  R, flagged high-value pitches identified on the scatter, investigate/
  report/never silently delete.
- Q-Q plots: how to read, when normality matters.
- Units in thousands throughout, constructions visible. Caveat box: no
  visible pattern is not proof. Utility (EiA3) + Tilly added.

### i03-inference-fit-ftest.qmd — changes vs old I03-model-usefulness.Rmd (+ moved-in I02 sections)

- Retitled to "Coefficient inference, fit, and the F-test"; anchor {#i03} kept.
- **Moved in from old I02-regression-inference.Rmd** and placed at the OPEN of
  In class: the SE of the slope, the confidence interval (worked by hand:
  1.0085 ± 1.96 × 0.0182 = (0.973, 1.044), df = 880 explained as n − 2,
  qt(0.975,880) = 1.963), and the t-test against zero (hand arithmetic
  t ≈ 55.4, then LIVE R verification with `pt()`). Each Basic pentad
  ingredient (estimate, SE, t, p, interval) explicitly named as it returns,
  with a mapping table onto the `summary()$coefficients` columns.
- Robust SEs demoted from an old-I02 body section to an **optional box** here
  (per redistribution plan): one thing they fix, list of what they cannot.
- Converted running units from $100,000s to **$1,000s** (`ask_1k`, `deal_1k`);
  all numbers re-verified with Rscript: slope 1.0085, SE 0.0182 (identical to
  old because both variables rescale together), interval (0.973, 1.044),
  SST = 103,509,324 / SSR = 80,441,122 / SSE = 23,068,202 (squared $1,000s),
  R² = 0.777, F = 3068.6 = 55.395², residual SE 161.9 ($1,000s ≈ $162,000).
- NO HIDDEN OBJECTS: old setup chunk built sharks/deals/deal_model invisibly;
  now built in a visible chunk at the top of In class (same as warm-up code),
  and rebuilt in the after-class answer chunk so blocks run alone.
- Added prep per scenario: pentad interval/test recipe reactivation, kept the
  small-large-small SSE/SSR/R² classification, new R warm-up extracting
  `summary()$coefficients`; video Stanford 3.4 kept, video-guide link added.
- Added new figure `fig-i03-decomposition` (one point's total deviation split
  into explained + residual, drawn before the SST = SSR + SSE algebra), per
  scenario "picture drawn". LIVE R computes all three with identity checked.
- **Promoted** the SST = 500 / SSE = 125 practice item to a worked example
  (@exm-i03-sst-sse), with the note that its answer check is posed by
  Mentimeter right before the in-class break (per scenario).
- R² section: what 0.777 means plus the four things it is not, EACH with a
  wrong sentence corrected; first two corrections worked, last two FADED as a
  pair task (per scenario "FADED in pairs").
- F formula read as explained-per-predictor over residual-per-df; the old
  "Read the complete R summary" section merged into the F-test section (the
  old chapter printed `summary(deal_model)` twice; now once).
- F = t² verified live; note that the equivalence dies in multiple regression
  (bridge to Lecture 5) kept and sharpened.
- Usefulness four-case list kept, now with one concrete business example per
  case (loyalty mailings, store staffing, 2020 travel demand, black-box
  forecasting) per scenario.
- ONE caveat box consolidating scope limits (classical SE vs L2 fan,
  influence, selection into deals, no causation); driving-question answer
  gives the actual numbers; preview of Tutorial 1 scope added.
- After class rebuilt to scenario (55 + 5): retrieval 6 items; FADED interval
  for a new coefficient row (the intercept row: (13.4, 41.8) by hand, R exact
  (13.36, 41.78)) then unassisted set (absorbing old practice items 2–4:
  R² = 0.20 reading, F = 20 calculation, why SSE cannot rise); full pipeline
  on equity-on-season with executed answer chunk (slope −0.824, SE 0.048,
  CI (−0.917, −0.731), R² 0.173, F 300.7) and 120-word conclusion; spaced
  review = one i02 diagnostics item (fan undermines classical SE); exam-style
  mock Q3 pattern (n = 102, slope 1.38, SE 0.46 → t = 3.0, CI (0.47, 2.29),
  F = t² = 9.0); Make it yours (EiA3) + Tilly line.
- Old I02 practice item on df with n = 75, k = 3 dropped (the n − k − 1 form
  is stated in body and reappears in the code sheet); old I02 assumptions
  content stayed in the new i02 chapter (not duplicated here).
- Closing updated: continue to Tutorial 1; formula-sheet line added; ISLR
  Sections 3.1.2–3.1.3, Nieuwenhuis 19–20.
- All chunks knit-tested from project root; outputs match every stated number.

### i04 — Multiple regression and what controls do (vs old I04-multiple-regression.Rmd)

- ADDED the constructed omitted-variable demonstration (two-predictor
  dataset where the simple slope of X is strongly positive and the adjusted
  slope near zero because Z drives both, mechanism visible in a coloured
  scatter) BEFORE the real-data stability case, with the explicit lesson
  that stability is informative but proves no absence of OVB.
- Coefficient-interpretation protocol and units table kept; "holding the
  other included predictors fixed" phrasing enforced; not-significant-is-
  not-zero said for description_words.
- Scaling to reader-relevant comparisons worked (five seasons, $500,000 —
  now 500 in thousands units, ten words), FADED combined contrast.
- What controls can and cannot do two-list section; collinearity as
  instability not bias; the coefficient plot read with the five-step
  sequence.
- Units in thousands, all models refit and verified; constructions visible.
- Nine-item practice set kept with items 6–9 flagged as the FADED-to-
  unassisted ladder; cumulative mini-task (paragraph connecting i02
  diagnostics to this model). Caveat box + utility (EiA3) + Tilly added.

### i05 — Categories as predictors and joint tests (vs old I05-dummies-f-tests.Rmd)

- ADDED the percent-versus-percentage-points block ("1.28%" is ambiguous;
  the precise sentence that replaces it) BEFORE any coefficient is read.
- ADDED the hand-plugged partial-F calculation ((436.25/2)/(82792/1429))
  before the anova() verification; joint-usefulness-vs-individual-
  significance contrast read in this very output.
- Measurement-boundary handling kept exactly (source category, known_gender
  subset built in the WARM-UP so no hidden objects remain in class,
  releveling changes labels not fits, unknown records excluded rather than
  treated as a group).
- Two-level indicator worked as two group means drawn as ticks on an axis;
  G−1 dummies and the trap with CHECK.
- Units in thousands where money enters; all numbers re-verified.
- Caveat box: broad source coding, selected records, two reference
  contrasts, no essentialist or causal claim. Utility (EiA3) + Tilly added.

### i06-interactions-curvature.qmd — changes vs old I06-interactions-polynomials.Rmd

- Retitled to "Interactions and curvature"; anchor {#i06} kept.
- **Reordered picture-first** per scenario: new schematic figure
  `fig-i06-two-lines` (two lines, different slopes) appears BEFORE any
  formula, with the how-many-numbers PREDICT (Mentimeter committed in prep,
  resolved in class: four numbers), then the coefficient-to-feature mapping
  (bullet list) and the small two-row table of group intercepts and slopes.
- Interaction coefficient framed as a **difference in slopes with units**
  (equity percentage points per season, between groups), with the
  quantitative-by-quantitative slope β1 + β3Z noted in passing.
- Centering given its own treatment: what it changes (lower-order meanings —
  women coefficient moves from a Season-0 comparison, 1.35, to an
  average-season comparison, 0.81) and what it cannot change (fitted values,
  residuals, R², the interaction estimate) — plus a collapsed check.
- **NO HIDDEN OBJECTS**: old setup chunk built known_gender, women, season_c,
  and both models invisibly; now ALL setup is visible in the in-class fit
  chunk (matching i05's known_gender construction, plus this lecture's
  broader `women` indicator with an explicit measurement note that it differs
  from i05's three-category factor), and rebuilt inside the answer chunk and
  echo:false figure chunks so each runs alone.
- Converted running units from ask_100k to **ask_1k** ($1,000s); re-verified
  with Rscript: season/women/interaction coefficients unchanged (men slope
  −0.799, women-represented slope −0.861, interaction −0.0615, SE 0.096,
  p 0.520), ask_1k coefficient −0.00268 per $1,000; quadratic model
  b1 = −1.713, b2 = 0.0510, partial F = 20.15 (p = 7.7e-06), adjusted R²
  0.186 → 0.196; Season 5→6 change −1.15, 10→11 −0.64.
- **Kept the exemplary non-significant-interaction wording** migrated near
  verbatim: "does not provide evidence that the season trend differs … also
  does not prove the slopes are identical", extended with the aphorism "No
  evidence of different trends is not proof of equal trends."
- Hierarchy principle kept with the `x * z` expansion shorthand; added the
  scenario's block-parallel sentence before the break (slopes differ by
  group / slopes differ along x).
- **Promoted** the Season 5→6 fitted-change calculation to a worked example
  (@exm-i06-quadratic-change) via β1 + β2(2x + 1), with R verification chunk
  and the standing rule "never read β1 alone while x² is in the model"
  (derivation of the 2x + 1 recipe shown).
- Partial F for the added quadratic term in LIVE R (`anova`), with the
  detectable-vs-dramatic adjusted-R² note kept; no-extrapolation warning
  attached to the plotted curve, sharpened with the verified vertex ("bottoms
  out just past Season 16, then would climb").
- ONE caveat box (was a plain section "Extensions do not replace
  assumptions"): flexibility repairs nothing about design; terms come from
  substantive questions; overfitting warning added.
- Driving-question answer section added with actual numbers: no detectable
  slope difference (with its imprecision limit), detectable mild curvature
  (−1.56 early vs −0.64 late per season), Seasons 1–16 only, observational.
- Prep rebuilt: videos kept (Stanford 3.5 + 7.1, video-guide link added);
  two-line derivation kept with collapsed check; PREDICT Mentimeter added;
  R warm-up now builds season_c/women visibly and plots per-group fitted
  lines (per scenario); math-refresher link updated.
- After class rebuilt to scenario (60 + 5): retrieval 5; centering
  verification kept (executed answer chunk, uncentered vs centered);
  FADED quadratic change Season 10→11 (−0.64) then unassisted with new
  coefficients (revenue-on-shop-age quadratic; also absorbs old practice
  item 1, the Y = 10 + 2X + 3D − 0.5XD two-lines item); cumulative mini-task
  extending the i04 diagnostics paragraph with one interaction/polynomial
  argument; spaced review one i05 partial-F item (436.25/2 over 82,792/1,429
  → F 3.76); exam-style mock Q5 (interaction slope misread corrected);
  Make it yours (EiA3) + Tilly line.
- Old practice items 3 (adjusted R² comparison) folded into the body's
  partial-F discussion; item 5's "not evidence that composition never
  matters" reasoning folded into the interaction reading and utility prompt.
- Closing updated: continue to Tutorial 2; formula-sheet line added; old
  ISLR/Nieuwenhuis references kept.
- All chunks knit-tested from project root; outputs match every stated number.

### intermediate/t01-exam-prep.qmd — changes vs old I-EP01.Rmd

- Migrated to Quarto with the Basic t01 tutorial pattern: outcomes box,
  exam-prep branding paragraph, pairs-first-with-AI protocol, collapsed
  `callout-note` answers, course-phase divs, closing utility prompt + Tilly.
- Anchor {#i-ep01} kept. Title extended to "Simple regression, diagnostics,
  and model usefulness" to match the new Lecture 1–3 allocation (i02 =
  diagnostics, i03 = inference/fit).
- **Task ordering rule implemented and stated to students**: Tasks 1–2
  (Lecture 1: fit/interpret; fitted value and residual), Task 3 (Lecture 2:
  diagnostics + influence), Tasks 4–5 (Lecture 3: inference; R² and F) —
  earlier-lecture material first, the day-after lecture last, with a brief
  note explaining the ordering is deliberate.
- Old Task 3 ("Inference and diagnostics") split to match the new lecture
  split: diagnostics now a standalone Task 3 that ALSO covers the promoted
  i02 influence content (rstandard beyond ±3 → 12; Cook's 4/n screen → 21;
  ask-150/deal-3,000 record; investigate–report–never-silently-delete rule);
  inference is Task 4 (t-test, hand-verified interval, robust-SE limits
  question kept as its bridge item).
- Converted all units from $100,000s to **$1,000s**; every printed number
  re-verified by executed chunks: fitted equation 27.571 + 1.0085x; Task 2
  (ask $500,000, agreed $450,000): fitted 531.83 ($531,826), residual −81.83
  (−$81,826) — old chapter's $531,800/−$81,800 replaced by exact values;
  t = 55.4, CI (0.973, 1.044); SST/SSE/SSR in squared $1,000s; R² 0.777;
  F 3068.6 = t².
- NO HIDDEN OBJECTS: old setup chunk built deals/deal_model invisibly; now a
  visible `iep01-load` chunk builds the data once, and every answer chunk
  re-creates `deal_model` so it runs alone. Old ```r display-only answers
  replaced with executed chunks whose output backs the stated numbers.
- Before class: kept memory items and code-sheet pointer; code-sheet link
  updated to the new anchor; math-refresher link converted to
  ../resources/math-refresher.html; scope now Lectures 1–3 as now taught.
- After class: timed individual practice (equity ~ season, 20 minutes) kept,
  model answer updated with verified numbers (−0.824, SE 0.048,
  CI (−0.917, −0.731), R² 0.173, F 300.7) and the striped-residuals reading
  from the new i02; added "Check your understanding" memory items (Basic t01
  pattern); added Make it yours utility prompt (EiA3-anchored) + Tilly line.
- Closing: continue to Lecture 4 (new i04 title).
- All chunks knit-tested from project root; outputs match stated numbers.

### intermediate/t02-exam-prep.qmd — changes vs old I-EP02.Rmd

- Migrated to Quarto with the tutorial pattern: outcomes box, exam-prep
  branding, pairs-first-with-AI protocol, collapsed answers, course-phase
  divs, closing utility prompt + Tilly. Anchor {#i-ep02} kept.
- **Task ordering rule**: the old order already ran Lecture 4 → 5 → 6
  (multiple regression; dummies + partial F; interaction; polynomial); kept,
  with each task now labelled by lecture and a brief student-facing note that
  the ordering is deliberate (tutorial meets the day after Lecture 6).
- Converted all units from ask_100k to **ask_1k** ($1,000s), matching
  i04–i06; numbers re-verified by executed chunks: Task 1 ask coefficient now
  −0.0029 per $1,000 (stated alongside −0.29 per $100,000 for readability),
  description-words CI (−0.351, 0.095) added explicitly, adjusted R² 0.186,
  overall F 110.6 with df added; Task 2 dummies 1.28 / 0.12 points, partial
  F 3.76 (p 0.023) with the joint-vs-individual contrast sharpened (mixed
  p ≈ 0.82 named); Task 3 slopes −0.799 / −0.861, interaction −0.061
  (p 0.520) with the i06 "no evidence of different trends, not proof of
  equal trends" wording; Task 4 b1 −1.713, b2 0.051, change Season 10→11
  −0.64 via b1 + b2(2x+1), partial F 20.1.
- NO HIDDEN OBJECTS: old setup chunk built sharks/known_gender/gender/women/
  season_c invisibly; now one visible `iep02-load` chunk performs the full
  construction (matching i05's `gender` relevel and i06's `women`/`season_c`
  lines exactly).
- Percent-vs-percentage-points guard added to the Task 2 answer; Task 3 adds
  "without overclaiming in either direction" to the prompt.
- Timed integrated task (30 minutes) kept; model-structure answer updated to
  ask_1k and now name-checks `rstandard()`/Cook's distance among diagnostics.
- Added Make it yours utility prompt (EiA3-anchored, designing the analysis
  they would run on their own venture) + Tilly line.
- Closing pointers kept (code sheet, mock exam) with anchors; R-refresher
  pointer replaced by the resources the new book has (math refresher,
  external video guide) — ⚠ QUESTION: the old close also linked an
  "R Refresher" page; I found no such resource in the new book's resources/
  and left it out — restore if one exists.
- All chunks knit-tested from project root; outputs match stated numbers.

### intermediate/code-sheet.qmd — changes vs old intermediate-code-sheet.Rmd

- Migrated to Quarto; anchor {#intermediate-code-sheet} kept; all `\[ \]` /
  `\( \)` math converted to `$$` / `$` per conventions. Intro line now says
  the sheet pairs key commands with the formulas they implement, organised
  by lecture.
- **Section split rebalanced to the new lecture allocation**:
  - old "Lecture 2: Coefficient inference and diagnostics" split in two;
  - new **Lecture 2: Assumptions, residual diagnostics, and influence** —
    diagnostic plots, `summary(residuals(m))` five-number line (added, since
    the i02 lecture promoted it), `rstandard()`, `cooks.distance()`, count
    screens (|rstandard| > 3, Cook > 4/n added), `plot(m, which = …)`, and
    the investigate/report/never-silently-delete rule; kept here with an
    explicit pointer that these commands are now ALSO worked through in the
    Lecture 2 chapter itself;
  - new **Lecture 3: Coefficient inference, fit, and the F-test** — t-test,
    df = n − k − 1 (with the simple-regression n − 2 special case noted),
    interval formula, `confint`/`df.residual`/`nobs`, manual t/p
    verification, SST/SSR/SSE, R², adjusted R², residual standard error,
    overall F (now annotated with the "explained per predictor over residual
    per df" reading from i03), and the robust-SE snippet moved under
    Lecture 3 (it is an optional box there now, and the sheet says so).
- Thousands units: workflow example changed from `x_10k <- x_euros / 10000`
  to `x_1k <- x_euros / 1000` with a line naming thousands as the course's
  running unit choice; Lecture 1 section gains one closing sentence on the
  rescaling rule (same-factor rescale moves intercept, not slope) matching
  i01's worked note.
- Lecture 6 section: added the one-step change formula b1 + b2(2x + 1)
  (promoted to a worked example in i06) ahead of the general xA→xB form, and
  the "never interpret b1 alone" phrasing; `*` shorthand labelled as the
  hierarchy principle.
- Commands-by-purpose table: added `summary(residuals(m))` row; otherwise
  kept.
- Session table, workflow checklist, Lectures 4–5 sections, Nieuwenhuis
  reference, and mock-exam pointer kept essentially verbatim.
- File knit-tested (display-only ```r blocks, nothing executes; no hidden
  objects by construction).

### intermediate/mock-exam.qmd — changes vs old mock-exam-intermediate.Rmd

- Faithful migration to
  `/home/claude/work/textbook-qm-ebi/intermediate/mock-exam.qmd`: all 5
  questions, tasks, points, printed R outputs, and marking guides UNCHANGED.
- Kept the page anchor `{#intermediate-mock-exam}` (linked from
  code-sheet.qmd and t02-exam-prep.qmd) and the link to
  `#intermediate-code-sheet` (exists in code-sheet.qmd).
- **Seed and data preserved exactly**: `set.seed(734)`, n = 320, identical
  generation code and model formulas. Re-ran everything with Rscript from the
  project root: every printed number matches the old file exactly —
  simple model (6.60/0.52/12.72; 1.38/0.11/12.35; RSE 4.57 on 318 df;
  R² 0.324), multiple model (2.45, 1.34, 0.26, 0.17, 3.08; RSE 4.09 on 315;
  R² 0.464 / adj 0.457; F 68.10 on 4 and 315), SST 9,831.91, SSE 5,272.57,
  extended-model estimates (9.20, 1.04, 2.96, −0.11, 0.24, 0.68), and the
  partial-F ANOVA table (5317.0 / 5053.8, Sum of Sq 263.23, F 8.18,
  p 0.00035).
- Units left as the exam's own (`marketing_10k` in €10,000s, growth in
  percentage points) — NOT converted to the course's thousands-of-dollars
  convention, per instructions.
- No-hidden-objects: the old `include=FALSE` setup chunk is now a VISIBLE
  chunk (`imock-data`) inside "Dataset used throughout", introduced as "the
  code that generated the dataset", building the data frame and the four
  models. Only the CSV write (dir.create + write.csv) stays in a small
  `include: false` chunk (`imock-write-csv`) — it creates no analysis objects
  and is commented as such.
- CSV download mechanism kept: the chunk still writes
  `docs/data/qm-intermediate-mock-exam.csv` (project-root relative;
  execute-dir is project, output-dir is docs, so it lands in the rendered
  site). The download link path adapted from `data/…` to `../data/…` because
  the rendered page now lives at `docs/intermediate/mock-exam.html` instead of
  the bookdown site root. Verified the write works from the project root.
- Diagnostics figure chunk: converted to `#|` options, labelled
  `fig-imock-diagnostics` with a fig-cap, kept `echo: false`; it uses
  `simple_model` from the visible dataset chunk above (construction visible).
  Plot code unchanged.
- `<details>` answer blocks converted to `::: {.callout-note collapse="true"}`
  with `## Model answer and marking guide`; `\[ \]`/`\( \)` math → `$$`/`$`.
- Added the standard options-only setup chunk (`imock-setup`).
- Question order (Q2 diagnostics before Q3 fit/F-test) already matches the new
  i02/i03 lecture allocation; no lecture-number references needed fixing.
- ⚠ QUESTION: with `freeze: auto`, a re-render that replays the frozen chunk
  will not re-write `docs/data/qm-intermediate-mock-exam.csv` after `quarto
  render` cleans docs/. If that bites, list the CSV under `project:
  resources:` in _quarto.yml or write it via a pre-render script instead.

### Changes: resources/math-refresher.qmd (from math-refresher.Rmd)

- Migrated Rmd -> qmd: all `\[ \]` display math converted to `$$ $$`, all
  `\( \)` inline math converted to `$ $`. Pipe tables kept as-is. Plain
  (non-executed) ```r fences kept; page has no executable chunks, so nothing
  to run and no quarto render performed (per task instructions).
- Kept page anchor `{#math-refresher}`. Grepped all of basic/*.qmd and
  intermediate/*.qmd: every chapter links only to the page
  (`../resources/math-refresher.html`), never to a section anchor, so no
  section anchors needed adding; auto-generated heading IDs retained.
- "What each chapter needs" table updated for the new content allocation:
  - Lecture 3 row gains "squared deviations, roots" (variance/SD moved from
    L4 into L3).
  - Lecture 4 row: dropped "powers, square roots" (variance out), added
    "products" (independence of events with its product-form check moved in
    from L5).
  - Lecture 5 row unchanged (still needs products/sums for covariance).
  - Lecture 8 row: dropped "t distributions" (t moved to L9).
  - Lecture 9 row: now "t distributions, degrees of freedom, t critical
    values, intervals, two-sided zero contrasts".
  - Lecture 10 row: added "one-sided and two-sided alternatives" (one-sided
    moved into L10).
  - Basic Tutorial 3 row: now "sums, fractions, roots, z-scores" (matches
    the t03 chapter's pointer text; "degrees of freedom" moved to the
    Tutorial 4 row, where the t04 chapter pointer names it, since the t
    distribution now sits after Tutorial 3).
  - Intermediate Lecture 2 row: now "standardisation, inequalities"
    (intervals dropped; inference moved to L3 -- L2 is assumptions and
    diagnostics, needing standardised residuals and threshold inequalities).
  - Intermediate Lecture 3 row: now "standardisation, intervals, squares,
    ratios, sums of squares" (gains the inference math from old L2; matches
    the i03 chapter pointer "squares, proportions, and standardisation").
  - All chapter names in the table are now relative links to the actual
    chapter .qmd files (../basic/bNN-*.qmd, ../intermediate/iNN-*.qmd,
    tutorial files), which Quarto resolves in the book layout.
- Body text edits for the new allocation:
  - "Powers, roots, and squared deviations": "variance" now reads
    "variance (Lecture 3)".
  - "Sets and event notation": added a two-sentence independence definition
    (conditional and product forms) with "the algebraic check used in
    Lecture 4", since event independence now lives in L4.
  - "Rescaling dollars to $100,000s" changed to "to thousands of dollars"
    to match the Intermediate running units decision (ask_1k/deal_1k).
- Kept unchanged: order of operations, symbols table, interval notation,
  variables/functions, lines/slopes, subscripts, summation, degrees of
  freedom section (chapter-agnostic), fractions/rearranging, indicators,
  interactions, polynomials, and the references (OpenStax, Khan Academy,
  Walsh "R as a Calculator" link kept verbatim), plus the AI-practice
  closing line.
- Verified with Rscript against data/shark_tank_teaching.csv: 1441 rows,
  882 deals, mean(deal_on_show) = 0.6120749, so the "approximately 0.612;
  882/1441 exact" example stands.

### Changes: resources/r-refresher.qmd (from r-refresher.Rmd)

- Faithful migration; content essentially unchanged. All nine Walsh
  "Programming for E&BI" links (https://walshc.github.io/ebi-prog/...) kept
  verbatim, as required.
- Dropped the bookdown part header `# (PART) Supplementary resources {-}`
  -- in Quarto, parts are declared in _quarto.yml, not in chapter files.
  ⚠ QUESTION: when the resources pages are added to _quarto.yml, wrap them
  in `- part: "Supplementary resources"` to recreate the old part division.
- Kept page anchor `{#r-refresher}` (b01 links to this page).
- Converted the `<div class="exam-bridge">` box to
  `::: {.callout-important} ## Assessment reminder` -- the new book's
  assets/styles.scss does not define .exam-bridge, so the raw div would
  render unstyled; a callout keeps the emphasis. (Page had no
  details/summary, so no collapsed callouts needed.)
- Added one sentence at the end of the regression-workflow section linking
  to the new [Intermediate code sheet](../intermediate/code-sheet.qmd)
  (relative .qmd path), which did not exist as a separate page target in
  the old layout note there.
- Code blocks kept as plain ```r fences (not executed), exactly as in the
  old page -- the five-minute check is meant to be run by the student, and
  the page deliberately does not print answers. No executable chunks, so
  nothing to test with Rscript beyond confirming the data file loads
  (data/shark_tank_teaching.csv reads: 1441 rows).

### Changes: resources/video-guide.qmd (from video-guide.Rmd)

- Kept page anchor `{#videos}`; all chapters link to the page as
  `../resources/video-guide.html`, which resolves.
- ALL video links preserved -- verified by diffing the sorted URL sets of
  the old and new pages (identical). Kept the OCW resource-page links for
  MIT clips (with transcripts) rather than switching to the raw YouTube
  URLs the chapters use.
- Section headings renamed to the new chapter titles (e.g. "Basic Lecture
  4: Conditioning, Bayes' rule, and independence"; "Intermediate Lecture 2:
  What the model assumes and how residuals betray it").
- Required-at-a-glance table and per-lecture sections re-organised to match
  the scenarios' Before-class lists and the chapters' Video preparation
  boxes (checked every chapter's video-prep div against the guide):
  - L4 required is now Conditional Probabilities + Bayes' Rule only;
    MIT 06.2 Variance moved to Lecture 3 as "Review when needed" with a
    note that variance/SD are taught in class in L3 (the L3 scenario's
    required prep stays PMFs/CDFs/Expectation, so Variance could not stay
    "required").
  - MIT 03.3 Independence of Two Events moved from L5 review to L4 review
    (event independence now taught in L4); L5 keeps 07.4 Independence of
    Random Variables (joint-PMF independence stays in L5).
  - L9 required is now 20.5 + 20.7 + Intro to Hypothesis Testing, matching
    the b09 chapter box and scenario; 20.6 (known-variance interval)
    demoted to L9 "Review when needed" so the link is kept. Added the note
    that the t distribution opens Lecture 9.
  - L10 required unchanged (Intro to Hypothesis Testing review + Type I/II
    Errors), with an added note that one-sided alternatives are handled in
    class in L10.
  - Intermediate L2 entry now says "first half, focusing on what can go
    wrong; Lecture 3 handles the test mechanics" (per the i02 scenario and
    chapter box); Stanford 3.2 is additionally listed under Intermediate
    L3 as "Review when needed" (second half: SEs, intervals, tests against
    zero -- the content that moved to i03). Same URL, so no new links.
  - Stanford 3.4 stays under Intermediate L3; 3.3 under L4; 3.5 under L5
    (qualitative predictors) and L6 (+7.1); 3.R kept as the Intermediate
    optional extension.
- Chapter column of the at-a-glance table now links each lecture to its
  chapter .qmd via relative paths (../basic/..., ../intermediate/...).
- Kept: the three-purpose legend, the "only Required is compulsory" scope
  paragraph, both playlist links, the Bertsekas-Tsitsiklis supplementary
  reading section with PDF link, the "table matches the Video preparation
  boxes" line, and the closing notation caveat.
- No details/summary in the old page, so no collapsed callouts were
  needed. No executable chunks; no render performed per task instructions.
- ⚠ QUESTION: the b03 chapter's video-prep box links "Probability Mass
  Functions" to the OCW page but "CDFs"/"Expectation" to raw YouTube URLs,
  while this guide consistently uses OCW pages -- same clips, different
  hosts. Harmless, but the chapters could be made consistent later.

### Changes: resources/reading-ladder.qmd (from reading-ladder.Rmd)

- Faithful migration; the reading protocol, progression table, bounded
  reading list, and end-state benchmark are unchanged in substance.
- Kept page anchor `{#reading-ladder}`. All ten external paper links kept
  as DOI/publisher links only (link, don't republish -- no copyrighted text
  copied); added one sentence to the Purpose box saying papers are linked
  at their publishers and to follow the DOI through the university library.
- Converted `<div class="chapter-map">` (Purpose) and
  `<div class="paper-lens">` (End-state benchmark) to
  `::: {.callout-note}` blocks with `## Purpose` / `## End-state benchmark`
  titles -- those CSS classes do not exist in the new book's
  assets/styles.scss, so the raw divs would render unstyled. (No
  details/summary in the old page, so nothing needed `collapse="true"`.)
- Stage column now links the named Basic lectures to their chapters via
  relative .qmd paths (Lecture 1 -> b01, Lectures 2--3 -> b02/b03,
  Lecture 5 -> b05). The lecture numbers themselves needed no change: the
  content reallocation (variance to L3, independence to L4, t to L9,
  one-sided to L10) does not move any reading-ladder stage.
- Rows for "Advanced" stages kept verbatim even though the advanced/ book
  section is not yet populated with matching chapters -- plain text, no
  dead links.
- No math, no executable chunks; nothing to run. No render performed per
  task instructions.
- ⚠ QUESTION: "Supplied thesis, Table 2/Table 3" refers to a course-
  provided thesis that is not in the repo; confirm where students will
  access it (Canvas?) and whether the page should say so explicitly.


## 2026-08-30 — Utility examples and reading-ladder integration

- Every "Make it yours" utility question (all 16 lectures + 6 tutorials)
  gained a collapsed "See an example, then write your own" callout, using
  one consistent fictional venture (a student-run campus meal-prep box
  business) so the examples feel concrete and cumulative across the book.
- resources/reading-ladder.qmd rewritten STUDENT-FACING: the six-question
  protocol front and centre, a "where you meet papers" table tied to the
  chapters that now actually assign them, bounded-reading rule, Advanced
  rows kept as a preview. The "supplied thesis, Table 2/3" objects were
  replaced with published papers (user decision): Tierney & Farmer (2002)
  serves both the correlation-table reading (b05) and regression-column
  reading (i03).
- NEW standing element "From the reading ladder (10 minutes)" added to the
  After-class practice of five chapters, each a bounded piece of a real
  paper with a collapsed model approach: b01 (Ajzen 1991 abstract —
  constructs vs variables), b05 (Tierney & Farmer correlation table), i03
  (Tierney & Farmer regression column + R²), i04 (Zhao, Seibert & Hills
  2005 — controls and the holding-fixed sentence), i05 (Brooks et al. 2014
  — categorical comparison, pp-vs-percent, no-causal-slide). Practice
  budgets raised by 10 minutes in those five chapters.

## 2026-08-30 — Figure redesign (all 45 figures)

- Every data figure rebuilt in ggplot2 to a single validated style: one
  message colour #009E73, contrast/fits #D55E00, third series #0072B2 (the
  colourblind-safe Okabe-Ito trio, checked with a palette validator), navy
  ink annotations, gold dashed labelled reference lines; theme_minimal base,
  horizontal-only gridlines, zero-based count axes, direct labels over
  legends, axis labels with units; multi-panel comparisons as facets with
  shared axes (the b08 CLT figure now literally has the "same axes" the
  text stresses).
- Every data figure's code is attached and folded: "See the R code for this
  figure" — fully self-contained blocks (library + data + seed inside), so
  the figures double as graph-making lessons. Concept diagrams (event
  panels, partition, Bayes tree, nested-model boxes, two-ticks sketch) keep
  their drawing code folded under "optional, not exam material".
- PMFs switched from bars to stick-and-dot lollipops (the statistically
  standard form; also replaces the unfortunate silhouette of the old
  same-mean figure's left panel in b03).
- All seeds, bin breaks, and printed numbers preserved; every chunk
  extracted and run standalone to verify. New dependency: ggplot2 (and
  patchwork for the Intermediate mock exam's two-panel diagnostics).
- R Refresher gained "How the figures in this book are made": the install
  line, the principles, and the recommended path (r4ds ch. 1, Healy's
  socviz.co, Wilke's Fundamentals of Data Visualization).

## 2026-09-29 — Typography correction

- Body font switched to the stack the bookdown prototype actually rendered
  in: "Helvetica Neue", Helvetica, then system fallbacks, Arial last
  (the prototype's gitbook layer set .book.font-family-1 to Helvetica Neue,
  overriding the body rule everyone assumed was in effect). Windows
  students get Arial, exactly as on the old site. Body letter-spacing
  0.2px restored to match the prototype's text rendering.

## 2026-09-29 — Driving questions gain motivation context

- Every lecture's driving-question card now opens with one or two muted
  lead-in sentences of business context: what is being measured and why the
  question is worth answering (e.g. b02 grounds "how likely" in investor
  thinking; b07 in audit sampling; i04 in separating overlapping
  explanations). The question itself is unchanged and rendered brighter
  below the context. New .dq-context style in assets/styles.scss.

## 2026-09-29 — End-of-lecture transitions expanded

- Every lecture's closing "Next:" preview rewritten as a full bridge
  paragraph: what the lecture's tools now allow, the gap or question they
  leave open, and what the next session introduces (named objects, not
  topic labels) — e.g. b01 now explains why a probability model is needed
  and which events it will price; b08 explains why the interval needs the
  t distribution. Tutorial previews name what to bring and what gets
  reused.

## 2026-09-29 — Sidebar cleanup

- GitHub repository icon removed from the sidebar title area (repo-url
  unset; the repo is maintenance infrastructure, not a student link).

## 2026-10-06 — Freeze round

Three layers, applied in this order on the state of 29 September.

**1. Claude's review of 3 October** (`qm-fixes-all.patch`): 159 text fixes
and the structural changes A1 to A22 (founder's question at the start of
every lecture, founder's decision boxes, must-know boxes, valuations as the
running example of Intermediate Lectures 1 to 3, Basic Lectures 7 to 10
rebalanced, reading block removed, QM Advanced marked as work in progress,
hats on estimates, plain-language pass). Details in
`Review round Oct 6/Claude's independent review/files/qm-fixes-all.md`.

**2. Merged plan** (Gabriela's notes and gap analysis plus the check of the
patched text, `Review round Oct 6/merged-review-plan.md`), with Valentina's
decisions of 6 October (see `DECISIONS.md`).

- Whole book: "In class" renamed "Lecture material". Session narration and
  lecturer-facing remarks removed. After class starts with "Read the lecture
  material (15 minutes)", new minimum path, total times updated. After-class
  headings in plain words. Definition boxes and collapsed Optional boxes
  introduced, old optional boxes converted. Variables and data named at
  every data reference.
- Basic 1: definition boxes for population and sample, variable types,
  median, quartiles and IQR. Proportion and range explained. Complete
  variable table. Valuation numbers moved to where the code shows them.
- Basic 2: why data analysis needs probability. Three more properties of
  probability. Optional box with set rules. Capital and lower-case
  convention. Probability 0 and 1 stated correctly for all variables.
- Basic 3: CDF figure with flat ends. mu, sigma squared, sigma introduced.
  Bernoulli box. A function of a random variable is a random variable.
  Shifting and rescaling with the SD rule, practised after class and in
  Tutorial 1. Interval rule for the CDF.
- Basic 4: conditional probability in words before the symbol. Complement
  rule under a condition. Definition boxes.
- Basic 5: new section "Sums of two variables". Covariance as a sum over the
  joint PMF. Conditional mean practised. Third variable explained.
- Basic 6: single value has probability zero and density explained with
  shrinking windows on equity offered (after Gabriela's text). Complement
  and symmetry rules. Quantile and percentile defined. Central 95% brought
  forward. Four new figures. Optional box with the integral. Sum of
  independent normals.
- Basic 7: random sample X_1..X_n and iid. Table parameter, estimator,
  estimate. Unbiasedness with a figure. Optional box on sampling without
  replacement.
- Basic 8: binomial section with figure. Estimated standard error of a
  proportion. Consistency. Sample size for a target margin of error.
  Probability for a sample mean worked in the lecture material.
- Basic 9: new title. Condition added to the interval recipe. Margin of
  error as precision. Multipliers come from the question or the sheet.
- Basic 10: critical-value rule. One-sided tests in one optional box. Two
  exam-style items given new numbers.
- Tutorials 1 to 4: new task parts for the added skills, one-sided leftovers
  removed, Phi notation removed, a model report added in Tutorial 4.
- Formula sheet: rules moved to the lectures that teach them (Lecture 3:
  shifting and rescaling, Lecture 5: sums). Added: quartiles and IQR, three
  properties of probability, short Bayes rule, conditional mean, uniform SD,
  complement and symmetry, unbiasedness, estimated SE of a proportion,
  binomial mean and variance, sample size, critical-value rule. Formal
  random-variable mapping and the perp symbol removed.
- Basic mock exam: Questions 3 and 5 given new numbers, because the lectures
  used the old ones.

**3. Intermediate points of 6 October.**

- Overview: the data, what the course builds on (table with links into
  Basic), a part for students who took Basic before 2026, laptop and
  code-along note, TestVision note.
- Lecture 1: least-squares formulas explained in words, slope as covariance
  over variance and as correlation times s_Y over s_X, R check. Units
  example moved after the fitted model.
- Lecture 3: decomposition figure redrawn. Residual standard error worded
  correctly. Robust standard errors as a normal section with output.
- Lecture 4 and Tutorial 2: specification tables in the layout of a research
  paper, with a `modelsummary` snippet.
- Lecture 6: founder's decision with consistent arithmetic.
- Mock exam: TestVision paragraph, wording, one answer extended.
- How to succeed: routine, minimum path, "what is examined", hours and
  checklists recomputed.

Verification: full render with Quarto 1.6.42 without errors or warnings, all
R chunks run from a clean session, internal links and anchors checked, three
independent reviews of the final text (statistics, order, wording) with all
findings applied.

How to succeed, same day: the calendar now gives dates and start times from
the programme timetable (TimeEdit export of 6 October), including the one
Basic lecture at 10:45 on Monday 26 October and the two tutorial slots per
group.
