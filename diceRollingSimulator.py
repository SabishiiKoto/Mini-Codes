import random as rd

# File title: Dice Rolling Simulator
# Feature: Rolling dice(s) with customize range

print("___Dice Rolling Simulator___")

try:
    playAgain = True
    min = 1
    max = 6
    while (playAgain == True):
        loop = int(input("Enter the number of dices you want to roll: "))
        i = 0
        print("\nDo you want to customize the dices? ")
        customizeDice = input("Enter 'Yes' (Y) or 'No' (N): ")
        if (customizeDice == "Yes" or customizeDice == "YES" or customizeDice == "Y" or customizeDice == "y"):
            min = int(input("\nEnter the smallest value of the dice: "))
            max = int(input("Enter the biggest value of the dice: "))
            for i in range(loop):
                randomNumber = rd.randint(min, max)
                print("{}: {}".format(i + 1, randomNumber))
        else:
            for i in range(loop):
                randomNumber = rd.randint(min,max)
                print("{}: {}".format(i + 1, randomNumber))
        print("\n___Play Again?___")
        again = input("YES (Y) / NO (N): ")
        if (again == "YES" or again == "yes" or again == "Y" or again == "y"):
            playAgain = True
        else:
            playAgain = False
except ValueError:
    print("Invalid input!")