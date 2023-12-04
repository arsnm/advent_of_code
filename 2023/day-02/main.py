def part1(input: str) -> str:
    max_colors = [12, 13, 14]
    result = 0
    colors = {"red": 0, "green": 1, "blue": 2}
    for game in filter(None, input.split("\n")):
        game = game.removeprefix("Game ")
        valid = True
        i, game = game.split(":")
        rounds = game.replace(" ", "").split(";")
        for round in rounds:
            cubes = round.split(",")
            cube_colors = [0] * len(colors)
            for cube in cubes:
                digit = "".join([c for c in cube if c.isdigit()])
                for color in colors.keys():
                    if cube.find(color) != -1:
                        cube_colors[colors[color]] = int(digit)
            valid = valid and all(
                cube_colors[i] <= max_colors[i] for i in range(len(max_colors))
            )
        if valid:
            result += int(i)
    return str(result)


def power(numbers: list) -> int:
    res = 1
    for number in numbers:
        res *= number
    return res


def part2(input: str) -> str:
    result = 0
    colors = {"red": 0, "green": 1, "blue": 2}
    for game in filter(None, input.split("\n")):
        game = game.removeprefix("Game ")
        _, game = game.split(":")
        rounds = game.replace(" ", "").split(";")
        minimum_number = [0] * len(colors)
        for round in rounds:
            cubes = round.split(",")
            cube_colors = [0] * len(colors)
            for cube in cubes:
                digit = "".join([c for c in cube if c.isdigit()])
                for color in colors.keys():
                    if cube.find(color) != -1:
                        cube_colors[colors[color]] = int(digit)
            minimum_number = [
                max(minimum_number[i], cube_colors[i]) for i in range(len(colors))
            ]
        result += power(minimum_number)
    return str(result)


if __name__ == "__main__":
    file = open("./input.txt", "r")
    input = file.read()
    part1(input)
    print(f"Part 1 : {part1(input)}, Part 2 : {part2(input)}")
