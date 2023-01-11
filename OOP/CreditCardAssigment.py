import pandas as pd
class CreditCardStatment:
    df = pd.DataFrame()
    def __init__(self):
        self.__owner_name = 'Shoshi'
        self.__cc_company = 'visa'
        self.__file_path = 'OOP\credit_card_bill.txt'
        
    def read_file(self):
        self.df=pd.read_csv(self.__file_path, header=None)

    def display_statment(self):
        if self.df.empty:
            print("The dataframe is empty, please read the data.")
        else:
            for index, row in self.df.iterrows():
                display_statment = "In "+ str(row[0])+ " " + str(row[1])+" NIS was spent on "+ str(row[2])
                print(display_statment)
        
            

    def __str__(self):
        return "This is {}'s {} credit card.".format(self.__owner_name, self.__cc_company)

    def set_name(self, new_name):
        self.__owner_name = new_name
        return self.__owner_name

    def set_compant_name(self, new_company_name):
        self.__cc_company = new_company_name
        return self.__cc_company

    def set_file_path(self, new_file_path):
        self.__file_path = new_file_path
        return self.__file_path