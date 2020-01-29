# jupyter themes
pipenv run jt -t monokai -fs 10 -tf sourcesans -tfs 11 -nf source -nfs 12

# notebook
pipenv run jupyter-notebook

# reset theme
command -v jt &>/dev/null && jt -r

exit 0
