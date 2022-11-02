cities = ['Vantaa', 'Helsinki', 'Espoo', 'Turku', 'Tampere', 'Oulu']
print(cities)
cities.sort()
print(cities)
cities.sort(reverse=True)
print(cities)
cities = ['Vantaa', 'Helsinki', 'Espoo', 'Turku', 'Tampere', 'Oulu']
print(sorted(cities))
print(sorted(cities, reverse=True))

cities.remove('Vantaa')
print(f'Vantaa removed {cities}')
cities.pop()
print(f'Last city removed {cities}')
del cities[0]
print(f'First city removed {cities}')
cities.insert(0, 'Kuopio')
print(f'Added Kuopio at first slot {cities}')
cities.append('Jyväskylä')
print(f'Added Jyväskylä at last slot {cities}')
print(f'Print last city: {cities[-1]}')