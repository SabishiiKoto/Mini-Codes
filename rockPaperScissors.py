import random as rd

# File title: Rock, Paper, Scissors
# Feature: Generate random item to play rock, paper, scissors

data = ["ROCK", "PAPER", "SCISSORS"]
dataMap = {"1": "ROCK", "2": "PAPER", "3": "SCISSORS"}


def randomChoice():
    randomItem = rd.choice(data)
    return randomItem

def searchChoide(number: str):
    return dataMap.get(number)

print("___Rock, Paper, Scissors Game___")
print("Pick a number to play when get asked!")
print("Input 'STOP' to leave the game!")
choice = input("""
1. Rock
2. Paper
3. Scissors
OR 'STOP' to leave the game.
You pick a number: 
""")
while (choice != "STOP"):
    if (not ("1" <= choice <= "3")):
        print("Choice is not valid! Please input again")
        choice = input("""
1. Rock
2. Paper
3. Scissors
OR 'STOP' to leave the game.
You pick a number: """)
    else:
        randomItem = randomChoice()
        choiceResult = searchChoide(choice)
        
        print("\n--Result--")
        print("You picked " + choiceResult)
        print("I picked " + randomItem)
        if (choice == "1"):  # rock
            if (randomItem == "rock"):
                print("Game is tie")
            elif (randomItem == "paper"):
                print("I win the game. Game over!")
            else:
                print("You win the game. I dare you to play again!")

        elif (choice == "2"):
            if (randomItem == "rock"):
                print("You win the game. I dare you to play again!")
            elif (randomItem == "paper"):
                print("Game is tie")
            else:
                print("I win the game. Game over!")
        else:
            if (randomItem == "rock"):
                print("I win the game. Game over!")
            elif (randomItem == "paper"):
                print("You win the game. I dare you to play again!")
            else:
                print("Game is tie")
        print("\n___Play Again?___")
        again = input("YES (Y) / NO (N): ")
        if (again == "YES" or again == "yes" or again == "Y" or again == "y"):
            choice = input("""
1. Rock
2. Paper
3. Scissors
OR 'STOP' to leave the game.
You pick a number: 
""")
        else:
            break