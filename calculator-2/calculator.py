"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


while True:    
    response = input("Enter your equation > ")
    response = response.split(' ')
    operation = response[0]
    if 'q' in response:
        print("Thanks for calculating!")
        break
    elif operation not in ("+", "-", "*", "/", "square", "cube", "pow", "mod"):
        print("That is not a known operation.")
    elif len(response) ==1:
        print("That's not enough input for an equation.")
    elif len(response) == 2:
        num1 = response[1]
    elif len(response) == 3:
        num1 = response[1]
        num2 = response[2]
    elif len(response) > 3:
        num1 = response[1]
        num2 = response[2]
        num3 = response[3] 
    elif not num1.isdigit() or not num2.isdigit():
        print("Those aren't numbers.")

    else:
        if operation == "+":
            result = add(float(num1), float(num2))

        elif operation == "-":
            result = subtract(float(num1), float(num2))

        elif operation == "*":
            result = multiply(float(num1), float(num2))

        elif operation == "/":
            result = divide(float(num1), float(num2))

        elif operation == "square":
            result = square(float(num1))

        elif operation == "cube":
            result = cube(float(num1))

        elif operation == "pow":
            result = power(float(num1), float(num2))

        elif operation == "mod":
            result = mod(float(num1), float(num2))

        else:
            result = "Please enter an operator followed by two integers."

        print(result)