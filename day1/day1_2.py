import re

lines = []


with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        lines.append(line)
result = 0

word_to_digit = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}
print(sum([int(word_to_digit.get(re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)[0],
                                 re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)[0]) +
                                 word_to_digit.get(re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)[-1],
                                 re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)[-1])) for line in lines]))
# print(sum([int((wtd := {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}).get(res := (re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line))[0], res[0]) + wtd.get(res[-1], res[-1])) for line in lines]))
#
# print(sum([int(word_to_digit.get(res := (re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line))[0], res[0]) + word_to_digit.get(res[-1], res[-1])) for line in lines]))
# for line in lines:
#     digits = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)
#     result += int(word_to_digit.get(digits[0], digits[0]) + word_to_digit.get(digits[-1], digits[-1]))
#
