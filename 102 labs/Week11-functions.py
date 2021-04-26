#################################################
######## Madeleine Nightengale-Luhan     ########
######## Lab 11 - Function Definitions   ########
######## Section - A                     ########
######## References: None                ########
######## Time: 30 minutes                ########
#################################################
        
# Imports
import math

################################################
########   Function 1 : PrintOutput     ########
################################################

def print_output(str_input):
    print(f"OUTPUT {str_input}")

################################################
########   Function 2 : TriangleArea    ########
################################################

def triangle_area(base, height):
    area = (base * height) / 2
    return print_output(f"{area:0.2f}") 

################################################
########   Function 3 : FeetToMeters    ########
################################################

def feet_to_meters(feet):
    conversion = feet * 0.3048
    return print_output(f"{conversion:0.3f}")

################################################
########   Function 4 : PolarCoords     ########
################################################

def polar_coords(x, y):
    r = math.sqrt(x * x + y * y)
    deg = math.atan(y / x)
    deg = (180.0 * deg) / (math.pi)
    print_output(f"r: {r}")
    print_output(f"theta: {deg:0.1f}")
    

################################################
########   Function 5 : EurosToDollars  ########
################################################

def euros_to_dollars(euro):
    conversion_2 = euro * 1.17
    return print_output(f"{conversion_2:0.2f}")        
