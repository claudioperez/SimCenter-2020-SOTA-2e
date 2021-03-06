# Claudio M. Perez
# Fall 2020

SHELL = /bin/bash -O globstar
#.SHELLFLAGS="-O extglob -c"

export TEXINPUTS:=./style//:${TEXINPUTS}
#export BSTINPUTS:=./texmf//:${BSTINPUTS}

.PHONY: tex all bib tables images idx

all:
	make idx
	make tex-draft
	make bib
	make tex
	make tables
	make tex

tables:
	csplit --prefix=build/.refsegs/xx build/editor.aux '/\\newlabel{refsegment\.*/-1' '{*}'
	> build/.refsegs/index.yaml
	for i in build/.refsegs/xx*; do \
	   printf -- "- \n" >> build/.refsegs/index.yaml; \
	   sed -n 's/\\abx@aux@cite{\(.*\)}/  - "\1"/p' $$i >> build/.refsegs/index.yaml; \
	done;
	python3 scripts/make-tables.py -k 'editor/keys.tex' > editor/tables.tex

fast: # make an incomplete build
	make idx
	make tex-draft
	make tex

tex:
	#- lualatex --output-directory=build --interaction=nonstopmode ./editor.tex
	- pdflatex -output-directory=build -interaction=nonstopmode ./editor.tex

tex-draft:
	# -  lualatex --output-directory=build --interaction=nonstopmode ./editor.tex
	-  pdflatex -draftmode -output-directory=build -interaction=nonstopmode ./editor.tex

bib:
	-  biber ./build/editor

idx: # process .bib file to add related reference keys
	python scripts/index-prgms.py > index.sed
	sed -i -f index.sed zotero-refs-BLT.bib

images:
	for i in `echo **/Figures/*.png | sed -r 's/ /\n/g' | sed -r 's/(.*)\.png/\1.pdf/g' | tr '\n' ' '`; do \
		make $$i; \
	done

%.pdf: %.png
	echo '$<' '$@'
	convert '$<' -density 300 -units PixelsPerInch '$@'


