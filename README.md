# Quantitative Methods to Understand E&BI: official textbook

Official student textbook for the QM learning line (QM Basic, QM
Intermediate, QM Advanced) in Tilburg's Entrepreneurship and Business
Innovation bachelor programme.

- **Published site:** https://valentinamel.github.io/textbook-qm-ebi (linked
  from Canvas)
- **Build system:** [Quarto](https://quarto.org) book, rendered to `docs/`
  and served by GitHub Pages.
- **Chapter sources:** `DECISIONS.md` records the agreed decisions and is
  authoritative. `CHANGELOG.md` records what changed per chapter.
- The previous prototype (valentinamel.github.io/textbook-prototype) stays
  untouched as internal reference.

## Build locally

Install Quarto (https://quarto.org/docs/get-started/) and R with `knitr`,
`rmarkdown`, `ggplot2`, `patchwork`, `lmtest`, and `sandwich`
(`install.packages(c("knitr", "rmarkdown", "ggplot2", "patchwork",
"lmtest", "sandwich"))`). The last two are needed for the robust standard
errors in Intermediate Lecture 3. Render in a UTF-8 locale.
Then, from this directory:

```sh
quarto render
```

Preview with live reload while editing:

```sh
quarto preview
```

The rendered site appears in `docs/`. Commit both source and `docs/` and
push. GitHub Pages serves `docs/`.

## Exam sheets as PDF

The QM Basic Formula Sheet and the QM Intermediate Code Sheet are attached
to the exams. Their PDFs are built from the sheet body of the two pages
(`basic/formula-sheet.qmd`, `intermediate/code-sheet.qmd`), so the web page
and the exam attachment cannot drift apart:

```sh
python3 scripts/build_exam_sheets.py
```

The script needs pandoc and xelatex. It writes
`assets/downloads/qm-basic-formula-sheet.pdf` (two pages) and
`assets/downloads/qm-intermediate-code-sheet.pdf` (three pages) and stops
when a formula or a code line is wider than its column. Run it after every
change to a sheet, then render the book.

## Data

`data/shark_tank_teaching.csv` is the frozen teaching view (1,441 pitches,
Seasons 1–16) derived from the archived Kaggle snapshot by
`scripts/build_teaching_data.R`. See `data/README.md` for variables,
interpretation rules, and integrity checksums. Chapters read the file with
the repo root as working directory (`execute-dir: project`).

## Conventions

- No hidden objects: every object used in chapter code is constructed in
  visible code on the same page.
- One caveat box per lecture, navy/teal. Collapsed model answers after every
  substantive question. Stated time budgets on Before class and After class
  of every lecture and tutorial, and minutes per tutorial task. Numbered
  figures.
- Chapter parts: Before class, Lecture material, After class. The text is
  written for the student only: no classroom script, no lecturer's notes.
- Definition boxes (`.definition-box`) are examinable. Optional boxes
  (`callout-tip`, collapsed, title starts with "Optional:") are not.
- Format names (see `DECISIONS.md`, 2026-10-09): "Check your preparation"
  before class, "Worked exam interpretation: <topic>" after class, invented
  examples start with "An invented example.", and every page ends with
  "Continue to <next item in `_quarto.yml`>: <its title>".
