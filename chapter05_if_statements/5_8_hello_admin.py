

usernames = ['admin', 'guest', 'user1','user2','user3']


if usernames:
    for user in usernames:
        if user=='admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f'Hello {user}, thank you for logging in!')
else: 
    print('There is literally no users!')