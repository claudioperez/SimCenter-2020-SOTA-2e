r"""
This script works in conjunction with a shell script to generate
a series of LaTeX tables summarizing digital resources which are
referenced throughout a LaTeX document. The accompanying shell
script is reproduced below:

```shell
csplit --prefix=build/.refsegs/xx build/editor.aux \
    '/\\newlabel{refsegment\.*/-1' '{*}'
> build/.refsegs/index.yaml # clear index file
for i in build/.refsegs/xx*; do \
    printf -- "- \n" >> build/.refsegs/index.yaml; \
    sed -n 's/\\abx@aux@cite{\(.*\)}/  - "\1"/p' $$i >> build/.refsegs/index.yaml; \
done;
python3 scripts/make-tables.py > editor/tables.tex
```
"""
import re
import yaml

CMD = lambda cmd: rf"\{cmd}"
NL = "\n"

INDEX = "build/.refsegs/index.yaml" # This file is generated through
                                    # a sed script that is invoked by 
                                    # running `make tables`

ABBREV = {
    "License :: OSI Approved :: GNU General Public License (GPL)": "GPL",
    "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)": "GPLv2+"
}


with open(INDEX,"r") as f:
    index = yaml.load(f,Loader=yaml.Loader)

with open("2020-2e.json") as f:     # This file is exported from Zotero
    items = yaml.load(f,Loader=yaml.Loader)["items"]

with open("sections.yaml") as f:
    section_names = yaml.load(f, Loader=yaml.Loader)

def proc_lic(text:str)->str:
    if (match:=re.search(r"\((.*)\)$", text)):
        return match.group(1)
    return text

def add_notes(notes, tags)->dict:
    num = max(notes.values()) if notes else 0
    keys = []
    for comment in [tag["tag"] for tag in tags if "Comment ::" in tag["tag"]]:
        text = comment.rsplit("::",1)[-1]
        if text not in notes:
            num += 1
            notes.update({text: num})
            keys.append(num)
        else:
            keys.append(notes[text])
    return keys


def tablenotes(notes):
    if notes:
        return f"""
    \\begin{{tablenotes}}
      \\footnotesize
      { (NL+"      ").join(f'{CMD("item")}[{num}]{{{text}}}' for text, num in notes.items())  }
    \\end{{tablenotes}}
"""
    else:
        return ""




print("""
% This file was generated using the Python script `scripts/make-tables.py`,
% which can be invoked by running `make tables` at the command line.\n
% Claudio M. Perez

\\begin{center}
""")

for i, lst in enumerate(index[1:23]):
    lst = lst if lst else []
    body = set() # use set container to automatically handle duplicates
    foot = set()

    notes = {} # text for footnotes

    head = f"""
\\begin{{table}}[]
    \\caption{{{section_names[i+1]}}}
    \\begin{{threeparttable}}
    \\centering
    %\\begin{{tabular}}{{l|cccc}}
    \\begin{{tabular}}{{p{{4cm}}|cccc}}
    %\\begin{{tabular}}{{l|ccccc}}
    \\toprule
    Name &  License & Platforms & Prog. Lang. & DesignSafe \\\\"""
    for j in lst:
        try: item = [k for k in items if k["citekey"]==j][0]
        except: continue
        # Title
        name = item["shortTitle"] if "shortTitle" in item else item["title"]
        name = f"\href{{{item['url']}}}{{{name}}}" if "url" in item else name
        # License
        lic = [tag["tag"] for tag in item["tags"] if "License" in tag["tag"]]
        lic = lic[0].rsplit("::",1)[-1].replace("License","") if lic else "-"
        lic = proc_lic(lic)
        # Operating System
        OS = [tag["tag"] for tag in item["tags"] if "Operating" in tag["tag"]]
        OS = "/".join(o.rsplit("::",1)[-1][:4] for o in sorted(OS)) if OS else "-"
        # DesignSafe
        DS = [tg["tag"] for tg in item["tags"] if "DesignSafe" in tg["tag"]]
        DS = DS[0].split("::")[-1].replace("True","\\checkmark") if DS else "-"
        # Prog. Lang
        PL = [tag["tag"] for tag in item["tags"] if "Programming" in tag["tag"]]
        PL = "/".join(o.rsplit("::",1)[-1] for o in sorted(PL)) if PL else "-"
        # Comments
        keys = add_notes(notes, item["tags"])
        #NT = ",".join(f"\\tnotex{{{k}}}" for k in keys)
        NT = r"\textsuperscript{" + ",".join(f"{k}" for k in keys) + "}"
        if item["itemType"] == "computerProgram":
            body = body.union({f"""
    {name} {NT} & {lic} & {OS} & {PL} & {DS}  \\\\"""})
    tail = f"""
    \\bottomrule
   %\\insertTableNotes
    \\end{{tabular}}
    {tablenotes(notes)}
    \\end{{threeparttable}}
    \\label{{tab:app-{i}}}
\\end{{table}}
%\\newline
\\vspace*{{2cm}}
%\\newline"""

    if body: # only print if there are items in the table body
        print(head,"".join(body),tail)

print("\\end{center}")

