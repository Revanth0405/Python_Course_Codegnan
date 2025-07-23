def main():
    print("Welcome to the ATM!")

    acc_no = input("Enter your account number: ")
    pin = input("Enter your PIN: ")
    if acc_no == "123456789" and pin == "1234":
        print("Login successful!")
        transactions = []
        balance = 5000  # Initial balance
        while True:
            print("\nATM Menu:")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. View Transaction History")
            print("5. Exit")

            choice = input("Please select an option (1-5): ")

            if choice == "1":
                print(f"Your current balance is: ${balance}")
            elif choice == "2":
                deposit = float(input("Enter amount to deposit: $"))
                balance += deposit
                print(f"Deposited ${deposit}. New balance is: ${balance}")
                transactions.append(f"Deposited ${deposit}. New balance is: ${balance}")
            elif choice == "3":
                withdraw = float(input("Enter amount to withdraw: $"))
                if withdraw > balance:
                    print("Insufficient funds!")
                else:
                    balance -= withdraw
                    print(f"Withdrew ${withdraw}. New balance is: ${balance}")
                    transactions.append(f"Withdrew ${withdraw}. New balance is: ${balance}")
            elif choice == "4":
                print("Transaction history is as follows.")
                if transactions:
                    for transaction in transactions:
                        print(transaction)
                else:
                    print("No transactions made yet.")
            elif choice == "5":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option, please try again.")
    else:
        print("Invalid account number or PIN. Please try again.")

if __name__ == "__main__":
    main()