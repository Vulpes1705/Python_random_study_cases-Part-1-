# Study beginner tasks 
# from https://www.w3resource.com/python-exercises/python-basic-exercises.php 

# THE TASK 
#  Write a Python program to print all even numbers from a given list of numbers in the same order and stop printing any after 237 in the sequence.
# Sample numbers list :

number_list = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

number_list2 = [    
    36, 461, 40, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 757, 215, 913, 232, 412, 564, 823, 28, 61, 951, 623, 947, 683, 211, 
    815, 67, 104, 237, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]

even_numbers = []

def print_even_numbers(numbers):
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
            
        if num == 237:
            print(even_numbers)
            break

# Example usage:

print_even_numbers(number_list)

print_even_numbers(number_list2)
