import os
from pathlib import Path

from aoc.utilities import load_data_as_list


DIR = Path(os.path.dirname(__file__))

name2score = {
    "rock": 1,
    "paper": 2,
    "scissor": 3
}

name2short = {
    "rock": ("A", "X"),
    "paper": ("B", "Y"),
    "scissor": ("C", "Z")
}

nameWinsAgainst = {
    "rock": "scissor",
    "paper": "rock",
    "scissor": "paper"
}


def get_score(opponent: str, me: str) -> int:
    WIN_POINTS = 6
    DRAW_POINTS = 3

    if opponent == me:
        return name2score[me] + DRAW_POINTS
    return WIN_POINTS + name2score[me] if nameWinsAgainst[me] == opponent else name2score[me]


def get_name(short: str) -> str:
    for k, v in name2short.items():
        if short in v:
            return k


def day02():
    rounds = [x.split() for x in load_data_as_list(DIR.joinpath("input.txt"))]
    print(sum((get_score(get_name(r[0]), get_name(r[1])) for r in rounds)))




if __name__ == "__main__":
    day02()
