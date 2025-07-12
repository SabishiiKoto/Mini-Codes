# File Title: Morse code Generator and Translator
# Feature: Generate Text to Morse code or translate Morse code to Text


print("___Morse Code Generator and Translator___")

data = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."}
data2 = {".-": "a", "-..." : "b", "-.-.": "c", "-.." : "d", "." : "e", "..-.": "f", "--.": "g", "....": "h", "..": "i", ".---" : "j", "-.-" : "k", ".-.." : "l", "--": "m", "-.": "n", "---": "o", ".--.": "p", "--.-": "q", ".-.": "r", "...": "s", "-": "t", "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y", "--..": "z"}

typeMenu = """
\t SELECT TYPE
1. Text to Morse code
2. Morse code to Text
""" 

print(typeMenu)
try:
    typeUnit = int(input("Enter the choice number: "))
    
    if typeUnit == 1:
        string = input("Enter the text: ")
        result = ""
        for i in range(len(string)):
            char = string[i]
            if char != " ":
                morse = data.get(char)
                result += morse
                result += " "
            else:
                result += "/ "
        print(result)
    elif typeUnit == 2:
        string = input("Enter the Morse code: ")
        result = ""
        list = string.split(" ")
        for i in list:
            if i != "/":
                result += data2.get(i)
            else:
                result += " "
        print(result)
except ValueError:
    print("Error when taking input!")
    
        