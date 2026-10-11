import os,re,glob,urllib.request,urllib.parse
from concurrent.futures import ThreadPoolExecutor
R=r"C:\Users\rajes\OneDrive\Documents\GitHub\NPTEL-The-Joy-of-Computing-using-Python\JRG JOC"
pat=re.compile(r"https://storage\.googleapis\.com/[^)\s\"'>]+")
files=[f for f in glob.glob(R+"/quizzes/**/*.md",recursive=True)]
todo={}  # url -> local abs path
per_file={}
for f in files:
    t=open(f,encoding="utf-8").read(); urls=set(pat.findall(t))
    if not urls: continue
    term_dir=os.path.relpath(f,R).replace("\\","/").split("/")[1]
    per_file[f]=urls
    for u in urls:
        p=urllib.parse.urlparse(u).path.split("/assets/img/",1)[-1]  # e.g. noc21_cs32/A0q6a.png
        todo[u]=os.path.join(R,"quizzes",term_dir,"img",urllib.parse.unquote(p))
def get(u):
    dst=todo[u]; os.makedirs(os.path.dirname(dst),exist_ok=True)
    if os.path.exists(dst) and os.path.getsize(dst)>0: return u,"cached"
    for _ in range(3):
        try:
            data=urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=30).read()
            open(dst,"wb").write(data); return u,"ok"
        except Exception as e: err=str(e)
    return u,"FAIL "+err
with ThreadPoolExecutor(8) as ex: res=list(ex.map(get,todo))
ok=sum(1 for _,s in res if not s.startswith("FAIL")); fails=[(u,s) for u,s in res if s.startswith("FAIL")]
print(len(todo),"urls",ok,"ok",len(fails),"failed")
for u,s in fails[:10]: print(u,s)
good={u for u,s in res if not s.startswith("FAIL")}
rows=[]
for f,urls in per_file.items():
    t=open(f,encoding="utf-8").read(); d=os.path.dirname(f)
    for u in urls:
        if u in good:
            rel=os.path.relpath(todo[u],d).replace("\\","/"); t=t.replace(u,rel); rows.append((u,os.path.relpath(todo[u],R).replace("\\","/")))
    open(f,"w",encoding="utf-8",newline="").write(t)
os.makedirs(R+"/sources",exist_ok=True)
open(R+"/sources/mirrored_images.tsv","w",encoding="utf-8").write("original_url\tlocal_path\n"+"\n".join(f"{a}\t{b}" for a,b in sorted(set(rows))))
print("rewrote",len(per_file),"files")
