#!/usr/bin/env python3
# coding: utf-8

"""
version update

updates a local _version_.txt file with the git version info
"""

# =======================================================
# Imports

from rich.console import Console
from git import Repo
import arrow

# =======================================================
# main loop

if __name__ == "__main__":
    console = Console()

    repo = Repo(search_parent_directories=True)
    commit_date = arrow.get(repo.commit("main").committed_date).to('local')
    if len(repo.tags) == 0:
        tag = r'\[no_tag]'
        # note : we are escaping the first bracket because :
        # https://rich.readthedocs.io/en/latest/markup.html#escaping
    else:
        tag = r'\[' + str(repo.tags[0]) + r']'
    version_string = (
        str(repo.head.reference)
        + ' '
        + tag
        + ' #'
        + repo.head.object.hexsha[0:4]
        + ' ('
        + str(commit_date)
        + ')'
    )
    console.print(version_string, style="orange_red1", highlight=False)
    with open('./_version_.txt', 'w') as version_file:
        version_file.write(version_string)
