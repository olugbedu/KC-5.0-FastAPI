history = []

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None

def perform_operation(operation):
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers.\n")
        return

    if operation == "1":
        result = add(num1, num2)
        symbol = "+"
    elif operation == "2":
        result = subtract(num1, num2)
        symbol = "-"
    elif operation == "3":
        result = multiply(num1, num2)
        symbol = "*"
    elif operation == "4":
        result = divide(num1, num2)
        symbol = "/"
        if result is None:
            return
    else:
        print("Invalid operation.")
        return

    entry = f"{num1} {symbol} {num2} = {result}"
    history.append(entry)
    print("Result:", result, "\n")

def show_history():
    if not history:
        print("No calculations yet.\n")
        return
    print("\n Calculation History ")
    for i, entry in enumerate(history, start=1):
        print(f"{i}. {entry}")
    print()

def main():
    while True:
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. View History")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice in ["1", "2", "3", "4"]:
            perform_operation(choice)
        elif choice == "5":
            show_history()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

main()
