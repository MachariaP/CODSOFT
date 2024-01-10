#!/usr/bin/python3

def add(a, b):
    """Additional function"""
    return a + b

def sub(a, b):
    """Subtraction function"""
    return a - b

def mul(a, b):
    """Multiplication function"""
    return a * b

def div(a, b):
    """Division function"""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero"

def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("A. Addition (+)")
    print("B. Subtraction (-)")
    print("C. Multiplication (*)")
    print("D. Division (/)")

while True:
    calculator()
    
    # Get user input
    choice = input("Choose an option (A/B/C/D): ").upper()

    # Confirm if choice is one of the options
    if choice in ('A', 'B', 'C', 'D'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

        if choice == 'A':
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == 'B':
            print(f"{num1} - {num2} = {sub(num1, num2)}")

        elif choice == 'C':
            print(f"{num1} * {num2} = {mul(num1, num2)}")

        elif choice == 'D':
            result = div(num1, num2)
            print(f"{num1} / {num2} = {result}")

    # Prompt user for next calculation or exit
    next_calculation = input("Do another calculation? (yes/exit): ").lower()
    if next_calculation == "exit":
        break
