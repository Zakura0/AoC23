lines = open("input.txt",  "r").read().split()
coords_set = set()
for i_row, row in enumerate(lines):
    for i_col, char in enumerate(row):
        if char.isdigit() or char == ".":
            continue
        for current_row in [i_row - 1, i_row, i_row + 1]:
            for current_col in [i_col - 1, i_col, i_col + 1]:
                if current_row < 0 or current_row >= len(lines) or current_col < 0 or current_col >= len(lines[current_row]):
                    continue
                if not lines[current_row][current_col].isdigit():
                    continue
                while current_col > 0 and lines[current_row][current_col - 1].isdigit():
                    current_col -= 1
                coords_set.add((current_row, current_col))
number_list = []
for row, col in coords_set:
    number = ""
    while col < len(lines[row]) and lines[row][col].isdigit():
        number += lines[row][col]
        col += 1
    number_list.append(int(number))
print(sum(number_list))

sum_p2 = 0
for i_row, row in enumerate(lines):
    for i_col, char in enumerate(row):
        if char != "*":
            continue
        coords_set_per_star = set()

        for current_row in [i_row - 1, i_row, i_row + 1]:
            for current_col in [i_col - 1, i_col, i_col + 1]:
                if current_row < 0 or current_row >= len(lines) or current_col < 0 or current_col >= len(lines[current_row]):
                    continue
                if not lines[current_row][current_col].isdigit():
                    continue
                while current_col > 0 and lines[current_row][current_col - 1].isdigit():
                    current_col -= 1
                coords_set_per_star.add((current_row, current_col))
        if len(coords_set_per_star) != 2:
            continue

        number_list_p2 = []
        for set_row, set_col in coords_set_per_star:
            number = ""
            while set_col < len(lines[set_row]) and lines[set_row][set_col].isdigit():
                number += lines[set_row][set_col]
                set_col += 1
            number_list_p2.append(int(number))
        sum_p2 += number_list_p2[0] * number_list_p2[1]
print(sum_p2)

