import sys,os,io,time,pymupdf
from rapidocr_onnxruntime import RapidOCR
eng=RapidOCR()
def page_text(pg,dpi):
    pix=pg.get_pixmap(dpi=dpi); img=pix.tobytes("png")
    res,_=eng(img)
    if not res: return ""
    # group boxes into lines by y centre
    items=[(sum(p[1] for p in b)/4,min(p[0] for p in b),t,(b[2][1]-b[0][1])) for b,t,s in res]
    items.sort(); lines=[];cur=[]
    for it in items:
        if cur and abs(it[0]-cur[-1][0])>max(10,0.6*it[3]): lines.append(cur);cur=[]
        cur.append(it)
    if cur: lines.append(cur)
    return "\n".join(" ".join(t for _,_,t,_ in sorted(l,key=lambda x:x[1])) for l in lines)
def run(pdf,out,dpi=170):
    d=pymupdf.open(pdf); t0=time.time(); parts=[]
    for i,pg in enumerate(d,1):
        parts.append(f"\n\n=== page {i} ===\n"+page_text(pg,dpi))
    open(out,"w",encoding="utf-8").write(f"OCR (RapidOCR, {dpi} dpi) of {os.path.basename(pdf)}; machine-read, check against the PDF.\n"+"".join(parts))
    print(os.path.basename(pdf),len(d),"pages",round(time.time()-t0),"s")
if __name__=="__main__": run(sys.argv[1],sys.argv[2],int(sys.argv[3]) if len(sys.argv)>3 else 170)
