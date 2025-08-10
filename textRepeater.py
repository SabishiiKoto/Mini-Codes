# File Title: Text Repeater
# Feature: Repeat a text multiple times.

print("___Text Repeater___")

repeatTime = input("Enter number of repetitions: ")

try:
    result = ""
    repeatTime = int(repeatTime)
    text = input("Enter the text: ")
    separator = input("Enter the separator between repetitions (double space for new line): ")
    if separator == "  ":
        separator = "\n"
    for i in range(repeatTime - 1):
        result += text + separator
        
    result += text
    print(result)
    
except ValueError:
    print("\nPlease input a number!")