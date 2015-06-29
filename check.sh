#!/usr/bin/env bash

clear
echo "Checking coding style using pep8..."
pep8 setup.py
pep8 test.py
pep8 loglikelihood/__init__.py
read -p "Press [Enter] key to continue to pylint."
pylint setup.py
read -p "   next..."
pylint loglikelihood/__init__.py
read -p "Press [Enter] key to continue to unit tests."
python tests/loglikelihood_test.py
