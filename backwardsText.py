# File Title: Backwards Text Generator
# Feature: Generate backwards version of the input text.

print("___Backwards Text Generator___")

inputText = input("Enter the text: ")
result = ""
for i in range(len(inputText) - 1, -1, -1):
    result += inputText[i]
    
print("The reversed text is: "+ result)
if result == inputText:
    print("It's a palindrome word!")
    