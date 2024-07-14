class BankAccount:
    
    def __init__(self, initial_balance = 0):

        self.account_balance = initail_balance
    
    def deposit(self,amount):
        self.account_balance += amount
        print(f"Deposited ${amount}. Balance is: ${self.account_balanc}")


    def withdraw(self,amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"Withdrew ${amount}. Balance is: ${self.account_balanc}")
            return('True')
        else:
            print('Insufficient funds')
            return('False')
        


    def display_balance(self):
        print('Your account balance is :', self.account_balance)
