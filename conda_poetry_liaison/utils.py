import os
import subprocess
from collections.abc import Iterable


def get_files(path: str, expression: str, recursive: bool = True) -> Iterable[str]:
    r"""Returns paths to all files in a given directory that matches a provided
    expression in the file name.

    Commonly used to find all files of a certain type, e.g., output or xyz
    files.

    Parameters
    ----------
    path
        Specifies the directory to search.
    expression
        Expression to be tested against all file names in ``path``.
    recursive : :obj:`bool`, default: ``True``
        Recursively find all files in all subdirectories.

    Returns
    -------
    :obj:`list` [:obj:`str`]
        All absolute paths to files matching the provided expression.
    """
    if not path.endswith("/"):
        path += "/"

    files = []
    for entry in os.scandir(path):
        if entry.is_file() and expression in entry.name:
            files.append(entry.path)
        elif recursive and entry.is_dir():
            files.extend(get_files(entry.path, expression, recursive))

    return files


def get_conda_env_path(env_name: str) -> str:
    r"""Gets the full path of a conda environment

    Parameters
    ----------
    env_name
        Name of conda environment.

    Returns
    -------

        Path to conda environment.
    """
    results = subprocess.run(
        ["conda", "info", "-e"],
        check=True,
        capture_output=True,
        text=True,
    )
    conda_envs = results.stdout
    for line in conda_envs.split("\n"):
        line_split = line.strip().split()
        if line_split[0] == env_name:
            env_path = line_split[-1]
            return env_path
    raise RuntimeError(f"Could not find conda environment with name {env_name}")
