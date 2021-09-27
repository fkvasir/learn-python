lucky_numbers = [3, 7, 0, 10, 9]
friends = ["Ricster", "Rexon", "Sharmaine", "Rayne", "Amanie", "Jhoanna", "Jlou"]
friends.extend(lucky_numbers) # extend is the given set of lists to another lists
print(friends)
friends.append("Jin Seyon") # append means to add
print(friends)
friends.insert(7, "Ricster") # all numbers or variables after index 7 are getting pushed to the right
friends.insert(0 , "Fulgent")
print(friends) 
friends.remove("Ricster") # remove the first "Ricster"
print(friends)
friends.clear # empty lists, removes every single element of the list
print(friends)
friends.pop() # pops an element off the list
# POP removes the last element
print(friends.index("Fulgent"))
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse
print(lucky_numbers)