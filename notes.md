# install

+ install a recent python stable release (perhaps not the very last one but the previous, to ensure module availability)
  + see https://devguide.python.org/versions/ and https://www.python.org/downloads/
  + I used python 3.12.x. You may need to update pyproject.toml if you plan to use another version: `requires-python = ">=3.12"`
+ update pip : `python -m pip install -U pip`

+ install poetry https://python-poetry.org/ : `pip install poetry`
+ disable virtual env `poetry config virtualenvs.create false`
+ now `poetry install` will install/update the required tools/dependencies in the current env

# use

+ use poetry to handle dependencies:
    + `poetry add rich` will install and add a new dependency
    + `poetry remove rich` will remove a dependency
    + `poetry show` lists the dependencies
      + you can also update manually pyproject.toml

+ use task & Taskfile.yml to automate things:
  + use `task update` before any commit, as it chains the following actions:
    + reformatting source code with black
    + analyzing with pylint
    + analyzing with vulture

