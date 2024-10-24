# Bank Account System

import random
from datetime import datetime



class BankAccount:
    def __init__(self, owner, account_type, balance=0):
        self.owner = owner
        self.balance = balance
        self.account_type = account_type
        self.account_number = self.generate_account_number()
        self.transaction_history = []  # Stores all transactions as a list of tuples (date, type, amount)

    # Method to generate a unique account number
    def generate_account_number(self):
        return f"{random.randint(1000000000, 9999999999)}"

    # Method to record transactions
    def record_transaction(self, transaction_type, amount):
        self.transaction_history.append((datetime.now(), transaction_type, amount))

    # Method to display account balance
    def check_balance(self):
        return f"Account holder: {self.owner}, Account Number: {self.account_number}, Balance: ${self.balance}"

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.record_transaction("Deposit", amount)
            return f"${amount} deposited successfully. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount!"

    # Method to withdraw money
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.record_transaction("Withdrawal", amount)
            return f"${amount} withdrawn successfully. New balance: ${self.balance}"
        elif amount > self.balance:
            return "Insufficient funds!"
        else:
            return "Invalid withdrawal amount!"

    # Method to print transaction history
    def display_transaction_history(self):
        if not self.transaction_history:
            return "No transactions found."
        else:
            history = f"Transaction History for {self.owner}:\n"
            for date, trans_type, amount in self.transaction_history:
                history += f"{date.strftime('%Y-%m-%d %H:%M:%S')} - {trans_type}: ${amount}\n"
            return history


# Saving Account

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, 'Savings', balance)
        self.interest_rate = interest_rate

    # Method to calculate interest
    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.record_transaction("Interest", interest)
        return f"Interest of ${interest} added. New balance: ${self.balance}"


# Checking Account

class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0):
        super().__init__(owner, 'Checking', balance)


# Create and Test the system

# Creating a Savings Account for Alice with $500 balance
savings_account = SavingsAccount("Amy", 500)

# Check balance and deposit money
print(savings_account.check_balance())
print(savings_account.deposit(200))  # Depositing $200

# Withdraw money
print(savings_account.withdraw(100))  # Withdrawing $100

# Calculate interest and apply it
print(savings_account.calculate_interest())  # Apply interest based on the balance

# Print transaction history for Alice
print(savings_account.display_transaction_history())




# Creating a Checking Account for Bob with $300 balance
checking_account = CheckingAccount("John", 300)

# Perform transactions on the checking account
print(checking_account.check_balance())
print(checking_account.deposit(150))  # Depositing $150
print(checking_account.withdraw(50))  # Withdrawing $50
print(checking_account.display_transaction_history())

