
responses = {}

while True:
    print("\n")
    name = input(f"\tWhat is your name? ")
    dream = input(f"\tWhat is your dream vacation destination? ")
    repeat = input(f"\tWould you like to continue polling? If yes, type anything, if no type 'no': ")
    responses[name] = dream
    if repeat.lower() == 'no':
        break
print("\n")
for name, response in responses.items():
    print(f"\t{name.title()} would like to visit {response.title()}")