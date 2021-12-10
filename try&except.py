try:
  x = int(input("Enter a number in cm\n-> "))
  y = int(input("Input a second larger number\n-> "))
  assigned_value = 6.23
  g = 0
  if y == x + 10:
    while g <= 10:
      print(x ,  (x * assigned_value))
      g += 1
      x += 1
  else:
    print("Invalid interval")
except:
  print("INVALID")
# /try-and-except-are-used-to-assign-what-to-do-for-expected-errors/
# my-lazyass-starts-procrastinating
try:
  name = input("ENTER YOUR NAME:")
  age = input("ENTER YOUR AGE:")
  print("Hello! So you are " + name + "!")
  print("Your age is" + "? " + age)
  numb = int(input("Type any number of your choice: "))
  print("Why did you choose " + numb + "as your number? Are you insane? Stupid idiot ")
except:
  print("Try again latur")