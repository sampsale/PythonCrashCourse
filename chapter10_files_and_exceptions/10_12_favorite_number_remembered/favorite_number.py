import json
filename = 'favorite_number.json'


#if favorite number stored, print it. otherwise ask for favorite username
try: 
    with open(filename, 'r') as f:
        number = json.load(f)
        print(f"I know your favorite number, it's {number}")
except:
    with open(filename, 'w') as f:
        favorite_number = input('What is your favorite number? ')
        json.dump(favorite_number, f)

