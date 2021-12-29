examplefile = open("file.txt", "r")
print(examplefile.read())
examplefile.close()

examplefile = open("file.txt", "a")
examplefile.write("Michael - Physical Education")
examplefile.close()
