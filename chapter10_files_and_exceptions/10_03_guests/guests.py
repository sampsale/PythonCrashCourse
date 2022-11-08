
filename= 'guests.txt'

with open(filename, 'w') as text_file:
    guest =input('Write a guest name: ')
    text_file.write(guest)