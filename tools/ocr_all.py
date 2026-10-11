import sys,os
sys.path.insert(0,os.path.dirname(__file__))
from ocr import run
R=r"C:\Users\rajes\OneDrive\Documents\GitHub\NPTEL-The-Joy-of-Computing-using-Python\JRG JOC"
jobs=["quizzes/2022-jan/extra-sources/JOC Jan-2022 Wk1 quiz (image-only).pdf",
"quizzes/2026-jan/extra-sources/JOC Jan-2026 Wk2 quiz (image-only).pdf",
"quizzes/2026-jan/extra-sources/JOC Jan-2026 Wk7 quiz (not submitted, no answers, image-only).pdf",
"quizzes/2024-jan/extra-sources/JOC Jan-2024 Wk3 quiz (image-only).pdf",
"quizzes/2025-jul/extra-sources/JOC Jul-2025 Wk4 quiz (image-only).pdf",
"exams/34 questions asked in JOC final center exam morning session.pdf",
"quizzes/2022-jul/JOC_2022_JulDec (scanned portal print, due 2022-08-10).pdf"]
for j in jobs:
    p=os.path.join(R,j)
    if os.path.exists(p): run(p,p[:-4]+".ocr.txt",200)
    else: print("missing",j)
print("DONE")
