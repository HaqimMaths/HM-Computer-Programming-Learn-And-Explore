'''
  Section: Python The List Exercises Part One
  Topic: Smallest integer inside a list
  By: Haqim Maths
  Date: 2024, December 24th

'''

integers = input('Enter integers seperated by comma: \n')
import re
integers_cleaned = re.sub(r'[^0-9.,-]', '', integers)
integers_list = [int(integer) for integer in integers_cleaned.split(',') if integer.split()]
MIN_INT = integers_list[0]
for x in integers_list:
  if MIN_INT > x:
    MIN_INT = x

print(f'Your list: {integers_list}')
print(f'Smallest value: {MIN_INT}')