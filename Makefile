
export TEXINPUTS:=./texmf//:${TEXINPUTS}
export BSTINPUTS:=./texmf//:${BSTINPUTS}

.PHONY: tex all bib

all:
	make tex
	# -  pdflatex -output-directory=build -draftmode -interaction=nonstopmode ./editor.tex
	make bib
	make tex
	# -  bibtex ./build/editor.aux

tex:
	# -  lualatex --output-directory=build --interaction=nonstopmode ./editor.tex
	-  pdflatex -output-directory=build -interaction=nonstopmode ./editor.tex

bib:
	-  biber ./build/editor

