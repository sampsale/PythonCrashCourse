
from modules import User, Admin

# instances of classes
user1 = User('sampsa', 'leikas', 'sampsa@leikas.com', 'finland')
user2 = User('john', last_name='doe',
             email='john@doe.com', country='United States')
user3 = User('jane', 'doe', 'jane@doe.com', 'united kingdom')
user4 = Admin('admin', 'admin', 'no email', 'classified', [
              'can delete post', 'can add post', 'can ban user', 'can mute users'])

# calling class methods
user4.print_priviliges()
