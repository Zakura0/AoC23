from collections import deque
grid = open("input.txt").read().splitlines()
s_row = s_col = 0
for r, row in enumerate(grid):
    for c, char in enumerate(row):
        if char == "S":
            s_row = r
            s_col = c

def bfs_flood(steps):
    
    def get_neighbors(x, y):
            return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        
    reachable = set()
    seen = {(s_row, s_col)}
    queue = deque([(s_row, s_col, steps)])
    while queue:
        row, col, steps = queue.popleft()
        if steps % 2 == 0:
            reachable.add((row, col))                       
        if steps == 0:
            continue         
        for next_row, next_col in get_neighbors(row, col):
            if next_row < 0 or next_row >= len(grid) or next_col < 0 or next_col >= len(grid[0]):
                continue
            if grid[next_row][next_col] == "#" or (next_row, next_col) in seen:
                continue
            seen.add((next_row, next_col))
            queue.append((next_row, next_col, steps - 1))
    return len(reachable)
print(bfs_flood(64))

            
