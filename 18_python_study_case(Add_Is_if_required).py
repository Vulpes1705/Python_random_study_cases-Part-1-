# Study beginner tasks 
# from https://www.w3resource.com/python-exercises/python-basic-exercises.php 

# THE TASK 
# Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. 
# Return the string unchanged if the given string already begins with "Is". 


print("This script will add \"Is\" if required. ")
user_input = input("Enter a string. ")

if user_input[0] == "I" and user_input[1] == "s":
    print("No \"Is\" addition required")
    print(user_input)
else: 
    print("\"Is\" was added to your string. ")
    print("Is" + user_input)