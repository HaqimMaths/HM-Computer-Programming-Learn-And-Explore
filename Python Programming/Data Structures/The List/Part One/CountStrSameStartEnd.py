'''
  Section: Python The List Exercises Part One
  Topic: Count str same start and end
  By: Haqim Maths
  Date: 2024, December 24th

'''

sample_list = ['abc', 'xyz', 'aba', '1221']

def find_same(text):
  same = 0
  for x in text:
    if(x[0] == x[-1]):
      same += 1
  return same
print(find_same(sample_list))