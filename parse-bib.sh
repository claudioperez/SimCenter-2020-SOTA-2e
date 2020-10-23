#! /usr/bin/bash
#
# Claudio Perez
#
# Use: 
# $ ./parse-bib.sh file.tex > refereces.bib

grep -A500 'References' $1 | tail -n+3 | head -n-2 \
| anystyle -f bib --stdout parse /dev/stdin #> "${1%.*}.bib"
