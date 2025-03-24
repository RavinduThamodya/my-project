def calculator():
    """Simple calculator with input validation."""
    while True:
        try:
            num1 = float(input("Enter first number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    while True:
        operator = input("Enter operation (+, -, *, /): ")
        if operator in ['+', '-', '*', '/']:
            break
        print("Invalid operator! Please enter +, -, *, or /.")

    while True:
        try:
            num2 = float(input("Enter second number: "))
            if operator == '/' and num2 == 0:
                print("Error! Division by zero is not allowed.")
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

    print(f"Result: {result}")

if __name__ == "__main__":
    calculator()
