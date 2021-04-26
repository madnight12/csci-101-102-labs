# Madeleine Nightengale-Luhan
# CSCI 101 - Section A
# Python Lab 10
# References: No one
# Time: 60 minutes

import csv
import math

print('Enter the name of the file containing the math problems.')
math_file = input('MATHFILE> ')
print('Enter the name of the file in which to store the results')
output_file = input('OUTPUTFILE> ')
array = []
with open('math.csv', 'r') as file:
    reader = csv.reader(file, delimiter= ',')
    for som in reader:
        value =som[0]
        k = 1
    while k < len(som):
        if(som[k]) == '*':
                value =(value * som[k+1])
        if(som[k]) == '/':
                value = (value / som[k+1])
        if(som[k]) == '+':
                value =(value + som[k+1])
        if(som[k]) == '-':
                value =(value - som[k+1])
        k = k + 2
    array.append(int(math.floor(value)))
with open('results.csv', 'w') as result:
    k = 0
    while k <= len(som):
        result.writerow(result[k])
        k += 1
        result.writerow(result[k])
        print(result)
