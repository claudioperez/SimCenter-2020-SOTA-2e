import os, logging
from typing import List, Tuple

import yaml, coloredlogs

logger = logging.getLogger(__name__)
coloredlogs.install()


def generate_patterns(ref: dict)->str:
    if "author" in ref:
        if len(ref["author"]) == 1:
            if "family" in ref["author"][0]:
                pass
                return f"{ref['author'][0]['family']}, {ref['issued'][0]['year']}"
                # return f"{ref['author'][0]['family']} {ref['issued'][0]['year']}"
                # return f"{ref['author'][0]['family']} ({ref['issued'][0]['year']})"
                # return f"{ref['author'][0]['family']} ({ref['issued'][0]['year']})"
            else:
                pass
                return f"{ref['author'][0]['literal']}, {ref['issued'][0]['year']}"
                # return f"{ref['author'][0]['literal']} {ref['issued'][0]['year']}"
                # return f"{ref['author'][0]['literal']} ({ref['issued'][0]['year']})"
                # return f"{ref['author'][0]['literal']} ({ref['issued'][0]['year']})"
        elif len(ref["author"])==2:
            if "issued" in ref:
                return f"{ref['author'][0]['family']} and {ref['author'][1]['family']}, {ref['issued'][0]['year']}"
                # return f"{ref['author'][0]['family']} and {ref['author'][1]['family']} {ref['issued'][0]['year']}"
                # return f"{ref['author'][0]['family']} and {ref['author'][1]['family']}, ({ref['issued'][0]['year']})"
                # return f"{ref['author'][0]['family']} and {ref['author'][1]['family']} ({ref['issued'][0]['year']})"
                # return fr"{ref['author'][0]['family']} et al\. ({ref['issued'][0]['year']})"
            else:
                pass
        elif len(ref["author"]) > 2:
            if "family" in ref["author"][0]:
                pass                                                                                                            #    et al         with "and"
                return f"{ref['author'][0]['family']} et al\\., {ref['issued'][0]['year']}"                                   # period, comma
                # return f"{ref['author'][0]['family']} et al\\. ({ref['issued'][0]['year']})"                                   # period, comma
                # return f"{ref['author'][0]['family']} et al\\. {ref['issued'][0]['year']}"                                    # period
                # return f"{ref['author'][0]['family']} and {ref['author'][1]['family']} et al\\., {ref['issued'][0]['year']}"  # period, comma       and
                # return f"{ref['author'][0]['family']} et al\\., ({ref['issued'][0]['year']})"
                # return f"{ref['author'][0]['family']} et al\\. ({ref['issued'][0]['year']})"
                #return f"{ref['author'][0]['family']} et al, ({ref['issued'][0]['year']})"
            else:
                pass

# def generate_patterns2(ref: dict)->str:
#     patterns = [] 
#     if "author" in ref:
#         if len(ref["author"]) == 1:
#             if "family" in ref["author"][0]:
#                 patterns.append(f"{ref['author'][0]['family']}, {ref['issued'][0]['year']}")
#                 patterns.append(f"{ref['author'][0]['family']} {ref['issued'][0]['year']}")
#                 # patterns.append(f"{ref['author'][0]['family']}, {ref['author'][0]['given']} ({ref['issued'][0]['year']})")
#             else:
#                 return f"{ref['author'][0]['literal']}, {ref['issued'][0]['year']}"
#         elif len(ref["author"])==2:
#             return f"{ref['author'][0]['family']} and {ref['author'][1]['family']}, {ref['issued'][0]['year']}"
#         elif len(ref["author"]) > 2:
#             if "family" in ref["author"][0]:
#                 return f"{ref['author'][0]['family']} et al\\., {ref['issued'][0]['year']}"
#             else:
#                 pass

def generate_script(pattern:str, replacement:str)->str: return f"""
#find . -type f -name '*.tex' \\
find Response/ -type f -name 'main.tex' \\
    -exec grep -q "{pattern}" {{}} \\; \\
    -exec nvim -c "%s/{pattern}/{replacement}/gc" -c 'wq' {{}} \\;
"""

def dry_script(pattern:str, replacement:str)->str: return f"""
find . -type f -name '*.tex' \\
    -exec grep -l "{pattern}" {{}} \\; \\
    -exec echo "%s/{pattern}/{replacement}/gc" \\;
"""


def main():

    with open("refs.yaml", "r") as f:
        refs = yaml.load(f,Loader=yaml.Loader)["references"]

    rng = refs[:]
    n = len(rng)
    for i, ref in enumerate(rng):
        logger.info(f"Entering ref {ref['id']} ({i}/{n})")
        patterns = [generate_patterns(ref)]
        for pattern in patterns:
            if pattern:
                if "'" in pattern:
                    logger.warning("Apostrophe found in {}".format(ref["id"]))
                    logger.warning(pattern)
                # script: str = dry_script(pattern, ref["id"])
                script: str = generate_script(pattern, ref["id"])
                logger.info(f"Executing script: {script}")
                os.system(script)
            else:
                logger.warning(f"No pattern generated for {ref['id']}")

if __name__=="__main__": main()

