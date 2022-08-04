# PYTHON FUNCTIONS

def my_function(heavy, light):
    print(heavy + "had a family with" + light)
my_function("Jake ", " Mary")

def my_function(*kids):
    print("The youngest son is " + kids[2])
my_function("John", "Jason", "Tigreal")

def my_function(child1, child2, child3):
    print("The oldest among the sons is" + child3)
my_function(child1=" Tigreal",child2=" Jason",child3=" John")

def my_function(country= "Philippines"):
    print("They lived in "+ country)
my_function("Sweden")
my_function("Germany")
my_function()
my_function("Russia")

# FUNCTIONS (lists)
def my_function(food):
    for x in food:
        print(x)
fruits = ["apple","mango","strawberry"]
my_function(fruits)

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))
#a
# RECURSIONS

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


# PYTHON SYNTAX
if 5 > 2:
    print("Hello world") # wont print if the statement is false.
if 10 < 3:
    print("BITCH")

# PYTHON COMMENTS

"""
This line is just a practice for comment
Comments can be used to prevent execution when testing code.
Comments are used to make the code more readable.
Comments can explain python code. You can use either (#) or three (")
Use three quote-marks before and at the end of the comments.
"""

# WORKING WITH STRINGS

phrase = "Hi! my name is Fulgent"
print(phrase)
print(phrase.isupper())
print(phrase.upper())
print(phrase.lower())
print(phrase.upper().isupper())

# length and position of characters

print(len(phrase))
print(phrase[0])
print(phrase[2])
print(phrase.index("F"))
print(phrase.replace("my name", "my first name").upper())
print(len(phrase.replace("Hi!", "Hello!")))

# FUNCTION STRINGS

def lower(self):
    print(self)
lower("My last name is Fulgent")
def my_love(one_and_only):
    print("I love my girlfriend and her name is " + one_and_only.upper())
my_love("Catherine")

def my_least_favorite_food(foods):
    for x in foods:
        print(x)
vegetables =["okra", "eggplant", "tae"]
my_least_favorite_food(vegetables)


# WORKING WITH NUMBERS
# mathematical operations
print(1 + 13)
print(20 * 9)
print(10 % 4)  # take the remainder out, read as "10 mod 4"

my_favorite_number = 13
print(my_favorite_number)
print(str(my_favorite_number))
print(str(my_favorite_number) + " is my favorite number.")
# when combining number with a string, put the number in the variable and assign "str"
# new code comment
# mathematical operations