# Functions
def get_info(): # Get basic info from user
    print("Welcome to the First Bank of Python!")
    name = input("\nHello, what is your name? ").title()
    savings = float(input("How much money would you like to set up your savings account with? "))
    checkings = float(input("How much money would you like to set up your checking account with? "))

    # Create an account (dict)
    bank_account = {
        "Name": name,
        "Savings": savings,
        "Checking": checkings
    }
    return bank_account

def make_deposit(bank_account,account,money): # The user wants to make a deposit
    bank_account[account] += money
    print(f"\n${money} has been deposited in {bank_account['Name']}'s {account} account.")

def make_withdrawal(bank_account,account,money): # The user wants to make a withdrawal
    if bank_account[account] - money >= 0: # If there is money in the account do the transaction
        bank_account[account] -= money
        print(f"\n${money} has been withdrawed from {bank_account['Name']}'s {account} account.")
    else: # Cancel transaction and show a message
        print(f"\nSorry, couldn't withdraw ${money}: insufficient credit in account.")
    
def display_info(bank_account): # Display account info
    print("\nAccount Balance")
    print("----------------")
    for key, value in bank_account.items():
        if key == "Name":
            print(f"{key}: {value}")
        else:    
            print(f"{key}: ${value}")

# Main code
my_account = get_info()
operating = True

while operating:
    display_info(my_account) # Show info to user
    # Ask the user for account type and what transaction wants to make
    account_type = input("\nWhat account would you like to access? (Savings / Checking) ").title()
    transaction = input("What type of transaction would you like to make? (Deposit / Withdrawal) ").lower()
    amount = float(input("How much money? "))

    # Check if the account type is valid
    if account_type == "Savings" or account_type == "Checking":
        # Check for transaction
        if transaction == "deposit":
            make_deposit(my_account,account_type,amount)
        elif transaction == "withdrawal":
            make_withdrawal(my_account,account_type,amount)
        else:
            print("\nSorry, that's not a valid transaction at the moment.")
    # If the account is invalid show a message        
    else:
        print("\nTransaction failed: couldn't find account.")

    choice = input("Would you like to do another transaction? (y/n) ")
    if choice != "y":
        display_info(my_account)
        print("\nThank you for using the First Bank of Python!")
        operating = False
