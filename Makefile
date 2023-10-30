SHELL := /usr/bin/env bash
PACKAGE_NAME := conda_poetry_liaison

.PHONY: poetry-download
poetry-download:
	curl -sSL https://install.python-poetry.org/ | python -
	poetry self add "poetry-dynamic-versioning[plugin]"

.PHONY: pre-commit-install
pre-commit-install:
	poetry run pre-commit install

# Reads `pyproject.toml`, solves environment, then writes lock file.
.PHONY: poetry-lock
poetry-lock:
	poetry lock --no-interaction
	poetry export --without-hashes > requirements.txt

.PHONY: install
install:
	poetry install --no-interaction
	- mkdir .mypy_cache
	- poetry run mypy --install-types --non-interactive --explicit-package-bases $(PACKAGE_NAME)

.PHONY: validate
validate:
	poetry run pre-commit run --all-files

.PHONY: formatting
formatting:
	poetry run isort --settings-path pyproject.toml ./
	poetry run black --config pyproject.toml ./



###   LINTING   ###

.PHONY: check-codestyle
check-codestyle:
	poetry run isort --diff --check-only --settings-path pyproject.toml $(PACKAGE_NAME)
	poetry run black --diff --check --config pyproject.toml $(PACKAGE_NAME)
	-poetry run pylint --rcfile pyproject.toml $(PACKAGE_NAME)

.PHONY: mypy
mypy:
	poetry run mypy --config pyproject.toml -p $(PACKAGE_NAME)

.PHONY: lint
lint: check-codestyle mypy



###   BUILD   ###

.PHONY: build
build:
	poetry build
