from collections import deque


def part1(input: str) -> str:
    res = 0
    lines = input.strip().split("\n")
    start = -1, -1
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "S":
                start = (i, j)
    visited = {start}
    q = deque([start])
    while len(q) > 0:
        i, j = q.popleft()
        char = lines[i][j]
        if (
            i > 0
            and char in "S|JL"
            and lines[i - 1][j] in "|7F"
            and (i - 1, j) not in visited
        ):
            visited.add((i - 1, j))
            q.append((i - 1, j))
        if (
            i < len(lines) - 1
            and char in "S|7F"
            and lines[i + 1][j] in "|JL"
            and (i + 1, j) not in visited
        ):
            visited.add((i + 1, j))
            q.append((i + 1, j))
        if (
            j > 0
            and char in "S-J7"
            and lines[i][j - 1] in "-LF"
            and (i, j - 1) not in visited
        ):
            visited.add((i, j - 1))
            q.append((i, j - 1))
        if (
            j < len(lines[i]) - 1
            and char in "S-LF"
            and lines[i][j + 1] in "-J7"
            and (i, j + 1) not in visited
        ):
            visited.add((i, j + 1))
            q.append((i, j + 1))
    res = len(visited) // 2
    return str(res)


def part2(input: str) -> str:
    res = 0
    lines = input.strip().split("\n")
    start = -1, -1
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "S":
                start = (i, j)
    pipes_loop = {start}
    q = deque([start])
    while len(q) > 0:
        i, j = q.popleft()
        char = lines[i][j]
        if (
            i > 0
            and char in "S|JL"
            and lines[i - 1][j] in "|7F"
            and (i - 1, j) not in pipes_loop
        ):
            pipes_loop.add((i - 1, j))
            q.append((i - 1, j))
        if (
            i < len(lines) - 1
            and char in "S|7F"
            and lines[i + 1][j] in "|JL"
            and (i + 1, j) not in pipes_loop
        ):
            pipes_loop.add((i + 1, j))
            q.append((i + 1, j))
        if (
            j > 0
            and char in "S-J7"
            and lines[i][j - 1] in "-LF"
            and (i, j - 1) not in pipes_loop
        ):
            pipes_loop.add((i, j - 1))
            q.append((i, j - 1))
        if (
            j < len(lines[i]) - 1
            and char in "S-LF"
            and lines[i][j + 1] in "-J7"
            and (i, j + 1) not in pipes_loop
        ):
            pipes_loop.add((i, j + 1))
            q.append((i, j + 1))
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if (i, j) not in pipes_loop:
                count_crossing_border = 0
                for k in range(i):
                    if (k, j) in pipes_loop:
                        count_crossing_border += lines[k][j] in "-7J"
                if count_crossing_border % 2 == 1:
                    res += 1
    return str(res)


if __name__ == "__main__":
    file = open("./input.txt", "r")
    input = file.read()
    print(f"Part 1 : {part1(input)}")
    print(f"Part 2 : {part2(input)}")
