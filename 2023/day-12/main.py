from itertools import permutations


def valid(record, info):
    count = 0
    on_streak = False
    streak_counted = 0
    valid = False
    for char in record:
        if char == "#":
            count += 1
            if not on_streak:
                on_streak = True
        else:
            if on_streak:
                on_streak = False
                valid = valid and count == info[streak_counted]
                streak_counted += 1
    return valid


def part1(input: str) -> str:
    res = 0
    lines = input.strip().split("\n")
    records, infos = [], []
    for line in lines:
        data = line.split()
        records.append(list(data[0]))
        infos.append([int(x) for x in data[1].split(",")])
    for i in range(len(records)):
        number_broken = sum(infos[i])
        index_unknown = [k for k in range(len(records[i])) if records[i][k] == "?"]
        possible_changes = permutations(index_unknown)
        for change  
    return str(res)


def part2(input: str) -> str:
    res = 0
    lines = input.strip().split("\n")
    return str(res)


if __name__ == "__main__":
    file = open("./input.txt", "r")
    input = file.read()
    print(f"Part 1 : {part1(input)}")
    print(f"Part 2 : {part2(input)}")
