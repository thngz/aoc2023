import re

input = []
with open("input.txt", "r") as f:
    for line in f:
        input.append(line.strip())


input = [
    "seeds: 79 14 55 13",
    "         ",
    "seed-to-soil map:",
    "50 98 2",
    "52 50 48",
    "        ",
    "soil-to-fertilizer map:",
    "0 15 37",
    "37 52 2",
    "39 0 15",
    "        ",
    "fertilizer-to-water map:",
    "49 53 8",
    "0 11 42",
    "42 0 7",
    "57 7 4",
    "       ",
    "water-to-light map:",
    "88 18 7",
    "18 25 70",
    "         ",
    "light-to-temperature map:",
    "45 77 23",
    "81 45 19",
    "68 64 13",
    "         ",
    "temperature-to-humidity map:",
    "0 69 1",
    "1 0 69",
    "       ",
    "humidity-to-location map:",
    "60 56 37",
    "56 93 4",
]

maps = []
seeds = []
map_start = False
map_name = ""
locations = []

for line in input:
    line = line.strip()
    map_name_match = re.search(r"\w+-\w+-\w+ map", line)

    line_nums = re.findall(r"\d+", line)
    if "seeds:" in line:
        seeds = [int(num) for num in line_nums]
    elif map_name_match:
        map_name = map_name_match.group()
        map_start = True
        continue
    if line and map_start:
        line_nums = [int(num) for num in re.findall(r"\d+", line)] + [map_name]
        maps.append(line_nums)

    elif not line:
        visited = set()
        map_start = False
        map_name = ""


def get_location(seed):
    visited_mappings = set()
    for dst, src, length, map_name in maps:
        to = src + length
        offset = dst - src
        if seed in range(src, to) and map_name not in visited_mappings:
            visited_mappings.add(map_name)
            seed += offset
    return seed


for seed in seeds:
    for i in range(0, len(seeds) - 1, 2):
        range_start = seeds[i]
        range_end = seeds[i] + seeds[i + 1] - 1

        for j in range(range_start, range_end):
            locations.append(get_location(j))

print(min(locations))
