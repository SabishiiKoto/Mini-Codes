import random as rd

# File title: Don't Guess My Number
# Feature: You will lose the game when you pick the chosen number.
# How To Play: Play with friends, to see who lose.

number = rd.randint(0,100)

print("I picked a number from 0 to 100!")
min = 0
max = 100
try:
    guess = int(input("Don't pick the number I chose: "))
    while (guess != number):
        if (guess > number):
            max = guess
            guess = int(input("Now pick a number from {} to {}: ".format(min, max)))
        else:
            min = guess
            guess = int(input("Now pick a number from {} to {}: ".format(min, max)))
        
except ValueError as e:
    print("Invalid input!")
print("You are boom. Game is over!")