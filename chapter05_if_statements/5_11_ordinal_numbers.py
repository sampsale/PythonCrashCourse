

numbers = list(range(1, 101))


for number in numbers:
    ## get last digit from number and print st nd rd th accordingly
    last_digit = int(repr(number)[-1])
    if (last_digit == 1):
        print(f'{number}st')
    elif (last_digit == 2):
        print(f'{number}nd')
    elif (last_digit == 3):
        print(f'{number}rd')
    else:
        print(f'{number}th')
