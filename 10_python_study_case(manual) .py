# Study beginner tasks 
# from https://www.w3resource.com/python-exercises/python-basic-exercises.php 

# THE TASK 
#  Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
# Sample function : abs()
# Expected Result :
# abs(number) -> number
# Return the absolute value of the argument.

# print(abs.__doc__)

user_choice = input("Enter a function name to see the description. ")
print(help(user_choice))

# sample solution print(abs.__doc__)