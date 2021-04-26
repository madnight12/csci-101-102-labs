# Madeleine Nightengale-Luhan
# CSCI 101 - Section A
# Python Lab 6: Timber Regrowth
# References: No one
# Time: 50 minutes

print('Input the number of years to print in the reforestation table:')
y = int(input('YEAR> '))
print('The reforestation table is then')
print('')
print('OUTPUT	   Year	     # Acres	  % of Forest')
acres = 2500.0
count = 0
while y >= 0:
    reforestation = (14000 - acres) / 14000
    new = (1 - reforestation) * 100
    var = acres * 0.02
    y = y - 1
    print(f"OUTPUT     {count}         {round(acres, 1)}       {round(new,2)}%")
    count = count + 1
    acres = acres + var
    
