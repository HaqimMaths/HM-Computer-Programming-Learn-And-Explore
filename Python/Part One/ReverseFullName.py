'''
  Topic: Python Basics Exercise Part One
  By: Haqim Maths
  Date: 2024, December 21th

'''

first_name = str(input('Enter first name: '))
last_name = str(input('Enter last name: '))
reversed_first_name = ''
reversed_last_name = ''
for x in range(len(first_name)):
#  //print(x)
  reversed_first_name += first_name[len(first_name) - 1 - x]
for x in range(len(last_name)):
#  //print(x)
  reversed_last_name += last_name[len(last_name) - 1 - x]

print(reversed_last_name + " " + reversed_first_name)

#Second method

'''# Input string
input_string = "Hello, World!"

# Initialize an empty string to store the reversed string
reversed_string = ""

# Iterate over the input string in reverse order
for char in input_string[::-1]:
    reversed_string += char

# Print the reversed string
print("Reversed string:", reversed_string)
'''