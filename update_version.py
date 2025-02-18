#!/usr/bin/env python3
# coding: utf-8

"""
version update

updates a local _version_.txt file with the git version info
nicolas.barthe@orange.com
"""

# =======================================================
# Imports

from rich import print
from git import Repo

# =======================================================
# main loop

if __name__ == "__main__":
    repo = Repo(search_parent_directories=True)
    version_string = (
        str(repo.head.reference)
        + ' '
        + str(repo.tags[0])
        + ' #'
        + repo.head.object.hexsha
    )
    print(version_string)
    with open('./_version_.txt', 'w') as version_file:
        version_file.write(version_string)
