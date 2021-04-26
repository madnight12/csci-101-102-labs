# Madeleine Nightengale-Luhan
# CSCI 101 - Section A
# Python Lab 9
# References: John Henke on the second choice if statement
# Time: 50 minutes 

import random

f = open('Declaration_of_independence.txt', 'r')
data = f.read().lower()
print('Would you like to print the number of times a specific word appears OR print the number of words of a specific length? (1 or 2)')
choice = int(input('CHOICE> '))

if choice == 1:
    print('Enter a word:')
    word = input('WORD> ')
    occurences = data.count(word.lower())
    print('The number of times', word, 'appears in the document is:')
    print('OUTPUT', occurences)
if choice == 2:
    print('Enter a length:')
    length = int(input('LENGTH> '))
    # Replace all newline characters with spaces.
    data = data.replace('\n', ' ')
    valid_letters = 'abcdefghijklmnopqrstuvwxyz '
    filtered_data = ''
    # Iterate over each character
    for character in data:
        # If it's in the string of valid characters
        if character in valid_letters:
            # add it onto the new string.
            filtered_data += character
    words = filtered_data.split()
    length_words = []
    for word in words:
        if len(word) == length:
            length_words.append(word)
    print('The number of words in the document with length', length, 'is:')
    print('OUTPUT', len(length_words))
    if len(length_words) == 0:
        print('No example random word of this length exists.')
        print('OUTPUT error')
    else:
        random.seed(len(length_words))
        print('One example random word of this length is:')
        print('OUTPUT', random.choice(length_words))
    
