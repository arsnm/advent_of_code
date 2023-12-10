types = {
    (5,): 7,
    (4, 1): 6,
    (3, 2): 5,
    (3, 1, 1): 4,
    (2, 2, 1): 3,
    (2, 1, 1, 1): 2,
    (1, 1, 1, 1, 1): 1,
}
card_rank_part1 = {
    "A": "14",
    "K": "13",
    "Q": "12",
    "J": "11",
    "T": "10",
    "9": "09",
    "8": "08",
    "7": "07",
    "6": "06",
    "5": "05",
    "4": "04",
    "3": "03",
    "2": "02",
}
card_rank_part2 = {
    "A": "13",
    "K": "12",
    "Q": "11",
    "T": "10",
    "9": "09",
    "8": "08",
    "7": "07",
    "6": "06",
    "5": "05",
    "4": "04",
    "3": "03",
    "2": "02",
    "J": "01",
}


def rank_part1(hand) -> int:
    cards = {}
    for card in hand:
        cards[card] = cards.get(card, 0) + 1
    type = tuple(sorted(cards.values(), reverse=True))
    type = types[type]
    res = str(type)
    for card in hand:
        res += card_rank_part1[card]
    return int(res)


def part1(input: str) -> str:
    res = 0
    raw_hands = [line for line in input.split("\n") if line]
    hands = []
    for hand in raw_hands:
        hands.append(tuple(hand.split()))
    sorted_hands = sorted(hands, key=lambda x: rank_part1(x[0]))
    for i in range(len(sorted_hands)):
        res += (i + 1) * int(sorted_hands[i][1])
    return str(res)


def rank_part2(hand) -> int:
    cards = {}
    joker = 0
    for card in hand:
        if card == "J":
            joker += 1
        else:
            cards[card] = cards.get(card, 0) + 1
    type = sorted(cards.values(), reverse=True)
    if joker == 5:
        type = types[(5,)]
    elif len(type) > 0:
        type[0] += joker
        type = types[tuple(type)]
    res = str(type)
    for card in hand:
        res += card_rank_part2[card]
    return int(res)


def part2(input: str) -> str:
    res = 0
    raw_hands = [line for line in input.split("\n") if line]
    hands = []
    for hand in raw_hands:
        hands.append(tuple(hand.split()))
    sorted_hands = sorted(hands, key=lambda x: rank_part2(x[0]))
    for i in range(len(sorted_hands)):
        res += (i + 1) * int(sorted_hands[i][1])
    return str(res)


if __name__ == "__main__":
    file = open("./input.txt", "r")
    input = file.read()
    print(f"Part 1 : {part1(input)}, Part 2 : {part2(input)}")
