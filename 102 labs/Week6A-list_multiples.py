# Madeleine Nightengale-Luhan
# CSCI 102 - Section A
# Week 6 - Lab A - List of Multiples
# References: No one
# Time: 20 minutes

print('Enter the number to create multiples for.')
n = int(input('NUMBER> '))
print('Enter the size of the list.')
s = int(input('SIZE> '))
print('Your list of multiples is as follows:')
list1 = []
x = 0
for x in range(0,s):
    x = x + 1
    z = n * x
    list1.append(z)
print('OUTPUT', list1)
    
