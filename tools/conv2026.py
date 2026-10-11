import os,re,glob,pymupdf
D=r"C:\Users\rajes\OneDrive\Documents\GitHub\NPTEL-The-Joy-of-Computing-using-Python\JRG JOC\quizzes\2026-jul"
os.makedirs(D+"/img",exist_ok=True)
BUL={"\uf0b7":"-","\uf0a7":"-","•":"-","\u2022":"-"}
def clean(t):
    for k,v in BUL.items(): t=t.replace(k,v)
    return t.replace("\xa0"," ").rstrip()
for pdf in sorted(glob.glob(D+"/week-*.pdf")):
    n=int(re.search(r"week-(\d+)",pdf)[1]); d=pymupdf.open(pdf); out=[]; state=None; buf=[]
    out.append(f"# JOC Jul-2026 · Week {n}\n")
    out.append(f"- Source: `{os.path.basename(pdf)}` (case-study assignment PDF supplied by the repo owner; the only source used for the Jul-2026 session). Answers and justifications are as printed in the PDF.\n")
    def flush():
        global buf,state
        if not buf: return
        txt=" ".join(b.strip() for b in buf)
        if state=="q": out.append("\n### "+txt+"\n")
        elif state=="opt": out.append("- "+txt)
        elif state=="ans": out.append("\n**"+txt+"**\n")
        elif state=="just": out.append("> "+txt+"\n")
        elif state=="scen": out.append("\n## "+txt+"\n")
        elif state=="bul": out.append("- "+txt.lstrip("- ").strip())
        else: out.append("\n"+txt+"\n")
        buf=[]
    for pi,pg in enumerate(d,1):
        if n>=11:  # slide-like scans with OCR text layer: keep the page image
            blk=[b for b in pg.get_text("dict")["blocks"] if b["type"]==1]
            if blk:
                fn=f"2026-jul-w{n:02d}-p{pi:02d}.{blk[0]['ext']}"; open(f"{D}/img/{fn}","wb").write(blk[0]["image"])
                flush(); out.append(f"\n---\n**Page {pi}** (scanned page; the text below is its OCR layer, check against the image)\n\n![page {pi}](img/{fn})\n"); state=None
        k=0
        for b in sorted(pg.get_text("dict")["blocks"],key=lambda b:(b["bbox"][1],b["bbox"][0])):
            if b["type"]==1 and n<11:
                k+=1; fn=f"2026-jul-w{n:02d}-p{pi:02d}-{k}.{b['ext']}"; open(f"{D}/img/{fn}","wb").write(b["image"])
                flush(); state=None; out.append(f"\n![program / figure, page {pi}](img/{fn})\n"); continue
            if b["type"]!=0: continue
            for l in b["lines"]:
                t=clean("".join(s["text"] for s in l["spans"]))
                if not t.strip(): flush(); state=None; continue
                s=t.strip()
                if re.match(r"(Question|MCQ|MSQ|MAQ)\s*\d+\s*(\(.*\))?\s*$",s): flush(); out.append("\n### "+s+"\n"); state="qbody"; buf=[]
                elif re.match(r"Q\d+\.",s): flush(); state="q"; buf=[s]
                elif re.match(r"[A-H]\.\s",s) and state in("q","opt","qbody"): flush(); state="opt"; buf=[s]
                elif re.match(r"(Correct )?Answers?\s*:",s): flush(); state="ans"; buf=[s]
                elif s.startswith("Justification:"): flush(); state="just"; buf=[s]
                elif s.startswith("Scenario") or s.startswith("Case Study"): flush(); state="scen"; buf=[s]
                elif s.startswith("- ") and state not in("q","opt","ans","qbody"): flush(); state="bul"; buf=[s]
                elif re.match(r"Week \d+\s*(–.*)?$",s) and not buf: continue
                else:
                    if state is None: state="p"
                    buf.append(s)
    flush()
    open(f"{D}/week-{n:02d}.md","w",encoding="utf-8").write("\n".join(out))
    print(n,len(re.findall(r"^### Q",'\n'.join(out),re.M)),"questions")
    print(len(re.findall(r"^\*\*Answer",'\n'.join(out),re.M)),"answers")
