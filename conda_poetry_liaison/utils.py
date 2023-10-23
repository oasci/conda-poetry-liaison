import os


def get_files(path, expression, recursive=True):
    r"""Returns paths to all files in a given directory that matches a provided
    expression in the file name.

    Commonly used to find all files of a certain type, e.g., output or xyz
    files.

    Parameters
    ----------
    path : :obj:`str`
        Specifies the directory to search.
    expression : :obj:`str`
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
