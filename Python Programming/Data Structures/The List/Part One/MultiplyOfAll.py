'''
  Section: Python The List Exercises Part One
  Topic: Multiply all items inside a list
  By: Haqim Maths
  Date: 2024, December 24th

'''

import re

numbers = input("Input numbers seperated by Hashtag(#): ")
numbers_cleaned = re.sub(r'[^0-9.,]', '', numbers)
numbers_list = [float(num.strip()) for num in numbers_cleaned.split(',') if num.strip()]
sum = 1
for x in numbers_list:
  sum *= x

print(f'Values inside the list: {numbers_list}')
print(f'Sum of all multiply: {sum}')