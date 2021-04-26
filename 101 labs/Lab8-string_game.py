# Madeleine Nightengale-Luhan
# CSCI 101 - Section A
# Python Lab 8
# References: No one
# Time: 60 mminutes

import random

print('Would you like to provide your own tring or generate random one? (1 or 2)')
choice = int(input('CHOICE> '))
kevin = 0
stacy = 0
if choice == 1:
    print('Enter a string for the game:')
    string = input('STRING> ')
    for i in range (0, len(string)):
        t = True
        if string[i] in 'AEIOU':
            t = False
            for j in range(i, len(string)):
                kevin += 1
        if t:
            for j in range(i, len(string)):
                stacy += 1
if choice == 2:
    print('Number to initialize the random generator:')
    seed = int(input('SEED> '))
    list1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    string = ''
    for i in range(6):
        random_number = random.randint(0, len(list1) - 1)
        string += list1[random_number]
    print('The randomly generated string for this game is', string)
print('With the string', string, "Kevin's score is", kevin, "Stacy's score is", stacy)
winner = 't'
if stacy > kevin:
    winner = 'Stacy'
    print(winner, 'wins!')
    print('OUTPUT', kevin)
    print('OUTPUT', stacy)
    print('OUTPUT', winner)
elif kevin > stacy:
    winner = 'Kevin'
    print(winner, 'wins!')
    print('OUTPUT', kevin)
    print('OUTPUT', stacy)
    print('OUTPUT', winner)
else:
    winner = 'tie!'
    print("It's a tie!")
    print('OUTPUT', kevin)
    print('OUTPUT', stacy)
    print('OUTPUT Draw')
    
    

