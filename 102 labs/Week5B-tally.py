# Madeleine Nightengale-Luhan
# CSCI 102 - Section A
# Week 5 - Lab B - Tally for Kids
# References: No one
# Time: 30 minutes

inputvar = 0
total = 0
print('Enter values to add. Enter quit when done.')
while inputvar != 'quit':
    inputvar =input('NUMBER> ')
    if inputvar == 'quit':
        break
    answer = int(inputvar)
    total = total + answer

print('The addition of the', len(inputvar), 'numbers entered is:')
print('OUTPUT', len(inputvar), 'numbers')
print('OUTPUT', total, 'total')
    
