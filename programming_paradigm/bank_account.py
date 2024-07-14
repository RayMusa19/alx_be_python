class BankAccount:

    def __init__(self, initial_balance = 0):

        self.account_balance = initial_balance

    def deposit(self,amount):
        self.account_balance += amount


    def withdraw(self,amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False



    def display_balance(self):
        self.print_account_balance = float(account_balance)
        print(f"Current Balance: ${self.print_account_balance}")
