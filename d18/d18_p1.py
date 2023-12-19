directions = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
visited = {(0, 0)}
border = [(0, 0)]
for line in open("input.txt"):
    direction, steps, color = line.split()
    d_row, d_col = directions[direction]
    steps = int(steps)    
    for i in range(steps):
        row, col = border[-1]
        border.append((row + d_row, col + d_col))
        visited.add((row + d_row, col + d_col))

def bfs_flood(visited):
    def get_neighbors(x, y):
        return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    start = (1, 1)
    queue = [start]
    visited.add(start)

    while queue:
        x, y = queue.pop(0)
        for nx, ny in get_neighbors(x, y):
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
bfs_flood(visited)
print(len(visited))

