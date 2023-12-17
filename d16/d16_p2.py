from collections import deque
grid = open("input.txt").read().splitlines()


def calc_energized(row, col, direc):
    laser = [(row, col, direc)]
    energized = set()
    queue = deque(laser)

    while queue:
        row, col, direc = queue.popleft()

        if direc == "r":
            row += 0
            col += 1
        elif direc == "l":
            row += 0
            col += -1
        elif direc == "u":
            row += -1
            col += 0
        elif direc == "d":
            row += 1
            col += 0
        
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid):
            continue

        char = grid[row][col]
        if char == "."  or (char == "-" and direc in "rl") or (char == "|" and direc in "ud"):
            if (row, col, direc) not in energized:
                energized.add((row, col, direc))
                queue.append((row, col, direc))
        elif char == "/":
            if direc == "r":
                direc = "u"
            elif direc == "l":
                direc = "d"
            elif direc == "u":
                direc = "r"
            elif direc == "d":
                direc = "l"
            if (row, col, direc) not in energized:
                energized.add((row, col, direc))
                queue.append((row, col, direc))
        elif char == "\\":
            if direc == "r":
                direc = "d"
            elif direc == "l":
                direc = "u"
            elif direc == "u":
                direc = "l"
            elif direc == "d":
                direc = "r"
            if (row, col, direc) not in energized:
                energized.add((row, col, direc))
                queue.append((row, col, direc))
        else:
            if direc in "lr" and char == "|":
                if (row, col, "u") not in energized:
                    energized.add((row, col, "u"))
                    queue.append((row, col, "u"))
                if (row, col, "d") not in energized:
                    energized.add((row, col, "d"))                    
                    queue.append((row, col, "d"))
            elif direc in "ud" and char == "-":
                if (row, col, "l") not in energized:
                    energized.add((row, col, "l"))
                    queue.append((row, col, "l"))
                if (row, col, "r") not in energized:
                    energized.add((row, col, "r"))                    
                    queue.append((row, col, "r"))

    energized_single = {(row, col) for (row, col, _) in energized}
    return len(energized_single)

maximum = 0
for row in range(len(grid)):
    maximum = max(maximum, calc_energized(row, -1, "r"))
    maximum = max(maximum, calc_energized(row, len(grid[0]), "l"))

for col in range(len(grid)):
    maximum = max(maximum, calc_energized(-1, col, "d"))
    maximum = max(maximum, calc_energized(len(grid), col, "u"))

print(maximum)



