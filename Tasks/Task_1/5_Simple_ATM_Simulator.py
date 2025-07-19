balance = 3000 

print("Welcome to the Simple ATM!")

while True:
    print("\nPlease choose an option:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(f"Your current balance is: ${balance:.2f}")

    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"${amount:.2f} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Error: Insufficient balance.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            balance -= amount
            print(f"${amount:.2f} withdrawn successfully.")

    elif choice == "4":
        print(f"\nThank you for using the ATM. Final balance: ${balance:.2f}")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
