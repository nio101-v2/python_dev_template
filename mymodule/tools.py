#!/usr/bin/env python3
# coding: utf-8

"""
tools

various functions
"""

# =======================================================
# Imports

from git import Repo
import arrow
import logging

log = logging.getLogger(__name__)


# =======================================================
# functions
def get_version():
    """retrieve the current local GIT version info"""
    repo = Repo(search_parent_directories=True)
    commit_date = arrow.get(repo.commit("main").committed_date).to('local')
    if len(repo.tags) == 0:
        log.warning("get_version(): warning: no tag set for local git repo")
        tag = 'no_tag'
    else:
        tag = repo.tags[0]
    version_string = "{} [{}] #{} ({})".format(
        str(repo.head.reference), tag, repo.head.object.hexsha[0:4], commit_date
    )
    return version_string
