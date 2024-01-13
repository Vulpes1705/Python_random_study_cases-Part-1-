# Study beginner tasks 
# from https://www.w3resource.com/python-exercises/python-basic-exercises.php 

# THE TASK 
#  Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

# Advanced version - user enters some random stuff and can complete the list fillment after sending an empty line. 

user_list = []
user_choice = input("Enter a number.")
user_list.append(user_choice)

while user_choice != "":
    print("Enter another number or an empty line to stop")
    user_choice = input("Enter a number.")
    user_list.append(user_choice)

user_list.pop()    
print("The final list is: " + str(user_list))



