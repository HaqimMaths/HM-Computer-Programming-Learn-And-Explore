'''
  Topic: Python Basics Exercise Part One
  By: Haqim Maths
  Date: 2024, December 21th

'''

numbers_in_text = str(input('Enter numbers seperated by comma: '))
numbers_in_list = numbers_in_text.split(',')
numbers_in_tuple = tuple(numbers_in_list)
print(f"List: {numbers_in_list}")
print(f"Tuple: {numbers_in_tuple}")