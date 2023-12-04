def neighbour_symbols(digit, env):
    start_i, start_j = digit[0]
    length = digit[1]
    valid = False
    for j in range(start_j - 1, start_j + length + 1):
        for i in range(start_i - 1, start_i + 2):
            if 0 <= i < len(env) and 0 <= j < len(env[i]):
                symbol = env[i][j]
                valid += (not symbol.isdigit()) and symbol != "."
    return valid


def interprete(digit, env) -> int:
    number = int("".join(env[digit[0][0]][digit[0][1] + j] for j in range(digit[1])))
    if number == 117:
        print("found", digit)
        print(neighbour_symbols(digit, env))
    return number


def part1(input: str) -> str:
    lines = input.split("\n")
    res = 0
    engine_schematic = [
        [lines[i][j] for j in range(len(lines[i]))] for i in range(len(lines))
    ]
    engine_schematic.pop()
    digits = []
    for i in range(len(engine_schematic)):
        length_current_digit = 0
        start_digit = (-1, -1)
        for j in range(len(engine_schematic[i])):
            if engine_schematic[i][j].isdigit():
                if length_current_digit == 0:
                    start_digit = (i, j)
                length_current_digit += 1
                if j == len(engine_schematic[i]):
                    digit = start_digit, length_current_digit
                    number = interprete(digit, engine_schematic)
                    digits.append((start_digit, length_current_digit))
                    length_current_digit = 0
            elif length_current_digit != 0:
                digit = start_digit, length_current_digit
                number = interprete(digit, engine_schematic)
                digits.append((start_digit, length_current_digit))
                length_current_digit = 0
    for digit in digits:
        if neighbour_symbols(digit, engine_schematic):
            number = interprete(digit, engine_schematic)
            res += number
    return str(res)


def part2(input: str) -> str:
    return ""


if __name__ == "__main__":
    file = open("./input.txt", "r")
    input = file.read()
    print(f"Part 1 : {part1(input)}, Part 2 : {part2(input)}")
