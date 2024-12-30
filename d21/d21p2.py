from collections import deque

with open("input.txt", "r") as file:
    grid = file.read().strip().splitlines()

height = len(grid)
width = len(grid[0])

start = (0, 0)

for row in range(height):
    for col in range(width):
        if grid[row][col] == "S":
            start = (row, col)

start_row, start_col = start

def bfs(start, steps_amount = 26501365):
    queue = [(start, steps_amount)]
    possible = set()
    visited = set()
    while queue:
        current, steps = queue.pop(0)
        if current in visited:
            continue
        visited.add(current)
        if steps % 2 == 0:
            possible.add(current)
        if steps == 0:
            continue
        x, y = current
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < height and 0 <= new_y < width and grid[new_x][new_y] != "#" and (new_x, new_y) not in visited:
                queue.append(((new_x, new_y), steps - 1))
    return len(possible)

steps = 26501365
assert steps % height == height // 2
grid_width = steps // height - 1
odd_grids = (grid_width // 2 * 2 + 1) ** 2
even_grids = ((grid_width + 1) // 2 * 2) ** 2

odd_points = bfs(start, height * 2 + 1)
even_points = bfs(start, height * 2)

top_corner = bfs((height - 1, start_col), height - 1)
bottom_corner = bfs((0, start_col), height - 1)
left_corner = bfs((start_row, width - 1), height - 1)
right_corner = bfs((start_row, 0), height - 1)

leftover_top_right = bfs((height - 1, 0), height // 2 - 1)
leftover_bottom_right = bfs((0, 0), height // 2 - 1)
leftover_bottom_left = bfs((0, width - 1), height // 2 - 1)
leftover_top_left = bfs((height - 1, width - 1), height // 2 - 1)

large_top_right = bfs((height - 1, 0), height * 3 // 2 - 1)
large_bottom_right = bfs((0, 0), height * 3 // 2 - 1)
large_bottom_left = bfs((0, width - 1), height * 3 // 2 - 1)
large_top_left = bfs((height - 1, width - 1), height * 3 // 2 - 1)

result = odd_grids * odd_points + even_grids * even_points + \
            top_corner + bottom_corner + left_corner + right_corner + \
            (grid_width + 1) * (leftover_top_right + leftover_bottom_right + leftover_bottom_left + leftover_top_left) + \
            grid_width * (large_top_right + large_bottom_right + large_bottom_left + large_top_left)
print(result)





