first = 5
second = 6
f = 0
while f <= 4:
  print (first, (first*second))
  f+=1
  first+=1
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
