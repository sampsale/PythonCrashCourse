import math
animals = ['dog', 'cat', 'horse', 'cow', 'sheep', 'donkey','parrot']


print(f'First three items on this list are: {animals[0:3]}')
print(f'Three items from the middle on this list are: {animals[math.floor(len(animals)/2-1):math.floor(len(animals)/2+2)]}')
print(f'Last three items on this list are: {animals[-3:]}')