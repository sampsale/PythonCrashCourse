import random

# possible items
possible_items = (65, 45, 15, 13, 12, 6,
                  55, 42, 37, 2, 'a', 'f', 'r', 'z', 'y')

# my ballot
my_ballot = (45, 'a', 'f', 6)

# list for winning items
winning = []

print("\n\tLottery starts now!")
counter = 0

# roll until I win 
while len(winning) < 4:
    counter += 1
    selected = random.choice(possible_items)
    if selected not in my_ballot:
        selected = random.choice(possible_items)
        winning.clear()
    elif selected not in winning:
        winning.append(selected)


print(f"\tIt took {counter} tries for ticket 45, a, f, 6 to win!")