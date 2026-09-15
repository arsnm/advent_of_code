from math import gcd


def part1(input: str) -> str:
    res = 0
    input = [line for line in input.split("\n") if line]
    path = input[0]
    maps = input[1:]
    dict_maps = {}
    for map in maps:
        map = map.replace(" ", "")
        map = map.split("=")
        start = map[0]
        left = map[1].split(",")[0][1:]
        right = map[1].split(",")[1][:-1]
        dict_maps[start] = (left, right)
    i = 0
    current = "AAA"
    while current != "ZZZ":
        if path[i] == "L":
            current = dict_maps[current][0]
        elif path[i] == "R":
            current = dict_maps[current][1]
        i = (i + 1) % len(path)
        res += 1
    return str(res)


def cycle(start, dict_maps, path):
    i = 0
    current = start
    cycle_len = -1
    while cycle_len == -1:
        if path[i % len(path)] == "L":
            pos = 0
        else:
            pos = 1
        current = dict_maps[current][pos]
        i += 1
        if current[-1] == "Z":
            cycle_len = i
    return cycle_len


def part2(input: str) -> str:
    res = 1
    input = [line for line in input.split("\n") if line]
    path = input[0]
    maps = input[1:]
    dict_maps = {}
    starts = []
    for map in maps:
        map = map.replace(" ", "")
        map = map.split("=")
        start = map[0]
        if start[-1] == "A":
            starts.append(start)
        left = map[1].split(",")[0][1:]
        right = map[1].split(",")[1][:-1]
        dict_maps[start] = (left, right)
    cycles = []
    for start in starts:
        length = cycle(start, dict_maps, path)
        cycles.append(length)
    for i in range(len(cycles)):
        res = int(res * cycles[i] / gcd(res, cycles[i]))
    return str(res)


if __name__ == "__main__":
    file = open("./input.txt", "r")
    input = file.read()
    print(f"Part 1 : {part1(input)}")
    print(f"Part 2 : {part2(input)}")
