'''
  Section: Functions
  Topic: Concat Fname and Lname
  Author: Haqim Maths (https://github.com/HaqimMaths)
  Date: 01/01/2025
'''

def concat_fname_and_lname(fname, lname):
    return f"{fname} {lname}"

fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
print(f"Your full name is {concat_fname_and_lname(fname, lname)}")
