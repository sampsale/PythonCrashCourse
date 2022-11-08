
import json
filename = 'favorite_number.json'

favorite_number = input('What is your favorite number? ')

#store favorite number
try: 
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
except:
    print('Something went wrong')