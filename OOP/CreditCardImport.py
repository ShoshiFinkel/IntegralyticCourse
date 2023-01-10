import pandas as pd
from CreditCardAssigment import CreditCardStatment

def main():
    shoshi_cc = CreditCardStatment('Shoshi Finkel', 'visa')
    print(shoshi_cc)
    shoshi_cc.read_file('OOP\credit_card_bill.txt')
    shoshi_cc.display_statment()

main()