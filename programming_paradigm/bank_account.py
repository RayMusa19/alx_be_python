class BankAccount:
    
    def __init__(self, initial_balance = 0)

        self.account_balance = initail_balance
    
    def deposit(self,amount):
        self.account_balance += amount


    def withdraw(self,amount):
        if account_balance >= amount:
            self.account_balance -= amount
            print('True')
        else:
            print('False')
        

    def display_balance(self):
        print('Current Balance:', self.account_balance)
