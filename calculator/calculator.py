#### CALCULATOR
#In this code, I created a basic calculator. It performs addition, subtraction, multiplication, and division.

from art_calculator import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for key in operations:
    print(key)
  # operation_symbol = input("Please choose an operation?: ")
  # calculation_function = operations[operation_symbol]
  # result = calculation_function(num1,num2)
  # print(f"{num1} {operation_symbol} {num2} = {result}")

  continue_calculating = True

  while continue_calculating:
    operation_symbol = input("Please choose an operation?: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    result = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {result}")

    if input(f"Type 'y' to continue calculating with {result}, 'n' to exit: ") == 'y':
      num1 = result
    else:
      continue_calculating = False
      calculator()

calculator()