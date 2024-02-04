# Study beginner tasks 
# from https://www.w3resource.com/python-exercises/python-basic-exercises.php 

# THE TASK 
# Write a Python program that concatenates all elements in a list into a string and returns it.  

#basic method 
basic_list = [1, 2, 3, 4, 5]
element0 = str(basic_list[0])
element1 = str(basic_list[1])
element2 = str(basic_list[2])
element3 = str(basic_list[3])
element4 = str(basic_list[4])

print("Basic method: ")
print(element0 + element1 + element2 + element3 + element4)

# complex method 


# Define a function called concatenate_list_data that takes a list as a parameter.
def conc_list_data(lst):
    result = ''  # Initialize an empty string called result.
    # Iterate through the elements in the list.
    for element in lst:
        result = result + str(element)  # Convert each element to a string and concatenate it to the result.

    return result  # Return the concatenated string.

print(" ") # space 
print("Complex method: ")
print(conc_list_data([1, 5, 12, 2]))