filename = 'reasons_to_like_programming.txt'

with open(filename, 'a') as text_file:
    reason = input('Why do you like programming? (Type "quit" to quit): ')
    # write guest in text file with new line until 'quit' is inputed 
    while reason != 'quit':
        text_file.write(f"{reason}")
        text_file.write(f"\n")
        reason = input('Why do you like programming? (Type "quit" to quit): ')
