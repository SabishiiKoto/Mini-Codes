
# File Title: Metric Conversion
# Feature: Given 3 types of conversion and convert the given unit to the selected unit.
# How To Run and Use: 
# 1. Run the file (download the file first I guess?)
# 2. Select the unit (temperature, length, weight)
# 3. Select the type to convert (temperature) or unit type of the input (length & weight)
# 4. Type the input number
# 5. (For length & weight) Select the unit type of the output


print("___Metric Conversion___")
menu = """
\t SELECT UNIT
1. Temperature conversion
2. Length conversion
3. Weight conversion
"""

temperatureMenu = """
\t SELECT UNIT
1. From Celsius to Fahrenheit
2. From Fahrenheit to Celsius
"""

lengthData = ["centimeters", "decimeters", "feet", "inches", "kilometers", "meters", "micrometers", "miles", "millimeters", "yards"]
lengthMenu = """
\t SELECT UNIT
1. Centimeters
2. Decimeters
3. Feet
4. Inches
5. Kilometers
6. Meters
7. Micrometer
8. Miles
9. Millimeters
10. Yards
"""

weightData = ["grams", "kilograms", "micrograms", "milligrams", "ounces", "pounds", "tonnes"]
weightMenu = """
\t SELECT UNIT
1. Grams
2. Kilograms
3. Micrograms
4. Milligrams
5. Ounces
6. Pounds
7. Tonnes
"""

print(menu)
typeUnit = input("Enter the choice in number (press ANY to STOP): ")


try:
    if (typeUnit == "1"):
        print(temperatureMenu)
        temperatureUnit = input("Enter the choice in number: ")
        if (temperatureUnit == "1"):
            celsiusInput = float(input("Enter the temperature in Celsius degree: "))
            fahrenheitOutput = celsiusInput * 9/5 + 32
            print("{:.4f} Fahrenhait degree".format(fahrenheitOutput))
            # From Celsius to Fahrenheit
        elif (temperatureUnit == "2"):
            fahrenheitInput = float(input("Enter the temperature in Fahrenheit degree: "))
            celsiusOutput = (fahrenheitInput - 32) * 5/9
            print("{:4f} Celsius degree".format(celsiusOutput))
            # From Fahrenheit to Celsius
    elif (typeUnit == "2"):
        print(lengthMenu)
        inputLengthUnit = int(input("Enter the input unit in number: "))
        inputLength = float(input("Enter the length in {}: ".format(lengthData[int(inputLengthUnit) - 1])))
        print(lengthMenu)
        outputLengthUnit = int(input("Enter the output unit in number: "))
        if (inputLengthUnit == outputLengthUnit):
            print("Your result is {} {}".format(inputLength,lengthData[int(inputLengthUnit) - 1]))
        else:
            outputLength = 0
            if (inputLengthUnit == 2): # is dm
                inputLength = inputLength * 10 # dm to cm
            elif (inputLengthUnit == 3): # is ft
                inputLength = inputLength * 30.48 # ft to cm
            elif (inputLengthUnit == 4): # is inches
                inputLength = inputLength * 2.54 # inch to cm
            elif (inputLengthUnit == 5): # is km
                inputLength = inputLength * 100000 # km to cm
            elif (inputLengthUnit == 6): # is m
                inputLength = inputLength * 100 # m to cm
            elif (inputLengthUnit == 7): # is micrometer
                inputLength = inputLength / 10000 # micrometer to cm
            elif (inputLengthUnit == 8): # is miles
                inputLength = inputLength * 160900 # miles to cm
            elif (inputLengthUnit == 9): # is millimeter
                inputLength = inputLength / 10 # millimeter to cm
            elif (inputLengthUnit == 10): # is yard
                inputLength = inputLength * 91.44 # yard to cm
                
            if (outputLengthUnit == 1):
                outputLength = inputLength
            elif (outputLengthUnit == 2): # cm to dm
                outputLength = inputLength / 10
            elif (outputLengthUnit == 3): # cm to ft
                outputLength = inputLength / 30.48 # ft to cm
            elif (outputLengthUnit == 4): # cm to inch
                outputLength = inputLength / 2.54
            elif (outputLengthUnit == 5): # cm to km
                outputLength = inputLength / 100000
            elif (outputLengthUnit == 6): # cm to m
                outputLength = inputLength / 100
            elif (outputLengthUnit == 7): # cm to micro
                outputLength = inputLength * 10000
            elif (outputLengthUnit == 8): # cm to miles
                outputLength = inputLength / 160900
            elif (outputLengthUnit == 9): # cm to mm
                outputLength = inputLength * 10
            elif (outputLengthUnit == 10): # cm to yard
                outputLength = inputLength / 91.44 # yard to cm
            print("Your result is {:.4f} {}".format(outputLength,lengthData[outputLengthUnit - 1]))
    
    elif (typeUnit == "3"):
        print(weightMenu)
        inputUnit = int(input("Enter the input unit in number: "))
        inputWeight = float(input("Enter the weight in {}: ".format(weightData[int(inputUnit) - 1])))
        print(weightMenu)
        outputUnit = int(input("Enter the output unit in number: "))
        
        if (inputUnit == outputUnit):
            print("Your result is {:.4f} {}".format(inputWeight, weightData[inputUnit - 1]))
        else:
            if (inputUnit == 1): # kg to g
                inputWeight = inputWeight * 1000
            elif (inputUnit == 2): # mcg to g
                inputWeight = inputWeight / 1000000
            elif (inputUnit == 3): # mg to g
                inputWeight = inputWeight / 1000
            elif (inputUnit == 4): # ounce to g
                inputWeight = inputWeight * 28.3495231
            elif (inputUnit == 5): # pound to g
                inputWeight = inputWeight * 453.59237
            elif (inputUnit == 6): # tonne to g
                inputWeight = inputWeight * 1000000
                
            outputWeight = 0
            if (outputUnit == 0): # g to g
                outputWeight = inputWeight
            elif (outputUnit == 1): # g to kg
                outputWeight = inputWeight / 1000
            elif (outputUnit == 2): # g to mcg
                outputWeight = inputWeight * 1000000
            elif (outputUnit == 3): # g to mg
                outputWeight = inputWeight * 1000
            elif (outputUnit == 4): # g to ounce
                outputWeight = inputWeight / 28.3495231
            elif (outputUnit == 5): # g to pound
                outputWeight = inputWeight / 453.59237
            elif (outputUnit == 6): # g to tonne
                outputWeight = inputWeight / 1000000
            print("Your result is {:.4f} {}".format(outputWeight, weightData[outputUnit - 1]))
        
except ValueError:
    print("Error when taking input!")
        
    
        
            
            
    