import string

def huffman(text):
    frequencies_dict = get_frequencies(text)
    #make binary tree
    # make file

def get_frequencies(text):
    frequencies_dict = {}
    letters = string.printable
    for letter in letters:
        frequencies_dict[letter] = 0
    for letter in text:
        frequencies_dict[letter] += 1
    return frequencies_dict
