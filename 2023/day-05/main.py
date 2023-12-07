def part1(input: str) -> str:
    seeds, *blocks = input.split("\n\n")

    seeds = list(map(int, seeds.split(":")[1].split()))

    for block in blocks:
        ranges = []
        for line in block.splitlines()[1:]:
            ranges.append((list(map(int, line.split()))))
        destination = []
        for seed in seeds:
            for dest, src, len in ranges:
                if src <= seed < src + len:
                    destination.append(dest + seed - src)
                    break
            else:
                destination.append(seed)
        seeds = destination
    res = min(seeds)
    return str(res)


def part2(input: str) -> str:
    input, *blocks = input.split("\n\n")

    input = input.split(":")[1].split()
    seeds = []
    for i in range(0, len(input), 2):
        seeds.append((int(input[i]), int(input[i]) + int(input[i + 1])))
    for block in blocks:
        ranges = []
        for line in block.splitlines()[1:]:
            ranges.append((list(map(int, line.split()))))
        destination = []
        while seeds:
            start, end = seeds.pop()
            for dest, src, length in ranges:
                os = max(start, src)  # overlap_start
                oe = min(src + length, end)  # overlap_end
                if os < oe:
                    destination.append((os - src + dest, oe - src + dest))
                    if os > start:
                        seeds.append((start, os))
                    if end > oe:
                        seeds.append((oe, end))
                    break
            else:
                destination.append((start, end))
        seeds = destination
    res = min(seeds)[0]
    return str(res)


if __name__ == "__main__":
    file = open("./input.txt", "r")
    input = file.read()
    print(f"Part 1 : {part1(input)}, Part 2 : {part2(input)}")
