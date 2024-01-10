#!/usr/bin/python3

# define the functions needed : add, sub, mul, div
def add(a, b):
    """
    Addational function

    Args:
        a: first integer
        b: secont integer

    Returns:
        The return value. a + b
    """
    return (a + b)

def sub(a, b):
     """
     Substraction function

     Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a - b
    """
    return (a - b)

def mul(a, b):
    """
    Multiplication function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a * b
    """
    return (a * b)

def div(a, b):
    """
    Division function

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a / b
    """
    return (a / b)

# Print options to the user
def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("A. Addition (+)")
    print("B. Substraction(-)")
    print("C. Multiplication(*)")
    print("D. Division (/)")

# Get user input
while True:
    choice = input("Choose an option(A/B/C/D): ")

    # Confirm if choice is one of the options
    if choice in('A', 'B', 'C', 'D'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a letter.")
            continue

        if choice == 'A':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == 'B':
            print(num1, "-", num2, "=", sub(num1, num2))

        elif choice == 'C':
            print(num1, "*", num2, "=", mul(num1, num2))

        elif choice == 'D':
            print(num1, "/", num2, "=", div(num1, num2))

    # while loop to continue the program untill user exits
    next_calculation = input("Let's do next calculation? (yes/exit): ")
    if next_calculation == "exit":
        break
else:
    print("Invalid input")
