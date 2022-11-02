animal = "dog"
print(f'Animal is: "{animal}"')
print('\nIs animal "dog"? I predict True')
print('dog'== animal)
print('\nIs animal "Dog"? I predict False')
print('Dog'==animal)
print('\nIs animal "Dog" to title? I predict True')
print('Dog'==animal.title())
print('\nIs animal "DOG" to to all caps? I predict True')
print('DOG'==animal.upper())

number = 666
print(f'\nNumber is {number}')
print('\nIs number higher than 665? I predict True')
print(number>665)
print('\nIs number lower than 666? I predict False')
print(number<666)
print('\nIs number lower OR EQUAL to 666? I predict True')
print(number<=666)
print('\nIs number lower than 667 and even? I predict True')
print(number < 667 and number % 2 == 0)

visited_countries = ['India', 'Sweden', 'Estonia', 'Spain']
print('\nI have visited: \n')
for country in visited_countries:
    print(country)

print('\nHave I visited "India"? I predict True')
print('India' in visited_countries)

print('\nHave I visited "Japan"? I predict False')
print('Japan' in visited_countries)

print('\nHave I NOT visited "Japan"? I predict True')
print('Japan' not in visited_countries)

print('\nHave I visited "sweden"? I predict False')
print('sweden' in visited_countries)

