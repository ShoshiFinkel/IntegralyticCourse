#Using the credit card bill file, define a class called CreditCardStatement.
#● Plan out what your class will need to do. Write a list of variables you think you will need and methods
# you may want to use when reading a credit card statement.
# ● 2 required methods:
# ○ Write a method to read the data from the file. (note: The file credit_card_bill.txt contains the name of the store,
# amount charged , and the date. Each one is separated by a comma. The separate charges are separated by a
# carriage return/enter. Dates are in the format dd/MM/yyyy)
# ○ Write a method that will display your credit card statement in a nice format.
# ● In another file, instantiate the object and call the method(s).
# ● Bonus: Include validation. For example, cannot be a future date.
# ● Bonus 2: define an additional class. Use it inside the CreditCardStatement class.
# ● Have fun with it! Include concepts that you’ve learned in other classes.

f = open("credit_card_bill.txt", "r")
print(f.read())