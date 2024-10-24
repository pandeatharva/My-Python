Bank Account System

This is a Python project that simulates a basic bank account system using Object-Oriented Programming (OOP) principles. The system allows users to create accounts, deposit and withdraw money, check account balances, and generate transaction history. 
It includes advanced features such as interest calculation for savings accounts, overdraft protection for checking accounts, and account-specific transaction logging.

Features:

Account Creation: Users can create accounts (Savings, Checking).
Deposit and Withdraw: Manage funds with deposit and withdrawal functionalities.
Balance Check: Check account balance at any time.
Transaction History: Keep track of all deposits and withdrawals.
Interest Calculation: Automatically calculate interest for Savings accounts.
Overdraft Protection: Prevent overdrawing from Checking accounts.
Error Handling: Proper management of invalid inputs and account-related errors.

Usage

Create Account: Create a new account (Savings or Checking).
Deposit: Deposit money into your account.
Withdraw: Withdraw money with overdraft protection in checking accounts.
Check Balance: View your current balance.
View Transactions: See the full history of your deposits and withdrawals.

Code Structure

Account Class: Base class that handles common functionality like deposits, withdrawals, and transaction logging.
SavingsAccount Class: Inherits from Account and adds interest calculation functionality.
CheckingAccount Class: Inherits from Account and implements overdraft protection.

OOP Principles Used

Encapsulation: All account-related operations are encapsulated within specific classes.
Inheritance: SavingsAccount and CheckingAccount inherit from the Account class.
Polymorphism: The deposit and withdraw methods behave differently depending on the account type.
Abstraction: The complexity of account management is abstracted away behind the Account class interface.
