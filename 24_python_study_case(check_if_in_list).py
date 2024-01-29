# Study beginner tasks 
# from https://www.w3resource.com/python-exercises/python-basic-exercises.php 

# THE TASK 
# Write a Python program that checks whether a specified value is contained within a group of values.
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False

import random #i love random

base_list = []
count = 0
repeater = random.randint(1, 15)
user_choice = input("Please Enter a number. ")

print("Your choice is: " + str(user_choice))

random_number = random.randint(-100, 100)

while count != repeater:
    random_number = random.randint(-100, 100)
    base_list.append(random_number)
    count = count + 1


print("The generated list is: " + str(base_list))

if user_choice in base_list:
    print("Your choice scores! Your number is in this list. ")
elif user_choice not in base_list:
    print("Sorry, your choice did not score. ")
else:
    print("Something went wrong. ")



