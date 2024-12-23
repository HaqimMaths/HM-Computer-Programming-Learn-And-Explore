'''
  Topic: Python Basics Exercise Part Three
  By: Haqim Maths
  Date: 2024, December 22nd

'''

random_list = [1, 5, 8, 3]
n = int(input('Enter a number to check whether its in my random list bro: '))

def is_there(n):
  return n in random_list

print(f"My list is {random_list}, and is your number there?: {is_there(n)}")