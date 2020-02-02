#!/bin/bash
command -v pipenv &>/dev/null || pip install --user pipenv && pipenv update
