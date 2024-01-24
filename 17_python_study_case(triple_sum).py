# Study beginner tasks 
# from https://www.w3resource.com/python-exercises/python-basic-exercises.php 

# THE TASK 
# Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.  


user_number1 = int(input("Please enter the first number. "))
user_number2 = int(input("Please enter the second number. "))
user_number3 = int(input("Please enter the third number. "))
sum = user_number1 + user_number2 + user_number3

if user_number1 == user_number2 == user_number3:
    print("Wow! You've unlocked a secret bonus. Sum is multiplied thrice. ")
    print(sum * 3)
else:
    print("Here's the sum of these numbers. ")
    print(sum)