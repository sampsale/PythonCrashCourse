

pet1 = {
    'name': 'masi',
    'animal': 'dog',
    'owner': 'raili'
}
pet2 = {
    'name': 'zili',
    'animal': 'dog',
    'owner': 'ronja'
}
pet3 = {
    'name': 'ykke',
    'animal': 'cat',
    'owner': 'harri'
}
pet4 = {
    'name': 'horsen',
    'animal': 'horse',
    'owner': 'forsen'
}

pets = [pet1, pet2, pet3, pet4]


for pet in pets:
    print(f'\t{pet["name"].title()} is a {pet["animal"]} and is owned by {pet["owner"].title()}.')