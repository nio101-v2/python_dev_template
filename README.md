# python bootstrap kit

## install

+ install a recent python stable release (perhaps not the very last one but the previous, to ensure module availability)
  + see https://devguide.python.org/versions/ and https://www.python.org/downloads/
  + I used python 3.12.x. You may need to update pyproject.toml if you plan to use another version: `requires-python = ">=3.12"`
+ update pip : `python -m pip install -U pip`

+ install poetry https://python-poetry.org/ : `pip install poetry`
+ disable virtual env `poetry config virtualenvs.create false`
+ now `poetry install` will install/update the required tools/dependencies in the current env

## use

+ use poetry to handle dependencies:
    + `poetry add rich` will install and add a new dependency
    + `poetry remove rich` will remove a dependency
    + `poetry show` lists the dependencies
      + you can also update manually pyproject.toml

+ use doctest to implement basic function testing
  + use `task test` to pass the tests from the docstrings

+ use task & Taskfile.yml to automate things:
  + use `task update` before any commit, as it chains the following actions:
    + reformatting source code with black
    + analyzing with pylint
    + analyzing with vulture
    + generate/update static documentation site with docstrings+source code

## best practices (non exhaustif)

+ utiliser le module faker pour générer des données de test/dev
  + [GitHub - joke2k/faker: Faker is a Python package that generates fake data for you.](https://github.com/joke2k/faker)
  + voir la démo dans main.py

+ utiliser un IDE pour développer
  + apport d'un IDE : auto-completion, linting, versioning git... on doit être x5-x10 fois plus efficace avec un IDE?
  + on peut développer à plusieurs en même temps (vs à plusieur sur un même fichier sur une VM !)
  + ex.: sublime text, visual studio code...

+ ne pas développer sur la machine en VI + workflow de type dev local poussé vers GIT et ensuite redescendu vers VM
  + utiliser des fichiers de test anonymisés pour développer en local sur sa machine
  + pas forcément besoin de connectivité
  + on peut utiliser un IDE

+ unicité de lieu : gitlab/github
  + tout avoir/mettre en un seul endroit
  + code source, config des outils, documentation, pipelines CI/CD, defects/bugs en utilisant gitlab|github/issues

+ afficher/exploiter la version du code dans le runtime
  + l'outil produit (que ce soit un CLI ou un serveur WEB basique qui répond à des req) doit afficher la version + date/heure
  + on peut toujours vérifier qu'on est bien/parle bien de la dernière version
  + voir la démo dans main.py

+ utiliser des fichiers de configuration pour paramétrer le runtime + utiliser un module CLI pour passer facilement des paramètres en ligne de commande (surchage / configuration par fichier)
  + voir la démo dans main.py
+ utiliser les fichiers de log (fichiers) pour debugger les taches très verbeuses (plutôt qu'à l'écran)
  + voir la démo dans main.py

+ toujours commenter le code source avec les docstrings (voir exemple main.py et les manuels mkdocs et mkdocstrings)
  + la doc sera génerée et poussée automatiquement vers le site gitlab page du repo (voir la pipeline gitlabCI)

+ automatiser avec makefile/Taskfile -> compléter Taskfile.yml
+ gérer les dépendances python avec poetry

+ exploiter la richesse des modules Python
  + [GitHub - vinta/awesome-python: An opinionated list of awesome Python frameworks, libraries, software and resources.](https://github.com/vinta/awesome-python)
  + pandas pour l'ETL/manipulation de données

+ prendre un workflow GIT basique genre [Centralized Workflow Guide | CraftQuest](https://craftquest.io/guides/git/git-workflows/centralized-workflow)
  + une seule branche : main et on peut travailler chacun sur des parties différentes en //
  + contrainte : toujours faire un checkout avant de faire un commit/push
  + si pas de téléscopage de push et si pas de travail en // sur les mêmes fichiers, pas de soucis...

+ utiliser doctest pour faire du test unitaire basique :
```python
D:\python\python_dev_template>python
Python 3.12.9 (tags/v3.12.9:fdb8142, Feb  4 2025, 15:27:58) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from mymodule.rules import rule_one
>>> rule_one(5)
rule #1: warning!
6
>>> rule_one(7)
rule #1: warning!
8
>>>
```
  + copier les exemples passés manuellement dans l'interpréteur dans les docstrings de la fonction.
  + faire un `task test`
