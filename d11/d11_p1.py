image = open("input.txt").read().splitlines()
empty_rows = [r for r, row in enumerate(image) if all(char == "." for char in row)]
empty_cols = [c for c, col in enumerate(zip(*image)) if all(ch == "." for ch in col)]
galaxies = [(r, c) for r, row in enumerate(image) for c, ch in enumerate(row) if ch == "#"]

sum_p1 = 0
multi = 2

for i, (row1, col1) in enumerate(galaxies):
    for (row2, col2) in galaxies[:i]:
        min_row = min(row1, row2)
        max_row = max(row1, row2)
        min_col = min(col1, col2)
        max_col = max(col1, col2)
        for row in range(min_row, max_row):
            sum_p1 += multi if row in empty_rows else 1
        for col in range(min_col, max_col):
            sum_p1 += multi if col in empty_cols else 1
print(sum_p1)