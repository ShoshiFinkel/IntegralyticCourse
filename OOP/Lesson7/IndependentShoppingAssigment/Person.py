class Person:
    def __init__(self):
        last_name = input("Hi there, what is your last name? ")
        address = input("What is your address? ")
        add_items_to_shopping_list = True 
        shopping_list = []
        new_item = None
        
    def add_to_shopping_list(self):
        while self.add_items_to_shopping_list:
            new_item = input("Enter the item to add to your shopping list: ")
            self.shopping_list.append(new_item)
            add_item = input("Do you have another item to add to your shopping list? Enter y or n")
            self.add_items_to_shopping_list = add_item == "y" #if the add_item is set to y, add_items_to_shopping_list will be True. If the user entered something else add_items_to_shopping_list will be False

        print("This is your shopping list: ")
        for list_item in shopping_list:
            print(list_item)

person = Person()
person.add_to_shopping_list()