result = 0
index = 0
cards = {}
for line in (open("input.txt", "r")):
    if index not in cards:
        cards[index] = 1
    card = line.strip().split(": ")[1].strip()
    winnings, numbers = card.split(" | ")
    winnings = list(map(int, winnings.split()))
    numbers = list(map(int, numbers.split()))
    wins = 0
    for element in winnings:
        if (element in numbers):
            wins += 1
    if wins > 0:
        result += 2 ** (wins - 1)
    for next_card in range(index + 1, index + wins + 1):
        cards[next_card] = cards.get(next_card, 1) + cards[index]
    index += 1
print(result)
print(sum(cards.values()))


