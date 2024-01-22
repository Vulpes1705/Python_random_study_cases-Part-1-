# Study beginner tasks 
# from https://www.w3resource.com/python-exercises/python-basic-exercises.php 

# THE TASK 
#  Write a Python program that prints the calendar for a given month and year.
# Note : Use 'calendar' module. 

import calendar

year = int(input("Please enter the year. "))
month = int(input("Please enter the month. "))
print(" ") #empty line
print("Year chosen: ")
print(year)
print("Month chosen: ")
print(month)
print(" ") #empty line
result = calendar.monthcalendar(year, month)
print(result)
