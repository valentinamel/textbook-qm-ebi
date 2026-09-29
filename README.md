# Quantitative Methods to Understand E&BI — official textbook

Official student textbook for the QM learning line (QM Basic, QM
Intermediate, QM Advanced) in Tilburg's Entrepreneurship and Business
Innovation bachelor programme.

- **Published site:** https://valentinamel.github.io/textbook-qm-ebi (linked
  from Canvas)
- **Build system:** [Quarto](https://quarto.org) book, rendered to `docs/`
  and served by GitHub Pages.
- **Chapter sources:** the per-lecture scenario files in
  `lecture-scenarios/` are the master plan; each chapter is derived from its
  scenario. `DECISIONS.md` records editorial decisions, `CHANGELOG.md` what
  changed per chapter relative to the prototype.
- The previous prototype (valentinamel.github.io/textbook-prototype) stays
  untouched as internal reference.

## Build locally

Install Quarto (https://quarto.org/docs/get-started/) and R with `knitr`,
`rmarkdown`, `ggplot2`, and `patchwork`
(`install.packages(c("knitr", "rmarkdown", "ggplot2", "patchwork"))`).
Then, from this directory:

```sh
quarto render
```

Preview with live reload while editing:

```sh
quarto preview
```

The rendered site appears in `docs/`. Commit both source and `docs/` and
push; GitHub Pages serves `docs/`.

## Data

`data/shark_tank_teaching.csv` is the frozen teaching view (1,441 pitches,
Seasons 1–16) derived from the archived Kaggle snapshot by
`scripts/build_teaching_data.R`. See `data/README.md` for variables,
interpretation rules, and integrity checksums. Chapters read the file with
the repo root as working directory (`execute-dir: project`).

## Conventions

- No hidden objects: every object used in chapter code is constructed in
  visible code on the same page.
- One caveat box per lecture, navy/teal; collapsed model answers after every
  substantive question; stated time budgets on Before/After class; numbered
  figures.
