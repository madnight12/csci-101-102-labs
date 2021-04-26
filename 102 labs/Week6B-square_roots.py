# Madeleine Nightengale-Luhan
# CSCI 102 - Section A
# Week 6 - Lab B - Estimating Square Roots
# References: No One
# Time: 60 minutes

print('How many numbers am I estimating John?')
c = int(input('COUNT> '))
print('Input each number to estimate.')
list1 = []
list2 = []
list3 = []
for i in range (0, c):
    num = float(input('NUMBER> '))
    initial_guess = 10
    better_guess = 0
    itera = 0
    while True:
        better_guess = (initial_guess + num / initial_guess) / 2
        itera += 1
        if initial_guess != better_guess:
            initial_guess = better_guess
        else:
            break
    list1.append(round(better_guess,2))
    list2.append(itera)
    list3.append(num)
print('The square roots are as follows:')
for i in range(len(list3)):
    print(f"OUTPUT After {list2[i]} iterations {list3[i]}^0.5 = {list1[i]}")
