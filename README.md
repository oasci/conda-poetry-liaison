<h1 align="center">conda_poetry_liaison</h1>

<h4 align="center">Make conda and poetry communicate</h4>

<p align="center">
    <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/conda_poetry_liaison">
    <img alt="PyPI - Version" src="https://img.shields.io/pypi/v/conda_poetry_liaison">
    <a href="https://github.com/oasci/conda-poetry-liaison/blob/main/LICENSE" target="_blank">
        <img src="https://img.shields.io/github/license/oasci/conda-poetry-liaison" alt="License">
    </a>
    <a href="https://github.com/oasci/conda-poetry-liaison/" target="_blank">
        <img src="https://img.shields.io/github/repo-size/oasci/conda-poetry-liaison" alt="GitHub repo size">
    </a>
    <a href="https://github.com/psf/black" target="_blank">
        <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Black style">
    </a>
</p>

> Do not use another package manager in a conda environment.

Many are given this advice, but we do this anyway.
We want our conda-only packages with the awesome features of [poetry](https://python-poetry.org/).
`conda_poetry_liaison` is a small collection of scripts to make this as painless and reproducible as possible.

## Installation

You can install `conda_poetry_liaison` with pip.

```bash
pip install conda_poetry_liaison
```

## Scripts

### `cpl-deps`

The primary issue of using other package managers like pip and poetry inside a conda environment is that they will not communicate.
If you install a package with conda, then install a different one in pip, conda will have no idea what has changed.
So once you start using pip or poetry, you cannot use conda to install a package in that same environment.

This script will add all Python packages installed in the conda environment into the `pyproject.toml` file.
Now, poetry will be aware of these packages during dependency solving.

```text
usage: cpl-deps [-h] [--env_name [ENV_NAME]] [--env_path [ENV_PATH]] [--group_name [GROUP_NAME]] [toml_path]

Notify poetry of conda Python packages

positional arguments:
  toml_path             Path to TOML file

options:
  -h, --help            show this help message and exit
  --env_name [ENV_NAME]
                        Name of conda environment to probe
  --env_path [ENV_PATH]
                        Path of conda environment to probe
  --group_name [GROUP_NAME]
                        Name of poetry dependency group
```

### `cpl-clean`

There seems to be a remnant of `direct_url.json` files from conda package installations that break poetry (as discussed [here](https://github.com/python-poetry/poetry/issues/6408)).
One workaround is to delete these files in the conda environment directory before using poetry.

```text
usage: cpl-clean [-h] [--env_name [ENV_NAME]] [--env_path [ENV_PATH]]

Notify poetry of conda Python packages

options:
  -h, --help            show this help message and exit
  --env_name [ENV_NAME]
                        Name of conda environment to probe
  --env_path [ENV_PATH]
                        Path of conda environment to probe
```

## Development

Install poetry if you do not have it.

```bash
make poetry-download
```

If you already have poetry installed, make sure you have [poetry-dynamic-versioning](https://github.com/mtkennerly/poetry-dynamic-versioning).

```bash
poetry self add "poetry-dynamic-versioning[plugin]"
```

Install the package.

```bash
make install
```

Install all pre-commits.

```bash
make pre-commit-install
```

## Deploying

A note to maintainers.

We use [bump-my-version](https://github.com/callowayproject/bump-my-version) to release a new version.
This will create a git tag that is used by [poetry-dynamic-version](https://github.com/mtkennerly/poetry-dynamic-versioning) to generate version strings and update `CHANGELOG.md`.

For example, to bump the `minor` version you would run the following command.

```bash
poetry run bump-my-version bump minor
```

After releasing a new version, you need to push and include all tags.

```bash
git push --follow-tags
```
