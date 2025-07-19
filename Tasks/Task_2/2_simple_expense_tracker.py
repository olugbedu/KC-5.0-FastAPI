expenses = []

def add_expense():
    item = input("Enter expense description: ")
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be positive.\n")
            return
        expenses.append({"item": item, "amount": amount})
        print("Expense added!\n")
    except ValueError:
        print("Invalid amount. Please enter a number.\n")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.\n")
        return
    print("\n Expense List ")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['item']} - ₦{exp['amount']:.2f}")
    print()

def show_total():
    if not expenses:
        print("No expenses to summarize.\n")
        return
    total = sum(_['amount'] for _ in expenses)
    avg = total / len(expenses)
    print(f"\nTotal expenses: ₦{total:.2f}")
    print(f"Average expense: ₦{avg:.2f}\n")

def main():
    while True:
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Show Total and Average")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.\n")

main()
