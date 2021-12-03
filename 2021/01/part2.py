from utilities import load_data_as_list

DATA = "data.txt"


def puzzle() -> int:
    content = load_data_as_list(DATA, int)
    return len([1 for i in range(2, len(content) - 1) if sum(content[i - 2:i + 1]) > sum(content[i - 3:i])])


if __name__ == "__main__":
    print(puzzle())
