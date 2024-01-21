# Study beginner tasks 
# from https://www.w3resource.com/python-exercises/python-basic-exercises.php 

# THE TASK 
# Write a Python program that accepts an integer (n) and computes the value of n + nn + nnn.
# Sample value of n is 5
# Expected Result : 615

print("Hello! Please, enter a number. ")
number = input()
result = int(number) + int(number+number) + int(number * 3)

print(result)