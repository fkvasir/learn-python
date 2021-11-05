print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

num1 = float(input("Enter first no.:\n"))

op = input("Enter operator: ")

num2 = float(input("Enter second no.:\n"))


if op == "+":
  print(num1 + num2)

elif op == "-":

  print(num1 - num2)

elif op == "*":
  print(num1 * num2)

elif op == "/":
  print(num1 / num2)

else:
  print("Invalid")
  
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

number1 = float(input("Enter any number of your choice:\n----->"))

operator = input("Enter what mathematical operations do you want to perform: ")

number2 = float(input("Input a number that you like:\n----->"))

if operator == "add" or operator == "addition" or operator == "+":
# //add-->float//
  print(float(number1 + number2))

elif operator == "subtract" or operator == "subtraction" or operator == "-":
# //subtract --> float//
  print(float(number1 - number2))

elif operator == "modul" or operator =="%":
  print(int(number1 % number2))

elif operator == "multiply" or operator == "multiplication" or operator == "*":
# //multiplication --> float// else-if
  print(float(number1 * number2))

elif operator == "divide" or operator == "division" or operator == "/":
# //divide --> float//
  print(float(number1/number2))

else:
# // no mathematical operations//
  print("Get the fuck outta here!!")
