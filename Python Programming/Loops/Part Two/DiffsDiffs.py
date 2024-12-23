import math

print(math.__doc__)

def difference_seventeen(n):
  if n <= 17:
    return abs(n - 17)
  else:
    return (n - 17) * 2

print(difference_seventeen(10))
print(difference_seventeen(39))