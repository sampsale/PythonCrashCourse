
# EXERCISE 9_3
class User:
    def __init__(self, first_name, last_name, email, country):
        # attributes
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email
        self.country = country
    # methods

    def greet_user(self):
        print(f"\tHello, {self.first_name} {self.last_name}!\n")

    def describe_user(self):
        print(f"\tUser name: {self.first_name} {self.last_name}")
        print(f"\tUser email: {self.email}")
        print(f"\tUser country:: {self.country.title()}\n")

# EXERCISE 9_10
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

# EXERCISE 9_11
class User:
    def __init__(self, first_name, last_name, email, country):
        # attributes
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email
        self.country = country
        self.login_attempts = 0
    # methods
    def greet_user(self):
        print(f"\tHello, {self.first_name} {self.last_name}!\n")

    def describe_user(self):
        print(f"\tUser name: {self.first_name} {self.last_name}")
        print(f"\tUser email: {self.email}")
        print(f"\tUser country: {self.country.title()}\n")

    def print_attempts(self):
        print(f"\tUser has {self.login_attempts} login attempts.")

    def increment_loging_attempts(self):
        self.login_attempts += 1

    def reset_loging_attempts(self):
        print(f"\tResetting {self.first_name}'s login attempts!")
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name, email, country, priviliges):
        super().__init__(first_name, last_name, email, country)
        self.priviliges = priviliges

    def print_priviliges(self):
        print(f"\tThe admin has the following priviliges: ")
        for privilige in self.priviliges:
            print(f"\t\t{privilige.title()}")
