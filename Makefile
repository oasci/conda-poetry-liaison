SHELL := /usr/bin/env bash
PACKAGE_NAME := conda-poetry-liaison

# notify_poetry_of_conda.py
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

.PHONY: validate
validate:
	poetry run pre-commit run --all-files

.PHONY: codestyle
codestyle:
	poetry run isort --settings-path pyproject.toml ./
	poetry run black --config pyproject.toml ./

.PHONY: formatting
formatting: codestyle
