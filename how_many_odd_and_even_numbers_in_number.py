# study case for the scrypt that analyzes a number
# of odd and even numbers in the user's number 

# Check if the input is integer
def inputInteger(prompt=None):
    while True:
        s = input(prompt)
        try:
            return int(s)
        except ValueError:
            print('Check failed. You have entered an incorrect value. Please try again and enter an integer.')

print("Hello! This programm can check how many odd and even numbers are there in your number. ")

# variables 
number = inputInteger('Enter your number: ')
evens = 0
odds = 0

# Just an imitation of system message
print("Check complete. Proceeding...")



while number > 0:
        counter = number % 10
        if counter % 2 == 0:
            evens = evens + 1
        else:
            odds = odds + 1
        number = number // 10

print("The result is: ")
print("Odds count: " + str(odds))
print("Evens count: " + str(evens))