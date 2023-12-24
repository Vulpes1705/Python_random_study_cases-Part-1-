# This programm can reverse-transform any digit
# Like 12345678 will be transform into 87654321 etc 

user_number = (int(input("Enter your number, please. ")))
sum = 0

while user_number > 0:
    current_state = user_number % 10
    sum = sum * 10 + current_state
    user_number = user_number // 10

print(sum)



