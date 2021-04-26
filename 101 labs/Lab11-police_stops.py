# Madeleine Nightengale-Luhan
# CSCI 101 - Section A
# Python Lab 11
# References: No one
# Time: 120 minutes
#
# Data Comparison: 188,127 males are in aurora and out of that number, 104,322 were stopped by the cops. 
# There are 229,090 white people in Aurora and out of that number, 113,807 were stopped by the cops.
# Lastly, there are 379,289 people who live in Aurora and out of the total population, 172,929 people were stopped by the cops.

import csv

def read_csv(file):
    array = []

    with open (file, 'r', encoding ='utf-8') as aurora_police:
        arrests = csv.reader(aurora_police, delimiter = ',')
        for row in arrests:
            array.append(row)
    return array

def stops_by_race(rows, race):
    index = 0
    if race == 'ALL':
        return len(rows) - 1
    for row in rows:
        if race == row[8]:
            index += 1
    return index

def stops_by_sex(rows, sex):
    num = 0
    if sex == 'ALL':
        return len(rows) - 1
    for row in rows:
        if sex == row[9]:
            num =+ 1
    return num




