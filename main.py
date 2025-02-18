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

    print("Hello, [bold magenta]World[/bold magenta]!", ":thumbs_up:")

    fake = Faker()
    print(fake.name())
    print(fake.address())
    print(fake.text(),)

    for i in tqdm(range(1000)):
        sleep(0.005)

    print("done.")
