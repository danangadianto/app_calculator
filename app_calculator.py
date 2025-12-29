def addition():
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter first number: "))
        result = num1 + num2
        print(f"Result: {result}")
    except:
        print("Invalid input. Please enter a valid number.")

def subtraction():
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter first number: "))
        result = num1 - num2
        print(f"Result: {result}")
    except:
        print("Invalid input. Please enter a valid number.")

def multiplication():
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter first number: "))
        result = num1 * num2
        print(f"Result: {result}")
    except:
        print("Invalid input. Please enter a valid number.")

def division():
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter first number: "))
        result = num1 / num2
        print(f"Result: {result}")
    except:
        print("Invalid input. Please enter a valid number.")