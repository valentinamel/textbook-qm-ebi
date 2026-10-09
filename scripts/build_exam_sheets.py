#!/usr/bin/env python3
"""Build the two exam PDFs from the sheet pages of the textbook.

    python3 scripts/build_exam_sheets.py

One source of truth: the PDF holds exactly the body of the web page, that
is, everything between `::: {.formula-sheet}` and the matching `:::` in

    basic/formula-sheet.qmd       -> assets/downloads/qm-basic-formula-sheet.pdf
    intermediate/code-sheet.qmd   -> assets/downloads/qm-intermediate-code-sheet.pdf

The introduction above that block is for the web page only.

Needs pandoc and xelatex (TeX Live or TinyTeX with amsmath, fontspec,
geometry, multicol, tabularx, fancyvrb, upquote). No R or Python packages.

Options:
    --keep DIR   also write the intermediate .tex and .log files to DIR
    --only NAME  build one sheet only (basic or intermediate)

The script stops with an error when a formula, a table, or a code line is
wider than its column, or when a sheet has more pages than `max_pages`.
"""

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILTER = Path(__file__).resolve().parent / "exam_sheet.lua"
BOOK_TITLE = r"Quantitative Methods to Understand E\&BI"

SHEETS = {
    "basic": dict(
        source="basic/formula-sheet.qmd",
        output="assets/downloads/qm-basic-formula-sheet.pdf",
        title="QM Basic Formula Sheet",
        orientation="portrait",
        columns=2,
        font_pt=9.0,        # never below 8
        lead_pt=10.5,
        code_pt=8.0,
        max_pages=2,        # front and back of one sheet
    ),
    "intermediate": dict(
        source="intermediate/code-sheet.qmd",
        output="assets/downloads/qm-intermediate-code-sheet.pdf",
        title="QM Intermediate Code Sheet",
        orientation="portrait",
        columns=2,
        font_pt=9.0,
        lead_pt=10.8,
        code_pt=8.5,        # 58 characters fit one column
        max_pages=4,
    ),
}

TEMPLATE = r"""\documentclass[10pt]{article}
\usepackage[a4paper,@@ORIENTATION@@,left=9mm,right=9mm,top=15mm,bottom=8mm,
            headheight=5mm,headsep=3mm,footskip=0mm]{geometry}
\usepackage{amsmath,amssymb}
\usepackage{fontspec}   % Latin Modern text, Computer Modern mathematics
\usepackage{multicol,array,tabularx,fancyvrb,upquote}

\makeatletter
% --- font sizes ----------------------------------------------------------
\newcommand\sheetsize{\fontsize{@@FONT@@}{@@LEAD@@}\selectfont}
\renewcommand\normalsize{\sheetsize
  \abovedisplayskip 3pt \belowdisplayskip 3pt
  \abovedisplayshortskip 2pt \belowdisplayshortskip 2pt}
\newcommand\sheetcodesize{\fontsize{@@CODE@@}{@@CODELEAD@@}\selectfont}
\newcommand\sheetheadsize{\fontsize{@@HEAD@@}{@@HEADLEAD@@}\selectfont}

% --- running head: title, book, page number --------------------------------
\def\ps@sheet{%
  \def\@oddhead{\vbox{\hbox to\textwidth{\sheetheadsize
    \textbf{@@TITLE@@}\hfil @@BOOK@@\hfil Page \thepage}%
    \vskip 2pt\hrule height 0.6pt}}%
  \let\@evenhead\@oddhead \def\@oddfoot{}\let\@evenfoot\@oddfoot}
\pagestyle{sheet}

% --- layout ----------------------------------------------------------------
\setlength\parindent{0pt}
\setlength\parskip{1.5pt}
\setlength\columnsep{7mm}
\setlength\columnseprule{0.3pt}
\setlength\multicolsep{0pt}
\setlength\tabcolsep{4pt}
\renewcommand\arraystretch{1.08}
\setlength\topsep{2pt}
\setlength\partopsep{0pt}
\raggedcolumns
\raggedbottom
\providecommand\tightlist{\setlength\itemsep{0pt}\setlength\parskip{0pt}}

% Section heading by lecture. Never left alone at the foot of a column.
\newcommand\sheetsection[1]{\par\addpenalty{-300}\addvspace{5pt plus 2pt}%
  {\interlinepenalty\@M\raggedright\sheetheadsize\bfseries #1\par}%
  \nobreak\vskip 1pt\hrule height 0.4pt\nobreak\vskip 2.5pt\@afterheading}

% Name of a formula or of a block of code. Stays with what follows it.
\newcommand\sheetlabel[1]{\par\addpenalty{-100}\addvspace{3pt plus 1pt}%
  {\interlinepenalty\@M\raggedright\bfseries #1\par}\nobreak\@afterheading}

% Display formula: its parts wrap at the places where the source has \qquad.
\newcommand\sheetsep{\hskip 1.5em plus 0.5em minus 0.3em\relax}
\newenvironment{sheetformula}{\par\vskip 1.5pt\begingroup
  \leftskip 1em\rightskip 0pt plus 1fil\parfillskip 0pt
  \interlinepenalty\@M \relpenalty\@M \binoppenalty\@M
  \lineskiplimit 2.5pt\lineskip 2.5pt\arraycolsep 3pt\noindent\ignorespaces}
  {\par\endgroup\vskip 1.5pt}

\newenvironment{sheettable}{\par\vskip 1.5pt\noindent\ignorespaces}{\par\vskip 1.5pt}

\newdimen\sheetcodeindent \sheetcodeindent=4pt
\fvset{fontsize=\sheetcodesize,samepage=true,xleftmargin=\sheetcodeindent}
\makeatother

\newcommand\sheetcolumns{@@COLUMNS@@}

\begin{document}
\normalsize
% Report how many code characters fit in one column (read by the script).
\begingroup\makeatletter
\dimen0=\textwidth \advance\dimen0 -\numexpr\sheetcolumns-1\relax\columnsep
\divide\dimen0 by \sheetcolumns \advance\dimen0 -\sheetcodeindent
\setbox2\hbox{\sheetcodesize\ttfamily M}%
\count0=\dimen0 \divide\count0 by \wd2
\typeout{SHEET-CODE-CHARS \the\count0}%
\endgroup
@@BODY@@
\end{document}
"""


def sheet_body(path: Path) -> str:
    """Return the text between `::: {.formula-sheet}` and its closing `:::`."""
    lines = path.read_text(encoding="utf-8").splitlines()
    try:
        start = next(i for i, line in enumerate(lines)
                     if re.match(r"^:::+\s*\{\.formula-sheet\}\s*$", line))
    except StopIteration:
        sys.exit(f"{path}: no '::: {{.formula-sheet}}' block found")
    depth, in_code, body = 1, False, []
    for line in lines[start + 1:]:
        if line.startswith("```"):
            in_code = not in_code
        elif not in_code and re.match(r"^:::+", line):
            if re.match(r"^:::+\s*$", line):
                depth -= 1
                if depth == 0:
                    return "\n".join(body) + "\n"
            else:
                depth += 1
        body.append(line)
    sys.exit(f"{path}: the '::: {{.formula-sheet}}' block is not closed")


def code_lines(body: str) -> list[str]:
    """Return the lines of all fenced code blocks of the sheet body."""
    lines, in_code = [], False
    for line in body.splitlines():
        if line.startswith("```"):
            in_code = not in_code
        elif in_code:
            lines.append(line)
    return lines


def run(cmd, **kwargs):
    return subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                          text=True, **kwargs)


def build(name: str, cfg: dict, keep: Path | None) -> bool:
    source = ROOT / cfg["source"]
    body_md = sheet_body(source)
    pandoc = run(["pandoc", "--from", "markdown", "--to", "latex",
                  "--lua-filter", str(FILTER)], input=body_md)
    if pandoc.returncode != 0:
        print(pandoc.stdout)
        sys.exit(f"{name}: pandoc failed")

    tex = TEMPLATE
    for key, value in {
        "ORIENTATION": cfg["orientation"],
        "FONT": f'{cfg["font_pt"]}pt',
        "LEAD": f'{cfg["lead_pt"]}pt',
        "CODE": f'{cfg["code_pt"]}pt',
        "CODELEAD": f'{cfg["code_pt"] * 1.17:.2f}pt',
        "HEAD": f'{cfg["font_pt"] + 1}pt',
        "HEADLEAD": f'{(cfg["font_pt"] + 1) * 1.2:.2f}pt',
        "TITLE": cfg["title"],
        "BOOK": BOOK_TITLE,
        "COLUMNS": str(cfg["columns"]),
        "BODY": pandoc.stdout,
    }.items():
        tex = tex.replace(f"@@{key}@@", value)

    ok = True
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        (tmp / "sheet.tex").write_text(tex, encoding="utf-8")
        env = dict(os.environ, SOURCE_DATE_EPOCH="0", FORCE_SOURCE_DATE="1")
        for _ in range(2):
            xelatex = run(["xelatex", "-interaction=nonstopmode",
                           "-halt-on-error", "sheet.tex"], cwd=tmp, env=env)
        log = (tmp / "sheet.log").read_text(encoding="utf-8", errors="replace")
        if keep:
            keep.mkdir(parents=True, exist_ok=True)
            shutil.copy(tmp / "sheet.tex", keep / f"{name}.tex")
            shutil.copy(tmp / "sheet.log", keep / f"{name}.log")
        if xelatex.returncode != 0 or not (tmp / "sheet.pdf").exists():
            print(xelatex.stdout[-3000:])
            sys.exit(f"{name}: xelatex failed")

        pages = int(re.search(r"Output written on .*\((\d+) pages?", log).group(1))
        code_chars = int(re.search(r"SHEET-CODE-CHARS (\d+)", log).group(1))
        too_long = [line for line in code_lines(body_md) if len(line) > code_chars]
        for line in too_long:
            print(f"  {name}: code line longer than {code_chars} characters: {line}")
        if too_long:
            ok = False
        problems = [line for line in log.splitlines()
                    if line.startswith(("Overfull \\hbox", "Missing character",
                                        "LaTeX Warning: Reference"))]
        for line in problems:
            print(f"  {name}: {line}")
        if problems:
            ok = False
        if pages > cfg["max_pages"]:
            print(f"  {name}: {pages} pages, more than the {cfg['max_pages']} allowed")
            ok = False

        target = ROOT / cfg["output"]
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(tmp / "sheet.pdf", target)
        print(f"{cfg['output']}: {pages} pages, text {cfg['font_pt']} pt, "
              f"code {cfg['code_pt']} pt ({code_chars} characters per line), "
              f"{cfg['columns']} columns, A4 {cfg['orientation']}")
    return ok


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--keep", type=Path, help="directory for .tex and .log")
    parser.add_argument("--only", choices=sorted(SHEETS))
    args = parser.parse_args()
    for tool in ("pandoc", "xelatex"):
        if shutil.which(tool) is None:
            sys.exit(f"{tool} is not installed")
    names = [args.only] if args.only else list(SHEETS)
    results = [build(name, SHEETS[name], args.keep) for name in names]
    if not all(results):
        sys.exit("Built with problems: see the lines above.")


if __name__ == "__main__":
    main()
