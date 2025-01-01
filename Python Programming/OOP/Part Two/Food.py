'''
  Section: OOP
  Topic: Food class
  Author: Haqim Maths (https://github.com/HaqimMaths)
  Date: 01/01/2025
'''

class Food:
    def __init__(self, name, price):
      self.name = name
      self.price = price

    def get_name(self):
      return self.name

    def get_price(self):
      return self.price

    def __str__(self):
      return f"Name: {self.name}, Price: {self.price}"
    
Food1 = Food("Macoroni", 10)
Food2 = Food("Sate", 9)
Food3 = Food("Nasi Lemak", 8)
print(f'{Food1}\n{Food2}\n{Food3}')