def is_even(n):
  if n % 2 == 0:
    return True
  else:
    return False

n = int(input('Input a number to check its even or not: '))
print(f"The {n} is: {is_even(n)}")