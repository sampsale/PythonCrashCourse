

age = input('\tWhat is your age? ')
age = int(age)


while True:
    if age < 3:
        print('\tFree entry!')
        break
    elif age >= 3 and age <= 12:
        print('\tEntry is 10€')
        break
    elif age > 12:
        print('\tEntry is 15€')
        break