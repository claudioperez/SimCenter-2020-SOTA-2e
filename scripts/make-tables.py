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
% Claudio M. Perez\n
""")

for i, lst in enumerate(index):
    lst = lst if lst else []
    body = set()
    head = f"""
\\subsection{{{i}}}
\\begin{{table}}[]
    \\centering
    \\begin{{tabular}}{{l|cc}}
    \\toprule
    Name &  License & Operating system\\\\"""
    for j in lst:
        try: item = [k for k in items if k["citekey"]==j][0]
        except: continue
        title = item["shortTitle"] if "shortTitle" in item else item["title"]
        lic = [tag["tag"] for tag in item["tags"] if "License" in tag["tag"]]
        lic = lic[0].rsplit("::",1)[-1].replace("License","") if lic else "-"
        OS = [tag["tag"] for tag in item["tags"] if "Operating" in tag["tag"]]
        OS = "/".join(op.rsplit("::",1)[-1] for op in OS) if OS else "-"
        if item["itemType"] == "computerProgram":
            name = f"\href{{{item['url']}}}{{{title}}}" \
                   if "url" in item else title
            body = body.union({f"""
    {name} & {lic} &{OS}\\\\"""})
    tail = f"""
    \\bottomrule
    \\end{{tabular}}
\\end{{table}}"""

    if body: print(head,"".join(body),tail)