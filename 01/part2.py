def main():
    with open("data.txt", 'r') as f:
        content = f.readlines()

    content = [x.replace("\n", '') for x in content]
    content = [int(x) for x in content]

    for i, first in enumerate(content):
        for j in range(i, len(content)):
            for k in range(j, len(content)):
                second = content[j]
                third = content[k]
                sum = first + second + third
                if sum == 2020:
                    print(first * second * third)


if __name__ == "__main__":
    main()