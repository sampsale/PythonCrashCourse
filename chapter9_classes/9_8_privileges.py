
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
    def __init__(self, first_name, last_name, email, country):
        super().__init__(first_name, last_name, email, country)
        self.priviliges = Priviliges(['can delete post', 'can add post', 'can ban user', 'can mute users'])


class Priviliges:
    def __init__(self, priviliges):
        self.priviliges = priviliges

    def print_priviliges(self):
        print(f"\tThe admin has the following priviliges: ")
        for privilige in self.priviliges:
            print(f"\t\t{privilige.title()}")


# instances of classes
user1 = User('sampsa', 'leikas', 'sampsa@leikas.com', 'finland')
user2 = User('john', last_name='doe',
             email='john@doe.com', country='United States')
user3 = User('jane', 'doe', 'jane@doe.com', 'united kingdom')
user4 = Admin('admin', 'admin', 'no email', 'classified')

# calling class methods
user4.priviliges.print_priviliges()
