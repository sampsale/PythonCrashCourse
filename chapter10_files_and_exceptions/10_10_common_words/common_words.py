
from collections import Counter

files = ['seitseman_veljesta.txt', 'kalevala.txt']



# split the words in the text into an array
def split_words(file):
    try:
        with open(file, encoding='utf-8') as book:
            contents = book.read()

    except:
        print(f'\n\tSomething went wrong with reading {file} ')
    else:
        words = contents.lower().split()
        most_common_word(words, file)



# get the most common word
def most_common_word(words, file):
    c = Counter(words)

    # count how many times 'ja' appears in text (and in finnish)
    ja_appears = c['ja']
    print(f"\n\tMost common words in {file}")

    # print the most used words
    for index, word in enumerate(c.most_common(3)):
        print(f"\t\t{index+1}th used word: {word[0]}")
        print(f"\t\tCount: {word[1]}")

    print(f"\t\t'ja' appears in {file} {ja_appears} times")

# iterate through text files
for book in files:
    split_words(book)
