#!/usr/bin/env bash

find . -name '*.coverage' -delete
find . -name '*.pyc' -delete
find . -name "*.egg-info" -type d -exec rm -r "{}" \;  2> /dev/null
find . -name "*__pycache__" -type d -exec rm -r "{}" \;  2> /dev/null
find . -name "*.eggs" -type d -exec rm -r "{}" \;  2> /dev/null
find . -name "*.cache" -type d -exec rm -r "{}" \;  2> /dev/null

# python setup.py test

pip install -e .
coverage run -a --source=md_link_mod $(which py.test) --doctest-modules md_link_mod
coverage run -a --source=md_link_mod $(which py.test)
coverage report -m

find . -name '*.coverage' -delete
find . -name '*.pyc' -delete
find . -name "*.egg-info" -type d -exec rm -r "{}" \;  2> /dev/null
find . -name "*__pycache__" -type d -exec rm -r "{}" \;  2> /dev/null
find . -name "*.eggs" -type d -exec rm -r "{}" \;  2> /dev/null
find . -name "*.cache" -type d -exec rm -r "{}" \;  2> /dev/null
