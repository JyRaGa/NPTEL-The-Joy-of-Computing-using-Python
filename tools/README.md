# tools/

Scripts used to build `JRG JOC/` (Python 3.14; OCR/PDF parts ran in a venv with `pymupdf`, `rapidocr-onnxruntime`, `pillow`). Paths inside are absolute to the author's machine; edit `R`/`D` at the top before re-running.

| Script | What it does |
|---|---|
| `build.py` | Copies the canonical Q&A files from the original repo layout into `JRG JOC/` (term folders, `programming-assignments/`, `exams/`, `practice/`). Copy only, skips files that exist. Writes `_manifest.tsv`. |
| `mirror.py` | Downloads every `storage.googleapis.com/.../assets/img/...` image used by the quiz markdown into `quizzes/<term>/img/<noc code>/` and rewrites the links to relative paths. List in `sources/mirrored_images.tsv`. |
| `ocr.py`, `ocr_all.py` | RapidOCR over image-only PDFs, writing `<name>.ocr.txt` next to each PDF (page markers `=== page N ===`). Machine-read: spacing and some characters are wrong. |
| `portal2md.py` | Parses NPTEL portal review printouts (PDF text layer) into `week-NN.md`: question, options, `[x]` = Accepted Answer, score line, plus a PNG crop of each question (`img/wNN-qNN-pP.png`) that is the ground truth. If a `week-NN.md` already exists from another source it writes `week-NN-portal-print.md` instead. |
| `conv2026.py` | Converts the Jul-2026 case-study PDFs (`2026 Assignments/`) to markdown with embedded code/figure images; Wk11–12 are scanned pages with an OCR layer. |
