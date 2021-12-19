# /two-dimensional-array/
number_s = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]

print(number_s[0][2])
print(number_s[2][1])
# /nested-forloops/
for row in number_s:
  print(row)

for row in number_s:
  for column in row:
    print(column)
# to be continued <--