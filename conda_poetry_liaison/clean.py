import argparse
import os

from .utils import get_files


def run_cleaning(env_path):
    if not isinstance(env_path, str):
        raise TypeError(f"env_path should be a string, not {type(env_path)}")
    direct_url_paths = get_files(env_path, "direct_url.json")
    for path in direct_url_paths:
        os.remove(path)


def main():
    parser = argparse.ArgumentParser(
        description="Notify poetry of conda Python packages"
    )
    parser.add_argument(
        "env_path",
        type=str,
        nargs="?",
        help="Path of conda environment to clean",
    )
    args = parser.parse_args()
    run_cleaning(args.env_path)


if __name__ == "__main__":
    main()
