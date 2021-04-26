# Madeleine Nightengale-Luhan
# CSCI 102 - Section A
# Week 7 - Lab A - Checkerboard
# References: Taylor Hicken (teammate) for help with loop
# References: Audrey Richard (classmate) for help with order of outputs in bracket
# Time: 40 minutes

print('What is the length of the sides of the checkerboard?')
L = int(input('LENGTH> '))
print('What are the strings with which to pattern it?')
first = input('FIRST> ')
second = input('SECOND> ')
array = []
x = 0

for i in range(L):
    array2 = []
    for j in range(L):
        if (x % 2 ==0):
            array2.append(first)
        else:
            array2.append(second)
        x += 1
    array.append(array2)
    if(L % 2 == 0):
        x += 1
print(f"A checkerboard with side length {L}, first string is {first}, and second string is {second} is:")    
for i in array:
    print('OUTPUT', i)
print('And the 2D array representation is:')
print('OUTPUT', array)
