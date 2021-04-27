# Madeleine Nightengale-Luhan
# CSCI 102 - Section A
# Week 12 - Utility using Git and Incremental Development
# References: No one
# Time: 50 minutes

# load_file function
def load_file(file_name):
    with open(file_name) as file:
        file_read = file.read()
        for line in file_read:
            lines = line.strip()
    return lines
# update_string funcntion
def update_string(some_string_1, some_string_2, index):
    some_string_1 = []
    for var in range(len(some_string_1)):
        some_string_1[index] = some_string_2
        print('OUTPUT', end = '')
        for var in range(len(some_string_1)):
            print(some_string_1[var], end = '')
# find_word_count function
def find_word_count(my_list, search_word):
    num = 0
    for find in my_list:
        word = mylist.split('')
        for found in word:
            if search_word == found:
                num += 1
    return num

    

