i = 1
"""
while (statement) --->/as-long-as-true/
"""
while i <= 10:
  print(i)
  i += 1
print ("Done with loop")
print("~~~~~~~~~~~~~~~~\n")
print("Input a number in centimeter to be converted to inches\nShould be a 10-interval number from the first and second number")
x = int(input("Enter a number in cm\n-> "))
y = int(input("Input a second larger number\n-> "))
CM_to_Inches = 0.3937
g = 0
if y == x + 10:
  while g <= 10:
    print(x ,  (x * CM_to_Inches))
    g += 1
    x += 1
else:
  print("Invalid interval")

print("\n~~~~~~~~~~~\n")
first = int(input("Enter a number in inches(should be a 5 interval numbers)\nhere => "))
error = "ERROR: interval should be 5"
second = int(input("Enter second number where you want to stop converting\nhere => "))
Inches_to_CM = 2.53
f = 0
if second == first + 5:
  while f <= 4:
    print(first , (first * Inches_to_CM))
    first += 1
    f += 1
else:
  print(error.upper)

print("Converting decimals into fraction(range should be 3 interval")
dcmals = float(input("Enter decimal numbers in a tenth place"))
error = print("Error: Try again")
dcmals_2 = float(input("Enter a second decimal number"))
decimals_to_fraction = dcmals*10
decimals_to_fraction_2 = dcmals_2*10
i = 0
if dcmals_2 == dcmals + 3:
  while i <= 3:
    print(dcmals + "/10 "+ "\n" +dcmals_2 + "/10 " )
else:
  print("error")
