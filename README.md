# JRG JOC: NPTEL "The Joy of Computing using Python" past questions and answers

Past weekly quizzes (and some programming assignments and exam material) for the IIT Ropar course, organised by NPTEL session. Everything here is **copied or derived** from the surrounding repo; nothing was deleted from the originals. Audit and per-file verdicts: [structure.md](structure.md). Every copied file is listed in [_manifest.tsv](_manifest.tsv); every markdown file with its source kind and trust level is in [inventory.tsv](inventory.tsv). Scripts that built this folder: [tools/](tools/).

Quiz questions, options and official answers are the course material of NPTEL / IIT Ropar and are reproduced here for study only. Upstream code licences are in [licenses/](licenses/).

## Layout

```
quizzes/<year>-<jan|jul>/
    week-NN.md                 one file per week (source differs by term, see inventory.tsv)
    week-NN-portal-print.md    second source for the same week, parsed from an NPTEL portal printout
    week-NN.pdf                2026-jul only: the owner's case-study PDFs
    *.pdf, *.ocr.txt           whole-term PDFs; OCR text of scanned PDFs (machine-read)
    extra-sources/             extra Scribd printouts for that term
    img/                       images the week files refer to (mirrored swayam images, page crops, figures)
    notebooks/, chatgpt-converted-md/   Jul-2023 only
programming-assignments/<term>/week-NN/*.py      solution code (Jan-2021, Jul-2021, Jan-2022)
exams/                         final-exam recollection (+ OCR text), online programming test, exam patterns
practice/                      IMP-question sets, topic lists, small MCQ banks
sources/ licenses/             where each file came from; upstream licences; mirrored-image list
_reference/                    low-trust material kept for reference only
```

Session rule: Week 1 in Dec/Jan = **Jan** session (Jan–Apr); Week 1 in Jul/Aug = **Jul** session (Jul–Oct).

## Conventions in the `week-NN.md` files

- Question text, all options and code are verbatim; `[x]` = the option shown ticked or marked in the source.
- **Trust differs by source.** In `*portal print*` files (`Week N: portal print` header), `[x]` = NPTEL's own Accepted Answer, and each question has a cropped page image (`img/wNN-qNN-pP.png`) that is the ground truth when the parsed text is noisy or the options are images. In video transcriptions and second-repo markdown, a tick is only the uploader's pick; Jul-2019 files carry an official-answers section that overrides it. In 2026-jul, answers are as printed in the owner's PDFs.
- Images that could not be transcribed are described in text; swayam-hosted images were downloaded into `img/` and the links made relative.
- OCR text (`*.ocr.txt`) is machine-read: spacing and some characters are wrong.

## Coverage

| Session | Quiz files in this folder |
|---|---|
| 2018-jul | portal print Wk1–6, 8–10 (88 accepted answers) + `JOC 2018.pdf`; video transcriptions Wk1–2 (Wk2 Q1 missing) |
| 2019-jan | week-03 … week-12 (video) |
| 2019-jul | week-01 … week-12 (video), checked against the official review page |
| 2020-jan | portal print Wk1–12 (Wk8 parsed 9 of 10 questions) + PDF + scrambled Scribd printouts |
| 2020-sep | portal print Wk1–12 + PDF; decoded answer sheets Wk1–12 (`extra-sources/`) |
| 2021-jan | week-00 … week-12 (md, second repo) + portal print Wk1–12; solutions in `programming-assignments/` |
| 2021-jul | week-00 … week-12 (md); solutions |
| 2022-jan | week-00 … week-12 (md); solutions |
| 2022-jul | week-00 … week-12 (video); scanned portal print of the same term (due 2022-08-10) with OCR text |
| 2023-jan | week-00 … week-12 (video) |
| 2023-jul | week-07 … week-12 (video); Wk1–12 ChatGPT-converted md and notebooks with screenshots; Wk1–6 Scribd printout |
| 2024-jan | week-00 … week-12 (video) + Scribd extras |
| 2024-jul | portal print Wk0–12 (every question has an Accepted Answer) |
| 2025-jan | portal print Wk1–12 + two PDFs + Scribd printouts (Wk2–6) |
| 2025-jul | Scribd answers + explanations Wk1–12 (no Wk5); week-05 (video) |
| 2026-jan | week-01 … week-12 (video, 15 questions per week) + Scribd extras |
| 2026-jul | week-01 … week-12 from the owner's `2026 Assignments/` PDFs (only source used for this session); Wk1–10 text + figures, Wk11–12 scanned pages with OCR text |

Known gaps: 2019-jan Wk1–2 (no source found); 2018-jul Wk7, 11, 12 (not in the PDF); 2023-jul Wk1–6 have no per-week transcription of their own beyond the ChatGPT md and notebooks; 2020-jul probably does not exist (2020 ran off-cycle as Sep-2020).

## Still to do

- Parse the OCR text of the scanned Jul-2022 print and the other image-only PDFs into week files; extract the Jul-2023 notebooks' screenshots.
