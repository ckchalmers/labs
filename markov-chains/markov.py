"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_path, file_path2):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    #file = open(file_path)
    text1 = open(file_path)
    text2 = open(file_path2)
    text1 = text1.read().replace('\n', ' ').strip()
    text2 = text2.read().replace('\n', ' ').strip()

    # return 'Contents of your file as one long string'
    return text1+text2


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    
    word_list = text_string.split(' ')
    
    # for word in word_list[:-1]:
        #bigram = (word, word_list[word_list.index(word)+1])
        # if word != word_list[-2]:
            #following_word = word_list[word_list.index(word)+2]
        #else:
    for position in range(len(word_list)-(n)):
        #bigram = (word_list[position], word_list[position+1])
        n_gram = tuple((word_list[position+i] for i in range(n)))
        if position < len(word_list)-n:
            following_word = word_list[position+n]
        if n_gram in chains:
            chains[n_gram].append(following_word)
        if n_gram not in chains:
            chains[n_gram] = [following_word]          

    return chains


def make_text(chains, n):
    """Return text from chains."""
  
    words = []

    #get a random tuple from the list of chains keys to be your starting bigram
    starting_grams = [key for key in chains.keys() if key[0]==key[0].title() and key[0]!="--"]
    random_selection = choice(starting_grams)
    for i in random_selection:
        words.append(i)
    #choose a word from the values in chains for that key & add it to words
    next_word = choice(chains[random_selection])
    words.append(next_word)
    #continue lookup up the last two words in words and using them to choose the next
        
    while not words[-1].endswith(('.','?','!')):
        #bigram = (words[-2], words[-1])
        n_gram = tuple((words[-n:]))
        if n_gram in chains:
            next_word = choice(chains[n_gram])
            words.append(next_word)
        else:
            break
        #count += 1   
    #return the words from the list as a string
    
    return ' '.join(words)


# Call the functions
n = int(sys.argv[1])
input_path = sys.argv[2]
input_path2 = sys.argv[3]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path, input_path2)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains, n)

print(random_text)
