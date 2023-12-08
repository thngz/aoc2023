import re
from multiprocessing import Process, Manager, Pool, Lock

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




visited = set()
processes = []

maps = []
seeds = []
map_start = False
map_name = ""
d = [0 for i in range(100)]
# pool = Pool()
ranges = []
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
        line_nums = re.findall(r"\d+", line)
        dst, src, length = int(line_nums[0]), int(
            line_nums[1]), int(line_nums[2])
        to = src + length
        offset = dst - src
        for i in range(0, len(seeds) - 1, 2):
            range_start = seeds[i]
            range_end = seeds[i] + seeds[i + 1]
            ranges.append((range_start + offset, range_end + offset))
            break
            # for j in range(range_start, range_end):
            #     seed = j
            #     temp = seed
            #     if d[seed] == 0:
            #         d[seed] = seed
            #     else:
            #         temp = d[seed]
            #     if temp in range(src, to) and seed not in visited:
            #         temp = d[seed] + offset
            #         d[seed] = temp
            #         visited.add(seed)

    elif not line:
        visited = set()
        map_start = False
        map_name = ""
for process in processes:
    process.join()
print(ranges)
# print(d)
# print(min([digit for digit in d if digit != 0]))
