from datetime import date

print(date.__doc__)

first_date = date(2014, 7, 2)
second_date = date(2014, 7, 11)
print(f"Differences {first_date - second_date}")