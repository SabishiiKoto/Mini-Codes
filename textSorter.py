# File Title: Text Sorter
# Feature: Sort text and print in it in line-separated list.

import random as rd

def toUppercaseFirstChar (char: str):
    number = ord(char[0])
    if 97 <= number <= 122:
        number -= 32
        return chr(number) + char[1:]
    return char
    
print("___Text Sorter___")

menu = """
--SELECT ONE--
1. A-Z
2. Z-A
3. In Reverse Order
4. Randomize
5. Just print the list"""

print(menu)
choice = input("Enter your choice: ")


print("\n--Text--")
print("Separated each new item with a comma")
inputText = input("Enter the list: ")

if " " in inputText:
    inputText = inputText.replace(', ', ',')


textList = inputText.split(",")


print("\n--Result--")

# A-Z
if choice == "1":
    textList.sort()
    for i in textList:
        print(toUppercaseFirstChar(i))

# Z-A
elif choice == "2":
    textList.sort()
    for i in range(len(textList) - 1, -1, -1):
        print(toUppercaseFirstChar(textList[i]))

# Reverse order
elif choice == "3":
    for i in range(len(textList) - 1, -1, -1):
        print(toUppercaseFirstChar(textList[i]))

# Randomize
elif choice == "4":
    while len(textList) > 0:
        randomIndex = rd.randint(0,len(textList) - 1)
        print(toUppercaseFirstChar(textList[randomIndex]))
        textList.pop(randomIndex)

# Just print the list      
elif choice == "5":
    for i in textList:
        print(toUppercaseFirstChar(i))
        
else:
    print("Invalid input!")
        