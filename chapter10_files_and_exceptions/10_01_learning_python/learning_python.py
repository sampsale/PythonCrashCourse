
text_file = 'learning_python.txt'

# reading an entire file
print("\n")
with open(text_file) as text:
    contents = text.read()
print(contents)

# reading line by line
print("\n")
with open(text_file) as text:
    for line in text:
        print(line.strip())

# making a list of lines
print("\n")
with open(text_file) as text:
    lines = text.readlines()

for line in lines:
    print(line.strip())