# Study beginner tasks 
# from https://www.w3resource.com/python-exercises/python-basic-exercises.php 

# THE TASK 
# Write a Python program that returns a string that is n (non-negative integer) copies of a given string.  

user_line = input("Please enter a line for multiplying. ")
user_count = abs(int(input("How many repeats? ")))
print(user_line * user_count)

