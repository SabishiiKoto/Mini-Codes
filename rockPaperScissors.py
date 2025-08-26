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
choice = input("""
\tSELECT CHOICE
1. Rock
2. Paper
3. Scissors
OR 'STOP' to leave the game.
You pick a number: """)
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
            if (randomItem == "ROCK"):
                print("Game is tie")
            elif (randomItem == "PAPER"):
                print("I win the game. Game over!")
            else:
                print("You win the game. I dare you to play again!")

        elif (choice == "2"):
            if (randomItem == "ROCK"):
                print("You win the game. I dare you to play again!")
            elif (randomItem == "PAPER"):
                print("Game is tie")
            else:
                print("I win the game. Game over!")
        else:
            if (randomItem == "ROCK"):
                print("I win the game. Game over!")
            elif (randomItem == "PAPER"):
                print("You win the game. I dare you to play again!")
            else:
                print("Game is tie")
        choice = input("""
\tSELECT CHOICE
1. Rock
2. Paper
3. Scissors
OR 'STOP' to leave the game.
You pick a number: """)
    