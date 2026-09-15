def part1(input: str) -> str:
    res = 0
    lines = input.strip().split("\n")
    for line in lines:
        values = list(map(int, line.split()))
        firsts_of_layers = [values[-1]]
        while values != [0] * len(values):
            values = [values[i + 1] - values[i] for i in range(len(values) - 1)]
            firsts_of_layers.append(values[-1])
        res += sum(firsts_of_layers)
    return str(res)


def part2(input: str) -> str:
    res = 0
    lines = input.strip().split("\n")
    for line in lines:
        values = list(map(int, line.split()))
        firsts_of_layers = [values[0]]
        while values != [0] * len(values):
            values = [values[i] - values[i + 1] for i in range(len(values) - 1)]
            firsts_of_layers.append(values[0])
        res += sum(firsts_of_layers)
    return str(res)


if __name__ == "__main__":
    file = open("./input.txt", "r")
    input = file.read()
    print(f"Part 1 : {part1(input)}")
    print(f"Part 2 : {part2(input)}")
