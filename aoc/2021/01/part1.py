from utilities import load_data_as_list


def puzzle(data_file: str) -> int:
    content = load_data_as_list(data_file, int)
    return len([1 for i in range(1, len(content) - 1) if content[i] > content[i-1]])


if __name__ == "__main__":
    print(puzzle("data.txt"))
