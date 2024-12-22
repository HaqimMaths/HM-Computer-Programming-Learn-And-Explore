'''
  Topic: Python Basics Exercise Part One
  By: Haqim Maths
  Date: 2024, December 21th

'''

a = int(input('Enter an integer: '))

n1 = int("%s" % a)
n2 = int("%s%s" % (a, a))
n3 = int("%s%s%s" % (a, a, a))

print(f'Result: {n1 + n2 + n3}')