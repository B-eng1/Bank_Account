class Account:
    # Creating a new bank account
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest
    
    def set_balance(self, balance):
        # Sets the balance for the user's account
        self.balance = balance
    
    def set_interest(self, interest):
        # Sets interest gained for this account
        self.interest = interest
    
    def deposit(self):
        amount = float(input("Enter the amount to be deposited: "))
        self.balance += amount
        print(f"\nAmount Deposited: {amount}")
    
    def withdraw(self):
        amount = float(input("Enter the amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print(f"\nYou Withdrew: {amount}")
        else:
            print("\nInsufficient balance")
    
    def display(self):
        # To display the current balance amount
        print(f"\nNet Available Balance = {self.balance}")
    
    def create_cd_account(self, balance, interest_rate, months):
        # Calculates interest and updates the balance
        self.balance = balance
        self.interest = interest_rate
        interest = self.calculate_interest(balance, interest_rate, months)
        self.balance += interest
        print(f"CD Account created with balance: {self.balance} after {months} months.")
    
    def calculate_interest(self, balance, apr, months):
        # To calculate interest on the account
        return balance * (apr / 100) * (months / 12)

# Example usage:
account = Account(1000, 2.5)
account.deposit()
account.withdraw()
account.display()

# Creating a CD account
account.create_cd_account(1000, 5, 12)