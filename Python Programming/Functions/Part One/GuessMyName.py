'''
  Section: Functions
  Topic: Guess My Name!
  Author: Haqim Maths (https://github.com/HaqimMaths)
  Date: 01/01/2025
'''

def guess_my_name(name):
  if name.lower() == "haqim":
    return True
  else:
    return False

name = input("Guess my name: ")
while(not guess_my_name(name)):
  name = input("Wrong! Guess my name again: ")
print("Correct! My name is Haqim")