

# creating restaurant class
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        # attributes
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    # methods
    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} serves {self.cuisine_type} food!")
    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open!")

# creating instance of restaurant class, giving name and cuisine type as arguments
king_kebab = Restaurant('king kebab', 'kebab')
liemi = Restaurant('liemi', 'japanese')
makikupla = Restaurant('mäkikupla', 'pizza')

# calling restaurant methods
king_kebab.describe_restaurant()
liemi.describe_restaurant()
makikupla.describe_restaurant()