rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'keravanjoki': 'finland'
}

for river, country in rivers.items():
    print(f'\t{river.title()} runs through {country.title()}.')

print('\nFollowing rivers have been mentioned:')
for river in rivers:
    print(f'\t{river.title()}')

print('\nFollowing countries have been mentioned:')
for country in rivers.values():
    print(f'\t{country.title()}')
