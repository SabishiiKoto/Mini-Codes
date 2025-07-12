import math

# File Title: Area Calculator
# Feature: Give formulas and take the needed data to calculate the area of the selected shape.

print("___Area Calculator___")

formula = ["A = a * a", "A = l * w", "A = 1/2 * b * h", "A = πr²", "A = b * h", "A = 1/2 * (a + b) * h"]
typeMenu = """
\t SELECT TYPE OF SHAPE
1. Square
2. Rectangle
3. Triangle
4. Circle
5. Parallelogram
6. Trapezoid
"""
try:
    print(typeMenu)
    typeUnit = int(input("Enter the shape in number: "))
    print(formula[typeUnit - 1])
    area = 0
    if typeUnit == 1:
        length = float(input("Enter the length of side (number only): "))
        area = length * length
    elif typeUnit == 2:
        length = float(input("Enter the length of the rectangle (number only): "))
        width = float(input("Enter the width of the rectangle (number only): "))
        area = length * width
    elif typeUnit == 3:
        base = float(input("Enter the base of the triangle (number only): "))
        height = float(input("Enter the height of the triangle (number only): "))
        area = base * height / 2
    elif typeUnit == 4:
        radius = float(input("Enter the radius of the circle (number only): "))
        area = (radius ** 2) * math.pi
    elif typeUnit == 5:
        height = float(input("Enter the height of the parallelogram (number only): "))
        base = float(input("Enter the base of the parallelogram (number only): "))
        area = height * base
    elif typeUnit == 61:
        height = float(input("Enter the height of the trapezoid (number only): "))
        base = float (input("Enter the base of the trapezoid (number only): "))
        length = float(input("Enter the parallel side of the base (number only):  "))
        area = ((base * length)/2) * height
    print("{:.4f} unit²".format(area))
    
except ValueError:
    print("Error when taking inputs!")

