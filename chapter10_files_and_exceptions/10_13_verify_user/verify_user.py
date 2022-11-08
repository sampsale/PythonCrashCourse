import json

#ask for username
def get_new_username():
    username = input('\tWhat is your username? ')
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"\tWe'll remember you when you come back, {username}!")

# greet the user and ask if his/her username is the one stored, if not ask for new username. if no username stored, ask for username
def greet_user():
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        get_new_username()
    else:
        right_username = input(f"\tIs your username {username} (y/n)? ")
        if right_username.lower() == 'y':
            print(f"\tWelcome back, {username}!")
        elif right_username.lower() == 'n':
            get_new_username()
        else:
            print('\tPlease type "y" or "n"')
            greet_user()

greet_user()
