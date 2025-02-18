# requirements

+ recent python stable release (not the very last one, to ensure module availability)
  + see https://devguide.python.org/versions/ and https://www.python.org/downloads/
  + update pip : `python -m pip install -U pip`

+ install poetry https://python-poetry.org/ : `pip install poetry`
+ disable virtual env `poetry config virtualenvs.create false`
+ `poetry install` will install/update dependencies in the current env
  + `poetry add rich` will add a new dependency
  + `poetry remove rich` will remove a dependency
  + `poetry show` lists the dependencies

