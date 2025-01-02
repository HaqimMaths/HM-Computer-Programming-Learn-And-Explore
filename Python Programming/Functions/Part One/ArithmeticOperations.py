'''
  Section: Functions
  Topic: Arithmetic Operations
  Author: Haqim Maths (https://github.com/HaqimMaths)
  Date: 02/01/2025
'''

def add(a, b):
    return a + b
def substraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b
def modulo(a, b):
    return a % b

a = input("Enter any number values for a: ")
a = float(a)
b = input("Enter any number values for b: ")
b = float(b)
symbol = input("Enter any arithmetic symbol (+, -, *, /, %): ")

if symbol == "+":
  print(f"Sum of {a} and {b} is {add(a, b)}")
elif symbol == "-":
  print(f"Difference of {a} and {b} is {substraction(a, b)}")
elif symbol == "*":
  print(f"Product of {a} and {b} is {multiplication(a, b)}")
elif symbol == "/":
  print(f"Quotient (Division) of {a} and {b} is {division(a, b)}")
else:
  print(f"Modulo of {a} and {b} is {modulo(int(a), int(b))} remainder")
