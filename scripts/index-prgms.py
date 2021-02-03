import yaml, json, os


with open("2020-2e.json") as f:
    refs = json.load(f)

i = 1
n = len(refs["items"])
for j,ref in enumerate(refs["items"]):

    pattern = ref["uri"][39:].strip()
    # print(f"{j}/{n}",pattern)
    replacement = ref["citekey"]
    # os.system(f"""
    # sed -i "s/{pattern}/{replacement}/g" 'zotero-refs-BLT.bib'
    # """)
    print(f"""
    s/{pattern}/{replacement}/g
    s/{pattern}/{replacement}/g""")
    # os.system(f"""
    # nvim -c "%s/{pattern}/{replacement}/g" -c 'wq' 'zotero-refs-BLT.bib'
    # """)

