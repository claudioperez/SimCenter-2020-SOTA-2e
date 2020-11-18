
export TEXINPUTS:=./texmf//:${TEXINPUTS}
export BSTINPUTS:=./texmf//:${BSTINPUTS}

#TEXINPUTS=./texmf//;
# LUAINPUTS=${TEXINPUTS}:${LUAINPUTS}

all:
	-  pdflatex -output-directory=build -interaction=nonstopmode ./editor.tex
	-  bibtex ./build/editor.aux
	-  pdflatex -output-directory=build -interaction=nonstopmode ./editor.tex

