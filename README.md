## A repo template for python packages

### Features

* Python 3.10 (but easy to change)
* Uses setup.cfg & pyproject.toml (not setup.py)
* [Unlicense](https://unlicense.org/)
* VS Code [development container](https://code.visualstudio.com/docs/remote/containers) definitions
* Configures [black](https://github.com/psf/black) & [isort](https://pycqa.github.io/isort/) to run on save in vscode
* Includes a github action which runs tests on PRs against main branch
* Includes (somewhat opinionated) tests template
* Includes a trivial `<package>.__version__` property

### Checklist

1. Add project details to `setup.cfg`
1. Update line 3 of `src/package_name/__init__.py` to include your package name
1. Rename the `src/package_name` directory to `src/<your actual package name>`
1. Change the LICENSE if you want to. https://choosealicense.com/
1. [_Optional_] If you want your minimum supported python version to differ from 3.10:
    
    1. Update your package definition: Line 22 of `setup.cfg`
    1. Configure black to lint properly: Line 10 of `pyproject.toml`
    1. Uncomment tests workflow to test relevent versions: Line 13 of `.github/workflows/tests.yaml`
    1. Update devcontainer image to use new version: Line 5 of `.devcontainer/Dockerfile`

1. Build your dev container & reopen your IDE 
1. Install your package in editable mode & start working: `pip install -e .[tests]`
1. Don't forget to rewrite this README.md