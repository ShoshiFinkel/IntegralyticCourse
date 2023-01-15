from BankAccount import BankAccount
def main():
    my_account = BankAccount('Shoshi Finkel', 3252461, 7346.5)
    my_account.deposit(100)
    my_account.withdraw(250)
    print(my_account)

main()