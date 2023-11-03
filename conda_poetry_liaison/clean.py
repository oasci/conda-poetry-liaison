from typing import Union

import argparse
import os

from .utils import get_conda_env_path, get_files


def run_cleaning(
    env_name: Union[str, None] = None,
    env_path: Union[str, None] = None,
) -> None:
    if env_path is None:
        if isinstance(env_name, str):
            env_path = get_conda_env_path(env_name)
        else:
            raise ValueError("Both env_name and env_path cannot be None")
    direct_url_paths = get_files(env_path, "direct_url.json")
    for path in direct_url_paths:
        try:
            os.remove(path)
        except FileNotFoundError:
            # Due to symlinks we often have repeated files.
            pass


def main():
    # pylint: disable=duplicate-code
    parser = argparse.ArgumentParser(
        description="Clean up the conda environment for use with poetry"
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
    args = parser.parse_args()
    run_cleaning(env_name=args.env_name, env_path=args.env_path)


if __name__ == "__main__":
    main()
