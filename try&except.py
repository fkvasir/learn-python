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