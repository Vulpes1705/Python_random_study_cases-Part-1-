# Study beginner tasks 
# from https://www.w3resource.com/python-exercises/python-basic-exercises.php 

# THE TASK 
#  Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user. 


user_number = int(input("Please enter a number. We'll tell if it's odd or even. "))
check = user_number % 2

if check == 0:
    print("Your number is even. ")
elif check == 1:
    print("Your number is odd. ")
else:
    print("Something went wrong. You were not supposed to see this message. ")
