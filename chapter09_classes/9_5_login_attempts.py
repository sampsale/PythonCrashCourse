
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


# instances of classes
user1 = User('sampsa', 'leikas', 'sampsa@leikas.com', 'finland')
user2 = User('john', last_name='doe',
             email='john@doe.com', country='United States')
user3 = User('jane', 'doe', 'jane@doe.com', 'united kingdom')

# calling class methods
user1.greet_user()
user2.greet_user()
user3.greet_user()

user1.increment_loging_attempts()
user1.increment_loging_attempts()
user1.increment_loging_attempts()
user1.increment_loging_attempts()
user1.print_attempts()
user1.describe_user()
user1.reset_loging_attempts()

user1.print_attempts()
user2.describe_user()
user3.describe_user()
