# Study beginner tasks 
# from https://www.w3resource.com/python-exercises/python-basic-exercises.php 

# THE TASK 
# Write a Python program to create a histogram from a given list of integers.  


base_list = []
print("Please enter a number of people working in the department. ")

departments = ["IT", "Sales", "Marketing", "HR", "Security"]

it_members = int(input("How many people are there in " + str(departments[0]) + " "))
sales_members = int(input("How many people are there in " + str(departments[1]) + " "))
marketing_members = int(input("How many people are there in " + str(departments[2]) + " "))
hr_members = int(input("How many people are there in " + str(departments[3]) + " "))
security_members = int(input("How many people are there in " + str(departments[4]) + " "))

print("Here's a histogram of our company employees. ")
print(str(departments[0]))
print("Number of emploees: " + str(it_members))
print("*" * int(it_members))

print(str(departments[1]))
print("Number of emploees: " + str(sales_members))
print("*" * int(sales_members))

print(str(departments[2]))
print("Number of emploees: " + str(marketing_members))
print("*" * int(marketing_members))

print(str(departments[3]))
print("Number of emploees: " + str(hr_members))
print("*" * int(it_members))

print(str(departments[4]))
print("Number of emploees: " +  str(security_members))
print("*" * int(security_members))