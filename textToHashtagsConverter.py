# File Title: Text To Hashtags Converter
# Feature: Instead of writing #Hi_there, write Hi there

print("___Text To Hashtags Converter___")
print("\nIf there are multiple hashtags, separated each by a double space.")
inputText = input("Enter the text: ")

separator = "_"
print("If you want to customize the separator between each word in a hashtag (like #Hi=there)")
customize = input ("Enter 'Y' or 'y': ")
if (customize == "Y" or customize == "y"):
    separator = input("Enter the new separator: ")


textList = inputText.split("  ")

for i in textList:
    i = i.replace(" ", separator)
    result = "#" + i
    print(result)