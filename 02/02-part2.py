def verify_line(line: str) -> bool:
    m = line.split()
    amount = m[0].split("-")
    min_amount = int(amount[0])
    max_amount = int(amount[1])

    letter = m[1].replace(":", "")
    password = m[2]
    return (password[min_amount - 1] == letter) ^ (password[max_amount - 1] == letter)


def main():
    with open("data.txt", 'r') as f:
        content = f.readlines()

    content = [x.replace("\n", '') for x in content]
    counter = sum(list(map(verify_line, content)))

    print(counter)


if __name__ == "__main__":
    main()