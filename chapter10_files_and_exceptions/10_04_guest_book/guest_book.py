
filename = 'guest_book.txt'

with open(filename, 'w') as text_file:
    guest = input('Write a guest name (Type "quit" to quit): ')
    # write guest in text file with new line until 'quit' is inputed 
    while guest != 'quit':
        text_file.write(f"{guest}")
        text_file.write(f"\n")
        guest = input('Write a guest name (Type "quit" to quit): ')
