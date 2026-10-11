import os,re,glob
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rows=[]
for f in sorted(glob.glob(R+"/quizzes/*/**/*.md",recursive=True)):
    rel=os.path.relpath(f,R).replace("\\","/"); parts=rel.split("/")
    term=parts[1]; head=open(f,encoding="utf-8").read(1500)
    m=re.search(r"week-(\d+)",parts[-1]); wk=int(m[1]) if m else ""
    if "chatgpt-converted-md" in rel: kind,trust="chatgpt_converted_md","author_marked_unverified"
    elif "portal print" in head.split("\n")[0]: kind,trust="portal_print_parsed","official_accepted_answers"
    elif "youtube.com" in head: kind,trust="youtube_transcription","author_ticks_unverified" + ("+official_section_at_end" if "Official accepted answers" in open(f,encoding="utf-8").read() else "")
    elif term=="2026-jul": kind,trust="case_study_pdf_md","answers_as_printed_in_pdf"
    elif term in("2021-jan","2021-jul","2022-jan"): kind,trust="second_repo_md","author_marked_unverified"
    else: kind,trust="other","unknown"
    nq=len(re.findall(r"^(?:\*\*\d+[\).]|### |\d+\.\s)",open(f,encoding="utf-8").read(),re.M))
    rows.append((term,wk,rel,kind,trust,nq))
with open(R+"/sources/inventory.tsv","w",encoding="utf-8") as fh:
    fh.write("term\tweek\tpath\tkind\ttrust\tapprox_question_headings\n"+"\n".join("\t".join(map(str,r)) for r in rows))
print(len(rows),"md files")
