def calculator():
    """Simple calculator with history tracking."""
    history = []

    while True:
        print("\nOptions:")
        print("1. Perform a calculation")
        print("2. View history")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            while True:
                try:
                    num1 = float(input("Enter first number: "))
                    break
                except ValueError:
                    print("Invalid input! Please enter a valid number.")

            while True:
                operator = input("Enter operation (+, -, , /, *, %, //): ")
                if operator in ['+', '-', '', '/', '*', '%', '//']:
                    break
                print("Invalid operator! Please enter +, -, , /, *, %, or //.")

            while True:
                try:
                    num2 = float(input("Enter second number: "))
                    if operator in ['/', '//', '%'] and num2 == 0:
                        print("Error! Division or modulus by zero is not allowed.")
                    else:
                        break
                except ValueError:
                    print("Invalid input! Please enter a valid number.")

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                result = num1 / num2
            elif operator == '**':
                result = num1 ** num2
            elif operator == '%':
                result = num1 % num2
            elif operator == '//':
                result = num1 // num2

            history.append(f"{num1} {operator} {num2} = {result}")
            print(f"Result: {result}")

        elif choice == '2':
            print("\nCalculation History:")
            if history:
                for i, record in enumerate(history, start=1):
                    print(f"{i}. {record}")
            else:
                print("No calculations performed yet.")

        elif choice == '3':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")

if _name_ == "_main_":
    calculator()
