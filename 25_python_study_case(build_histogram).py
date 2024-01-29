# Study beginner tasks 
# from https://www.w3resource.com/python-exercises/python-basic-exercises.php 

# THE TASK 
# Write a Python program to create a histogram from a given list of integers.  


# a slight upgrade of this task.  

base_list = []
print("Please enter a value (number) to add to the list. ")

user_input = int(input("Enter your number. "))

while len(base_list) <= 10:
    base_list.append(user_input)
    print(base_list)
    user_input = int(input("Add another one. "))
print("Histogram: ")

line1 = str((base_list)[0])
line2 = str((base_list)[1])
line3 = str((base_list)[2])
line4 = str((base_list)[3])
line5 = str((base_list)[4])
line6 = str((base_list)[5])
line7 = str((base_list)[6])
line8 = str((base_list)[7])
line9 = str((base_list)[8])
line10 = str((base_list)[9])

print("*" * int((base_list)[0]))
print("*" * int((base_list)[1]))
print("*" * int((base_list)[3]))
print("*" * int((base_list)[4]))
print("*" * int((base_list)[2]))
print("*" * int((base_list)[5]))
print("*" * int((base_list)[6]))
print("*" * int((base_list)[7]))
print("*" * int((base_list)[8]))
print("*" * int((base_list)[9]))