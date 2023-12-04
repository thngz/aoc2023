input = []
with open("input.txt", "r") as f:
    input = f.readlines()
# input = [
#     "467..114..",
#     "...*......",
#     "..35..633.",
#     "617*......",
#     ".....+.58.",
#     "..592.....",
#     "......755.",
#     "...$.*....",
#     ".664.598..",
#     # ".664.598.*",
#     # "........300",
#     # "..........*",
#     # "........200",
#     # "..........",
# ]
# 554887
# 95338089 TOO HIGH
# 43306530 TOO LOW
row_length = len(input)
column_length = len(input[0])

total_sum = 0


def has_gear(x, y):
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
            if current_item == "*":
                return (current_row, current_column)
    return None


num = ""
nums_near_gears = []
gear_neighbors = 0
d = {}
for i in range(len(input)):
    input[i] = input[i].strip()
    for j in range(len(input[0])):
        current = input[i][j]
        if current.isdigit():
            num += current
        else:
            if num:
                for k in reversed(range(j)):
                    if input[i][k].isdigit():
                        gear_coord = has_gear(i, k)
                        if gear_coord:
                            d[gear_coord] = d.get(gear_coord, []) + [int(num)]
                            break
                    elif not input[i][k].isdigit():
                        break
            num = ""
    if num:
        for k in reversed(range((j))):
            if input[i][k].isdigit():
                gear_coord = has_gear(i, k)
                if gear_coord:

                    d[gear_coord] = d.get(gear_coord, []) + [int(num)]
                    break
            elif not input[i][k].isdigit():
                break
    num = ""
print(sum([gear[0] * gear[1] for gear in d.values() if len(gear) == 2]))
print(total_sum)
