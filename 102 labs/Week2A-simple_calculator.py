# Madeleine Nightengale-Luhan
# CSCI 102 - Section A
# Week 2 -Lab A- Simple Calender
# References: No one
# Time: 25 minutes 


operand_one = float(0.0)
operand_two = float(0.0)
sum_1 = float(0.0)
difference = float(0.0)
quotient = float(0.0)
remainder = float(0.0)

print('Input the first operand.')
operand_one = float(input('FIRST> '))
print('Input the second operand')
operand_two = float(input('SECOND> '))

sum_1 = float(operand_one + operand_two)
difference = float(operand_one - operand_two)
quotient = operand_one // operand_two
remainder = operand_one % operand_two

print('The sum of', operand_one, 'and', operand_two, 'is', round(sum_1, 1))
print('The difference of', operand_one, 'and', operand_two, 'is', round(difference, 1))
print('The quotient of', operand_one, 'and', operand_two, 'is', int(quotient))
print('The remainder of', operand_one, 'and', operand_two, 'is', round(remainder, 2))
      
