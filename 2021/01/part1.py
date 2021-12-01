from typing import List

DATA = "data.txt"


def load_data(path: str) -> List[int]:
    with open(path, "r") as f:
        return list(map(int, filter(lambda x: len(x), f.read().split("\n"))))


def main():
    content = load_data(DATA)

    counter = 0
    for i, _ in enumerate(content):
        if i == 0:
            continue

        if content[i] > content[i-1]:
            counter += 1

    print(counter)


if __name__ == "__main__":
    main()
