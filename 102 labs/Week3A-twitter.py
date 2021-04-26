# Madeleine Nightengale-Luhan
# CSCI 102 - Section A
# Week 3 - Lab A - Twitter Decoding
# References: Zy-book 17.10 for layout of code
# Time: 30 minutes

print('Enter the Tweet of Message abbreviation to decode.')

tweet = input("TWEET> ")
print('The decoded abriviation is:')

if tweet == 'LOL':
    print('OUTPUT LOL = laughing out loud')
elif tweet == 'BFN':
    print('OUTPUT BFN = bye for now')
elif tweet == 'FTW':
    print('OUTPUT FTW = for the win')
elif tweet == 'IRL':
    print('OUTPUT IRL = in real life')
elif tweet == 'BTW':
    print('OUTPUT BTW = by the way')
elif tweet == 'DM':
    print('OUTPUT DM = direct message')
elif tweet == 'AFAIK':
    print('OUTPUT AFAIK = as far as I know')
elif tweet == 'IDK':
    print("OUTPUT IDK = I don't know")
else:
    print("OUTPUT Sorry, don't know that one")
    
