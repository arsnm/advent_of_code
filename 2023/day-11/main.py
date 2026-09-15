def part1(input: str) -> str:
    res = 0
    lines = input.strip().split("\n")
    lines = [list(line) for line in lines]
    vert_exp = []
    hori_exp = []
    for i in range(len(lines)):
        if all(lines[i][j] == "." for j in range(len(lines[i]))):
            vert_exp.append(i + len(vert_exp))
    for j in range(len(lines[0])):
        if all(lines[i][j] == "." for i in range(len(lines))):
            hori_exp.append(j + len(hori_exp))
    for i in vert_exp:
        lines.insert(i, lines[i])
    for j in hori_exp:
        for i in range(len(lines)):
            lines[i].insert(j, ".")
    galaxies = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "#":
                galaxies.append((i, j))
    while len(galaxies) > 1:
        ig, jg = galaxies.pop()
        for io, jo in galaxies:
            path_length = abs(ig - io) + abs(jg - jo)
            res += path_length
    return str(res)


VOID_LENGTH = 1000000


def part2(input: str) -> str:
    res = 0
    lines = input.strip().split("\n")
    lines = [list(line) for line in lines]
    vert_exp = []
    hori_exp = []
    for i in range(len(lines)):
        if all(lines[i][j] == "." for j in range(len(lines[i]))):
            vert_exp.append(i)
    for j in range(len(lines[0])):
        if all(lines[i][j] == "." for i in range(len(lines))):
            hori_exp.append(j)
    galaxies = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "#":
                galaxies.append((i, j))
    while len(galaxies) > 1:
        ig, jg = galaxies.pop()
        for io, jo in galaxies:
            voids = 0
            for v in vert_exp:
                if ig < v < io or io < v < ig:
                    voids += 1
            for h in hori_exp:
                if jg < h < jo or jo < h < jg:
                    voids += 1
            path_length = abs(ig - io) + abs(jg - jo) + voids * (VOID_LENGTH - 1)
            res += path_length
    return str(res)


if __name__ == "__main__":
    file = open("./input.txt", "r")
    input = file.read()
    print(f"Part 1 : {part1(input)}")
    print(f"Part 2 : {part2(input)}")
