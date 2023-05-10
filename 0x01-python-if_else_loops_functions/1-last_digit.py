#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if number < 0:
    last_digits = "-" +str(last_digit)
else:
    last_digits = str(last_digit)
string = str(number)
if last_digit > 5:
    print("Last digit of " +string+ " is " +last_digits + " and is greater than 5")
elif last_digit == 0:
    print("Last digit of " +string+ " is " +last_digits + " and is 0")
elif last_digit < 6 and last_digit != 0:
    print("Last digit of " +string+ " is " +last_digits + " and is less than 6 and not 0")
