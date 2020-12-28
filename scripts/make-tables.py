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
import yaml


INDEX = "build/.refsegs/index.yaml" # This file is generated through
                                    # a sed script that is invoked by 
                                    # running `make tables`

with open(INDEX,"r") as f:
    index = yaml.load(f,Loader=yaml.Loader)

with open("2020-2e.json") as f:     # This file is exported from Zotero
    items = yaml.load(f,Loader=yaml.Loader)["items"]

print("""
% This file was generated using the Python script `scripts/make-tables.py`,
% which can be invoked by running `make tables` at the command line.\n
% Claudio M. Perez
""")

for i, lst in enumerate(index):
    lst = lst if lst else []
    body = set() # use set container to automatically handle duplicates
    foot = set()
    head = f"""
\\subsection{{{i}}}
\\begin{{table}}[]
    \\centering
    \\begin{{tabular}}{{l|ccc}}
    \\toprule
    Name &  License & Operating system & DesignSafe \\\\"""
    for j in lst:
        try: item = [k for k in items if k["citekey"]==j][0]
        except: continue
        # Title
        name = item["shortTitle"] if "shortTitle" in item else item["title"]
        name = f"\href{{{item['url']}}}{{{name}}}" if "url" in item else name
        # License
        lic = [tag["tag"] for tag in item["tags"] if "License" in tag["tag"]]
        lic = lic[0].rsplit("::",1)[-1].replace("License","") if lic else "-"
        # Operating System
        OS = [tag["tag"] for tag in item["tags"] if "Operating" in tag["tag"]]
        OS = "/".join(o.rsplit("::",1)[-1] for o in sorted(OS)) if OS else "-"
        # DesignSafe
        DS = [tg["tag"] for tg in item["tags"] if "DesignSafe" in tg["tag"]]
        DS = DS[0].split("::")[-1].replace("True","Y") if DS else "-"
        # Comments
        cm = [tg["tag"] for tg in item["tags"] if "Comment ::" in tg["tag"]]
        cm = set(c.rsplit("::",1)[-1] for c in sorted(cm))
        if item["itemType"] == "computerProgram":
            body = body.union({f"""
    {name} & {lic} & {OS} & {DS} \\\\"""})
    tail = f"""
    \\bottomrule
    \\end{{tabular}}
\\end{{table}}"""

    if body: # only print if there are items in the table body
        print(head,"".join(body),tail)

