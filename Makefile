
export TEXINPUTS:=./texmf//:${TEXINPUTS}
export BSTINPUTS:=./texmf//:${BSTINPUTS}

.PHONY: tex all bib

all:
	make tex #> /dev/null
	make bib
	make tex
	make tex
	# -  bibtex ./build/editor.aux

tex:
	-  lualatex --output-directory=build --interaction=nonstopmode ./editor.tex

bib:
	-  biber ./build/editor

