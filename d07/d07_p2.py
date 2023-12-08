def type_of_hand(hand):
    joker_count = 0
    if "J" in hand:
        joker_count = hand.count("J")
        hand = hand.replace("J", "")
    if joker_count == 5:
        return 6
    card_occ = []
    cards = set()
    for card in hand:
        if card not in cards:
            card_occ.append(hand.count(card))
            cards.add(card)
    card_occ.sort(reverse = True)
    card_occ[0] += joker_count
    if 5 in card_occ:
        return 6
    if 4 in card_occ:
        return 5
    if 3 in card_occ:
        if 2 in card_occ:
            return 4
        return 3
    if card_occ.count(2) == 2:
        return 2
    if 2 in card_occ:
        return 1
    return 0

values = {"A": 14, "K": 13, "Q": 12, "J": 1, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}    

hands = []
for line in open("input.txt"):
    hand, bid = line.split()
    hands.append((hand, int(bid)))
hands.sort(key = lambda sort_hand: (type_of_hand(sort_hand[0]), [values.get(char)  for char in sort_hand[0]]), reverse=False)
sum_p1 = 0
for rank, (hand, bid) in enumerate(hands):
    sum_p1 += (rank + 1) * bid
print(sum_p1)

