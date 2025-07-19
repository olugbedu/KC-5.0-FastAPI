from budget_utils import Transaction, load_transactions, save_transactions, summarize_by_category

def add_transaction():
    category = input("Enter category (e.g., food, transport): ").strip()
    try:
        amount = float(input("Enter amount: "))
        txn = Transaction(category, amount)
        data = load_transactions()
        data.append(txn.to_dict())
        save_transactions(data)
        print("Transaction added.")
    except ValueError:
        print("Invalid amount. Please enter a number.")

def view_transactions():
    data = load_transactions()
    if not data:
        print("No transactions found.")
        return
    for txn in data:
        print(f"{txn['date']} - {txn['category']} - ₦{txn['amount']}")

def view_summary():
    data = load_transactions()
    summary = summarize_by_category(data)
    if not summary:
        print("No transactions to summarize.")
        return
    print("\nCategory Summary:")
    for cat, total in summary.items():
        print(f"{cat}: ₦{total}")

def main():
    while True:
        print("\n=== Personal Budget Tracker ===")
        print("1. Add Transaction")
        print("2. View All Transactions")
        print("3. View Summary by Category")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
