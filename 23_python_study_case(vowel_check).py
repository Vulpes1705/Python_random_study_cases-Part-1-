# Study beginner tasks 
# from https://www.w3resource.com/python-exercises/python-basic-exercises.php 

# THE TASK 
#  Write a Python program to test whether a passed letter is a vowel or not.  

letter = input("Please enter a letter. ")
vowels = ("a", "e", "i", "o", "u", "y", "а", "е", "ё", "и", "й", "о", "у", "э", "ы", "ю", "я")

if letter in vowels:
    print("Yes! It's a vowel. ")
else:
    print("No! It's not a vowel. ")