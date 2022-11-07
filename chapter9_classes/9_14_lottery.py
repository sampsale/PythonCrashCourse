import random

# possible items
possible_items = (65, 45, 15, 13, 12, 6,
                  55, 42, 37, 2, 'a', 'f', 'r', 'z', 'y')

# list for winning items
winning = []


print("\n\tThe winning numbers or letters are: ")
# roll until winning list has four 
while len(winning) < 4:
    selected = random.choice(possible_items)
    # if selected already in winning list, don't add to list
    while selected not in winning:
        winning.append(selected)
        print(f"\t\t{selected}")
