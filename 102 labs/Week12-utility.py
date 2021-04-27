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
#score_finder function
def score_finder(player_names, player_scores, player_to_find):
    for i in range(len(player_names)):
        if (player_names[i].lower() == player_to_find.lower()):
            print(f"OUTPUT {player_names[i]} got a score of {player_scores[i]}")
            return
    print('OUTPUT player not found')
#union function
def union(list_a, list_b):
    array = []
    for character in list_a:
        for word in list_b:
            if character not in str(word):
                array.append(word)
        for words in list_a:
            if character not in str(words):
                array.append(words)
    return array
#intersect function
def intersect(list_a, list_b):
    array = []
    for num in list_a:
        for var in list_b:
            if num == var:
                array.append(num)
    return array
#not_in function
def not_in(list_a, list_b):
    array = []
    for num in list_a:
        if num not in list_b:
            array.append(num)
    return array
# is_prime
def is_prime(value):
    import math
    if value > 0 and value < 3:
        if value == 1:
            prime_num = 'false'
            print('False')
        if value == 2:
            prime_num = 'true'
            print('True')
    else:
        prime_num = 'true'
        num = math.floor(math.sqrt(value))
        for i in range(2, num + 1):
            if num % value == 0:
                print('False')
            if num:
                print('True')

    

