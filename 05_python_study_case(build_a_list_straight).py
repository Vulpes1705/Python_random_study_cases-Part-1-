# Study beginner tasks 
# from https://www.w3resource.com/python-exercises/python-basic-exercises.php 

# THE TASK 
#  Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

# user_input = "1, 2, 3"

# list_example = [int(item) for item in user_input.split(",")]
# print(list_example)



user_input = input(" Please enter some numbers divided by commas. \n Like this: 1, 2, 3 \n And i will transform them into a list. ")

def tranform_my_stringed_numbers_into_list(user_input):
    example_list = [int(item) for item in user_input.split(",")]
    print(example_list)

print(tranform_my_stringed_numbers_into_list(user_input))




# print("Your list of numbers is: ", numbers)


# user_input = input("Enter a number for a list or enter empty space (\" \") to stop. ")

# print(user_input)

