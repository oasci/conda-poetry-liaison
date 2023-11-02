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

## Example

Create and activate a conda environment.
For this example, we are creating an environment named `sunshine`.

```bash
conda create -y -n sunshine python=3.11 && conda activate sunshine
```

Install the following required packages.

```bash
conda install -y -c conda-forge poetry pre-commit tomli tomli-w \
pip install conda_poetry_liaison
```

**NOTE:** We are waiting for the [conda-forge recipe](https://github.com/conda-forge/conda-poetry-liaison-feedstock) for `conda_poetry_liaison` to build.
For the time being, the only way to install it is with `pip`.

Install your desired packages; for example, suppose you want `numpy`, `scipy`, and `matplotlib`.

```bash
conda install -y -c conda-forge numpy scipy matplotlib
```

Update the `tool.poetry.group.conda.dependencies` group in your `pyproject.toml` with the `cpl-deps` script.

```bash
cpl-deps pyproject.toml --env_name sunshine
```

Cleanup your conda environment with `cpl-clean` before switching to using poetry exclusively.

```bash
cpl-clean --env_name sunshine
```

Now you are good to go!
For example, you can run `poetry install` to install all poetry-managed PyPI packages in `pyproject.toml`.

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

## License

Code contained in this project is released under the [MIT License](https://spdx.org/licenses/MIT.html) as specified in [`LICENSE`][license].
This license grants you the freedom to use, modify, and distribute it as long as you include the original copyright notice contained in [`LICENSE`][license] and the following disclaimer.

> Portions of this code were incorporated and adapted with permission from [conda-poetry-liaison](https://github.com/oasci/conda-poetry-liaison) by OASCI under the [MIT License](https://github.com/oasci/conda-poetry-liaison/blob/main/LICENSE).

[license]: https://github.com/oasci/conda-poetry-liaison/blob/main/LICENSE
