import sys,os,re,collections,pymupdf
def lines_of(pg):
    out=[]
    for b in pg.get_text("dict")["blocks"]:
        if b["type"]!=0: continue
        for l in b["lines"]:
            t="".join(s["text"] for s in l["spans"])
            if t.strip()=="": continue
            out.append((l["bbox"][1],l["bbox"][0],t,l["bbox"][3]))
    return sorted(out)
def fix(L):
    pts=[y for y,x,t,_ in L if re.fullmatch(r"\d+ point",t.replace(" "," ").strip())]
    out=[]
    for y,x,t,y1 in L:
        m=re.match(r"(\d{1,2}\))\s+(\S.*)",t.strip())
        if m and x<215 and any(abs(y-p)<5 for p in pts): out+=[(y,x,m[1],y1),(y+0.01,x+16,m[2],y1)]
        else: out.append((y,x,t,y1))
    return out
MARK=re.compile(r"\d+\)")
N=lambda z:re.sub(r"\s","",z)
def page_marks(L,mxfb=None):
    cand=[(y,x,int(t.replace(" ","").strip()[:-1])) for y,x,t,_ in L if MARK.fullmatch(t.replace(" ","").strip()) and x<215]
    pts=[y for y,x,t,_ in L if re.fullmatch(r"\d+ point",t.replace(" "," ").strip())]
    P=[c for c in cand if any(abs(c[0]-p)<8 for p in pts)]
    import collections as _c
    mx=max(_c.Counter(round(c[1]) for c in P).items(),key=lambda kv:(kv[1],kv[0]))[0] if P else mxfb
    if mx is None: return cand
    return [c for c in cand if abs(c[1]-mx)<=6]
def convert(pdf,outdir,term,verbose=True,title="portal print"):
    d=pymupdf.open(pdf); os.makedirs(outdir+"/img",exist_ok=True)
    allL=[fix(lines_of(pg)) for pg in d]
    # per-page layout (marker x), fall back to previous page of same size
    mxs=[]; last={}
    for pg,L in zip(d,allL):
        mk=page_marks(L); key=(round(pg.rect.width),round(pg.rect.height))
        if mk: last[key]=min(x for _,x,_ in mk)
        mxs.append(last.get(key))
    # fill leading Nones from the first known value of that size
    first={}
    for pg,mx in zip(d,mxs):
        key=(round(pg.rect.width),round(pg.rect.height))
        if mx and key not in first: first[key]=mx
    mxs=[mx or first.get((round(pg.rect.width),round(pg.rect.height)),170) for pg,mx in zip(d,mxs)]
    weeks=collections.OrderedDict(); cw=None
    for i,(pg,L) in enumerate(zip(d,allL)):
        hdr=" ".join(t for y,x,t,_ in L if y<30)
        m=re.search(r"Unit \d+ - [Ww]eek (\d+)",hdr)
        if m: cw=int(m[1])
        else:
            for y,x,t,_ in L:
                a=re.fullmatch(r"Assignment (\d+)",t.strip())
                if a: cw=int(a[1]); break
        if cw is not None: weeks.setdefault(cw,[]).append(i)
    report={}
    for w,pages in weeks.items():
        items=[]; head=[]; cur=None
        for pi in pages:
            pg=d[pi]; W=pg.rect.width; H=pg.rect.height; mx=mxs[pi]
            raw=[(y,x,t,y1) for y,x,t,y1 in allL[pi] if y>=28 and y1<=H-22]
            L=[r for r in raw if r[1]>=mx-8]
            marks=[(y,n) for y,x,n in page_marks(L,mx)]
            if not marks:  # unnumbered layout: a question starts at each "N point(s)" line
                pl=[(y,x) for y,x,t,y1 in raw if re.fullmatch(r"\d+ points?",t.replace("\xa0"," ").strip())]
                qx=[x for y,x,t,y1 in raw if pl and any(abs(y-yy)<3 for yy,_ in pl) and x<pl[0][1]-60]
                if pl and qx:
                    mx=min(qx); marks=[(y,0) for y,_ in pl]; L=[r for r in raw if r[1]>=mx-8]
            bounds=[y for y,_ in marks]
            def region(lo,hi): return [(y,x,t) for y,x,t,_ in L if lo-1<=y<hi-1 and not re.fullmatch(r"\d+ points?\s*",t.replace("\xa0"," ").strip()) and not (x<mx+8 and MARK.fullmatch(t.replace("\xa0","").strip()))]
            segs=[(None,28,bounds[0] if bounds else H)]
            for k,(y,n) in enumerate(marks): segs.append((n,y,bounds[k+1] if k+1<len(bounds) else H-22))
            for n,lo,hi in segs:
                reg=region(lo,hi)
                if n is None:
                    if cur is None: head+=[t for _,_,t in reg]; continue
                    target=cur
                else:
                    nb=any(t.startswith("\xa0") and x>=mx+8 and not t.strip().startswith("Accepted") for y,x,t,_ in L)
                    cur={"n":n or len(items)+1,"lines":[],"crops":[],"mx":mx,"nb":nb}; items.append(cur); target=cur
                target["lines"]+=reg
                if hi-lo>12:
                    clip=pymupdf.Rect(mx-10,max(lo-4,0),W-20,min(hi,H-22))
                    nm=f"w{w:02d}-q{target['n']:02d}-p{pi+1}.png"
                    pg.get_pixmap(dpi=130,clip=clip).save(f"{outdir}/img/{nm}"); target["crops"].append(nm)
        md=[f"# JOC {term} · Week {w}: {title}\n",
            f"- Source: `{os.path.basename(pdf)}` pages {pages[0]+1}–{pages[-1]+1} (portal review printout). Parsed text below; the cropped image under each question is the exact page content (code, figures and ticks as printed) and is authoritative.",
            "- `[x]` = option equal to the portal's **Accepted Answer** (official). Lines may carry stray spaces from the PDF text layer.\n"]
        hd=[t.strip() for t in head if t.strip() and re.search(r"(Due on|Due date|Score:|Assignment submitted|@)",t)]
        if hd: md.append("> "+" · ".join(hd[:5])+"\n")
        for it in items:
            q=[];opts=[];res=[];acc=[];mode="q"; om=it["mx"]+17
            for y,x,t in it["lines"]:
                s=t.replace("\xa0"," ").strip()
                if re.match(r"(Yes|No), the answer",s.replace(" ","")[:30].replace("theanswer","the answer")) or re.match(r"(Yes|No), the answer",s) or re.match(r"Score:",s) or s.startswith("Partially Correct"): mode="res"; res.append(s); continue
                if s.startswith("Accepted Answers"): mode="acc"; continue
                if mode=="acc": acc.append(s); continue
                if mode=="res": continue
                if (t.startswith("\xa0") and x>=om-9) if it["nb"] else x>=om: mode="opt"; opts.append(s); continue
                if mode=="opt": opts[-1]+=" "+s; continue
                q.append(s)
            md.append(f"### Q{it['n']}. "+(q[0] if q else "(question text in image)"))
            for s in q[1:]: md.append(s)
            md.append("")
            accset={N(a) for a in acc}
            for o in opts: md.append(f"- [{'x' if N(o) in accset else ' '}] {o}")
            if not opts and acc: md.append("Accepted answer(s): "+"; ".join(acc))
            elif acc and not any(N(o) in accset for o in opts): md.append("> Accepted answer (not matched to a printed option): "+"; ".join(acc))
            if res: md.append("> "+" ".join(res))
            for c in it["crops"]: md.append(f"\n![page crop](img/{c})")
            md.append("")
        fn=f"{outdir}/week-{w:02d}.md"
        if os.path.exists(fn) and ": portal print" not in open(fn,encoding="utf-8").readline(): fn=f"{outdir}/week-{w:02d}-portal-print.md"
        open(fn,"w",encoding="utf-8").write("\n".join(md))
        report[w]=len(items)
    if verbose: print(report)
    return report
if __name__=="__main__": convert(sys.argv[1],sys.argv[2],sys.argv[3])
