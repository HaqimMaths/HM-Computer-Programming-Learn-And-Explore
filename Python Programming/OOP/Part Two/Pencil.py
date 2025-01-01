'''
  Section: OOP
  Topic: Pencil class
  Author: Haqim Maths (https://github.com/HaqimMaths)
  Date: 01/01/2025
'''

class Pencil:
    def __init__(self, brand, price):
      self.brand = brand
      self.price = price

    def get_brand(self):
      return self.brand

    def get_price(self):
      return self.price

    def __str__(self):
      return f"Brand: {self.brand}, Price: {self.price}"

Pencil1 = Pencil("Faber Castell", 5)
Pencil2 = Pencil("Stabilo", 4)
Pencil3 = Pencil("Pilot", 3)
print(f'{Pencil1}\n{Pencil2}\n{Pencil3}')