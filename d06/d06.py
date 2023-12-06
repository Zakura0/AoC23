temp = []
for line in open("input.txt").read().splitlines():
    temp.append(list(map(int, line.split(":")[1].split())))
times, records = temp
races = []
for time, record in zip(times, records):
    races.append((time, record))
mult = 1
for time, record in races:
    won = 0
    for hold in range(time):
        if hold * (time - hold) > record:
            won += 1
    mult *= won
print(mult)

actual_time = ""
actual_record = ""
for time in times:
    actual_time += str(time)
for record in records:
    actual_record += str(record)
actual_time = int(actual_time)
actual_record = int(actual_record)
won_p2 = 0
for hold in range(actual_time):
    if hold * (actual_time - hold) > actual_record:
        won_p2 += 1
print(won_p2)

