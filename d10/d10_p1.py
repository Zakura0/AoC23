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
    #Down
    if (curr_row + 1, curr_col) not in seen_pipes and curr_row < len(pipe_grid) - 1 and curr_char in "|7FS" and pipe_grid[curr_row + 1][curr_col] in "|JL":
        seen_pipes.add((curr_row + 1, curr_col))
        queue.append((curr_row + 1, curr_col))
    #Left
    if (curr_row, curr_col - 1) not in seen_pipes and 0 < curr_col and curr_char in "-J7S" and pipe_grid[curr_row][curr_col - 1] in "-FL":
        seen_pipes.add((curr_row, curr_col - 1))
        queue.append((curr_row, curr_col - 1))
    #Right
    if (curr_row, curr_col + 1) not in seen_pipes and curr_col < len(pipe_grid[curr_row]) - 1 and curr_char in "-FLS" and pipe_grid[curr_row][curr_col + 1] in "-J7":
        seen_pipes.add((curr_row, curr_col + 1))
        queue.append((curr_row, curr_col + 1))
print(math.floor(len(seen_pipes) / 2))
