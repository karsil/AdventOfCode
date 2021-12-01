from typing import List

DATA = "data.txt"


def load_data(path: str) -> List[int]:
    with open(path, "r") as f:
        return list(map(int, filter(lambda x: len(x), f.read().split("\n"))))


def main():
    content = load_data(DATA)

    counter = 0
    MAX = len(content)

    previous_sum = 0
    for i, _ in enumerate(content):
        if i == 0 or i == 1:
            continue
        if i + 1 == MAX:
            break

        window_sum = sum([content[i-1], content[i], content[i+1]])
        if window_sum > previous_sum:
            counter += 1

        previous_sum = window_sum

    print(counter)


if __name__ == "__main__":
    main()
