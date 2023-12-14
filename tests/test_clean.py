from conda_poetry_liaison.clean import run_cleaning


def test_clean(conda_env_path):
    run_cleaning(conda_env_path)
