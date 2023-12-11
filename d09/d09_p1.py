def extrapolate(num_line):
    all_zero = True
    for num in num_line:
        if num == 0:
            all_zero = True
        else:
            all_zero = False
            break
    if all_zero:
        return 0

    next_line_nums = [y - x for x, y in zip(num_line, num_line[1:])]
    difference = extrapolate(next_line_nums)
    return num_line[-1] + difference
sum_p1 = 0

for line in open("input.txt"):
    nums = list(map(int, line.split()))
    sum_p1 += extrapolate(nums)
print(sum_p1)
