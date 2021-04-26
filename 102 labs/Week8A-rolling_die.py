# Madeleine Nightengale-Luhan
# CSCI 102 - Section A
# Week 8 - Lab A - Rolling a Die
# References: None
# Time: 30 minutes

import random

print('Input the number of rolls to make:')
random_num = int(input('NUMBER> '))
print('Input the seed for the random number generator:')
seed = int(input('SEED> '))
random.seed(seed)

occur1 = 0
occur2 = 0
occur3 = 0
occur4 = 0
occur5 = 0
occur6 = 0

print('Your', random_num,'rolls follow:')
for i in range(0, random_num):
    rolls = random.randint(1,6)
    if rolls == 1:
        occur1 += 1
    if rolls == 2:
        occur2 += 1
    if rolls == 3:
        occur3 += 1
    if rolls == 4:
        occur4 += 1
    if rolls == 5:
        occur5 += 1
    if rolls == 6:
        occur6 += 1

print('OUTPUT 1 occurred', occur1, 'times')
print('OUTPUT 2 occurred', occur2, 'times')
print('OUTPUT 3 occurred', occur3, 'times')
print('OUTPUT 4 occurred', occur4, 'times')
print('OUTPUT 5 occurred', occur5, 'times')
print('OUTPUT 6 occurred', occur6, 'times')
    
