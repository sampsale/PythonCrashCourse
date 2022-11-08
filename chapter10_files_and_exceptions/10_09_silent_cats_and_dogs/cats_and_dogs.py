

file_names = ['cats.txt', 'dogs.txt']


def read_files(filename):
    try:
        with open(filename) as text_file:
            contents = text_file.readlines()
    # if either file not found, don't print error
    except FileNotFoundError:
        pass
    else: 
        for animal in contents:
            print(f"\t{animal.title().strip()}")


for file in file_names:
    read_files(file)
