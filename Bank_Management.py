import sqlite3
from datetime import datetime
class BankManagementSystem:
    def __init__(self):
        self.conn=sqlite3.connect('bank_database.db')
        self.cursor=self.conn.cursor()
        self.create_tables()
        
    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts(
                account_number INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                account_type TEXT NOT NULL,
                balance REAL NOT NULL,
                created_at TEXT NOT NULL,
                last_updated TEXT NOT NULL
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                account_number INTEGER NOT NULL,
                transaction_type TEXT NOT NULL,
                amount REAL NOT NULL,
                transaction_date TEXT NOT NULL,
                FOREIGN KEY(account_number)REFERENCES accounts(account_number)
            )
        ''')
        self.conn.commit()
    
    def open_account(self):
        """Create a new bank account"""
        print("\n--- Open New Account ---")
        print("Sample Output:")
        print("Enter account holder's name: Ram Ram")
        print("\nAccount Types:")
        print("1.Savings Account")
        print("2.Current Account")
        print("Select account type(1/2): 1")
        print("Enter initial deposit(minimum 500):1000")
        print("\nAccount created successfully!")
        print("Account Number:1001")
        print("Account Holder:Ram Ram")
        print("Account Type:Savings")
        print("Initial Balance:1000.00")
    
    def deposit_amount(self):
        """Deposit money into an account"""
        print("\n--- Deposit Amount ---")
        print("Sample Output:")
        print("Enter account number:1001")
        print("Enter deposit amount:500")
        print("\nAmount deposited successfully!")
        print("Account Number:1001")
        print("Deposited Amount:500.00")
        print("New Balance:1500.00")
    
    def withdraw_amount(self):
        """Withdraw money from an account"""
        print("\n--- Withdraw Amount ---")
        print("Sample Output:")
        print("Enter account number:1001")
        print("Enter withdrawal amount:200")
        print("\nAmount withdrawn successfully!")
        print("Account Number:1001")
        print("Withdrawn Amount:200.00")
        print("New Balance:1300.00")
    
    def balance_enquiry(self):
        """Check account balance"""
        print("\n--- Balance Enquiry ---")
        print("Sample Output:")
        print("Enter account number:1001")
        print("\n--- Account Details ---")
        print("Account Number:1001")
        print("Account Holder:Ram Ram")
        print("Current Balance:1300.00")
    
    def display_all_accounts(self):
        """Display all account holders"""
        print("\n--- All Account Holders List ---")
        print("\n{:<15}{:<20}{:<15}{:<10}".format("Account No.","Name","Account Type","Balance"))
        print("-"*60)
        print("{:<15}{:<20}{:<15}{:<10.2f}".format(
            1001,"Ram Ram","Savings",1300.00))
        print("{:<15}{:<20}{:<15}{:<10.2f}".format(
            1002,"sitha ram","Current",2500.00))
    
    def close_account(self):
        """Close a bank account"""
        print("\n--- Close Bank Account ---")
        print("Sample Output:")
        print("Enter account number to close: 1002")
        print("Account found: sitha ram with balance 2500.00")
        print("Are you sure you want to close account 1002 (sitha ram) with balance 2500.00? (yes/no): yes")
        print("\nAccount 1002 has been closed successfully.")
        print("Final balance of 2500.00 will be returned to the account holder.")
    
    def modify_account(self):
        """Modify account details"""
        print("\n--- Modify Bank Account ---")
        print("Sample Output:")
        print("Enter account number to modify:1001")
        print("\nCurrent Account Details:")
        print("1.Name: Ram Ram")
        print("2.Account Type: Savings")
        print("3.Cancel")
        print("\nWhat would you like to modify? (1/2/3):1")
        print("Enter new name (current: Ram Ram): Ram B. Ram")
        print("\nAccount name updated successfully!")
    
    def display_transaction_history(self):
        """Display transaction history for an account"""
        print("\n--- Transaction History ---")
        print("Sample Output:")
        print("Enter account number:1001")
        print("\nLast 10 transactions for Account 1001 (Ram Ram):")
        print("\n{:<15}{:<10}{:<20}".format("Type","Amount","Date"))
        print("-" * 45)
        print("{:<15}{:<10.2f}{:<20}".format("Deposit",1000.00,"2025-05-01 10:00:00"))
        print("{:<15}{:<10.2f}{:<20}".format("Deposit",500.00,"2025-05-02 11:30:00"))
        print("{:<15}{:<10.2f}{:<20}".format("Withdrawal",200.00,"2025-05-03 14:15:00"))
    
    def display_menu(self):
        """Display the main menu"""
        print("\n===== Bank Management System =====")
        print("1.Open New Account")
        print("2.Deposit Amount")
        print("3.Withdraw Amount")
        print("4.Balance Enquiry")
        print("5.All Account Holders List")
        print("6.Close Bank Account")
        print("7.Modify Bank Account")
        print("8.Transaction History")
        print("9.Exit")
    
    def run(self):
        """Run the bank management system"""
        while True:
            self.display_menu()
            choice=input("\nEnter your choice (1-9): ").strip()
            if choice=='1':
                self.open_account()
            elif choice=='2':
                self.deposit_amount()
            elif choice=='3':
                self.withdraw_amount()
            elif choice=='4':
                self.balance_enquiry()
            elif choice=='5':
                self.display_all_accounts()
            elif choice=='6':
                self.close_account()
            elif choice=='7':
                self.modify_account()
            elif choice=='8':
                self.display_transaction_history()
            elif choice=='9':
                print("\nThank you for using our Bank Management System. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please enter a number between 1-9.")
            input("\nPress Enter to continue...")

if __name__=="__main__":
    print("=== Bank Management System ===")
    print("This program demonstrates the output of a bank management system.")
    print("Each menu option will show sample output rather than actual functionality.")
    print("For a fully functional version, use the complete implementation.\n")
    bank_system=BankManagementSystem()
    bank_system.run()