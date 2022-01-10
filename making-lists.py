# List def FUNCTIONS
def foods_I_love(desserts):

  for x in desserts:

    print(x)

desserts = ["leche flan", "mango float", "chocolate cake"]
foods_I_love(desserts)
print("_________________\n")

# Just a normal LIST
friends = ["Minju", 2 , "Tzuyu"]
print(friends)

print("___________________\n")
# Referring elements by their index

friends = ["Minju", "Nagyung" , "Tzuyu"] # in coding, always start from zero 

# --> each element of friends has a corresponding index
# Minju = 0, Nagyung = 1, Tzuyu = 2 meanwhile if the index is negative(-) it starts from the zero Minju = -3, Nagyung = -2, Tzuyu = -1

print(friends[2])
print(friends[-3])
print(friends[-1])
print(friends[-2])
print(friends[0])
print(friends[1])
print("_________________________________\n")
# If I want to print all of the elements but except the first then:
print("Printing-all-elements-except-one")
print(friends[1:])
print(friends[2:])
print("___________________________\n")

# In specifying a range
print("Specifying range")
close = ["Minju", "Nagyung", "Tzuyu", "Lisa", "Meru"]
print(close[1:4])
print(close[3:4])

print("_____________________________\n")
# Modifying element
print("Modifying element")
close[1] = "Minjoo"
print(close[1])
# //Basically just changing one value of an element without changing others//