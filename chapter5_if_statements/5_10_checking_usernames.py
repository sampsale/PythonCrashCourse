current_users = ['admin', 'guest', 'Joe', 'idi', 'ann']
new_users = ['lisa', 'mary', 'john', 'joe', 'barack']


for user in new_users:
    if user.lower() in [user.lower() for user in current_users]:
        print('You need to enter another username! Already in use.')
    else:
        print('Username available!')