from collections import deque 
import math
pipe_grid = open("input.txt").read().strip().splitlines()
row_s = 0
col_s = 0
s_found = False
for r, row in enumerate(pipe_grid):
    for c, char in enumerate(row):
        if char == "S":
            row_s = r
            col_s = c
            s_found = True
            break
        else:
            continue
    if (s_found):
        break

s = {"|", "-", "J", "L", "7", "F"}

#BFS
seen_pipes = set()
seen_pipes.add((row_s, col_s))
queue = deque([(row_s, col_s)])

while queue:
    curr_row, curr_col = queue.popleft()
    curr_char = pipe_grid[curr_row][curr_col]
    #Up
    if (curr_row - 1, curr_col) not in seen_pipes and 0 < curr_row and curr_char in "|JLS" and pipe_grid[curr_row - 1][curr_col] in "|7F":
        seen_pipes.add((curr_row - 1, curr_col))
        queue.append((curr_row - 1, curr_col))
        if curr_char == "S":
            s &= {"|", "J", "L"}
    #Down
    if (curr_row + 1, curr_col) not in seen_pipes and curr_row < len(pipe_grid) - 1 and curr_char in "|7FS" and pipe_grid[curr_row + 1][curr_col] in "|JL":
        seen_pipes.add((curr_row + 1, curr_col))
        queue.append((curr_row + 1, curr_col))
        if curr_char == "S":
            s &= {"|", "7", "F"}
    #Left
    if (curr_row, curr_col - 1) not in seen_pipes and 0 < curr_col and curr_char in "-J7S" and pipe_grid[curr_row][curr_col - 1] in "-FL":
        seen_pipes.add((curr_row, curr_col - 1))
        queue.append((curr_row, curr_col - 1))
        if curr_char == "S":
            s &= {"-", "J", "7"}
    #Right
    if (curr_row, curr_col + 1) not in seen_pipes and curr_col < len(pipe_grid[curr_row]) - 1 and curr_char in "-FLS" and pipe_grid[curr_row][curr_col + 1] in "-J7":
        seen_pipes.add((curr_row, curr_col + 1))
        queue.append((curr_row, curr_col + 1))
        if curr_char == "S":
            s &= {"-", "F", "L"}

s_symbol = s.pop()
pipe_grid = [row.replace("S", s_symbol) for row in pipe_grid]
for r, row in enumerate(pipe_grid):
    for c, char in enumerate(row):
        if (r, c) not in seen_pipes:
            row = row[:c] + "." + row[c + 1:]
            pipe_grid[r] = row

outside = set()

for r, row in enumerate(pipe_grid):
    inside = False
    for c, char in enumerate(row):
        if char == "|":
            inside = not inside
        elif char == "-":
            continue
        elif char in "LF":
            up = char == "L"
        elif char in "7J":
            if char != ("J" if up else "7"):
                inside = not inside
        elif char == ".":
            pass
        if not inside:
            outside.add((r, c))
            
print(len(pipe_grid) * len(pipe_grid[0]) - len(outside | seen_pipes))

