# List def FUNCTIONS
def foods_I_love(desserts):

  for x in desserts:

    print(x)

desserts = ["leche flan", "mango float", "chocolate cake"]
foods_I_love(desserts)


# Just a normal LIST
friends = ["Minju", 2 , "Tzuyu"]
print(friends)


# Referring elements by their index

friends = ["Minju", "Nagyung" , "Tzuyu"] # in coding, always start from zero 

# each element of friends has a corresponding index
# Minju = 0, Nagyung = 1, Tzuyu = 2 meanwhile if the index is negative(-) it starts from the zero Minju = -3, Nagyung = -2, Tzuyu = -1

print(friends[2])
print(friends[-3])
print(friends[-1])
print(friends[-2])
print(friends[0])
print(friends[1])

# If I want to print all of the elements but except the first then:
print(friends[1:])
print(friends[2:])

# In specifying a range
close = ["Minju", "Nagyung", "Tzuyu", "Lisa", "Meru"]
print(close[1:4])
print(close[3:4])

# Modifying element
close[1] = "Minjoo"
print(close[1])
# Basically just changing one value of an element without changing others