'''
  Topic: Python Basics Exercise Part Three
  By: Haqim Maths
  Date: 2024, December 22nd

'''

text = str(input('Enter any words: '))
n = int(input('Enter number of copies: '))
result = ""
if len(text) < 2:
  x = 0
  while x < n:
    result += text
    x = x + 1
else:
  x = 0
  while x < n:
    result += text[0]
    result += text[1]
    x = x + 1

print(result)