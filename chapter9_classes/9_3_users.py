from modules import User

# instances of classes
user1 = User('sampsa', 'leikas', 'sampsa@leikas.com', 'finland')
user2 = User('john', last_name='doe',
             email='john@doe.com', country='United States')
user3 = User('jane', 'doe', 'jane@doe.com', 'united kingdom')

# calling class methods
user1.greet_user()
user2.greet_user()
user3.greet_user()

user1.describe_user()
user2.describe_user()
user3.describe_user()
