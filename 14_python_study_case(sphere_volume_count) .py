# Study beginner tasks 
# from https://www.w3resource.com/python-exercises/python-basic-exercises.php 

# THE TASK 
# Write a Python program to get the volume of a sphere with radius six.
# Let radius be user input value

# hint - formula: V = 4/3 π r³, 

radius = int(input("Enter the number for the sphere radius value. "))
cube_radius = radius ** 3
pi = 3.1415
sphere_volume = (4/3) * pi * cube_radius

print("The volume of desired sphere is: ")
print(sphere_volume)
