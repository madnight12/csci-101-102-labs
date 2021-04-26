# Madeleine Nightengale-Luhan
# CSCI 101 - Section A
# Python Lab 4
# References: No one
# Time: 80 minutes

print('Please eneter the filing stutus')
status = input('STATUS> ')
print('Please enter the income earned:')
income_earned = int(input('INCOME> '))
num = 9325
num2 = 18650

if status == 'single':
    if income_earned <= 9325:
        tax = income_earned * 0.1
        tax = int(tax)
        print(f"The tax owed by this person (single filing status) with {income_earned} income is {tax}")
        print(f"OUTPUT {tax}")
        percent = round(((tax / income_earned) * 100), 2)
        print(f"The percent of income paid in taxes is {percent}")
    elif income_earned >= 9326 and income_earned <= 37950:
        tax = ((num * 0.1) + ((income_earned - num) * 0.15))
        tax = int(tax)
        print(f"The tax owed by this person (single filing status) with {income_earned} income is {tax}")
        print(f"OUTPUT {tax}")
        percent = round(((tax / income_earned) * 100), 2)
        print(f"The percent of income paid in taxes is {percent}")
    elif income_earned >= 37951 and income_earned <= 91900:
        tax = (num * 0.1) + ((37950 - num) * 0.15) + ((income_earned - 37950) * 0.25)
        tax = int(tax)
        print(f"The tax owed by this person (single filing status) with {income_earned} income is {tax}")
        print(f"OUTPUT {tax}")
        percent = round(((tax / income_earned) * 100), 2)
        print(f"The percent of income paid in taxes is {percent}")
    elif income_earned >= 91901 and income_earned <= 191650:
        tax = (num * 0.1) + ((37950 - num) * 0.15) + ((91900 - 37950) * 0.25) + ((income_earned - 91900) * 0.28)
        tax = int(tax)
        print(f"The tax owed by this person (single filing status) with {income_earned} income is {tax}")
        print(f"OUTPUT {tax}")
        percent = round(((tax / income_earned) * 100), 2)
        print(f"The percent of income paid in taxes is {percent}")
    elif income_earned >= 191651 and income_earned <= 416900:
        tax = (num * 0.1) + ((37950 - num) * 0.15) + ((91900 - 37950) * 0.25) + ((191650 - 91900) * 0.28) + ((income_earned - 191650) * 0.33)
        tax = int(tax)
        print(f"The tax owed by this person (single filing status) with {income_earned} income is {tax}")
        print(f"OUTPUT {tax}")
        percent = round(((tax / income_earned) * 100), 2)
        print(f"The percent of income paid in taxes is {percent}")
    elif income_earned >= 416901 and income_earned <= 418400:
        tax = (num * 0.1) + ((37950 - num) * 0.15) + ((91900 - 37950) * 0.25) + ((191650 - 91900) * 0.28) + ((416900 - 191650) * 0.33) + ((income_earned - 416900) * 0.35)
        tax = int(tax)
        print(f"The tax owed by this person (single filing status) with {income_earned} income is {tax}")
        print(f"OUTPUT {tax}")
        percent = round(((tax / income_earned) * 100), 2)
        print(f"The percent of income paid in taxes is {percent}")
    elif income_earned >= 418401:
        tax = (num * 0.1) + ((37950 - num) * 0.15) + ((91900 - 37950) * 0.25) + ((191650 - 91900) * 0.28) + ((416900 - 191650) * 0.33) + ((418400 - 416900) * 0.35) + ((income_earned - 418400) * 0.396)
        tax = int(tax)
        print(f"The tax owed by this person (single filing status) with {income_earned} income is {tax}")
        print(f"OUTPUT {tax}")
        percent = round(((tax / income_earned) * 100), 2)
        print(f"The percent of income paid in taxes is {percent}")

if status == 'joint':
    if income_earned <= 18650:
        tax = income_earned * 0.1
        tax = int(tax)
        print(f"The tax owed by this person (joint filing status) with {income_earned} income is {tax}")
        print(f"OUTPUT {tax}")
        percent = round(((tax / income_earned) * 100), 2)
        print(f"The percent of income paid in taxes is {percent}")
    elif income_earned >= 18651 and income_earned <= 75900:
        tax = ((num2 * 0.1) + ((income_earned - num2) * 0.15))
        tax = int(tax)
        print(f"The tax owed by this person (joint filing status) with {income_earned} income is {tax}")
        print(f"OUTPUT {tax}")
        percent = round(((tax / income_earned) * 100), 2)
        print(f"The percent of income paid in taxes is {percent}")
    elif income_earned >= 75901 and income_earned <= 153100:
        tax = (num2 * 0.1) + ((37950 - num2) * 0.15) + ((income_earned - 75900) * 0.25)
        tax = int(tax)
        print(f"The tax owed by this person (joint filing status) with {income_earned} income is {tax}")
        print(f"OUTPUT {tax}")
        percent = round(((tax / income_earned) * 100), 2)
        print(f"The percent of income paid in taxes is {percent}")
    elif income_earned >= 153101 and income_earned <= 233350:
        tax = (num2 * 0.1) + ((37950 - num2) * 0.15) + ((153100 - 75900) * 0.25) + ((income_earned - 153100) * 0.28)
        tax = int(tax)
        print(f"The tax owed by this person (joint filing status) with {income_earned} income is {tax}")
        print(f"OUTPUT {tax}")
        percent = round(((tax / income_earned) * 100), 2)
        print(f"The percent of income paid in taxes is {percent}")
    elif income_earned >= 233351 and income_earned <= 416900:
        tax = (num2 * 0.1) + ((37950 - num2) * 0.15) + ((153100 - 75900) * 0.25) + ((233350 - 153100) * 0.28) + ((income_earned - 233350) * 0.33)
        tax = int(tax)
        print(f"The tax owed by this person (joint filing status) with {income_earned} income is {tax}")
        print(f"OUTPUT {tax}")
        percent = round(((tax / income_earned) * 100), 2)
        print(f"The percent of income paid in taxes is {percent}")
    elif income_earned >= 416901 and income_earned <= 470700:
        tax = (num2 * 0.1) + ((37950 - num2) * 0.15) + ((153100 - 75900) * 0.25) + ((233350 - 153100) * 0.28) + ((416900 - 233350) * 0.33) + ((income_earned - 416900) * 0.35)
        print(f"The tax owed by this person (joint filing status) with {income_earned} income is {tax}")
        print(f"OUTPUT {tax}")
        percent = round(((tax / income_earned) * 100), 2)
        print(f"The percent of income paid in taxes is {percent}")
    elif income_earned >= 470701:
        tax = (num2 * 0.1) + ((37950 - num2) * 0.15) + ((153100 - 75900) * 0.25) + ((233350 - 153100) * 0.28) + ((416900 - 233350) * 0.33) + ((470700 - 416900) * 0.35) + ((income_earned - 470700) * 0.396)
        tax = int(tax)
        print(f"The tax owed by this person (joint filing status) with {income_earned} income is {tax}")
        print(f"OUTPUT {tax}")
        percent = round(((tax / income_earned) * 100), 2)
        print(f"The percent of income paid in taxes is {percent}")
        
    
   

