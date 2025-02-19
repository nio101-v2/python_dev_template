#!/usr/bin/env python3
# coding: utf-8

"""
rules

implement rules
"""

# =======================================================
# Imports

# import pandas
import logging

log = logging.getLogger(__name__)


# =======================================================
# functions
def rule_one(input_value):
    """implement rule #1"""
    log.warning("rule #1: warning!")
    return input_value + 1
