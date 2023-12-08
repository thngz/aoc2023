import re
input = []

with open("input.txt", "r") as f:
    input = f.readlines()

# input = ["Time:      7  15   30", "Distance:  9  40  200"]

time = int("".join(re.findall(r"\d+", input[0])))
distance_to_beat = int("".join(re.findall(r"\d+", input[1])))

result = 1
over_record_times = [
    time - j
    for j in range(1, time - 1)
    if (time - j) * j > distance_to_beat
]

print(len(over_record_times))
