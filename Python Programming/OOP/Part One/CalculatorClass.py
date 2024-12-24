'''
  Section: Python OOP Exercises Part One
  Topic: Simple Arithmetic Calculator
  By: Haqim Maths
  Date: 2024, December 24th

'''

class Calculator:
  @staticmethod
  def add(a, b):
    return a + b
  @staticmethod
  def minus(a, b):
    return a - b
  @staticmethod
  def multiply(a, b):
    return a * b
  @staticmethod
  def divide(a, b):
    return a / b
  @staticmethod
  def modulo(a, b):
    return a % b

print(f'10 + 9.8 = {Calculator.add(10, 9.8)}')
print(f'90.2 - 81.3 = {Calculator.minus(90.2, 81.3)}')
print(f'16.5 * 32 = {Calculator.multiply(16.5, 32)}')
print(f'20.31 / 239.1 = {Calculator.divide(20.31, 239.1)}')
print('20 %% 2 = %d' % Calculator.modulo(20, 2))