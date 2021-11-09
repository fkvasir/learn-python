i = 1
"""
while (statement) --->/as-long-as-true/
"""
while i <= 10:
  print(i)
  i += 1
  
print ("Done with loop")

print("~~~~~~~~~~~~~~~~\n")



x = int(input("Enter a number in cm\n-> "))
y = int(input("Input a second larger number\n-> "))
CM_to_Inches = 0.3937
g = 0
while g <= 11:
  if y == x + 10:
    print(x ,  (x+g) * CM_to_Inches)
  else:
    print("\nError: Invalid Intervals\n")
  g += 11