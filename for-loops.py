print("\n~~~~~~~~~~~~~~")
family = ["Laura", "Caridad", "Hamsel"]
for member in family:
  print(member)
print("\n~~~~~~~~~~\n")
for letter in "Kvasir":
  print(letter)
print("\n~~~~~~~~~~~\n")
crhs = ["Shyne", "Cthrn", "Nrhmd", "Dryl"]
for cruhsi in crhs:
  print(cruhsi)
print("\n~~~~~~~~~\n")
for index in range(7):
  print(index)
print("\n~~~~~~~~~\n")
for index in range(len(crhs)): # //the-same-as-the-first-but-w/range//
  print(crhs[index])
print("\n")
for cruhsi in crhs:
  if cruhsi == "Dryl":
    print("-since g11")
  elif cruhsi == "Nrhmd":
    print("-since g11(beginning)")
  elif cruhsi == "Cthrn":
    print("-since g10(summer)")
  elif cruhsi == "Shyn":
    print("-since g10")
  print(cruhsi)
print("\n~~~~~~~~~\n")
for cruhsi in crhs:
  if cruhsi == [0]:
    print("firstIteration")
  elif cruhsi == [1]:
    print("secondIteration")
  else:
    print("lastIteration")
print("finish")
print("\n\n")


for i in range(0,11):
  print(i)

for i in range(0,11):
  if i == 5:
    print ("Ohlala")
    continue
  print(i)