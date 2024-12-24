'''
  Section: Section: Python OOP Exercises Part One
  Topic: Display simple details about a person
  By: Haqim Maths
  Date: 2024, December 24th

'''

from datetime import date

class Person:
  def __init__(self, name, country, date_of_birth):
    self.__name = name
    self.__country = country
    self.__date_of_birth = date_of_birth
  def get_name(self):
    return self.__name
  def get_country(self):
    return self.__country
  def get_date_of_birth(self):
    return self.__date_of_birth
  def __str__(self):
    return f'Name: {self.get_name()} | Country: {self.get_country()} | Date of birth: {self.get_date_of_birth()}\n'
  def get_age(self):
    return date.today().year - self.__date_of_birth.year

person_one = Person('Harith', 'Indonesia', date(2003, 10, 9))
print(f'Person One details: {person_one}')
print(f'Age: {person_one.get_age()}')