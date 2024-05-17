#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
l_d = number % 10
l_d_n = l_d - 10

if number>0:
    if l_d > 5:
        print("Last digit of", number, "is", l_d, "and is greater than 5")
    elif l_d == 0:
        print("Last digit of", number, "is", l_d, "and is 0")
    else:
        print("Last digit of", number, "is", l_d, "and is less than 6 and not 0")
elif number == 0:
        print("Last digit of", number, "is", l_d, "and is 0")
else:
    if l_d_n == 0:
        print("Last digit of", number, "is", l_d_n, "and is 0")
    else:
        print("Last digit of", number, "is", l_d_n, "and is less than 6 and not 0")
