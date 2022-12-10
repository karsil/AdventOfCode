from utilities import load_data_as_list
import numpy as np


def dec(number: np.ndarray) -> int:
    return sum((2**i for i, b in enumerate(reversed(number)) if b))


def puzzle(file_path: str) -> int:
    l_data = load_data_as_list(file_path, postprocess=lambda x: x.split()[0])
    a = np.array(list(map(list, l_data))).astype(int)
    gamma = np.round(a.sum(axis=0) / len(a)).astype(bool)
    return dec(gamma) * dec(~gamma)


if __name__ == "__main__":
    print(puzzle("data.txt"))
