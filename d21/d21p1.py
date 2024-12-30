with open("input.txt", "r") as file:
    grid = file.read().strip().splitlines()

height = len(grid)
width = len(grid[0])

start = (0, 0)

for row in range(height):
    for col in range(width):
        if grid[row][col] == "S":
            start = (row, col)

def bfs():
    queue = [(start, 0)]
    possible = set()
    visited = set()
    while queue:
        current, steps = queue.pop(0)
        if (current, steps) in visited:
            continue
        visited.add((current, steps))
        if steps == 64:
            possible.add(current)
        x, y = current
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < height and 0 <= new_y < width and grid[new_x][new_y] != "#" and steps < 64:
                queue.append(((new_x, new_y), steps + 1))
    return possible

print(len(bfs()))
