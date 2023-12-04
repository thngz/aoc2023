import re

input = []
with open("input.txt", "r") as f:
    input = f.readlines()
# input = [
#     "........$....743..../.......-................+........................*990..................343......#.....*...............*....684.........",
#     "......651.....................644....................887.812........187.................783........749...928.291...........131...........293"
# ]
# 554887
row_length = len(input)
column_length = len(input[0])

total_sum = 0


def has_specials(x, y):
    for dx, dy in (
        (-1, -1),
        (0, -1),
        (1, -1),
        (-1, 0),
        (1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
    ):
        current_row = x + dx
        current_column = y + dy
        if 0 <= current_row < row_length and 0 <= current_column <= column_length:
            current_item = input[current_row][current_column]
            if current_item not in set('.0123456789') and current_item != "\n":
                return True
    return False


num = ""
for i in range(len(input)):
    input[i] = input[i].strip()
    print(input[i])
    for j in range(len(input[0])):
        current = input[i][j]
        if current.isdigit():
            num += current
        else:
            if num:
                for k in reversed(range(j)):
                    if input[i][k].isdigit() and has_specials(i, k):
                        # print(input[i][k], num)
                        total_sum += int(num)

                        break
                    elif not input[i][k].isdigit():
                        break

            num = ""
    if num:
        for k in reversed(range((j))):
            if input[i][k].isdigit() and has_specials(i, k):
                print(input[i][k], num)
                total_sum += int(num)
                break
            elif not input[i][k].isdigit():
                break
        num = ""


print(total_sum)
