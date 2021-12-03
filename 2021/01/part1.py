from utilities import load_data_as_list

DATA = "data.txt"


def puzzle():
    content = load_data_as_list(DATA, int)
    return len([1 for i in range(1, len(content) - 1) if content[i] > content[i-1]])


if __name__ == "__main__":
    print(puzzle())
