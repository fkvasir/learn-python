try:
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
except:
  print("INVALID")