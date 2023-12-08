import re
import math

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

# input = [
#     "LR",
#     "11A = (11B, XXX)",
#     "11B = (XXX, 11Z)",
#     "11Z = (11B, XXX)",
#     "22A = (22B, XXX)",
#     "22B = (22C, 22C)",
#     "22C = (22Z, 22Z)",
#     "22Z = (22B, 22B)",
#     "XXX = (XXX, XXX)",
# ]

# input = ["LLR", "AAA = (BBB, BBB)", "BBB = (AAA, ZZZ)", "ZZZ = (ZZZ, ZZZ)"]
directions = [1 if letter == "R" else 0 for letter in input[0]]
m = {}
for line in input[1:]:
    line = line.strip()
    if not line:
        continue
    node, locations = line.split(" = ")
    locations = tuple(re.findall(r"\w+", locations))
    m[node] = locations

nodes_to_advance = [node for node in m.keys() if node.endswith("A")]
end_nodes = [node for node in m.keys() if node.endswith("Z")]

paths = [None for i in range(len(end_nodes))]

for i in range(len(nodes_to_advance)):
    start = nodes_to_advance[i]
    end = end_nodes[i]
    current = m[start]
    pointer = 0
    direction = directions[0]
    current_path = []

    while not start.endswith("Z"):
        start = current[direction]
        current = m[start]

        # print(start, current)
        pointer += 1
        pointer %= len(directions)
        direction = directions[pointer]
        current_path.append(start)
    paths[i] = current_path

lengths = [len(path) for path in paths]
print(math.lcm(*lengths))
