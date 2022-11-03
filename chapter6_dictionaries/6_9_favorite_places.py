favorite_places = {
    'david': ['los angeles', 'london', 'new york'],
    'boris' : ['moscow', 'kiev','st petersburg'],
    'jani': ['korso', 'koivukylä'],
    'sampsa': ['home']
}


for person, places in favorite_places.items():
    print(f"\n{person.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")
