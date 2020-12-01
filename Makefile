
export TEXINPUTS:=./texmf//:${TEXINPUTS}
export BSTINPUTS:=./texmf//:${BSTINPUTS}

.PHONY: tex all bib

all:
	make idx
	make tex-draft
	make bib
	make tex
	make tex

inc:
	make idx
	make tex-draft
	make tex

draft:
	make tex-draft
	# -  pdflatex -output-directory=build -draftmode -interaction=nonstopmode ./editor.tex
	make bib
	make tex-draft

tex:
	# -  lualatex --output-directory=build --interaction=nonstopmode ./editor.tex
	-  pdflatex -output-directory=build -interaction=nonstopmode ./editor.tex

tex-draft:
	# -  lualatex --output-directory=build --interaction=nonstopmode ./editor.tex
	-  pdflatex -draftmode -output-directory=build -interaction=nonstopmode ./editor.tex

bib:
	-  biber ./build/editor
idx:
	python scripts/index-prgms.py > index.sed
	sed -i -f index.sed zotero-refs-BLT.bib

%.pdf: %.png
	echo '$<' '%@'
	convert '$<' '%@' -density 300 -units PixelsPerInch
