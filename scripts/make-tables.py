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
% which can be invoked by running `make tables` at the command line.

% Claudio M. Perez

""")

for i, lst in enumerate(index):
    head = f"""
\\subsection{{{i}}}

\\begin{{table}}[]
    \\centering
    \\begin{{tabular}}{{l|cc}}
    \\toprule
    Name &  License & Operating system\\\\"""
    body = set()
    # if lst:
    for j in lst:
        try:
            item = [k for k in items if k["citekey"]==j][0]
        except:
            # print(j)
            continue
        license = [tag["tag"] for tag in item["tags"] if "License" in tag["tag"]]
        license = license[0] if license else "-"
        if item["itemType"] == "computerProgram":
            name = f"\href{{{item['url']}}}{{{item['title']}}}" \
                   if "url" in item else item["title"]
            body = body.union({f"""
    {name} & {license.rsplit("::",1)[-1].replace("License","")} &\\\\"""})
    tail = f"""
    \\bottomrule
    \\end{{tabular}}
\\end{{table}}"""

    if body:
        print(head,"".join(body),tail)