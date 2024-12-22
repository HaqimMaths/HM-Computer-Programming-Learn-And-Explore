'''
  Topic: Python Basics Exercise Part Three
  By: Haqim Maths
  Date: 2024, December 22nd

'''

def count_four(n):
  count = 0
  for num in n:
    if num == 4:
      count += 1

  return count

print(count_four([1,2,3,4,5,6,7,8,9]))
print(count_four([1,2,4,4,4,4,4,4,3,3,2,1,2,4]))