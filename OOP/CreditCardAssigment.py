# ● Bonus: Include validation. For example, cannot be a future date.
# ● Bonus 2: define an additional class. Use it inside the CreditCardStatement class.
# ● Have fun with it! Include concepts that you’ve learned in other classes.
import pandas as pd
import datetime
class CreditCardStatment:
    df = pd.DataFrame()
    def __init__(self, owner_name, cc_type):
        self.owner_name = owner_name
        self.cc_type = cc_type
        
    def read_file(self, file_path):
        self.df=pd.read_csv(file_path, header=None)

    def display_statment(self):
        for index, row in self.df.iterrows():
            display_statment = "In "+ str(row[0])+ " " + str(row[1])+" NIS was spent on "+ str(row[2])
            print(display_statment)

    def __str__(self):
        return "This is {}'s {} credit card.".format(self.owner_name, self.cc_type)
