class Card1:
    def __init__(self, winning, numbers) -> None:
        self.winning = set(winning)
        self.numbers = numbers

    def points(self):
        found = {}
        power = 0
        for number in self.numbers:
            if number in self.winning:
                found[number] = found.get(number, 0) + 1
        for winner in found:
            power += found[winner]
        if found != {}:
            points = 2 ** (power - 1)
        else:
            points = 0
        return points


def part1(input: str) -> str:
    lines = input.split("\n")
    lines.pop()
    cards = []
    for line in lines:
        values = line.split(":")[1].split("|")
        winning = [int(win) for win in values[0].split(" ") if win != ""]
        numbers = [int(num) for num in values[1].split(" ") if num != ""]
        cards.append(Card1(winning, numbers))
    res = sum([card.points() for card in cards])
    return str(res)


from collections import deque


def calculate_copies(winning: set, numbers: list):
    found = {}
    copies = 0
    for number in numbers:
        if number in winning:
            found[number] = found.get(number, 0) + 1
    for winner in found:
        copies += found[winner]
    return copies


def part2(input: str) -> str:
    lines = input.split("\n")
    lines.pop()
    queue = deque()
    res = 0
    copies = [0] * len(lines)
    for i, line in enumerate(lines):
        values = line.split(":")[1].split("|")
        winning = set([int(win) for win in values[0].split(" ") if win != ""])
        numbers = [int(num) for num in values[1].split(" ") if num != ""]
        copies[i] = calculate_copies(winning, numbers)
        queue.append(i)
    while len(queue) > 0:
        res += 1
        card = queue.popleft()
        for i in range(copies[card]):
            queue.append(card + 1 + i)
    return str(res)


if __name__ == "__main__":
    file = open("./input.txt", "r")
    input = file.read()
    print(f"Part 1 : {part1(input)}, Part 2 : {part2(input)}")
