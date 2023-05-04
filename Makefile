#* Variables
SHELL := /usr/bin/env bash
PYTHON := python

.PHONY: codestyle
codestyle:
	poetry run ruff --fix .
	poetry run black .

.PHONY: formatting
formatting: codestyle

.PHONY: test
test:
	poetry run pytest --cov-report=html --cov=tfl tests/

.PHONY: mypy
mypy:
	poetry run mypy .

.PHONY: update-dev-deps
update-dev-deps:
	poetry add -D bandit@latest darglint@latest "isort[colors]@latest" mypy@latest pre-commit@latest pydocstyle@latest pylint@latest pytest@latest pyupgrade@latest coverage@latest coverage-badge@latest pytest-html@latest pytest-cov@latest
	poetry add -D --allow-prereleases black@latest

.PHONY: pycache-remove
pycache-remove:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf

.PHONY: dsstore-remove
dsstore-remove:
	find . | grep -E ".DS_Store" | xargs rm -rf

.PHONY: mypycache-remove
mypycache-remove:
	find . | grep -E ".mypy_cache" | xargs rm -rf

.PHONY: pytestcache-remove
pytestcache-remove:
	find . | grep -E ".pytest_cache" | xargs rm -rf

.PHONY: ruff-remove
ruff-remove:
	find . | grep -E ".ruff_cache" | xargs rm -rf

.PHONY: build-remove
build-remove:
	rm -rf build/

.PHONY: coverage-remove
coverage-remove:
	rm -rf .coverage
	rm -rf htmlcov/

.PHONY: cleanup
cleanup: pycache-remove dsstore-remove mypycache-remove pytestcache-remove build-remove coverage-remove ruff-remove
