'''
  Section: Section: Python OOP Exercises Part One
  Topic: Calculate the area and perimeter of a circle
  By: Haqim Maths
  Date: 2024, December 24th

'''

PI = 3.14159
import math

class Circle:
  def __init__(self, radius):
    self.__radius = radius
  def get_radius(self):
    return self.__radius
  def calculate_area(self):
    return PI * math.pow(self.__radius, 2)
  def calculate_perimeter(self):
    return 2 * PI * self.__radius

circle = Circle(10)
print(f'Radius of a circle: {circle.get_radius()}cm')
print(f'Area: {circle.calculate_area()}cm')
print(f'Perimeter: {circle.calculate_perimeter()}cm')