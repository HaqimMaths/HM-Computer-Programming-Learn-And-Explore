'''
  Section: Python The List Exercises Part One
  Topic: Largest integer in a list
  By: Haqim Maths
  Date: 2024, December 24th

'''

integers = input('Enter as many integers as you can! and seperated it by comma or other values also can!:\n')
import re
integers_cleaned = re.sub(r'[^0-9.,]', '', integers)
integers_list = [int(integer) for integer in integers_cleaned.split(',') if integer.split()]
print(f'Your list: {integers_list}')
MAX_INT = integers_list[0]
for x in integers_list:
  if(MAX_INT < x):
    MAX_INT = x

print(f'The largest int inside your list is: {MAX_INT}')