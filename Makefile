
export TEXINPUTS:=./texmf//:${TEXINPUTS}
export BSTINPUTS:=./texmf//:${BSTINPUTS}

all:
	-  lualatex --output-directory=build --interaction=nonstopmode ./editor.tex > /dev/null
	-  bibtex ./build/editor.aux
	-  lualatex --output-directory=build --interaction=nonstopmode ./editor.tex

