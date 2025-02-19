#!/usr/bin/env python3
# coding: utf-8

"""
main template demo

provides a skeleton/sample file + demo
"""

# =======================================================
# Imports

import configparser
import logging
from rich.console import Console
from rich.progress import Progress
from rich.logging import RichHandler
from logging import Formatter
from logging import FileHandler

# from logging.handlers import RotatingFileHandler

import time

# import pandas
from tqdm import tqdm
from time import sleep
from faker import Faker
import mymodule.tools as tools
import mymodule.rules as rules

# =======================================================
# helpers


def helping_function():
    """
    fake gelping function
    """
    return


def main():
    """demo main loop"""
    console = Console()

    # prepare logging
    LOGFORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGFORMAT_RICH = '%(message)s'
    error_console = Console(stderr=True)
    rh = RichHandler(console=error_console)
    rh.setFormatter(Formatter(LOGFORMAT_RICH))
    # setting up the log, here with a basic one-shot log file
    # for rotating file, see comment below
    logging.basicConfig(
        level=logging.WARNING,
        # format=LOGFORMAT,python
        format=LOGFORMAT,
        handlers=[
            rh,
            # logging.StreamHandler(sys.stderr),
            FileHandler('main.log', mode='w', encoding="UTF-8", delay=False),
            # RotatingFileHandler(
            #     'main.log', maxBytes=1024 * 1024 * 10, backupCount=2  # 10Mb
            # ),  # only 1 files
        ],
    )
    log = logging.getLogger('main')

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
    for i in tqdm(range(100)):
        sleep(0.005)
    print("")

    with Progress() as progress:
        task = progress.add_task("Processing...", total=100)
        for i in range(100):
            time.sleep(0.01)
            progress.update(task, advance=1)
    print("")

    # use a function from mymodule and test log output
    new_value = rules.rule_one(1)
    log.error("that's a fatal error!")

    #
    # logging.basicConfig(level="INFO", handlers=[RichHandler()])
    # logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG, handlers=[RichHandler()])
    # log = logging.getLogger("rich")

    # log.info("This is an info message.")
    # log.error("This is an error message.")

    # done
    console.print("\n[bold magenta]done![/bold magenta] :thumbs_up:")


# =======================================================
# main loop

if __name__ == "__main__":
    main()
