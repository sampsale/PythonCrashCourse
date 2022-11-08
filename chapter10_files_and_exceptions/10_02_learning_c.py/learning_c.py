text_file = 'learning_python.txt'

# reading an entire file, but replacing 'Python' with 'C'
print("\n")
with open(text_file) as text:
    contents = text.read()
print(contents.replace('Python', 'C'))

# reading line by line, but replacing 'Python' with 'C'
print("\n")
with open(text_file) as text:
    for line in text:
        print(line.strip().replace('Python', 'C'))

# making a list of lines, but replacing 'Python' with 'C'
print("\n")
with open(text_file) as text:
    lines = text.readlines()

for line in lines:
    print(line.strip().replace('Python', 'C'))