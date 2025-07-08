# File Title: Word Counter
# Feature: Count the total words and characters of the input text.

print("___Word Counter___")

def wordCount(string: str):
    list = str.split(" ")
    return len(list)

def charCount(string: str):
    return len(string)

str = input("Input the text: ")
words = wordCount(str)
char = charCount(str)
print("\nRESULT:")
print("{} words".format(words))
print("{} characters".format(char))