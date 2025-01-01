'''
  Section: Functions
  Topic: Swap Number
  Author: Haqim Maths (https://github.com/HaqimMaths)
  Date: 01/01/2025
'''

def swap_number(a, b):
    a, b = b, a
    return a, b
a = 10
b = 20
print(f"Before swap: a = {a}, b = {b}")
a, b = swap_number(a, b)
print(f"After swap: a = {a}, b = {b}")
