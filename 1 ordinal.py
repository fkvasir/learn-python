#No. 1

name = ["L","y","n","n","i","e"]
def ordinal():
  w = ord(name[0])
  x = ord(name[1])
  y = ord(name[2])
  z = ord(name[3])
  return x, y


"""
No. 2 - Compute the following equation:
>>> a
5(x^3/2) + 3x^2 + 11
"""
def compute(num):
  k = (num*num*num)/2
  l = 5*k
  m = num*num
  n = 3*m
  h = l+n+11
  return h
compute(x)
"""
>>> b
"""
def compute_1():