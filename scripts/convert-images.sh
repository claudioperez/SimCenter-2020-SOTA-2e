shopt -s globstar;
for img in **/*.png; do convert "$img" "${img%.*}.pdf" -density 300 -units PixelsPerInch; done
