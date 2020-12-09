def main():
    with open("data.txt", 'r') as f:
        content = f.readlines()
    content = [x.replace("\n", '') for x in content]
    content = [int(x) for x in content]

    for i, first in enumerate(content):
        for j in range(i, len(content)):
            second = content[j]
            sum = first + second
            if sum == 2020:
                print(first * second)


if __name__ == "__main__":
    main()