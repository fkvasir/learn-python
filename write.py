examplefile = open("file.txt", "r")
print(examplefile.read())
examplefile.close()

examplefile = open("file.txt", "a")
examplefile.write("\nKelly - Biology")
examplefile.close()

