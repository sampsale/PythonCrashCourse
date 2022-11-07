person1 = {
    'first_name': 'raili',
    'last_name': 'löyttyniemi',
    'age': 61,
    'city': 'helsinki'
}
person2 = {
    'first_name': 'sampsa',
    'last_name': 'leikas',
    'age': 27,
    'city': 'helsinki'
}

person3 = {
    'first_name': 'juha',
    'last_name': 'leikas',
    'age': 61,
    'city': 'helsinki'
}

persons = [person1, person2, person3]


for index, person in enumerate(persons):
    print(f'\tPerson {index+1} is {person["first_name"].title()} {person["last_name"].title()}. He/she is {person["age"]} years old and lives in {person["city"].title()}.')