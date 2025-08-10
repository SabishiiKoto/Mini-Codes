# File Title: RGB to Hex
# Feature: Turn RGB to Hexadecimal or vice versa.

print("___RGB <-> Hex___")
dic = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
list = ["RED", "GREEN", "BLUE"] 
choice2Dict = {"0": 0, "1": 1, "2": 2, "3":3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11, "C": 12, "D": 13,"E": 14, "F": 15}

menu = """
--SELECT ONE--
1. RGB -> Hex
2. Hex -> RGB"""

print(menu)
choice = input ("Enter 1 or 2: ")

if choice == "1":
    try:
    
        totalResult = ""
        for i in list:
            number = int(input(format("Enter the {} code: ".format(i))))
            result = ""
            if number == 0:
                result = "00"
            while (number != 0):
                first = number % 16
                if first in dic:
                    result = dic.get(first) + result
                else:
                    result = str(first) + result
                number = number // 16
        
            if len(result) == 1:
                result = "0" + result
            totalResult += result
        
        print("\n--Result--")
        print("#" + totalResult)
    except ValueError:
        print("Please enter number only")

elif choice == "2":
    try: 
        number = (input("Enter the number in hexadecimal (e.g., #000000): "))
        
        if number[0] == "#":
            number = number[1:]
            
        number = number.upper()
        
        i = 0
        print("\n--Result--")
        
        while i < len(number):
            
            first = choice2Dict.get(number[i]) * 16
            second = choice2Dict.get(number[i + 1])
            
            index = i//2
            colorName = list[index]
            print("The {} code is {}".format(colorName, first + second))
            
            i += 2
        
    except ValueError:
        print("Please enter number only")
    except:
        print("Invalid input")
else:
    print("Invalid input")
    
    

    
    



