# File Title: Text Compare
# Feature: Compare characters between 2 texts.

print("___Text Compare___")

text1 = input("Enter the first text: ")
text2 = input("Enter the second text: ")

if (text1 == text2):
    print("Same text")
else:
    result = ""
    long = None
    short = None
    
    print("\nHOW DOES IT WORK?")
    print("If _ is shown, then both text 1 and text 2 have the character")

    if len(text1) >= len(text2):
        long = text1
        short = text2
        print("If word is shown, then text 1 has the word that text 2 does not")
        print("If / is shown, then text 2 has something that text 1 does not")
    else:
        long = text2
        short = text1
        print("If word is shown, then text 2 has the word that text 1 does not")
        print("If / is shown, then text 1 has something that text 2 does not")

    
    for i in short:
        if i in long:
            index = long.index(i)
            result += long[0:index]
            result += "_"
            long = long[index + 1:]
            
        else:
            result += "/"
            
    print("\nThe difference: " + result)
            
        
