'''
  Topic: Python Basics Exercise Part Three
  By: Haqim Maths
  Date: 2024, December 22nd

'''

base = float(input('Enter the base for triangle: '))
height = float(input('Enter the height for triangle: '))

def calc_area(base, height):
  return (1 / 2) * (base * height)

print(f'The area of your triangle is: {calc_area(base, height)} square units')