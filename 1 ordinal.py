#No. 1
from traceback import print_tb
name = ["L","y","n","n","i","e"]
w = ord(name[0])
x = ord(name[1])
y = ord(name[2])
z = ord(name[3])
print_tb

"""
No. 2 - Compute the following equation:
>>> a
5(x^3/2) + 3x^2 + 11
"""
try:
  def compute(num):
    k = (num*num*num)/2
    l = 5*float(k)
    m = num*num
    n = 3*float(m)
    h = float(l)+float(n)+11
    return h
  compute(int(x))
except:
  print("Wrong")
"""
>>> b
"""
  def compute(num):
    k = (num*num*num)/2
    l = 5*float(k)
    m = num*num
    n = 3*float(m)
    h = float(l)+float(n)+11
    return h
  compute(int(y))
