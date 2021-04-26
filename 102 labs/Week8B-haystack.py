# Madeleine Nightengale-Luhan
# CSCI 102 - Section A
# Week 8 -Lab B - Combing Through a Haystack
# References: None
# Time: 45 minutes

print('Enter a DNA string s:')
s = input('s> ')
print('Enter a substring t:')
t = input('t> ')
var = 0
sub_len = len(t)
alist = []

for i in range(len(s)):
    if s[i: i + sub_len] == t:
        var += 1
        alist.append(i)
print('The total number of substrings found is', var)
print('OUTPUT', var)
print('The locations of these substrings in s are: ', end= '')
for i in range(len(alist)):
    print(f"{alist[i] + 1} ", end= '')


