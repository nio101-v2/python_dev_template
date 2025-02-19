#!/usr/bin/env python3
# coding: utf-8

"""
main template

provides a skeleton/sample file
"""

# =======================================================
# Imports

import configparser
import pandas
from tqdm import tqdm
from time import sleep
from faker import Faker
from rich.console import Console
import mymodule.tools as tools
import mymodule.rules as rules

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
    console = Console()

    # read .ini config file
    config = configparser.ConfigParser()
    config.read("config.ini")
    startup_wait = config.getint('startup', 'wait')
    max_delay = config.getint('alive_check', 'max_delay')
    # also: getfloat, getint, getboolean

    # retrieve and show current local GIT version
    console.print(
        tools.get_version(), style="orange_red1", highlight=False, markup=False
    )
    # markup is set to false to prevent tag being interpreted as a markup by rich
    # see https://github.com/textualize/rich/blob/master/FAQ.md#why-does-content-in-square-brackets-disappear
    console.print("\n[bold magenta]Hello, World![/bold magenta]\n")

    # print some fake info
    fake = Faker()
    console.print(fake.name())
    console.print(fake.address())
    console.print(fake.text(), "\n")

    # and some fake progress bar
    for i in tqdm(range(1000)):
        sleep(0.005)

    # use a function from mymodule
    new_value = rules.rule_one(1)

    # done
    console.print("\n[bold magenta]done![/bold magenta] :thumbs_up:")
