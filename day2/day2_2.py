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


class Game:
    def __init__(self, id, bc, rc, gc):
        self.id = id
        self.bc = bc  # blue count
        self.rc = rc  # red count
        self.gc = gc  # green count

games = []

for game_line in input:
    game_name, game_results = game_line.split(":")
    game_name = int(game_name.split(" ")[1])
    color_matches = re.finditer(r"(\d+ blue)|(\d+ red)|(\d+ green)", game_results)

    game = Game(game_name, 0, 0, 0)

    for match in color_matches:
        blue_match = match.group(1)
        red_match = match.group(2)
        green_match = match.group(3)
        
        blues = int(blue_match.split(" ")[0])
        if blue_match:
            blues = int(blue_match.split(" ")[0])
            game.bc = max(game.bc, blues)
        if red_match:
            reds = int(red_match.split(" ")[0])
            game.rc = max(game.rc, reds)
        if green_match:
            greens = int(green_match.split(" ")[0])
            game.gc = max(game.gc, greens)

    games.append(game)

print(sum([game.bc * game.rc * game.gc for game in games]))
