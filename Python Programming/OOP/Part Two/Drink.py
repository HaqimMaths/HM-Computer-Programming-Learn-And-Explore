'''
  Section: OOP
  Topic: Drink class
  Author: Haqim Maths (https://github.com/HaqimMaths)
  Date: 01/01/2025
'''

class Drink:
    def __init__(self, name, price):
      self.name = name
      self.price = price

    def get_name(self):
      return self.name

    def get_price(self):
      return self.price

    def __str__(self):
      return f"Name: {self.name}, Price: {self.price}"

Drink1 = Drink("Milo", 2)
Drink2 = Drink("Teh Tarik", 1)
Drink3 = Drink("Kopi O", 1)
print(f'{Drink1}\n{Drink2}\n{Drink3}')