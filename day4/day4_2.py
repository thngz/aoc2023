import re

input = []

with open("input.txt", "r") as f:
    input = f.readlines()

input = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
]

card_counts = [1 for i in range(len(input)+1)]


for line in input:
    card_name, line = line.split(":")
    card_name = int(card_name.strip().split(" ")[-1])

    winning_hand, current_hand = line.split("|")
    winning_numbers = set(re.findall(r"\d+", winning_hand))
    current_hand_numbers = set(re.findall(r"\d+", current_hand))
    intersection = winning_numbers.intersection(current_hand_numbers)

    if len(intersection) > 0:
        cards_to_be_copied = [card_name + i for i in range(len(intersection))]
        card = cards_to_be_copied[0]
        current = card_counts[card]
        print(current)
        print(cards_to_be_copied)
        print(card_counts)
        for i in range(len(intersection)):
            card_counts[card + i + 1] += current

print(sum(card_counts)-1)
