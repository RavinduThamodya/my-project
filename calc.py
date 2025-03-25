import os

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_number(prompt):
    """Gets a valid float number from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def get_operator():
    """Gets a valid operator from the user."""
    while True:
        operator = input("Enter operation (+, -, *, /, **, %, //): ")
        if operator in ['+', '-', '', '/', '*', '%', '//']:
            return operator
        print("Invalid operator! Please enter +, -, *, /, **, %, or //.")

def calculator():
    """Enhanced calculator with a user-friendly menu interface."""
    history = []

    while True:
        clear_screen()
        print("==== Calculator Menu ====")
        print("1. Perform a calculation")
        print("2. View history")
        print("3. Exit")
        print("=========================")

        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            num1 = get_number("Enter first number: ")
            operator = get_operator()
            num2 = get_number("Enter second number: ")

            if operator in ['/', '//', '%'] and num2 == 0:
                print("Error! Division or modulus by zero is not allowed.")
                input("Press Enter to continue...")
                continue

            result = eval(f"{num1} {operator} {num2}")

            history.append(f"{num1} {operator} {num2} = {result}")
            print(f"\nResult: {result}")
            input("Press Enter to continue...")

        elif choice == '2':
            print("\nCalculation History:")
            if history:
                for i, record in enumerate(history, start=1):
                    print(f"{i}. {record}")
            else:
                print("No calculations performed yet.")
            input("Press Enter to continue...")

        elif choice == '3':
            print("Exiting the calculator. Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1, 2, or 3.")
            input("Press Enter to continue...")

if _name_ == "_main_":
    calculator()
