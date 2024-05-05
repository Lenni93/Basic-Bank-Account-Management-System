class BankAccount:
    def __init__(self, account_number, balance=0.00):
        """
        Constructor method to initialize the account number and balance.
        """
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        """
        Method to deposit money into the account.
        """
        self.__balance += amount
        print(f"Deposite $ {amount:.2f}. \nNew balance: ${self.__balance:.2f}")
        # ✳️ Write code to add the deposited amount to the balance
    
    def withdraw(self, amount):
        """
        Method to withdraw money from the account.
        """
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdraw amount:{amount:.2f}, Current balance{self.__balance:.2f}$")
        else:
            print("Insufficient funds")
        # ✳️ Write code to check if there are sufficient funds and deduct the withdrawn amount from the balance

    def get_balance(self):
        """
        Method to retrieve the current balance.
        """
        print(f"Current balance is:{self.__balance}$")
        # ✳️ Write code to return the current balance

    def return_balance(self):
        return self.__balance
class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0.00, interest_rate=0.00):
        """
        Constructor method to initialize the account number, balance, and interest rate.
        """
        super().__init__(account_number, balance)
        self.__interest_rate = interest_rate

        # ✳️ Call the superclass constructor to initialize common attributes
        # ✳️ Initialize the interest rate attribute

    def calculate_interest(self):
        """
        Method to calculate and add interest to the account balance.
        interest rate is as example 50 / 100 = 0.5 * 50 = 25
        new_balance = 50 + 25
        interest_earned = 75
        """
        current_balance = super().return_balance()
        interest_earned = current_balance * (self.__interest_rate / 100)
        new_balance = interest_earned + current_balance
        print(f"Interest earned:{interest_earned:.2f}. \nNew balance{new_balance:.2f} ")
        # ✳️ Write code to calculate the interest based on the current balance and interest rate
        # ✳️ Write code to add the calculated interest to the account balance



#  Main functionality of the classes
def main():
    print("*****WELCOME!*****")
    bank_account = input("Enter your account number: ")
    balance = input("Enter your balance: ")

    if not balance.isnumeric() or float(balance) < 0:
        print("Please, enter your valid balance!")
    else:
        balance = float(balance)
        bank_account = BankAccount(bank_account, balance)
        while True:
            operation = input(""""
            Select operation from the menu:
            =======MENU=======
            [1] Check balance
            [2] Make a deposite
            [3] withraw balance
            [4] Open a savings bank account
            [5] Exit
            """"")
            if not operation.isnumeric():
                print("Please, enter valid operation.")
                continue
            else:
                operation = int(operation)
                if operation < 1 or operation > 5:
                    print("Please enter a valid choice. ")
                    continue
                else:
                    if operation == 5:
                        print("Goodbye.")
                        break
                    elif operation == 1:
                        bank_account.get_balance()
                    elif operation == 2:
                        deposit = input("Enter your deposit: ")
                        if not deposit.isnumeric():
                            print("Enter a valid amount.")
                            continue
                        else:
                            deposit = float(deposit)
                            if deposit < 0:
                                print("Enter a valid amount.")
                            else:
                                bank_account.deposit(deposit)
                    elif operation == 3:
                        withdraw = input("Enter amount: ")
                        if not withdraw.isnumeric():
                            print("Enter a valid amount.")
                            continue
                        else:
                            withdraw = float(withdraw)
                            if withdraw < 0:
                                print("Enter a valid amount.")
                            else:
                                bank_account.withdraw(withdraw)
                    elif operation == 4:
                        interest_rate = input("Enter the interest rate: ")
                        if not interest_rate.isnumeric():
                            print("Enter a valid amount.")
                            continue
                        else:
                            interest_rate = float(interest_rate)
                            if interest_rate < 0:
                                print("Enter a valid amount.")
                            else:
                                account_balance = bank_account.return_balance()
                                savings_account = SavingsAccount(bank_account, account_balance, interest_rate)
                                savings_account.calculate_interest()
# Initialize the program.
if __name__ == "__main__":
    main()

#
# #class BankAccount:
#     def __init__(self, account_number, balance=0):
#         """
#         Constructor method to initialize the account number and balance.
#         """
#         self.account_number = account_number
#         self.balance = 0
#
#     def deposit(self, amount):
#         """
#         Method to deposit money into the account.
#         """
#         self.balance += amount
#         # ✳️ Write code to add the deposited amount to the balance
#
#     def withdraw(self, amount):
#         """
#         Method to withdraw money from the account.
#         """
#         if amount >= self.balance:
#             self.balance -= amount
#         else:
#             print("Insufficient funds")
#         # ✳️ Write code to check if there are sufficient funds and deduct the withdrawn amount from the balance
#
#     def get_balance(self):
#         """
#         Method to retrieve the current balance.
#         """
#         return self.balance
#         # ✳️ Write code to return the current balance
#
#
# class SavingsAccount(BankAccount):
#     def __init__(self, account_number, balance=0, interest_rate=0):
#         """
#         Constructor method to initialize the account number, balance, and interest rate.
#         """
#         super().__init__(account_number, balance)
#         self.interest_rate = interest_rate
#
#         # ✳️ Call the superclass constructor to initialize common attributes
#         # ✳️ Initialize the interest rate attribute
#
#     def calculate_interest(self):
#         """
#         Method to calculate and add interest to the account balance.
#         """
#         interest_earned = self.balance * (self.interest_rate / 100)
#         self.balance += interest_earned
#         return self.balance
#         # ✳️ Write code to calculate the interest based on the current balance and interest rate
#         # ✳️ Write code to add the calculated interest to the account balance
#
#
# # Testing the functionality of the classes
# if __name__ == "__main__":
#     bank_account = BankAccount(123456789, 1000)
# # ✳️ Create a BankAccount instance with account number "123456789" and initial balance of 1000
#     bank_account.deposit(500)
# # ✳️ Deposit 500 into the account
#     bank_account.withdraw(200)
# # ✳️ Withdraw 200 from the account
#     print("Bank Account:", bank_account.get_balance())
# # ✳️ Get the current balance of the bank account
#     saving_account = SavingsAccount(987654321, 2000, 5)
# # ✳️ Create a SavingsAccount instance with account number "987654321", initial balance of 2000, and interest rate of 5%
#     saving_account.deposit(1000)
# # ✳️ Deposit 1000 into the savings account
#     saving_account.calculate_interest()
# # ✳️ Calculate and add interest to the savings account
#     print("Saving Account Balance:", saving_account.get_balance())
# # ✳️ Get the current balance of the savings account after adding interest