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
import sys

import yaml
import pandas as pd

# These are useful in nested formatted strings where backslashes
# raise a syntax error
CMD = lambda cmd: rf"\{cmd}"
NL = "\n"

INDEX = "build/.refsegs/index.yaml" # This file is generated through
                                    # a sed script that is invoked by 
                                    # running `make tables`



with open(INDEX,"r") as f:
    index = yaml.load(f,Loader=yaml.Loader)

with open("2020-2e.json") as f:     # This file is exported from Zotero
    items = yaml.load(f,Loader=yaml.Loader)["items"]

with open("sections.yaml") as f:
    section_names = yaml.load(f, Loader=yaml.Loader)



def process_opsys(text:str)->str:
    # print(text,file=sys.stderr)
    return text.rsplit("::",1)[-1][:4]

def proc_lic(text:str)->str:
    #print(text,file=sys.stderr)
    text = text[0].rsplit("::",1)[-1].replace("License","") if text else "-"
    match = re.search(r"\((.*)\)$", text)
    if match:
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
      %\\footnotesize
      { (NL+"      ").join(f'{CMD("item")}[{num}]{{{text.replace("&",CMD("&"))}}}' for text, num in notes.items())  }
    \\end{{tablenotes}}
"""
    else:
        return ""




print("""
% This file was generated using the Python script `scripts/make-tables.py`,
% which can be invoked by running `make tables` at the command line.\n
% Claudio M. Perez

%\\begin{center}
""")

Licenses = set()
OpSystems = set()
for i, lst in enumerate(index[1:23]):
    #print(table)
    lst = lst if lst else []
    body = set() # use set container to automatically handle duplicates
    foot = set()
    notes = {} # text for footnotes

    head = f"""
\\begin{{table}}
    \\centering
    \\begin{{threeparttable}}
    \\caption{{{section_names[i+1]}}}
    \\begin{{tabular}}{{p{{35mm}}|cccc}}
    \\toprule
    Name &  License & Platforms & Prog. Lang. & DesignSafe \\\\"""
    for j in lst:
        try: item = [k for k in items if k["citekey"]==j][0]
        except: continue
        # Title
        name = item["shortTitle"] if "shortTitle" in item else item["title"]
        link = f"\href{{{item['url']}}}{{{name}}}" if "url" in item else name
        # License
        lic = [tag["tag"] for tag in item["tags"] if "License" in tag["tag"]]
        Licenses = Licenses.union(lic)
        lic = proc_lic(lic)
        # Operating System
        OS = [tag["tag"] for tag in item["tags"] if "Operating" in tag["tag"]]
        OpSystems = OpSystems.union(OS)
        OS = "/".join(process_opsys(o) for o in sorted(OS)) if OS else "-"
        # DesignSafe
        DS = [tg["tag"] for tg in item["tags"] if "DesignSafe" in tg["tag"]]
        DS = DS[0].split("::")[-1].replace("True","\\checkmark") if DS else "-"
        # Prog. Lang
        PL = [tag["tag"] for tag in item["tags"] if "Programming" in tag["tag"]]
        PL = "/".join(o.rsplit("::",1)[-1] for o in sorted(PL)) if PL else "-"
        # Notes/Comments
        keys = add_notes(notes, item["tags"])
        # 
        NT = r"\textsuperscript{" + ",".join(f"{k}" for k in keys) + "}"
        if item["itemType"] == "computerProgram":
            body = body.union({f"""
    %{name}
    {link} {NT} & {lic} & {OS} & {PL} & {DS}  \\\\"""})
    tail = f"""
    \\bottomrule
    \\end{{tabular}}
    {tablenotes(notes)}
    \\end{{threeparttable}}
    \\label{{tab:app-{i}}}
\\end{{table}}
\\vspace*{{2cm}}

"""
    rows = [rw for rw in sorted(body)]
    if body: # only print if there are items in the table body
        print(head,"".join(rows),tail)

#print("\\end{center}")

if __name__ == "__main__":
    # print(OpSystems,file=sys.stderr)
    if "-k" in sys.argv:
        keysfile = sys.argv[sys.argv.index("-k") + 1]
        license_keys = pd.DataFrame(
                [license.rsplit("::",1)[-1]  for license in Licenses],
                index = [proc_lic([license]) for license in Licenses],
                columns = ["Full license name"],
        )
        os_keys = pd.DataFrame(
                [opsys.rsplit("::",1)[-1] for opsys in OpSystems],
                index = [process_opsys(opsys) for opsys in OpSystems],
                columns = ["Operating System"],

        )
        # print(os_keys,file=sys.stderr)
        with open(keysfile,"w+") as f:
            f.write(license_keys.to_latex(
                caption="Abbreviations of license names used in appendices.",
                label="tab:keys-licenses"
            ))
            f.write("\n")
            f.write(os_keys.to_latex(
                caption="Abbreviations of operating system names used in appendices.",
                label="tab:keys-os"
            ))
            f.write("\\pagebreak")

