# Madeleine Nightengale-Luhan
# CSCI 102 - Section A
# Week 3 - Lab B - Enhanced Calculator
# References: No one
# Time: 35 minutes

print('Welcome to out Enhanced Calculator!')

operand_one = float(0.0)
operand_two = float(0.0)
sum_1 = float(0.0)
difference = float(0.0)
product = float(0.0)
quotient = float(0.0)
remainder = float(0.0)
print('Input the first operand.')
operand_one = float(input('FIRST> '))
print('Input the second operand.')
operand_two = float(input('SECOND> '))

sum_1 = (operand_one + operand_two)
difference = (operand_one - operand_two)
product = (operand_one * operand_two)
quotient = (operand_one // operand_two)
remainder = (operand_one % operand_two)
      

print('Choose one of the following operations:')
print(' 1 - addition')
print(' 2 - subtraction')
print(' 3 - multiplication')
print(' 4 - division')
operation = int(input('OPERATION> '))

if operation == 1:
      print('The result of the addition is:', f"{sum:.6f}")
      print('OUTPUT', f"{sum:.6f}")
elif operation == 2:
      print('The result of the subtraction is:', f"{difference:.6f}")
      print('OUTPUT', f"{difference:.6f}")
elif operation == 3:
      print('The result of the multipication is:', f"{product:.6f}")
      print('OUTPUT', f"{product:.6f}")
elif operation == 4:
    print('The result of the division is:', int(quotient), '(quotient) and ', int(remainder),'(remainder)')
    print('OUTPUT', int(quotient))
    print('OUTPUT', int(remainder))

print('Thank you for using our calculator.')
    

    

      
