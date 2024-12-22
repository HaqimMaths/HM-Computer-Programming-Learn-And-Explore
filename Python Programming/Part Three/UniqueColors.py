'''
  Topic: Python Basics Exercise Part Three
  By: Haqim Maths
  Date: 2024, December 22nd

'''

color_list_one = str(input('Enter different colors for first list seperated by comma: '))
color_list_one = set(color.strip() for color in color_list_one.split(","))
color_list_two = str(input('Enter different colors for second list seperated by comma: '))
color_list_two = set(color.strip() for color in color_list_two.split(","))

print('Diff between color one and color two: ')
print(color_list_one.difference(color_list_two))
print('Diff between color two and color one: ')
print(color_list_two.difference(color_list_one))