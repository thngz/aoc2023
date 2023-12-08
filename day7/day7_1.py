from enum import Enum

input = []
# with open("input.txt", "r") as f:
#     input = f.readlines()
input = [
    "32T3K 765",
    "T55J5 684",
    "KK677 28",
    "KTJJT 220",
    "QQQJA 483",
#     # "22222 25",
#     # "2AAAA 26",
#     # "33332 27",
#     # "77888 28",
#     # "77788 29",
#     # "KTTAA 27",
#     # "AAAAA 26",
#     # "AAAA4 27",
#     # "TTTAA 26",
]
# input = [
#     "2345A 2",
#     "2345J 5",
#     "J345A 3",
#     "32T3K 7",
#     "T55J5 17",
#     "KK677 11",
#     "KTJJT 23",
#     "QQQJA 19",
#     "JJJJJ 29",
#     "JAAAA 37",
#     "AAAAJ 43",
#     "AAAAA 53",
#     "2AAAA 13",
#     "2JJJJ 41",
#     "JJJJ2 31",
# ]
# 250112823 too low
CardValues = Enum(
    "CardValues",
    ["1", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"],
)

HandRanks = Enum(
    "HandRanks", ["HI", "ONE_P", "TWO_P", "THREE_OK", "FH", "FOUR_OK", "FIVE_OK"]
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
        return f"{self.rank} {self.bid}"


hands = []
for line in input:
    cards, bid = line.split(" ")

    cards = [CardValues[card].value for card in cards]
    duplicates = [card for card in cards if cards.count(card) > 1]
#
    length = len(duplicates)
    rank = HandRanks["HI"]

    if length == 5:
        if all(duplicates[0] == duplicate for duplicate in duplicates):
            rank = HandRanks["FIVE_OK"]
        else:
            rank = HandRanks["FH"]
    elif length == 4:
        if len(set(duplicates)) == 1:
            rank = HandRanks["FOUR_OK"]
        else:
            rank = HandRanks["TWO_P"]
    elif length == 3:
        rank = HandRanks["THREE_OK"]
    elif length == 2:
        rank = HandRanks["ONE_P"]
    hand = Hand(rank, int(bid), cards)
    hands.append(hand)
s = sorted(hands)
# print(s)
result = sum([s[i].bid * (i + 1) for i in range(len(s))])
print(result)
