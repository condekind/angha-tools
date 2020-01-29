#!/bin/bash

# WARNING: Doesn't work with Zsh

# setup python 3.8 env
command -v pipenv &>/dev/null         || exit 1
pipenv --venv || pipenv --python 3.8  || exit 1

# math, statistics, data science
pipenv install "Cython"               || exit 1
pipenv install "numpy"                || exit 1
pipenv install "scipy"                || exit 1
pipenv install "pandas"               || exit 1
pipenv install "scikit-learn"         || exit 1

# notebook, plots
pipenv install "unidecode"            || exit 1
pipenv install "matplotlib"           || exit 1
pipenv install "colorspacious"        || exit 1
pipenv install "jupyter"              || exit 1
pipenv install "notebook"             || exit 1
pipenv install "ipywidgets"           || exit 1
pipenv install "plotly"               || exit 1

echo "success"
exit 0
