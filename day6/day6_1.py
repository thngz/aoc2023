import re
input = []

with open("input.txt", "r") as f:
    input = f.readlines()

# input = ["Time:      7  15   30", "Distance:  9  40  200"]

times = [int(num) for num in re.findall(r"\d+", input[0])]
distances = [int(num) for num in re.findall(r"\d+", input[1])]

# print(times, distances)
result = 1
for i in range(len(times)):
    time = times[i]
    distance_to_beat = distances[i]

    over_record_times = [
        time - j
        for j in range(1, time - 1)
        if (time - j) * j > distance_to_beat
    ]
    result *= len(over_record_times)
print(result)
