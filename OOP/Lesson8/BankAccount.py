class BankAccount:
    def __init__(self,name ,account_number, balance):
       self.account_number = account_number
       self.name = name
       self.balance = balance

    def deposit(self, deposit):
        self.balance += deposit
        return self.balance 

    def withdraw(self, withdraw):
        self.balance -= withdraw
        return self.balance

    def __str__(self):
        return("Hi {}, account number: {}, your balance is: {}".format(self.name, self.account_number, self.balance))
