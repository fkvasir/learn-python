print(2**3) # /2^3-two-to-the-3rdpower/

def to_thepower(base_num, power_num):
  result = 1
  for index in range(power_num):
    result = result * base_num
  return result
print(to_thepower(3, 2))
print(to_thepower(3, 4))
print(to_thepower(2, 3))
print(to_thepower(10, 2))
print(to_thepower(3, 0))