# Study beginner tasks 
# from https://www.w3resource.com/python-exercises/python-basic-exercises.php 

# THE TASK 
#  Write a Python program to test whether a number is within 100 of 1000 or 2000.  
# 900-1000-1100 or 1900 - 2100 

user_number = int(input("Please enter the number to check if it belongs to the ranges 900-1100 or 1900-2100. "))
print("Your number is " + str(user_number))
if user_number in range(900, 1101):  # +1 так как иначе не срабатывает граничное значение 
    print("Your number is somewhere between 900 and 1100. ")
elif user_number in range(1900, 2101): # +1 так как иначе не срабатывает граничное значение 
    print("Your number is somewhere between 1900 and 2100. ")
else: 
    print("Your number is out of specified range.")
