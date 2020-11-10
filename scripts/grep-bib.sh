# grep -P "\([^\d|^\)]*, \d{4}[a-d,\)]" main.tex

# \(([A-Z,a-z]*) et al., (\d{4})\)

([A-Z]\.[A-Z]\.), ([A-Z][A-Z,a-z]*) -> $2, $1
