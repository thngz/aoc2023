input = []

with open("input.txt", "r") as f:
    for line in f:
        input.append(line.strip())

# input = [
#     "0 3 6 9 12 15",
#     "1 3 6 10 15 21",
#     "10 13 16 21 30 45",
# ]


def get_diffs(nums):
    return [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]


result = 0
for line in input:
    nums = [int(num) for num in line.split(" ")]
    diffs = get_diffs(nums)
    diffs_history = []

    while any(diffs):
        diffs_history.append(diffs)
        diffs = get_diffs(diffs)

    diffs_history.append(diffs)
    diffs_history.reverse()

    diffs_history.append(nums)
    diffs_history[0].append(0)

    for i, diff in enumerate(diffs_history[1:]):
        diff.append(diffs_history[i][-1] + diff[-1])

    result += diffs_history[-1][-1]
print(result)
