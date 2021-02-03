grep -orhP --include="main.tex" '(paragraph|[a-z]*section)\{.*?\}' . | sed 's/paragraph/    /g'
