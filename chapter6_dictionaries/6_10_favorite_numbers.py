favorite_numbers = {
    'john': [60, 15],
    'david': [666, 420],
    'joe': [69],
    'sampsa': ['none'],
    'idas': [1, 2, 3, 4, 5, 6]
}

for person, numbers in favorite_numbers.items():
    print(f"\t\n{person.title()}'s favorite numbers are: ")
    for number in numbers: 
        print(f"\t\t{number}")