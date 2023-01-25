import multiprocessing
class BankAccount:
    def __init__(self,name ,account_number, balance):
       self.account_number = account_number
       self.name = name
       self.balance = balance

    def deposit(self, deposit, message):
        self.balance += deposit
        print("Your balance is:", self.balance)
        print(message)
        return self.balance 

    def withdraw(self, withdraw, message):
        self.balance -= withdraw
        print("Your balance is:", self.balance)
        print(message)
        return self.balance

    def __str__(self):
        return("Hi {}, account number: {}, your balance is: {}.".format(self.name, self.account_number, self.balance))

if __name__ == '__main__':
    my_account = BankAccount('Shoshi Finkel', 3252461, 7346.5)
    deposit_process = multiprocessing.Process(target=my_account.deposit, args=[100,'process1']) 
    withdraw_process = multiprocessing.Process(target=my_account.withdraw, args=[250,'process2'])
    str_process = multiprocessing.Process(target=print, args=[my_account])
    str_process.start()
    deposit_process.start()
    withdraw_process.start()
    str_process.join()
    deposit_process.join()
    withdraw_process.join()
    
    



