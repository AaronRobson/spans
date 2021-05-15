.DEFAULT_GOAL := all

.PHONY: all
all: check test

.PHONY: install-packages
install-packages:
	pip3 install --upgrade \
	  -r dev-requirements.txt \
	  -r requirements.txt \
	  -r tests/requirements.txt

.PHONY: check
check: lint type-check

.PHONY: lint
lint:
	flake8 .

.PHONY: type-check
type-check:
	mypy .

.PHONY: test
test: unittest mutation-test

.PHONY: unittest
unittest:
	python3 -m unittest

.PHONY: mutation-test
mutation-test:
	mut.py --target spans --unit-test tests -m

.PHONY: run
run:
	python3 spans.py $(args)
