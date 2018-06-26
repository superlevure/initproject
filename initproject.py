"""
Init a new Python module
"""

import os
import sys
import venv
import shutil


if __name__ == "__main__":

    MODULE_FOLDER = os.path.dirname(os.path.abspath(__file__))
    EXECUTION_FOLDER = os.getcwd()

    PROJECT_NAME = sys.argv[1]
    # Project's folder creation
    try:
        os.mkdir(PROJECT_NAME)
    except FileExistsError:
        sys.exit("A folder with the project's name already exists")

    # Enter the project's folder
    os.chdir(PROJECT_NAME)

    # Git init
    os.system("git init")

    # Virtual environnement creation
    new_env = venv.EnvBuilder(with_pip=True)
    new_env.create(".env")

    # Download common modules
    os.system(".env/bin/pip install pylint black")

    # Create vscode workspace
    os.mkdir(".vscode")

    shutil.copyfile(
        MODULE_FOLDER + "/.vscode/settings.json",
        EXECUTION_FOLDER + "/" + PROJECT_NAME + "/.vscode/settings.json",
    )

    shutil.copyfile(
        MODULE_FOLDER + "/" + "initproject.code-workspace",
        EXECUTION_FOLDER + "/" + PROJECT_NAME + "/" + PROJECT_NAME + ".code-workspace",
    )

    # Create git ignore
    shutil.copyfile(
        MODULE_FOLDER + "/" + ".gitignore",
        EXECUTION_FOLDER + "/" + PROJECT_NAME + "/.gitignore",
    )

    # Create folder tree and files
    os.mkdir(PROJECT_NAME)
    os.mkdir("tests")
    os.mkdir("docs")

    if simple_project:
        with open(PROJECT_NAME + ".py", "w") as file:
            pass
    else:
        with open(PROJECT_NAME + "/__init__.py", "w") as file:
            pass

    with open(PROJECT_NAME + "/__init__.py", "w") as file:
        pass
