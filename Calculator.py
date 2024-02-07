# Importing math library
from math import *

# Calculation methods
multiplication = 'g'
division = 'd'
addition = 'p'
subtraction = 'm'
square_root = 'k'
exponentiation = 'e'

# Area calculation methods
circle_area = 'sa'
triangle_area = 'ta'
rectangle_area = 'fa'

# Perimeter calculation methods
circle_perimeter = 'so'
triangle_perimeter = 'to'
rectangle_perimeter = 'fo'

# Creating the menu for the calculator
print('''
    SanneCodes Calculator

    |--------------------|-----------|
    | Calculation method:| shortcut: |
    |--------------------|-----------|
    | Plus  (+)          |    'p'    |
    | Minus (-)          |    'm'    |
    | Multiplication (*) |    'g'    |
    | Division (/)       |    'd'    |
    | Square root        |    'k'    |
    | Exponent           |    'e'    |
    |--------------------------------|
    | Calculate Area                 |
    |--------------------------------|
    | Circle             |   'sa'    |
    | Triangle           |   'ta'    |
    | Square             |   'fa'    |
    |--------------------------------|
    | Calculate Perimeter             |
    |--------------------------------|
    | Circle             |   'so'    |
    | Triangle           |   'to'    |
    | Square             |   'fo'    |
    |--------------------|-----------|


             ? how to use ?
Write the shortcut that is on the same line as the calculation method you want to use, and press 'Enter' on the keyboard:
''')

# Using a while loop to allow the calculator to be used multiple times
while True:
    # Storing user input to determine which calculation to perform
    calculation_method = input(">>> ")
    if multiplication in calculation_method:
        print("You selected Multiplication")
        number1 = int(input("First number: "))
        number2 = int(input("Second number: "))
        result = number1 * number2
        print(f"The result is : {result}")
    elif subtraction in calculation_method:
        print("You selected Subtraction")
        number1 = int(input("First number: "))
        number2 = int(input("Second number: "))
        result = number1 - number2
        print(f"The result is : {result}")
    elif addition in calculation_method:
        print("You selected Addition")
        number1 = int(input("First number: "))
        number2 = int(input("Second number: "))
        result = number1 + number2
        print(f"The result is : {result}")
    elif division in calculation_method:
        print("You selected Division")
        number1 = int(input("First number: "))
        number2 = int(input("Second number: "))
        result = number1 / number2
        print(f"The result is : {result}")
    elif square_root in calculation_method:
        print("You selected Square root")
        number1 = int(input("Enter the number to find its square root: "))
        answer = sqrt(number1)
        print(f"The square root of {number1} is {answer}")
    elif exponentiation in calculation_method:
        print("You selected Exponentiation")
        number1 = int(input("Enter the base: "))
        number2 = int(input("Enter the exponent: "))
        answer = number1 ** number2
        print(f"The answer for {number1}^{number2} is {answer}")
    elif circle_area in calculation_method:
        print("You selected to calculate the area of a circle")
        radius = int(input("Enter the radius: "))
        result = 3.14 * radius ** 2
        print("The area is", result)
    elif triangle_area in calculation_method:
        print("You selected to calculate the area of a triangle")
        base = int(input("Enter the base: "))
        height = int(input("Enter the height: "))
        result = base * height / 2
        print("The area is", result)
    elif rectangle_area in calculation_method:
        print("You selected to calculate the area of a rectangle")
        length = int(input("Enter the length: "))
        width = int(input("Enter the width: "))
        result = length * width
        print("The area is", result)
    elif circle_perimeter in calculation_method:
        print("You selected to calculate the perimeter of a circle")
        diameter = int(input("Enter the diameter: "))
        result = 3.14 * diameter
        print("The perimeter is", result)
    elif triangle_perimeter in calculation_method:
        print("You selected to calculate the perimeter of a triangle")
        side1 = int(input("Enter the length of side 1: "))
        side2 = int(input("Enter the length of side 2: "))
        side3 = int(input("Enter the length of side 3: "))
        result = side1 + side2 + side3
        print("The perimeter of the triangle is", result)
    elif rectangle_perimeter in calculation_method:
        print("You selected to calculate the perimeter of a rectangle")
        side1 = int(input("Enter the length of side 1: "))
        side2 = int(input("Enter the length of side 2: "))
        result = 2 * (side1 + side2)
        print("The perimeter of the rectangle is", result)
    else:
        print("!ERROR! The calculation method you entered was not recognized !ERROR!")  # Error message
