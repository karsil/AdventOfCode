import os
from pathlib import Path

from aoc.utilities import load_data_as_list


DIR = os.path.dirname(__file__)


def day01():
    return load_data_as_list(Path(DIR).joinpath("input.txt"))


if __name__ == "__main__":
    print(day01())
