#!/usr/bin/env python3
# coding: utf-8

"""
main template

provides a skeleton/sample file
"""

# =======================================================
# Imports

from rich import print
from git import Repo

# =======================================================
# helpers

def helping_function():
    """
    blablabla
    """
    return

# =======================================================
# main loop

if __name__ == "__main__":
    repo = Repo(search_parent_directories=True)
    version_string = str(repo.head.reference) + ' / ' + str(repo.tags) + ' #' + repo.head.object.hexsha
    with open('./_version_.txt', 'w') as version_file:
        version_file.write(version_string)
    print(version_string)
    print("done.")
