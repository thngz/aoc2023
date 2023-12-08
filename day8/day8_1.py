import re

input = []

with open("input.txt", "r") as f:
    for line in f:
        input.append(line.strip())

# input = [
#     "RL",
#     "AAA = (BBB, CCC)",
#     "BBB = (DDD, EEE)",
#     "CCC = (ZZZ, GGG)",
#     "DDD = (DDD, DDD)",
#     "EEE = (EEE, EEE)",
#     "GGG = (GGG, GGG)",
#     "ZZZ = (ZZZ, ZZZ)",
# ]

# input = ["LLR", "AAA = (BBB, BBB)", "BBB = (AAA, ZZZ)", "ZZZ = (ZZZ, ZZZ)"]
directions = [1 if letter == "R" else 0 for letter in input[0]]
m = {}
print(input[2:])
for line in input[2:]:
    line = line.strip()
    if not line:
        continue
    node, locations = line.split(" = ")
    locations = tuple(re.findall(r"\w+", locations))
    m[node] = locations


start, end = "AAA", "ZZZ"
current = m[start]

counter = 0
pointer = 0
direction = directions[0]

while start != end:
    start = current[direction]
    current = m[start]
    counter += 1
    pointer += 1
    pointer %= len(directions)
    direction = directions[pointer]

print(counter)
# print(map)
