#!/bin/bash

# jupyter themes
pipenv run jt               \
  -t monokai                \
  -fs 10                    \
  -tf sourcesans            \
  -tfs 11                   \
  -nf source                \
  -nfs 12                   || exit 2

# notebook
pipenv run jupyter-notebook || exit 2

# reset theme
pipenv run jt -r
