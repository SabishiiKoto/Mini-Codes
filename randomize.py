# File Title: Random Picker
# Feature: Input options, and it will pick a random one.
# (Run code in terminal, not IntelliJ because the effect might not work).

import random as rd
import os
import time

print("___Random Picker___")
loop = 0
try:
    loop = int(input("Enter number of options: "))
except ValueError:
    print("Input error.")
    
lst = []
history = []

for i in range(loop):
    item = input("Enter option {}: ".format(i + 1))
    lst.append(item)

again = True
while again:
    chosenOption = ""
    if len(lst) > 1:
        for i in range(10):
            chosenOption = rd.choice(lst)
            os.system('cls' if os.name == 'nt' else 'clear')
            print("CHOSEN OPTION: {}".format(chosenOption))
            time.sleep(0.2)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        chosenOption = lst[0]
        print("CHOSEN OPTION: {}".format(lst[0]))

    history.append(chosenOption)
    lst.remove(chosenOption)

    if len(lst) == 0:
        again = False
        
    else:
        choice = input("Enter to continue or 'STOP' to exit: ")
        if choice == "STOP":
            again = False
        else:
            again = True

i = 1
print("\n--Pick History--")
for item in history:
    print("{}. {}".format(i,item))
    i += 1
    
print("End of program.\n")