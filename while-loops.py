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
while y == x + 10:
  print(x ,  (x * CM_to_Inches))
  y += 1
  x += 1