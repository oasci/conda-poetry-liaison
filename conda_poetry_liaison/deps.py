from typing import Union

import argparse
import subprocess

import tomli
import tomli_w


def check_if_include_package(conda_str: str) -> bool:
    r"""Checks if we should include a package in pyproject.toml"""
    if "" == conda_str.strip():
        return False
    if "_" == conda_str[0]:
        return False
    return True


def run_notify(
    toml_path: str,
    env_name: Union[str, None] = None,
    env_path: Union[str, None] = None,
    group_name: str = "conda",
    save=True,
):
    command = ["conda", "run"]
    if env_path is not None:
        command.extend(["-p", env_path])
    elif env_name is not None:
        command.extend(["-n", env_name])
    else:
        raise ValueError("Both env_name and env_path cannot be None")
    command.extend(["pip", "list"])

    results = subprocess.run(
        command,
        check=True,
        capture_output=True,
        text=True,
    )
    conda_packages = results.stdout.split("\n")[3:]

    with open(toml_path, mode="rb") as f:
        toml_file = tomli.load(f)

    conda_group_label = f"tool.poetry.group.{group_name}.dependencies"
    # Overwrite (or assign) conda group dependencies
    toml_file[conda_group_label] = {}
    for conda_package in conda_packages:
        if not check_if_include_package(conda_package):
            continue
        conda_package_split = conda_package.strip().split()
        toml_file[conda_group_label][
            conda_package_split[0]
        ] = f"^{conda_package_split[1]}"
    if save:
        with open(toml_path, "wb") as f:
            tomli_w.dump(toml_file, f)


def main():
    parser = argparse.ArgumentParser(
        description="Notify poetry of conda Python packages"
    )
    parser.add_argument(
        "toml_path",
        type=str,
        nargs="?",
        help="Path to TOML file",
    )
    parser.add_argument(
        "--env_name",
        type=str,
        nargs="?",
        default=None,
        help="Name of conda environment to probe",
    )
    parser.add_argument(
        "--env_path",
        type=str,
        nargs="?",
        default=None,
        help="Path of conda environment to probe",
    )
    parser.add_argument(
        "--group_name",
        type=str,
        nargs="?",
        default="conda",
        help="Name of poetry dependency group",
    )
    args = parser.parse_args()
    run_notify(
        args.toml_path,
        env_name=args.env_name,
        env_path=args.env_path,
        group_name=args.group_name,
        save=True,
    )


if __name__ == "__main__":
    main()
