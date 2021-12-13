open("file.txt", "r")# read
open("file.txt", "w")# write
open("file.txt", "a")# append - cant change anything in the file but can add new information
open("file.txt", "r+")# all the power of reading and writing
"""
The sample above lets you open, read, write or append file. 
"""
sample_file = open("file.txt", "r")

print(sample_file.readline())
print(sample_file.readline())

sample_file.close() 