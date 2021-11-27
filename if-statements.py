is_male = True

if is_male:
  print("You are a male")
else:
  print("You are not a male")

print("__________________________________ \n")


# More complicated

is_male = True
is_tall = True

if is_male or is_tall:
  print("You are a male or tall or both") # IF EITHER OR BOTH OF THE STATEMENTS IS TRUE THEN THIS WILL PRINT OUT
else:
  print("You are neither male or tall") # IF TWO ARE FALSE THEN THIS WILL BE PRINTED INSTEAD
# ONLY IF "OR" IS USED


is_male = False
is_tall = True

if is_male or is_tall:
  print("You are a male or tall or both")
else:
  print("You are neither male or tall")


is_male = False
is_tall = False

if is_male or is_tall:
  print("You are a male or tall or both") # ONLY ONE TRUE CONDITION IS NEEDED
else:
  print("You are neither male or tall") # BOTH OF THE CONDITION SHOULD BE FALSE

is_male = True
is_tall = False

if is_male or is_tall:
  print("You are a male or tall or both! ")
else:
  print("You are neither male or tall! ") 

print("______________________________________________ \n")

is_male = False
is_tall = True

if is_male and is_tall:
  print("You are a tall male! ") # both should be true
else:
  print("You are not a male nor tall or both! ")  # only one false condition is needed

is_male = False
is_tall = True

if is_male and is_tall:
  print("You are a male or tall or both! ")
elif is_male and not(is_tall):
  print("You are a short male. oOoF!!!") # ELSE-IF or ELIF is commonly used to add another condition
elif not(is_male) and is_tall:
  print("You are a tall lady. <3 ")
else:
  print("You are neither male or tall! ") 


is_male = False
is_tall = False

if is_male and is_tall:
  print("You are a male or tall or both! ")
elif is_male and not(is_tall):
  print("You are a short male. oOoF!!!")
elif not(is_male) and is_tall:
  print("You are a tall lady. <3 ")
else:
  print("You are neither male or tall! ") 


is_male = True
is_tall = True

if is_male and is_tall:
  print("You are a tall male")
elif is_male and not(is_tall):
  print("You are a short male. oOoF!!!")
elif not(is_male) and is_tall:
  print("You are a tall lady. <3 ")
else:
  print("You are neither male or tall! ") 