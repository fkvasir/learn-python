import time
name = "Lynn"

def ordinalname(n):
  for i in name:
    print(ord(i), end =" ")
    time.sleep(.15)
  print()