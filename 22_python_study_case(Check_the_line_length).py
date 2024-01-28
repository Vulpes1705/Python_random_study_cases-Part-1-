# Study beginner tasks 
# from https://www.w3resource.com/python-exercises/python-basic-exercises.php 

# THE TASK 
#  Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. 
# Return n copies of the whole string if the length is less than 2.  


# check if the string less is less than 2
# if yes -  "string" * n 
# if no - "st" * n

user_string = input("Please enter a string for a check. ")
n = abs(int(input("How many repeats? ")))

if len(user_string) < 2:
    print("short line! " + str(n) + " repeats.")
    print(user_string * n)

else:
    print("normal line! " + str(n) +  " repeats.")
    print((user_string[:2]) * n)