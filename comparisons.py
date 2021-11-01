
def max_number(num1, num2, num3):
  if num1 >= num2 and num1 >= num3:
    return num1
  elif num2 >= num1 and num2 >= num3:
    return num2
  else:
    return num3
  
print(max_number(1, 13, 50))

numb1 = input("Enter a first number:\n ")
numb2 = input("Enter a second number:\n ")
def comparison(numb1, numb2):
  if numb1 == numb2:
    return numb1 
    
print(comparison(2,3))

number1 = input("Input your favorite number \n====>")
number2 = input ("Input a random number\n ====>")
if number1 == number2:
  result = int(number1)*int(number2)
  print(result)
else:
  multiply = int(number1)+int(number2)
  print(multiply)