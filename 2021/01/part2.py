from typing import List

DATA = "data.txt"


def load_data(path: str) -> List[int]:
    with open(path, "r") as f:
        return list(map(int, filter(lambda x: len(x), f.read().split("\n"))))


def main():
    content = load_data(DATA)

    counter = 0
    previous_sum = 0
    for i in range(2, len(content) - 1):
        window_sum = sum(content[i - 2:i + 1])
        if window_sum > previous_sum:
            counter += 1
        previous_sum = window_sum

    print(counter)


if __name__ == "__main__":
    main()
