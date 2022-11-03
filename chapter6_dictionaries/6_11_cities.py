cities = {
    'helsinki': {
        'country': 'finland',
        'population': 600_000,
        'fact': 'Capital of Finland'
    }, 'new york': {
        'country': 'USA',
        'population': 10_000_000,
        'fact': 'Largest city in the US'
    }, 'kerava': {
        'country': 'finland',
        'population': 20_000,
        'fact': "It's irrelevant"
    }
}

for city, info in cities.items():
    print(f"\tCity: {city.title()}")
    for key, data in info.items():
        ## if string, add period
        if (isinstance(data, str)):
            print(f"\t\t{key.title()}: {data}.")
        ## if int, separate number by commas
        else: 
            print(f"\t\t{key.title()}: {data:,}")
        
