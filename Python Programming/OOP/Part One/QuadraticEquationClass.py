'''
  Section: Section: Python OOP Exercises Part One
  Topic: Quadratic Equation Class
  By: Haqim Maths
  Date: 2024, December 24th

'''

class QuadraticEquation:
  __a = 0
  __b = 0
  __c = 0
  @classmethod
  def set_coefficients(cls, a, b, c):
    cls.__a = a
    cls.__b = b
    cls.__c = c
  @classmethod
  def get_a(cls):
    return cls.__a
  @classmethod
  def get_b(cls):
    return cls.__b
  @classmethod
  def get_c(cls):
    return cls.__c
  @classmethod
  def get_result(cls):
    import math
    discriminant = math.pow(cls.__b, 2) - 4 * cls.__a * cls.__c
    x1 = -cls.__b + math.sqrt(discriminant) / (2 * cls.__a)
    x2 = -cls.__b - math.sqrt(discriminant) / (2 * cls.__a)
    return f'x1: {x1}\n x2: {x2}'

print(QuadraticEquation._QuadraticEquation__a)
QuadraticEquation.set_coefficients(1, -3, 2)
print(QuadraticEquation.get_result())