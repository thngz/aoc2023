from enum import Enum
from collections import Counter

input = []
with open("input.txt", "r") as f:
    input = f.readlines()
# input = [
#     "32T3K 765",
#     "T55J5 684",
#     "KK677 28",
#     "KTJJT 220",
#     "QQQJA 483",
# ]
CardValues = Enum(
    "CardValues",
    ["1", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"],
)

HandRanks = Enum(
    "HandRanks", ["HI", "ONE_P", "TWO_P",
                  "THREE_OK", "FH", "FOUR_OK", "FIVE_OK"]
)


class Hand:
    def __init__(self, rank, bid, cards):
        self.rank = rank
        self.bid = bid
        self.cards = cards

    def __eq__(self, other):
        return self.rank.value == other.rank.value

    def __lt__(self, other):
        if self == other:
            for i in range(len(self.cards)):
                if other.cards[i] > self.cards[i]:
                    return True
                elif self.cards[i] > other.cards[i]:
                    return False
        else:
            return self.rank.value < other.rank.value

    def __repr__(self):
        return f"{self.bid}, {self.cards}"


def get_rank(special_hands):
    rank = HandRanks["HI"]
    if 5 in special_hands:
        rank = HandRanks["FIVE_OK"]
    elif 4 in special_hands:
        rank = HandRanks["FOUR_OK"]
    elif special_hands == [3, 2]:
        rank = HandRanks["FH"]
    elif special_hands == [3, 1, 1]:
        rank = HandRanks["THREE_OK"]
    elif special_hands == [2, 2, 1]:
        rank = HandRanks["TWO_P"]
    elif special_hands == [2, 1, 1, 1]:
        rank = HandRanks["ONE_P"]
    return rank


hands = []
for line in input:
    cards, bid = line.split(" ")

    cards = [CardValues[card].value for card in cards]

    card_counts = Counter(cards)
    special_hands = sorted(card_counts.values(), reverse=True)

    rank = get_rank(special_hands)
    hand = Hand(rank, int(bid), cards)
    hands.append(hand)

s = sorted(hands)
result = sum([hand.bid * (i + 1) for i, hand in enumerate(s)])
print(result)
