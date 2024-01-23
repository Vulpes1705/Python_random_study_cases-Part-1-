# Study beginner tasks 
# from https://www.w3resource.com/python-exercises/python-basic-exercises.php 

# THE TASK 
# Write a Python program to calculate the difference between a given number and 17. 
# If the number is greater than 17, return twice the absolute difference. 

user_number = int(input("Please enter a number. "))
if user_number <= 17:
    print("Your number is less than 17. ")
    print(17 - int(user_number))

elif user_number > 17:
    print("Your number is greater than 17. ") 
    print(abs((17 - int(user_number))*2))

else:
    ("Something went wrong somehow. ")