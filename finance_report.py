import csv
import os
from collections import defaultdict

FILE_NAME = "transactions.csv"


def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["type", "category", "amount"])


def add_transaction():
    transaction_type = input("Type (income/expense): ").lower()
    category = input("Enter category: ")

    if transaction_type not in ["income", "expense"]:
        print("Invalid transaction type!")
        return

    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

    except ValueError:
        print("Enter a valid amount.")
        return

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([transaction_type, category, amount])

    print("Transaction saved successfully!")


def generate_report():
    income = 0
    expenses = 0
    categories = defaultdict(float)

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            amount = float(row["amount"])

            if row["type"] == "income":
                income += amount
            else:
                expenses += amount
                categories[row["category"]] += amount

    balance = income - expenses

    print("\n===== FINANCIAL REPORT =====")
    print(f"Total Income: Rs. {income:.2f}")
    print(f"Total Expenses: Rs. {expenses:.2f}")
    print(f"Remaining Balance: Rs. {balance:.2f}")

    print("\nCategory-wise Expenses:")

    if categories:
        for category, amount in categories.items():
            print(f"{category}: Rs. {amount:.2f}")
    else:
        print("No expenses recorded.")

    with open("finance_report.txt", "w") as file:
        file.write("PERSONAL FINANCE REPORT\n")
        file.write(f"Income: Rs. {income:.2f}\n")
        file.write(f"Expenses: Rs. {expenses:.2f}\n")
        file.write(f"Balance: Rs. {balance:.2f}\n")

        for category, amount in categories.items():
            file.write(f"{category}: Rs. {amount:.2f}\n")

    print("\nReport exported to finance_report.txt")


def view_transactions():
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            print(" | ".join(row))


def main():
    initialize_file()

    while True:
        print("\n===== PERSONAL FINANCE SYSTEM =====")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Generate Report")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            generate_report()
        elif choice == "4":
            print("Program closed.")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
