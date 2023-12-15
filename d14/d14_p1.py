grid = open("input.txt").read().splitlines()
grid_tilted = list(map("".join, zip(*grid)))
grid_sorted = []
for row in grid_tilted:
    grid_sorted_row = "#".join("".join(sorted(list(split), reverse=True)) for split in row.split("#"))
    grid_sorted.append(grid_sorted_row)
sorted_grid_tilted = list(map("".join, zip(*grid_sorted)))
print(sum(row.count("O") * (len(sorted_grid_tilted) - r) for r, row in enumerate(sorted_grid_tilted)))