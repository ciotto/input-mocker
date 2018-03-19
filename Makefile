SHELL := /bin/bash

init:
	pip install -r requirements_dev.txt

test:
	coverage run -m tests
	coverage report

travis:
	coverage run -m tests
