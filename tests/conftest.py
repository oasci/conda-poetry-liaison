import os
import shutil
import subprocess

import pytest

TEST_DIR = os.path.dirname(__file__)


@pytest.fixture(scope="session", autouse=True)
def conda_env_path():
    env_path = os.path.join(TEST_DIR, "envs", "cpl-test")
    return env_path


@pytest.fixture(scope="session", autouse=True)
def set_conda_env(conda_env_path):
    if os.path.exists(conda_env_path):
        shutil.rmtree(conda_env_path)
    subprocess.run(["conda", "create", "-p", conda_env_path], check=True)
    install_packages = ["scipy"]
    install_packages_cmd = [
        "conda",
        "install",
        "-p",
        conda_env_path,
        "-c",
        "conda-forge",
    ] + install_packages
    subprocess.run(install_packages_cmd, check=False)
