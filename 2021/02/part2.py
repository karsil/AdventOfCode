from enum import Enum

from utilities import load_data_as_list


class Direction(Enum):
    FORWARD = ("forward", lambda d, h, a, v: (d + (a * v), h + v, a))
    DOWN = ("down", lambda d, h, a, v: (d, h, a + v))
    UP = ("up", lambda d, h, a, v: (d, h, a - v))

    def __str__(self):
        return self.value[0]

    def __call__(self, depth: int, horizontal: int, aim: int, value: int, *args, **kwargs):
        return self.value[1](depth, horizontal, aim, value)

    @staticmethod
    def of(value: str) -> 'Direction':
        l_value = value.strip().lower()
        for t in Direction:
            if str(t) == l_value:
                return t
        raise ValueError("Not a valid direction")


def puzzle(file_path: str) -> int:
    l_content = load_data_as_list(file_path)
    l_depth = 0
    l_horizontal = 0
    l_aim = 0
    for line in l_content:
        l_direction = line.split()[0]
        l_value = int(line.split()[1])
        l_depth, l_horizontal, l_aim = Direction.of(value=l_direction)(l_depth, l_horizontal, l_aim, l_value)
    return l_depth * l_horizontal


if __name__ == "__main__":
    print(puzzle("data.txt"))
