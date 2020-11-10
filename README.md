# SimCenter 2020 SOTA 2e


## Parsing Citations

1. Run `parse-bib.sh` on text files that include a raw bibliography at the end to create a `.bib` file.
2. Import generated `.bib` to Zotero and clean;
    - Merge duplicates
    - Fix reversed author names
    - Validate DOIs
    - run `cite.py --dry` to identify malformed citekeys
3. Export Zotero library to `fullBib.bib`
4. Replace `custom_rules.yaml` to disambiguate a/b references.
5. Run `cite.py` to identify all references to items in `fullBib.bib`. This will produce the following effects and outcomes:
    - Replace identified references with cite keys from `fullBib.bib`
    - Generate a log
6. Run `grep-log.sh` to analyze log file
    - No. of substitution commands executed
    - No. of citations with no matches
7. Run `citecmd.py` to wrap references in appropriate commands.

8. Run `grep-bib.sh` to identify remaining raw references.
9. Compile full `.tex` project and check for any outliers by hand
10. Loop over pre-existing `.bib` files replace changed citekeys
11. Check special cases:
    1. Error dececting command "*"
    2. FEMA/HAZUS/ATC references
    3. ISO (i.s.o)
    4. NIC
    5. AWP-ODC
    6. NGA-West2
    7. FEMA Mitigation Division
    8. Hazard/Storm_Wind/main Fang et al., 2018b
    9. CrossCutting/AI: "Market Research Future, 2019" / "future2019global"
    10. e.g.
    11. NOAA Reanalysis Data 2018
    12. [for example
    13. MISSING: "Nickel et al., 2016", AI
    14. all of `CFD_Water.tex`
