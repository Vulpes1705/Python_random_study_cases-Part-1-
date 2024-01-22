# Study beginner tasks 
# from https://www.w3resource.com/python-exercises/python-basic-exercises.php 

# THE TASK 
# Write a Python program to calculate the number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days 

import datetime
from datetime import date

year1 = int(input("Enter the year for the first date. "))
month1 = int(input("Enter the month for the first date. (1-12)"))
day1 = int(input("Enter the day for the first date. (1-31)"))

year2 = int(input("Enter the year for the second date. "))
month2 = int(input("Enter the month for the second date. (1-12) "))
day2 = int(input("Enter the day for the second date. (1-31)"))

first_date = date(year1,month1,day1)
second_date = date(year2,month2,day2)
difference_in_days = (first_date - second_date).days

print("The difference between: ")
print(first_date)
print("and")
print(second_date)
print("is " + str(difference_in_days) + " days.")




