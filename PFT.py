# Personal Finance Tracker

class Transaction:
    def __init__(self, date, description, amount, category):
        self.date = date
        self.description = description
        self.amount = amount
        self.category = category

class FinanceTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, date, description, amount, category):
        transaction = Transaction(date, description, amount, category)
        self.transactions.append(transaction)

    def view_transactions(self):
        for transaction in self.transactions:
            print(f"Date: {transaction.date}, Description: {transaction.description}, Amount: {transaction.amount}, Category: {transaction.category}")

    def get_balance(self):
        balance = 0
        for transaction in self.transactions:
            balance += transaction.amount
        return balance

    def get_expenses_by_category(self):
        expenses = {}
        for transaction in self.transactions:
            if transaction.category in expenses:
                expenses[transaction.category] += transaction.amount
            else:
                expenses[transaction.category] = transaction.amount
        return expenses

def main():
    tracker = FinanceTracker()

    while True:
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Get Balance")
        print("4. Get Expenses by Category")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            tracker.add_transaction(date, description, amount, category)
        elif choice == "2":
            tracker.view_transactions()
        elif choice == "3":
            print(f"Balance: {tracker.get_balance()}")
        elif choice == "4":
            expenses = tracker.get_expenses_by_category()
            for category, amount in expenses.items():
                print(f"Category: {category}, Amount: {amount}")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()