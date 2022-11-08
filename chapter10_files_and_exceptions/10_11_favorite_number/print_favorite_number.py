import json
filename = 'favorite_number.json'

#print favorite number if stored
with open(filename, 'r') as f:
    number = json.load(f)
    print(f"I know your favorite number, it's {number}")