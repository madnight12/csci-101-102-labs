# Madeleine Nightengale-Luhan
# CSCI 102 - Section A
# Week 9A - Word Search
# References: Audrey Richard for help on import random word 
# Time: 30 minutes

import random

f = open('dictionary.txt', 'r')
list_lines = f.readlines()

word_list = []
max_len = 0

print('Enter the length of the words to find:')
length = int(input('LENGTH> '))

for words in list_lines:
    if len(words) == (length + 1):
        word_list.append(words)
        max_len += 1
print('The number of words with length', length, 'is:')
print('OUTPUT', max_len)
if len(word_list) != 0:
    random.seed(len(word_list))
    print(f"Here is one random word with length {length}:")
    print('OUTPUT', random.choice(word_list))
else:
    print('There are no words of length', length, 'in the dictionary.')
    print('OUTPUT None')
