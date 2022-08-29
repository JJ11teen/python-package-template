## A repo template for python packages

### Features

* Python 3.10 (but easy to change)
* Uses setup.cfg & pyproject.toml (not setup.py)
* MIT licence
* VS Code development container definitions
* Configures black & isort to run on save in vscode
* Includes a github action which run tests on PRs against main branch
* Includes tests template

### Checklist

1. Add project details to `setup.cfg`
1. Rename the `src/package_name` directory to actually include your package name
1. Change licence if you don't want the MIT licence
1. [_Optional_] If you want your minimum supported python version to differ from 3.10:
    
    1. Update your package definition: Line 22 of `setup.cfg`
    1. Configure black to lint properly: Line 10 of `pyproject.toml`
    1. Uncomment tests workflow to test relevent versions: Line 13 `.github/workflows/tests.yaml`
    1. Update devcontainer image to use new version: Line 5 `.devcontainer/Dockerfile`

1. Build your dev container & reopen your IDE 
1. Install your package in editable mode & start working: `pip install -e .[tests]`
1. Don't forget to rewrite this README.md!