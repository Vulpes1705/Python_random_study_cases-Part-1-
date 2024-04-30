import random

d6_range = [1, 2, 3, 4, 5, 6]
d20_range = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
number_of_d6 = 0
number_of_d20 = 0
#dice_result = random.choice(d6_range)

def roll_some_dice(number_of_d6, number_of_d20):
    number_of_d6 = int(input("How many d6 to roll? "))
    number_of_d20 = int(input("How many d20 to roll? "))
    print("You've rolled " + str(number_of_d6) + " d6's and " + str(number_of_d20) + " d20's." )
    while number_of_d6 > 0:
        print("D6 result = " + str(random.choice(d6_range)))
        number_of_d6 = number_of_d6 - 1
    while number_of_d20 > 0:
        print("D20 result = " + str(random.choice(d20_range)))
        number_of_d20 = number_of_d20 - 1

roll_some_dice(number_of_d6, number_of_d20)
