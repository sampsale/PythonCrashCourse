# creating restaurant class
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        # attributes
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    # methods

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} serves {self.cuisine_type} food! It has served {self.number_served} customers.")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open!")

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, increment):
        self.number_served += increment


# creating instance of restaurant class, giving name and cuisine type as arguments
king_kebab = Restaurant('king kebab', 'kebab')

# calling restaurant methods
king_kebab.set_number_served(5500)

king_kebab.increment_number_served(65)
king_kebab.describe_restaurant()
king_kebab.open_restaurant()
