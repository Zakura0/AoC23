from heapq import heappop, heappush

grid = [list(map(int, line.strip())) for line in open("input.txt")]

seen = set()
#(heat_loss, row, col, direction_row, direction_col, steps)
p_queue = [(0, 0, 0, 0, 0, 0)]

while p_queue:
    h_loss, row, col, direction_row, direction_col, steps = heappop(p_queue)

    if row == len(grid) - 1 and col == len(grid[0]) - 1:
        print(h_loss)
        break

    if (row, col, direction_row, direction_col, steps) in seen:
        continue
    seen.add((row, col, direction_row, direction_col, steps))

    if steps < 3 and (direction_row, direction_col) != (0, 0):
        next_row = row + direction_row
        next_col = col + direction_col        
        if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]):
            heappush(p_queue, (h_loss + grid[next_row][next_col], next_row, next_col, direction_row, direction_col, steps + 1))

    for new_direction_row, new_direction_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if (new_direction_row, new_direction_col) != (direction_row, direction_col) and (new_direction_row, new_direction_col) != (-direction_row, -direction_col):
            next_row = row + new_direction_row
            next_col = col + new_direction_col        
            if 0 <= next_row < len(grid) and 0 <= next_col < len(grid[0]):
                heappush(p_queue, (h_loss + grid[next_row][next_col], next_row, next_col, new_direction_row, new_direction_col, 1))

            

        