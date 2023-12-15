grid = tuple(open("input.txt").read().splitlines())

def cycle():
    global grid
    for i in range(4):
        grid = tuple(map("".join, zip(*grid)))
        grid = tuple("#".join(["".join(sorted(tuple(group), reverse=True)) for group in row.split("#")]) for row in grid)
        grid = tuple(row[::-1] for row in grid)

seen_configs = {grid}
array_grid = [grid]

iteration = 0
while True:
    iteration += 1
    cycle()
    if grid in seen_configs:
        break
    seen_configs.add(grid)
    array_grid.append(grid)    
first_of_cycle = array_grid.index(grid)
offset = iteration - first_of_cycle
grid = array_grid[(1000000000 - first_of_cycle) % offset + first_of_cycle]
print(sum(row.count("O") * (len(grid) - r) for r, row in enumerate(grid)))