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
from rich import print
from tqdm import tqdm
from time import sleep
from faker import Faker

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
    # read .ini config file
    config = configparser.ConfigParser()
    config.read("config.ini")
    startup_wait = config.getint('startup', 'wait')
    max_delay = config.getint('alive_check', 'max_delay')
    # also: getfloat, getint, getboolean

    # read current version
    with open(file='./_version_.txt', encoding='utf-8', mode='r') as version_file:
        version = version_file.read()
    version = version.rstrip("\n\r")

    print(version, "\n")
    print("Hello, [bold magenta]World[/bold magenta]!", ":thumbs_up:", "\n")

    fake = Faker()
    print(fake.name())
    print(fake.address())
    print(fake.text(), "\n")

    for i in tqdm(range(1000)):
        sleep(0.005)

    print("done.")
