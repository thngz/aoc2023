import re

input = []

with open("input.txt", "r") as f:
    input = f.readlines()

# input = [
#     "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
#     "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
#     "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
#     "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
#     "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
# ]

games = []

for game_line in input:
    game_name, game_results = game_line.split(":")
    game_name = int(game_name.split(" ")[1])
    color_matches = re.finditer(r"(\d+ blue)|(\d+ red)|(\d+ green)", game_results)

    invalid_game = False

    for match in color_matches:
        blue_match = match.group(1)
        red_match = match.group(2)
        green_match = match.group(3)

        if not invalid_game:
            if blue_match:
                blues = int(blue_match.split(" ")[0])
                invalid_game = blues > 14
            if red_match:
                reds = int(red_match.split(" ")[0])
                invalid_game = reds > 12
            if green_match:
                greens = int(green_match.split(" ")[0])
                invalid_game = greens > 13

    if not invalid_game:
        games.append(game_name)

print(sum([game_id for game_id in games]))
