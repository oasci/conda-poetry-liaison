# Changelog

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- A `make refresh` command to automate virtual environment creation.

### Changed

- Removed `poetry-dynamic-versioning` as a package dependency.

## [0.1.1] - 2023-10-30

### Fixed

- `cpl-clean` would always raise `ValueError`.

## [0.1.0] - 2023-10-30

### Added

- `cpl-clean` can take environment path or name.

### Fixed

- Splitting conda package name and versions.

## [0.0.2] - 2023-10-24

### Added

- Example command to bump version.
- Badges to documentation.
- Documentation about deploying to PyPI.

### Fixed

- `try` when removing `direct_url.json` files because of symbolic links that repeated files.

## [0.0.1] - 2023-10-23

- Initial release!
