import random

part1 = ["Bitch", "What","River","Moshi", "Hi"]
part2 = ["flowing", "I hate", "you sucks", "where are you?"]
part3 = ["in everything", "thank you", "sorry"]
part4 = ["losing", "regrets", "lucky"]

combination = [part1 , part2, part3, part4]

for part in combination: # for haiku structure
  r = random.randint(0, len(part)-1)
  print(part[r])

sentence = []
for part in combination: # sentence structure
  r = random.randint(0, len(part)-1)
  sentence.append(part[r])
print(" ".join(sentence))

# LIST COMPREHENSIONS

numbers = [1,2,3,10,5,14,20]
squares = []
for num in numbers:
  squares.append(num * num)
print(squares)