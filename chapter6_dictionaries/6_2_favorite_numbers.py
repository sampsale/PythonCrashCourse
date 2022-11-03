favorite_numbers = {
    'john': 60,
    'david': 51,
    'joe': 9,
    'sampsa': 12,
    'idas': 666
}

for person in favorite_numbers:
    print(f"\t{person.title()}'s favorite number is {favorite_numbers[person]}")