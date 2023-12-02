sum_p1 = 0
sum_p2 = 0
game_index = 1
for line in open("input.txt", "r"):
    game = line.strip().split(": ")[1].split("; ")
    invalid = False
    lowest  = {"red": 0, "green": 0, "blue": 0}
    for subgame in game:
        amounts  = {"red": 0, "green": 0, "blue": 0}
        for current_color in subgame.split(", "):            
            color_count, color_name = current_color.split()
            amounts[color_name] = int(color_count)
        for color_element in lowest:
            lowest[color_element] = max(lowest[color_element], amounts[color_element])
        if amounts["red"] > 12 or amounts["green"] > 13 or amounts["blue"] > 14:
            invalid = True
    if not invalid:
        sum_p1 += game_index
    game_index += 1
    sum_p2 += lowest["red"] * lowest["green"] * lowest["blue"]
print(sum_p1)
print(sum_p2)


            
            
