favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

people_to_poll = ['jen', 'sampsa', 'sarah', 'jacob', 'joe']

for person in people_to_poll:
    if (person in favorite_languages):
        print(f'Thanks for taking the poll, {person.title()}!')
    if (person not in favorite_languages):
        print(f'You should take the poll, {person.title()}!')