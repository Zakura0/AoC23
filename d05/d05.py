data, *maps = open("input.txt").read().split("\n\n")

data = list(map(int, data.split(":")[1].split()))

seeds = []

for i in range(0, len(data), 2):
    seeds.append((data[i], data[i] + data[i + 1] - 1))
for m in maps:
    r = []
    for line in m.splitlines()[1:]:
        r.append(list(map(int, line.split())))
    results = []
    for lower,upper in seeds:
        for d_start, r_start, r_length in r:
            offset = d_start - r_start
            #1122 und 2211
            if lower > r_start + r_length - 1 or upper < r_start:
                continue
            #1212
            if lower <= r_start and upper <= r_start + r_length + 1:
                results.append((r_start + offset, upper + offset))
                seeds.append((lower, r_start - 1))
                break
            #2121
            elif r_start <= lower and r_start + r_length - 1 <= upper:
                results.append((lower + offset, (r_start + r_length - 1) + offset))
                seeds.append((r_start + r_length, upper))
                break
            #1221
            elif lower <= r_start and r_start + r_length - 1 <= upper:
                results.append((r_start + offset, (r_start + r_length - 1) + offset))
                seeds.append((lower, r_start - 1))
                seeds.append((r_start + r_length, upper))
                break
            #2112
            elif r_start <= lower and upper <= r_start + r_length - 1:
                results.append((lower + offset, upper + offset))
                break

        else:
            results.append((lower,upper))
    seeds = results
print(min(seeds)[0])


        
