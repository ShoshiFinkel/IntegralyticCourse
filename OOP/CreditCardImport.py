import pandas as pd
from CreditCardAssigment import CreditCardStatment

def main():
    shoshi_cc = CreditCardStatment()
    shoshi_cc.__owner_name = 'Sara'
    shoshi_cc.set_name('Sara')
    shoshi_cc.__cc_company = "diners"
    shoshi_cc.set_compant_name("diners")
    shoshi_cc.__df = 'OOP\credit_card_bill.txt'
    shoshi_cc.set_file_path("OOP\credit_card_bill.txt")
    print(shoshi_cc)
    shoshi_cc.read_file()
    shoshi_cc.display_statment()

main()