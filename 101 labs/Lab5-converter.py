# Madeleine Nightengale-Luhan
# CSCI 101 - Section A
# Python Lab 5
# References: No One
# Time: 120 minutes

print('Welcome to the Binary-Octal-Decimal Converter')
var = 'y'
bracket = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
r = 0
while var == 'y' or var == 'yes' or var == 'Yes' or var == 'yES' or var == 'yeS' or var == 'yEs' or var == 'Y' or var == 'YES':
    print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
    print('Enter an option:')
    print('1. Binary-Decimal Conversion')
    print('2. Decimal-Binary Conversion')
    print('3. Octal-Decimal Conversion')
    print('4. Decimal-Octal Conversion')
    print('5. Quit')

    choice = int(input('OPTION> ' ))
    if choice == 1:
        correct = True 
        binary = str(input('BINARY-STR> '))
        for index in binary:
            if index not in '01':
                print('ERROR: Input', binary, 'is NOT a binary number.')
                print('OUTPUT ERROR')
                correct = False
                break
        if correct == True:
            i = len(binary)
            num = 0
            decima1 = 0
            while i > 0:
                decimal += (2 ** num) * int(binary[i - 1])
                num += 1
                i = i - 1
            print(f"Binary {binary} is Binary {decimal}")
            print(f"OUTPUT {decimal}")
        print(f"Would you like to continue (y/n)?")
        var = input('CONTINUE> ')  
    if choice == 2:
        decimal = str(input('DECIMAL-STR> ' ))
        correct = True
        for index in decimal:
            if index not in bracket:
                print(f"ERROR: Input {decimal} is NOT a decimal number.")
                print(f"OUTPUT ERROR")
                correct = False
                break
        if correct == True:
            decimal = int(decimal)
            binary = ''
            while decimal > 0:
                if decimal % 2 == 0:
                    binary = '0' + binary
                else:
                    binary = '1' + binary
                decimal = int(decimal / 2)
            print(f"Decimal {decimal} is Binary {binary}")
            print(f"OUTPUT {binary}")
        print(f"Would you like to continue (y/n)?")
        var = input('CONTINUE> ')
    if choice == 3:
        octal = str(input('OCTAL-STR> '))
        correct = True
        for index in octal:
            if index not in bracket:
                print(f"ERROR: Input {octal} is NOT an octal number.")
                print(f"OUTPUT ERROR")
                incorrect = False
                break
            i = len(octal)
            num = 0
            decimal = 0
        while i > 0:
            decimal += (8 ** num) * int(octal[i - 1])
            num += 1
            i = i - 1
        print(f"Octal {octal} is Decimal {decimal}")
        print(f"OUTPUT {decimal}")
        print(f"Would you like to continue (y/n)?")
        var = input('CONTINUE> ') 
    if choice == 4:
        decimal = str(input('DECIMAL-STR> '))
        correct = True
        for index in decimal:
            if index not in bracket:
                print(f"ERROR: Input {decimal} is NOT a decimal number.")
                print(f"OUTPUT ERROR")
                correct = False
                break
            if correct == True:
                octal = ''
                decimal = int(decimal)
                while decimal > 0:
                    r = decimal % 8
                    octal = str(r) + octal
                    decimal = decimal // 8
            print(f"Decimal {decimal} is Octal {octal}")
            print(f"OUTPUT {octal}")
            print(f"Would you like to continue (y/n)?")
        var = input('CONTINUE> ')   
    if choice == 5:
        break
    if choice > 5 or choice < 1:
        print(f"ERROR: Please choose from [1-5]")
        print(f"OUTPUT ERROR")
        print(f"Would you like to continue (y/n)?")
        var = input('CONTINUE> ')
print('OUTPUT Goodbye!')
print('=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
