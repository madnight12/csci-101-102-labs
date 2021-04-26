# Madeleine Nightengale-Luhan
# CSCI 102 - Section A
# Week 10 Lab
# References: No One
# Time: 75 minutes

import csv

file = open('formations.csv', 'r')


reader = csv.reader(file, delimiter= ',')
with open('formations_parsed.csv', 'w') as csv_file2:
    writer = csv.writer(csv_file2)
    head_list = ['Depth', 'Start Depth', 'End Depth', 'Average Depth', 'Formation']
    writer.writerow(head_list)

for var in reader:
        depth = var[0]
        f = var[1]
        s = depth.split('-')
        start = s[0]
        end = s[-1]
        average = (float(end) + float(start)) / 2
        average = round(average, 1)
        writer.writerow([depth, s, end, average, f])


            
