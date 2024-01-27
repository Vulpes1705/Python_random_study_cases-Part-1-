# Study beginner tasks 
# from https://www.w3resource.com/python-exercises/python-basic-exercises.php 

# THE TASK 
# Write a Python program to count the number 4 in a given list.  


input_string = input("Enter a list of at leaset 4 elements, separated by space. Like this: 4 8 X @ a 3.  ")

list  = input_string.split()
print("Your list is complete:")
print(list)
list_length = len(list)

if len(list) < 4:
    print("You've entered a list which is too short. Please try again. ")
else:
    print("Now choose a number of element to be displayed. ")
    what_element = int(input(" ")) 
    print("Your choise: " + str(list[what_element - 1]))
    print("The fourth element of your list is: ")
    print(list[3])





