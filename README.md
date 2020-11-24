# SimCenter 2020 SOTA 2e


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

## Special Cases

> an `x` denotes a resolved case

  - [x] Error detecting command "*"
  - [ ] FEMA/HAZUS/ATC references
  - [ ] Science and Technology Council, 2016a/b
  - [ ] ISO (i.s.o)
  - [ ] NIC
  - [ ] AWP-ODC
  - [ ] NGA-West2
  - [ ] FEMA Mitigation Division
  - [x] Hazard/Storm_Wind/main: Fang et al., 2018b
  - [x] "e.g."
  - [ ] NOAA Reanalysis Data 2018
  - [ ] `[for example`
  - [ ] CrossCutting/AI:  `Market Research Future, 2019` , `future2019global`
  - [x] Duenas-Osorio et al., 2007
  - [ ] Change et al., 2000
  - [ ] Miller and Baker, 2016
  - [ ] ESDU (1983)
  - [x] Johansen et al. (2016)
  - [x] Fan et al
  - [x] Kepert, 2010a
  - [x] Kepert, 2010b
  - [x] Au and Beck 2003b
  - [x] Au and Beck 2003a
  - [x] Deb et al. 2019a
  - [x] Deb et al. 2019b
  - [ ] Zhang and Taflanidis 2018b
  - [ ] Zhang and Taflanidis 2018a
  - [ ] Ramancha et al. 2021b
  - [ ] Ramancha et al. 2021a., 2019
  - [x] Gao and Mosalam 2018a
  - [x] Gao and Mosalam 2018b
  - [ ] Zsarnóczay, 2018 [pelicun]
  - [ ] Youd and Perkins (1987)
  - [ ] Mandli and Dawson (2014)
  - [ ] Hoarau, 2016
  - [ ] National Science and Technology Council, 2016a, 2016b, 2019

## Missing

- [ ] CrossCutting/AI:
  - [ ] `Nickel et al., 2016`
- [x] Hazards/Tsunami
- Hazards/Storm_Surge: 
  - `Berger et al., 2011`
  - `Mandli et al., 2014`
- [ ] Response/CFD_wind
  - All
- [ ] Response/CFD_water
  - All
- [ ] Response/Structural
  - All


## Questions

### CrossCutting

#### AI

- Hyperlink formatting?
- hyperlinks

### Appendix

