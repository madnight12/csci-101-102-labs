# Madeleine Nightengale-Luhan
# CSCI 101 - Section A
# Week 3 - Lab - Alarm
# References: No one
# Time: 20 minutes

Hours = int(input('HOURS> '))
Minutes = int(input('MINUTES> '))

A = int(40)

if Hours == 0 and Minutes < A:
    print('OUTPUT', 23, minutes + 20)
if Hours == 0 and Minutes >= A:
    print('OUTPUT', '0', minutes - A)
if Minutes >= A:
    print('OUTPUT', hours, minutes - A)
if Minutes < A and Hours != 0:
    print('OUTPUT', Hours - 1, Minutes + 20)
if Minutes < 10:
    print('OUTPUT ', Hours, '0', Minutes)
