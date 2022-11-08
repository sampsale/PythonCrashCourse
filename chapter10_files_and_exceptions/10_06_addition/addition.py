

# ask for two numbers to add together. if something else is inputed; throw error 
while True:
    print("\tGive me two numbers and I'll add them together")
    print("\tType 'q' to quit")
    number_one = input("\tNumber one: ")
    if number_one == 'q':
        break
    number_two = input("\tNumber two: ")
    if number_two == 'q':
        break
    try:
        result = int(number_one) + int(number_two)
    except ValueError:
        print("\nPlease just input numbers")
    else: 
        print(f"\nResult: {result}")