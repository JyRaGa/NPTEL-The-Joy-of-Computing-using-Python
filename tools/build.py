import os,re,shutil,glob
R=r"C:\Users\rajes\OneDrive\Documents\GitHub\NPTEL-The-Joy-of-Computing-using-Python"
O=os.path.join(R,"JRG JOC")
log=[]
def cp(src,dst):
    src=os.path.join(R,src); dst=os.path.join(O,dst)
    if not os.path.exists(src): print("MISSING",src); return
    os.makedirs(os.path.dirname(dst),exist_ok=True)
    if os.path.exists(dst): return
    shutil.copy2(src,dst); log.append((os.path.relpath(src,R),os.path.relpath(dst,O)))
def term(s):  # "Jan-2019" -> "2019-jan"
    m,y=s.split('-'); return f"{y}-{m.lower()}"
Y="_incoming/youtube"; S="_incoming/scribd"
# 1. YouTube transcriptions -> quizzes/<term>/week-NN.md
for f in sorted(glob.glob(os.path.join(R,Y,"JOC *.md"))):
    n=os.path.basename(f); m=re.match(r"JOC (\w+-\d+) Wk(\d+) ",n)
    cp(f"{Y}/{n}",f"quizzes/{term(m[1])}/week-{int(m[2]):02d}.md")
# images referenced by those files
for f in glob.glob(os.path.join(R,Y,"img","*")):
    n=os.path.basename(f); m=re.match(r"(\w+-\d+)-W",n)
    cp(f"{Y}/img/{n}",f"quizzes/{term(m[1])}/img/{n}")
# 2. Scribd PDFs -> quizzes/<term>/extra-sources/
for f in sorted(glob.glob(os.path.join(R,S,"JOC *"))):
    n=os.path.basename(f)
    if os.path.isdir(f): continue
    m=re.match(r"JOC (\w+-\d+)",n)
    if m: cp(f"{S}/{n}",f"quizzes/{term(m[1])}/extra-sources/{n}")
    else: cp(f"{S}/{n}",f"practice/{n}")
# 3. Canonical PDFs
cp("Question Papers/JOC 2018.pdf","quizzes/2018-jul/JOC 2018.pdf")
cp("Question Papers/JOC Jan-Aug 2020.pdf","quizzes/2020-jan/JOC Jan-Aug 2020.pdf")
cp("Question Papers/JOC Sep-Dec 2020.pdf","quizzes/2020-sep/JOC Sep-Dec 2020.pdf")
cp("NptelQuizzes.pdf","quizzes/2020-sep/NptelQuizzes (cipher text layer, see decoded txt in extra-sources).pdf")
cp("4th repo/Previous Year Quizes/1. Joc 2021 January to April.pdf","quizzes/2021-jan/JOC Jan-Apr 2021 (text PDF).pdf")
cp("Question Papers/JOC_2022_APRIL_DEC.pdf","quizzes/2022-jul/JOC_2022_JulDec (scanned portal print, due 2022-08-10).pdf")
cp("JOY-OF-COMPUTING-USING-PYTHON.pdf","quizzes/2024-jul/JOY-OF-COMPUTING-USING-PYTHON (portal print, Wk0-12).pdf")
cp("Python-NPTEL.pdf","quizzes/2025-jan/Python-NPTEL (portal print, Wk1-12).pdf")
cp("The-Joy-of-Computing-Using-Python-JAN-2025.pdf","quizzes/2025-jan/The-Joy-of-Computing-Using-Python-JAN-2025 (typed, inline answers).pdf")
# 4. second repo: Jan-2021, Jul-2021, Jan-2022
S2="second repo/NPTEL-The-Joy-of-Computing-using-Python-main"
for src,t,pat in [(S2,"2021-jan",r"Week(\d+)$"),(S2+"/Aug - Dec 2021 JOC Course","2021-jul",r"Week (\d+)$"),(S2+"/Jan - Apr 2022 JOC Course","2022-jan",r"Week (\d+)$")]:
    for d in sorted(glob.glob(os.path.join(R,src,"Week*"))):
        m=re.search(pat,d)
        if not m: continue
        w=int(m[1]); wn=os.path.basename(d)
        for f in sorted(os.listdir(d)):
            if f=="README.md": cp(f"{src}/{wn}/{f}",f"quizzes/{t}/week-{w:02d}.md")
            elif f.endswith(".py"): cp(f"{src}/{wn}/{f}",f"programming-assignments/{t}/week-{w:02d}/{f}")
# 5. Jul-2023: Assignments md, third-repo notebooks
for f in sorted(glob.glob(os.path.join(R,"Assignments","WEEK *.md"))):
    n=os.path.basename(f); w=int(re.search(r"(\d+)",n)[1])
    cp(f"Assignments/{n}",f"quizzes/2023-jul/chatgpt-converted-md/week-{w:02d}.md")
for f in sorted(glob.glob(os.path.join(R,"third repo","Week *","*.ipynb"))):
    p=os.path.relpath(f,R).replace("\\","/"); cp(p,f"quizzes/2023-jul/notebooks/{os.path.basename(f)}")
# 6. Jul-2026: use ONLY '2026 Assignments'
for f in sorted(glob.glob(os.path.join(R,"2026 Assignments","*.pdf"))):
    n=os.path.basename(f); m=re.search(r"(?:week[-_ ]?)(\d+)",n,re.I)
    cp(f"2026 Assignments/{n}",f"quizzes/2026-jul/week-{int(m[1]):02d}.pdf")
# 7. Exams / practice / reference
cp(S2+"/Online Programming Test Solution/README.md","exams/online-programming-test-2021/README.md")
for n in os.listdir(os.path.join(R,S2,"Online Programming Test Solution")):
    if n.endswith(".py"): cp(f"{S2}/Online Programming Test Solution/{n}",f"exams/online-programming-test-2021/{n}")
cp(S2+"/Aug - Dec 2021 JOC Course/Exam Pattern.md","exams/exam-pattern-2021-second-repo.md")
cp(S2+"/Exam Pattern.md","exams/exam-pattern-second-repo.md")
cp("third repo/EXAM_PATTERN.md","exams/exam-pattern-2023-oct-third-repo.md")
cp("Question Papers/34 questions asked in JOC final center exam morning session.pdf","exams/34 questions asked in JOC final center exam morning session.pdf")
for i in (1,2,3): cp(f"The-Joy-of-Computing-Using-Python-PART-{i}.pdf",f"practice/IMP-questions-part-{i}.pdf")
cp("Nptel-Python-Mcqs.pdf","practice/Nptel-Python-Mcqs (generic, not from the course).pdf")
for f in sorted(glob.glob(os.path.join(R,"5th repo","*.md"))):
    cp("5th repo/"+os.path.basename(f),"_reference/5th-repo-answer-site (spam, unverified)/"+os.path.basename(f))
cp("Question Papers/relevant urls.md","sources/relevant urls.md")
cp(S+"/../_sources.tsv","sources/scribd_sources.tsv") if False else None
cp("_incoming/_sources.tsv","sources/scribd_sources.tsv")
cp("_incoming/youtube/_candidates_dated.tsv","sources/youtube_candidates_dated.tsv")
cp("LICENSE","licenses/LICENSE-upstream-gxuxhxm-MIT")
cp(S2+"/LICENSE","licenses/LICENSE-kishanrajput23-MIT")
cp("structure.md","structure.md")
with open(os.path.join(O,"_manifest.tsv"),"w",encoding="utf-8") as fh:
    fh.write("source\tcopied_to\n"+"\n".join(f"{a}\t{b}" for a,b in log))
print(len(log),"files copied")
