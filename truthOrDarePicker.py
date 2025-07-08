# File Title: Truth or Dare Picker
# Feature: 
# - It will randomly pick a number or a name of a person (if it is given) for the truth or dare game.
# - A dare will be forced after three truths are chosen, and vice versa.

import random as rd

print("___Truth or Dare Picker___")


data = []

def pickFromData():
    randomItem = rd.choice(data)
    return randomItem

try:
    truth = 0
    dare = 0
    loop = int(input("Enter the number of people: "))
    if (loop > 0):
        customize = input("""
Do you want to input the name of each person?
Enter 'YES' (Y) or 'NO' (N): 
""")
        if (customize == 'Yes' or customize == "YES" or customize == "Y" or customize == "y"):
            for i in range(loop):
                name = input("Enter person {}'s name: ".format(i+1))
                data.append(name)
                
        else:
            for i in range(loop):
                data.append(i + 1)
        playAgain = True
        while (playAgain):
            randomItem = pickFromData()
            print("\n{} is picked.".format(randomItem))
            if (truth < 3 and dare < 3):
                choice = input("Enter 'Truth' (T) or 'Dare' (D): ")
                if ((choice == "Truth" or choice == "T" or choice == "t") and truth < 3):
                    truth += 1
                    dare = 0
                    print("{} chose TRUTH".format(randomItem))
                else:
                    dare += 1
                    truth = 0
                    print("{} chose DARE".format(randomItem))
            elif (truth >= 3):
                print("{} have to choose DARE".format(randomItem))
                truth = 0
                dare += 1
            elif (dare >= 3):
                print("{} have to choose TRUTH".format(randomItem))
                truth += 1
                dare = 0
            print("__Continue?__")
            again = input("Enter 'Yes' (Y) or 'No' (N): ")
            if (again == 'No' or again == 'N' or again == 'n'):
                playAgain = False
            
except ValueError:
    print("Invalid input!")
