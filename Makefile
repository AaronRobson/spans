.DEFAULT_GOAL := all

.PHONY: all
all: check test

.PHONY: install-packages
install-packages:
	python3 -m pip install --upgrade --upgrade-strategy eager \
	  -r dev-requirements.txt \
	  -r requirements.txt \
	  -r tests/requirements.txt

.PHONY: check
check: lint type-check

.PHONY: lint
lint:
	python3 -m flake8 .

.PHONY: type-check
type-check:
	python3 -m mypy .

.PHONY: test
test: unittest mutation-test

.PHONY: unittest
unittest:
	python3 -m unittest $(testcase)

.PHONY: mutation-test
mutation-test:
	mut.py --target spans --unit-test tests -m

.PHONY: run
run:
	python3 spans.py $(args)
