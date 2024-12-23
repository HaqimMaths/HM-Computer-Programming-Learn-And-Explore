'''
  Topic: Python Basics Exercise Part Three
  By: Haqim Maths
  Date: 2024, December 22nd

'''

input_data = input('Enter numbers or words seperated by comma (,): ')
input_list = input_data.split(',')

def concat_str(list):
  result = ''
  for x in list:
    result = result + x

  return result

print(f"Your list: {input_list}")
print(f"Your concat list: {concat_str(input_list).replace(' ', '')}")