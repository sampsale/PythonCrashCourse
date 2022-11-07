# creating restaurant class
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        # attributes
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    # methods

    def describe_restaurant(self):
        print(f"\t{self.restaurant_name.title()} serves {self.cuisine_type} food!")

    def open_restaurant(self):
        print(f"\t{self.restaurant_name.title()} is open!")

# creating ice cream stand class


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def print_flavors(self):
        print(
            f"\tThe Ice Cream stand {self.restaurant_name.title()} has the following flawors:")
        for flavor in self.flavors:
            print(f"\t\t{flavor.title()}")


# creating instance of restaurant child class icecreamstand
peten_jaatelo = IceCreamStand('peten jäätelo', 'ice cream', ['vanilla', 'chocolate', 'liquorice', 'pear', 'salmiac'])
peten_jaatelo.describe_restaurant()
peten_jaatelo.open_restaurant()
peten_jaatelo.print_flavors()