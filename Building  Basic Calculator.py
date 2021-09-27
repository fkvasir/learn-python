print("For adding digits")
number_1 = input("Enter a number: ")
number_2 = input("Enter the second number: ")
result = number_1 + number_2
print(result) # Python will just add the numbers as a digit because it is a string

"""
 Python will assume that it is a string
 So you need to convert the string that has been input by the user as string
 For example
"""

intro = "For multiplication" # applying string functions and calculator
print(intro.upper())
number_3 = input("Enter a number: ")
number_4 = input("Enter any number: ")
result1 = int(number_3) * int(number_4)
print(result1)

# Another example
# mix of defined functions & calculators

okay ="For finding quotient"
def introduction(intro1):
  print(intro1.upper())
introduction(okay)
num2 = input("Enter a dividend: ")
num3 = input("Enter the divisor: ")
quotient = int(num2) / int(num3)
print(quotient)

# But if you try to put decimal places in the input it will says an error because "int" don't read decimal places
# instead of using "int", use "float" because float means any decimal numbers
# For example

intro3 ="For finding the remainder"
print(intro3.upper)
num4 = input("Enter a dividend: ")
num5 = input("Enter a divisor: ")
remainder = float(num4) % float(num5)
print(remainder) # Since we can't concatenate an integer with a string (so I assign the value of the remainder as a string)

# For EXAMPLE
from math import *
intro3 ="for finding the square root"
print(intro3.upper)
num4 = input("Enter a dividend: ")
num5 = input("Enter a divisor: ")
remainder = float(num4) % float(num5)
print("The square root of your want number" + str(remainder))
# This is only for my practice in coding

from math import*
finding_difference = "in order to find the difference of two numbers"
def my_introduction(introd):
  print(introd.upper())
my_introduction(finding_difference)
enter = input ("Enter an integer: ")
integer2 = input ("Enter another integer: ")
difference = float(enter) - float(integer2)
print(" The difference of two numbers is: " + int(difference))
