#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
last_digit_negative = last_digit - 10

if number>0:
    if last_digit > 5:
        print("Last digit of", number, "is", last_digit, "and is greater than 5")
    elif last_digit == 0:
        print("Last digit of", number, "is", last_digit, "and is 0")
    else:
        print("Last digit of", number, "is", last_digit, "and is less than 6 and not 0")
elif number == 0:
        print("Last digit of", number, "is", last_digit, "and is 0")
else:
    if last_digit_negative == 0:
        print("Last digit of", number, "is", last_digit_negative, "and is 0")
    else:
        print("Last digit of", number, "is", last_digit_negative, "and is less than 6 and not 0")
        