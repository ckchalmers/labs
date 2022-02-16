import sys
from collections import Counter

"""Count words in file."""
def count_words(filename):
    text = open(filename)
    text = text.read()
    text = text.replace("\n", " ").strip()
    words = text.split(" ")
    words = [word.strip(",.\n.?").lower() for word in words]

    word_count = Counter(words)

    #result = sorted(word_count.items())
    #print (result)

    #for line in text:
        #words = line.split(" ")
        #print(type(words))
        #words = [word.strip(".,?") for word in words]
        #for word in words:
            #print(type(word))
            #word = word.strip(",.\n.?").lower()
            #word_count[word] = word_count.get(word, 0) + 1
    for key, value in sorted(word_count.items(), key = lambda x: (-x[1], x[0])):
        print("{} {}".format(key, value))

file_name = sys.argv[1]
count_words(file_name)

