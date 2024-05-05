class BankAccount:
    def __init__(self, account_number, balance=0):
        """
        Constructor method to initialize the account number and balance.
        """
        self.account_number = account_number
        self.balance = 0

    def deposit(self, amount):
        """
        Method to deposit money into the account.
        """
        self.balance += amount
        # ✳️ Write code to add the deposited amount to the balance
    
    def withdraw(self, amount):
        """
        Method to withdraw money from the account.
        """
        if amount >= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")
        # ✳️ Write code to check if there are sufficient funds and deduct the withdrawn amount from the balance

    def get_balance(self):
        """
        Method to retrieve the current balance.
        """
        return self.balance
        # ✳️ Write code to return the current balance


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0):
        """
        Constructor method to initialize the account number, balance, and interest rate.
        """
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

        # ✳️ Call the superclass constructor to initialize common attributes
        # ✳️ Initialize the interest rate attribute

    def calculate_interest(self):
        """
        Method to calculate and add interest to the account balance.
        """
        interest_earned = self.balance * (self.interest_rate / 100)
        self.balance += interest_earned
        return self.balance
        # ✳️ Write code to calculate the interest based on the current balance and interest rate
        # ✳️ Write code to add the calculated interest to the account balance


# Testing the functionality of the classes
if __name__ == "__main__":
    bank_account = BankAccount(123456789, 1000)
# ✳️ Create a BankAccount instance with account number "123456789" and initial balance of 1000
    bank_account.deposit(500)
# ✳️ Deposit 500 into the account
    bank_account.withdraw(200)
# ✳️ Withdraw 200 from the account
    print("Bank Account:", bank_account.get_balance())
# ✳️ Get the current balance of the bank account
    saving_account = SavingsAccount(987654321, 2000, 5)
# ✳️ Create a SavingsAccount instance with account number "987654321", initial balance of 2000, and interest rate of 5%
    saving_account.deposit(1000)
# ✳️ Deposit 1000 into the savings account
    saving_account.calculate_interest()
# ✳️ Calculate and add interest to the savings account
    print("Saving Account Balance:", saving_account.get_balance())
# ✳️ Get the current balance of the savings account after adding interest
