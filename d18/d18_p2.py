from collections import deque
directions = {"3": (-1, 0), "1": (1, 0), "2": (0, -1), "0": (0, 1)}
border_verticies = [(0, 0)]
tiles_in_border = 0
for line in open("input.txt"):
    _, _, hexa = line.split()
    hexa = hexa.strip("()")[1:]
    d_row, d_col = directions[hexa[-1]]
    steps = int(hexa[:-1], 16)
    tiles_in_border += steps
    row, col = border_verticies[-1]
    border_verticies.append((row + d_row * steps, col + d_col * steps))

area = sum(border_verticies[i][0] * (border_verticies[(i + 1) % len(border_verticies)][1] - border_verticies[(i - 1)][1]) for i in range(len(border_verticies)))
gauss = abs(area) // 2
picks = gauss - tiles_in_border // 2 + 1
print(picks + tiles_in_border)


        



