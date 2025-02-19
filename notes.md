# requirements

+ install a recent python stable release (perhaps not the very last one but the previous, to ensure module availability)
  + see https://devguide.python.org/versions/ and https://www.python.org/downloads/
  + I used python 3.12.x. You may need to update pyproject.toml if you plan to use another version: `requires-python = ">=3.12"`
+ update pip : `python -m pip install -U pip`

+ install poetry https://python-poetry.org/ : `pip install poetry`
+ disable virtual env `poetry config virtualenvs.create false`
+ now `poetry install` will install/update the required tools/dependencies in the current env
  + note that :
    + `poetry add rich` will add a new dependency
    + `poetry remove rich` will remove a dependency
    + `poetry show` lists the dependencies
      + you can also update manually pyproject.toml

+ task & Taskfile.yml replace make/makefile to help at automating things
  + `task version` updates a local _version_.txt file that reflects the current git branch/tag/commit hash to be displayed at runtime
  + `task format` uses black to reformat the source code files

