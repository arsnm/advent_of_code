digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def part1(input: str) -> str:
    sum = 0
    for line in input.split("\n"):
        first_digit, last_digit = "", ""
        for char in line:
            if char.isdigit():
                if first_digit == "":
                    first_digit = char
                last_digit = char
        if (first_digit, last_digit) != ("", ""):
            sum += int(first_digit + last_digit)
    return str(sum)


def part2(input: str) -> str:
    sum = 0
    for line in input.split("\n"):
        first_digit, last_digit = -1, -1
        for i, char in enumerate(line):
            if char.isdigit():
                if first_digit == -1:
                    first_digit = int(char)
                last_digit = int(char)
            else:
                for j in range(3, 6):
                    if i + j <= len(line) and line[i : i + j] in digits:
                        digit = digits[line[i : i + j]]
                        if first_digit == -1:
                            first_digit = digit
                        last_digit = digit
        if (first_digit, last_digit) != (-1, -1):
            number = first_digit * 10 + last_digit
            print(number)
            sum += first_digit * 10 + last_digit
    return str(sum)


if __name__ == "__main__":
    file = open("./input.txt", "r")
    input = file.read()
    print(f"Part 1 : {part1(input)}, Part 2 : {part2(input)}")
