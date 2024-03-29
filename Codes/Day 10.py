#Basic Calculator
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1*n2
  
def divide(n1, n2):
  if n2 == 0:
    return "You can't divide by 0"
  else:
    return n1/n2

dict = {
"+" : add,
"-" : subtract,
"*" : multiply,
"/" : divide
  
}


def calculator():
  num1 = float(input("What is the first number?"))
  for key in dict:
    print (key)
  should_continue = True
  
  while should_continue:
    operational_symbol = input("Pick an operation")
    num2 = float(input("What is the second number?"))
    calculation_function = dict[operational_symbol]
    answer = calculation_function(num1, num2)
      
    print(f"{num1} {operational_symbol} {num2} = {answer}")
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()
