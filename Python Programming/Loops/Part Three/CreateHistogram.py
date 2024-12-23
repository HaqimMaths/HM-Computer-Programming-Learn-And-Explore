'''
  Topic: Python Basics Exercise Part Three
  By: Haqim Maths
  Date: 2024, December 22nd

'''

symbol = str(input('Lets create a histogram by using your symbol: '))
total_bars = int(input('Enter the total bars: '))
inputted = 0
format_histogram = [0] * total_bars
while inputted < total_bars:
  format_histogram[inputted] = int(input(f'Enter the length for bar {inputted + 1}: '))
  inputted = inputted + 1

print('Your histogram: ')

completed = 0
while completed < len(format_histogram):
  print(symbol * format_histogram[completed])
  completed = completed + 1