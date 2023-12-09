def part1(input: str) -> str:
    input = input.split("\n")[:-1]
    time, distance = input
    times = tuple(map(int, time.split(":")[1].split()))
    distances = tuple(map(int, distance.split(":")[1].split()))

    res = 1

    for time, distance in zip(times, distances):
        speed = -1
        beaten_record = [0] * (time + 1)
        for ms in range(time + 1):
            speed += 1
            parcoured = (time - ms) * speed
            beaten_record[ms] = int(parcoured > distance)
        res *= sum(beaten_record)
    return str(res)


def part2(input: str) -> str:
    input = input.split("\n")[:-1]
    time, distance = input
    time = int("".join(tuple(time.split(":")[1].split())))
    distance = int("".join(tuple(distance.split(":")[1].split())))

    res = 0

    speed = -1
    for ms in range(time):
        speed += 1
        parcoured = (time - ms) * speed
        res += int(parcoured > distance)
    return str(res)


if __name__ == "__main__":
    file = open("./input.txt", "r")
    input = file.read()
    print(f"Part 1 : {part1(input)}, Part 2 : {part2(input)}")
