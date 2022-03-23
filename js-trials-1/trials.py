"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)

def get_all_evens(nums):
    even_nums = []
    for num in nums:
        if num %2 == 0:
            even_nums.append(num)
    return even_nums

def get_odd_indices(items):
    result = []
    for item in items:
        if item %2 != 0:
            result.append(item.index())
    return result

def print_as_numbered_list(items): 
    count = 1
    for item in items:
        print(f"{count}. {item}")
        count +=1

def get_range(start, stop):
        nums = []

    for i in range(start, stop, 1):
        nums.append(i)

    return nums

def censor_vowels(word):
    chars = []

    for letter in word:
        if letter in ['a', 'e', 'i', 'o', 'u']:
            chars.append('*')
        else:
            chars.append(letter) 

    return ''.join(chars) 

def snake_to_camel(string):
    camelCase = []
    
    for word in string.split('_'):
        camelCase.append(F"{word[0].upper()}{word[1:]}")

    return ''.join(camelCase)

def longest_word_length(words):
    longest = len(words[0])

    for word in words:
        if len(word) > longest:
            longest = len(word)

    return longest

def truncate(string):
    result = []

    for char in string:
        if len(result) == 0 or char !=result[-1]:
            result.append(char)
        
    return "".join(result)


def has_balanced_parens(string):
    parens = 0

    for char in string:
        if char == '(':
            parens +=1
        elif char == ')':
            parens -= 1

    return parens == 0

def compress(string):
    compressed = []

    curr_char = ""
    char_count = 0
    for char in string:
        if char != curr_char:
            compressed.append(curr_char)
            if char_count >1:
                compressed.append(str(char_count))
            curr_char = char
            char_count = 0
        else:
            char_count +=1

    compressed.append(curr_char)
    if (char_count >1):
        compressed.append(str(char_count))

    return ''.join(compressed)