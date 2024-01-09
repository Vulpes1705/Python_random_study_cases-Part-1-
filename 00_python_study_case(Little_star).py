#. Study beginner tasks from https://www.w3resource.com/python-exercises/python-basic-exercises.php 

#THE TASK 
# Write a Python program to print the following string in a specific format (see the output).
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! 
# Up above the world so high, Like a diamond in the sky. 
# Twinkle, twinkle, little star, How I wonder what you are"

# Expected output:

# Twinkle, twinkle, little star,
# 	(8)	How I wonder what you are! 
# 		(16) Up above the world so high,   		
# 		(16) Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
# 	(8)	How I wonder what you are! 

space = "        "
double_space = space * 2
start_line = "Twinkle, twinkle, little star, \n" + space + "How I wonder what you are!\n"

print(start_line)
print(double_space + "Up above the world so high,\n")
print(double_space + "Like a diamond in the sky.\n")
print(start_line)

