# Madeleine Nightengale-Luhan
#CSCI 102- Section A
#Week 5 - Lab A - Stuck in a Time Loop
# References: no one
# Time: 20 minutes

print("Enter the wizard's magic number.")
wizardnum = int(input('N> '))
N = 0
if wizardnum > 100 or wizardnum < 1:
    print('Error: input must be between 1 and 100!')
    print('OUTPUT ERROR')
else:
    while N < wizardnum:
        N = N + 1
        print('OUTPUT', N, 'Abracadabra')
    
    
