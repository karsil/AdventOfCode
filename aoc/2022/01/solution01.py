import os
from pathlib import Path

from aoc.utilities import load_data_as_list


DIR = Path(os.path.dirname(__file__))


def day01():
    data = ((int(y) for y in x.split()) for x in load_data_as_list(DIR.joinpath("input.txt"), split="\n\n"))
    each = sorted(map(sum, data), reverse=True)
    print(f"Top: {each[0]}")
    print(f"Sum of top 3: {sum(each[0:3])}")


if __name__ == "__main__":
    day01()
