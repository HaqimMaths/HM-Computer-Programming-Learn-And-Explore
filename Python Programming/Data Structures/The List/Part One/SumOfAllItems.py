'''
  Section: Python The List Exercises Part One
  Topic: Sum of all numbers inside a list
  By: Haqim Maths
  Date: 2024, December 24th

'''

numbers = input('Enter numbers seperated by comma: ')
numbers_list = [int(num.strip()) for num in numbers.split(',') if num.strip()]
result = 0
for x in numbers_list:
  result += x

print(result)