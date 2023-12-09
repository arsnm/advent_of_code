types = {
    (5): 7,
    (4, 1): 6,
    (3, 2): 5,
    (3, 1, 1): 4,
    (2, 2, 1): 3,
    (2, 1, 1, 1): 2,
    (1, 1, 1, 1, 1): 1,
}
card_rank = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


def rank(hand) -> int:
    cards = {}
    for card in hand:
        cards[card] = cards.get(card, 0) + 1
    type = types[tuple(list(cards.values().sort()))]
    rank = [type] + [card_rank[card] for card in hand]
    return tuple(rank)


def part1(input: str) -> str:
    res = 0
    return str(res)


def part2(input: str) -> str:
    res = 0
    return str(res)


if __name__ == "__main__":
    file = open("./input.txt", "r")
    input = file.read()
    print(f"Part 1 : {part1(input)}, Part 2 : {part2(input)}")
