# SimCenter 2020 SOTA 2e

## Citing Software



## Parsing Citations


1. Run `parse-bib.sh` on text files that include a raw bibliography at the end to create a `.bib` file.
2. Import generated `.bib` to Zotero and clean;
    - Merge duplicates
    - Fix reversed author names
    - Validate DOIs
    - run `cite.py --dry` to identify malformed citekeys
3. Export Zotero library to `zotero-refs.bib`
4. Replace `custom_rules.yaml` to disambiguate a/b references.
5. Run `cite.py` to identify all references to items in `zotero-refs.bib`. This will produce the following effects and outcomes:
    - Replace identified references with cite keys from `zotero-refs.bib`
    - Generate a log
6. Run `grep-log.sh` to analyze log file
    - No. of substitution commands executed
    - No. of citations with no matches
7. Run `citecmd.py` to wrap references in appropriate commands.
8. Run `grep-bib.sh` to identify remaining raw references.
10. Loop over pre-existing `.bib` files replace changed citekeys
11. Check special cases
1.  Finalize wrapping citations
2.  Color citations and proof read

