# Find the secret 4 digit code in less than 10 tries

# Incorporate the Random Library
import random

# Define variables
first_digit = random.randint(0, 9)
second_digit = random.randint(0, 9)
third_digit = random.randint(0, 9)
fourth_digit = random.randint(0, 9)

guess = int(input("Enter a four-digit number "))

guess_digits = [int(x) for x in str(guess)]
guess1 = guess_digits[0]
guess2 = guess_digits[1]
guess3 = guess_digits[2]
guess4 = guess_digits[3]


