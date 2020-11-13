
export TEXINPUTS:=../texmf//:${TEXINPUTS}
export BSTINPUTS:=../texmf//:${BSTINPUTS}

#TEXINPUTS=./texmf//;
# LUAINPUTS=${TEXINPUTS}:${LUAINPUTS}

all:
	- cd src && pdflatex -output-directory=build -interaction=nonstopmode ./editor.tex
	- cd src && bibtex ./build/editor.aux
	- cd src && pdflatex -output-directory=build -interaction=nonstopmode ./editor.tex

