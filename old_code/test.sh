#!/bin/bash

clear

echo "=== Linting 'src' directory ==="
flake8 src
LINT_SRC=$?
printf "\n"

echo "=== Linting 'test' directory ==="
flake8 test
LINT_TEST=$?
printf "\n"

if [[ $LINT_SRC == 0 && $LINT_TEST == 0 ]]; then
  python3 -m unittest discover test
fi
