# Madeleine Nightengale-Luhan
# CSCI 101 - Section A
# Python Lab 2A
# Reference: No one
# Time: 30 minutes

print('Input the five lists of characters to be encrypted.')
list_1 = input('LIST1> ')
rotated_list_1 = list_1[-2]
input_1 = list_1[-1]
list1 = rotated_list_1 + input_1 + list_1[0: len(list_1) - 2]
list_2 = input('LIST2> ')
list2 = list_2[:-2]
list_3 = input('LIST3> ')
list3 = list_3[len(list_3) // 2:]
list_4 = input('LIST4> ')
letter_3 = list_4[2]
letter_4 = list_4[4]
list4 = list_4[0:2] + letter_4 + list_4[3] + letter_3 + list_4[5: len(list_4)]
list_5 = input('LIST5> ')
print('The encrypted message is:')
output = (list_5[0:2] + ' ' + list1 + list2 + list3 + list4 + ' ' + list_5[2:])
print(output)
