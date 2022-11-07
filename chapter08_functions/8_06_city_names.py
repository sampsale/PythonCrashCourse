


def city_names(city, country):
   return (f"\t\n{city.title()}, {country.title()}")


helsinki = city_names(city='helsinki', country='finland')
print(helsinki)

new_york = city_names('new york', 'usa')
print(new_york)

paris = city_names('paris', country='france')
print(paris)