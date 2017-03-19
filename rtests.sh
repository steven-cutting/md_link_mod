#! /usr/bin/env bash

coverage run -a --source=md_link_mod $(which py.test) --doctest-modules md_link_mod

coverage run -a --source=md_link_mod $(which py.test)

coverage report -m
