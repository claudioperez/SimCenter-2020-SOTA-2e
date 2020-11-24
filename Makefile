
export TEXINPUTS:=./texmf//:${TEXINPUTS}
export BSTINPUTS:=./texmf//:${BSTINPUTS}

all:
	-  lualatex --output-directory=build --interaction=nonstopmode ./editor.tex > /dev/null
	-  bibtex ./build/editor.aux | grep -i "warning"
	-  lualatex --output-directory=build --interaction=nonstopmode ./editor.tex | grep -i "Warning"

