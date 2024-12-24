'''
  Section: Section: Python OOP Exercises Part One
  Topic: Create classes for 3 different shapes!
  By: Haqim Maths
  Date: 2024, December 24th

'''

import math

class Shape:
  def calculate_area(self):
    pass
  def calculate_perimeter(self):
    pass

class Circle(Shape):
  PI = 3.14159
  def __init__(self, radius):
    self.__radius = radius
  def set_radius(self, radius):
    self.__radius = radius
  def get_radius(self):
    return self.__radius
  def __str__(self):
    return f'Radius: {self.get_radius()}cm'
  def calculate_area(self):
    return Circle.PI * math.pow(self.get_radius(), 2)
  def calculate_perimeter(self):
    return 2 * Circle.PI * self.get_radius()

class Triangle(Shape):
  def __init__(self, side1, side2, side3):
    self.__side1 = side1 # a (base)
    self.__side2 = side2 # b (height)
    self.__side3 = side3 # c
  def set_side1(self, side1):
    self.__side1 = side1
  def set_side2(self, side2):
    self.__side2 = side2
  def set__side3(self, side3):
    self.__side3 = side3
  def get_side1(self):
    return self.__side1
  def get_side2(self):
    return self.__side2
  def get_side3(self):
    return self.__side3
  def __str__(self):
    return f'Side1: {self.get_side1()}cm | Side2: {self.get_side2()}cm | Side3: {self.get_side3()}cm'
  def calculate_area(self):
    return (1 / 2) * self.get_side1() * self.get_side2()
  def calculate_perimeter(self):
    return self.get_side1() + self.get_side2() + self.get_side3()

class Square(Shape):
  def __init__(self, length):
    self.__length = length
  def set_length(self, length):
    self.__length = length
  def get_length(self):
    return self.__length
  def __str__(self):
    return f'Length: {self.get_length()}cm'
  def calculate_area(self):
    return math.pow(self.get_length(), 2)
  def calculate_perimeter(self):
    return 4 * self.get_length()

# Testings
circle_one = Circle(6)
print(f'Circle one radius: {circle_one}')
print(f'Area: {circle_one.calculate_area()} square cm')
print(f'Perimeter: {circle_one.calculate_perimeter()}cm')
print('Set radius to 10cm')
circle_one.set_radius(10)
print(f'New circle one radius: {circle_one}')
print(f'New Area: {circle_one.calculate_area()} square cm')
print(f'New Perimeter: {circle_one.calculate_perimeter()}cm')
triangle_one = Triangle(10, 20, 30)
print(f'Triangle one bases: {triangle_one}')
print(f'Area: {triangle_one.calculate_area()} square cm')
print(f'Perimeter: {triangle_one.calculate_perimeter()}cm')
square_one = Square(16.45)
print(f'Square one length: {square_one}')
print(f'Area: {square_one.calculate_area()} square cm')
print(f'Perimeter: {square_one.calculate_perimeter()}cm')