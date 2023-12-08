def type_of_hand(hand):
    card_occ = [hand.count(card) for card in hand]
    if 5 in card_occ:
        return 6
    if 4 in card_occ:
        return 5
    if 3 in card_occ:
        if 2 in card_occ:
            return 4
        return 3
    if card_occ.count(2) == 4:
        return 2
    if 2 in card_occ:
        return 1
    return 0

values = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}    

hands = []
for line in open("input.txt"):
    hand, bid = line.split()
    hands.append((hand, int(bid)))
hands.sort(key = lambda sort_hand: (type_of_hand(sort_hand[0]), [values.get(char)  for char in sort_hand[0]]), reverse=False)
print(hands)
sum_p1 = 0
for rank, (hand, bid) in enumerate(hands):
    sum_p1 += (rank + 1) * bid
print(sum_p1)

