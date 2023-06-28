.PHONY: codestyle
codestyle:
	poetry run ruff --fix .
	poetry run black .

.PHONY: check-ruff
check-ruff: ## Check that code conforms to ruff rules.
	poetry run ruff . --format=github

.PHONY: check-black
check-black: ## Check that code conforms with black style.
	poetry run black . --check --verbose --diff --color

.PHONY: formatting
formatting: codestyle ## Format your code.

.PHONY: test
test: ## Run unit tests.
	poetry run pytest --cov=tfl --cov-report term --cov-report xml:coverage.xml --cov-report=html tests/

.PHONY: build-docs
build-docs:
	poetry run mkdocs build --verbose --clean --strict --site-dir public

.PHONY: check-mypy
check-mypy: ## Check for typing errors.
	poetry run mypy .

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
	rm -rf coverage.xml

.PHONY: public-remove
public-remove:
	rm -rf public

.PHONY: cleanup
cleanup: pycache-remove dsstore-remove mypycache-remove pytestcache-remove build-remove coverage-remove ruff-remove public-remove ## Cleanup residual files.

.DEFAULT_GOAL := help

.PHONY: help
# See <https://gist.github.com/klmr/575726c7e05d8780505a> for explanation.
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
