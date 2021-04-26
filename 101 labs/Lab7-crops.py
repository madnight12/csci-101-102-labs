# Madeleine Nightengale-Luhan
# CSCI 101 - Section A
# Python Lab 7
# References: Niko Magnan (roomate) for help with nested lists 
# Time: 195 minutes 

print('Input the number of rows and columns in the crop field:')
row = int(input('ROWS> '))
col = int(input('COLUMNS> '))
print('Input each row of the crop field.')
crop = []
watered = True
notwatered = []

for i in range(row):
    rowin = input('ROW' + str(i) + '> ')
    rowlist = rowin.split()
    crop.append(rowlist)
    
for j in range(row):
    for k in range(col):
        cropwatered = False
        if crop[j][k] == 'c':
            for l in range(row):
                for m in range(col):
                    if crop[m][l] == 'w':
                        if (l == j or l == j + 1 or l == j - 1) and (m == k or m == k + 1 or m == k - 1):
                            cropwatered = True
            if cropwatered == False:
                watered = False
                nowater = (j,k)
                notwatered.append(nowater)

if watered == True:
    print('All crops are watered!')
    print('OUTPUT True!')
if watered == False:
    print('Not all crops are watered!')
    print('OUTPUT False')
    print('The following crops are not watered:')
    print('OUTPUT', notwatered)
                        
