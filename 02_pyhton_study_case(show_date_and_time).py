# Study beginner tasks 
# from https://www.w3resource.com/python-exercises/python-basic-exercises.php 

# THE TASK 
#  Write a Python program to display the current date and time.
# Sample Output :
# Current date and time :
# 2014-07-05 14:34:14

from datetime import datetime

# # datetime object containing current date and time
now = datetime.now()


# dd/mm/YY H:M:S
dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
print("Current date and time: ", dt_string)
