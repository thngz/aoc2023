import re

lines = []

with open("input.txt", "r") as f:
    lines = f.readlines()

# test_lines = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
sum = 0
for line in lines:
    digits = re.findall(r"\d", line)
    num = digits[0] + digits[-1]
    sum += int(num)
print(sum)
