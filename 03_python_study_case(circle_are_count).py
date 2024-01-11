# Study beginner tasks 
# from https://www.w3resource.com/python-exercises/python-basic-exercises.php 

# THE TASK 
#  Write a Python program that calculates the area of a circle based on the radius entered by the user.
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504


def count_circle_area(radius):
    radius = float(input("Please enter the circle radius. "))
    area = (3.14159265 * (radius ** 2) )
    print("r = " + str(radius))
    print("Area = " + str(area))

print(count_circle_area(6))

