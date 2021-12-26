x = 5
y = 9
g = 0
while g <= 4:
  print(x ,  (x * y))
  g += 1
  x += 1
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
  # /conversion-errors/