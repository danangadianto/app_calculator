def addition():
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter first number: "))
        result = num1 + num2
        print(f"Result: {result}")
        input("Press Enter to continue...")
    except:
        print("Invalid input. Please enter a valid number.")

def subtraction():
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter first number: "))
        result = num1 - num2
        print(f"Result: {result}")
        input("Press Enter to continue...")
    except:
        print("Invalid input. Please enter a valid number.")

def multiplication():
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter first number: "))
        result = num1 * num2
        print(f"Result: {result}")
        input("Press Enter to continue...")
    except:
        print("Invalid input. Please enter a valid number.")

def division():
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter first number: "))
        result = num1 / num2
        print(f"Result: {result}")
        input("Press Enter to continue...")
    except:
        print("Invalid input. Please enter a valid number.")

def app_menu():
    print("===SIMPLE CALCULATOR===")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    while True:
        try:
            user_input = int(input("Enter your choice (1-5): "))
            if user_input == 1:
                addition()
            elif user_input == 2:
                subtraction()
            elif user_input == 3:
                multiplication()
            elif user_input == 4:
                division()
            elif user_input == 5:
                print("Thank you for using the calculator.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except:
            print("Invalid input. Please enter a valid number.")

app_menu()