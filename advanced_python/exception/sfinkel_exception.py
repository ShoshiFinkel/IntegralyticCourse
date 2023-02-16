customer_name = input("Please enter your name ")
print('Hi', customer_name, '\nwelcome to our clothing store')
clothing_dict = {'socks': 12, 'black skirt': 100, 'blue skirt': 130,  'shirt': 80, 'dress': 450, 'sweater': 145}
print('Items for purchase in our store:', [item for item in clothing_dict])
dic_of_order = {}
finish = 'n'
total = 0
while finish != 'y':
    num_of_items = 0
    item_to_purch = input('Please enter the item you would like to purchase: ')
    try:
        print("The price of", item_to_purch, "is:", clothing_dict[item_to_purch], 'NIS')
    except KeyError:
        item_to_purch = input("Item not in store. Please enter a item from our items' list: ")
        print("The price of", item_to_purch, "is:", clothing_dict[item_to_purch], 'NIS')
    try:
        num_of_items += int(input('Please enter the amount of item you would like to purchase: '))
        print("The total for", num_of_items, item_to_purch, "is:", clothing_dict[item_to_purch] * num_of_items, 'NIS')
        total += clothing_dict[item_to_purch] * num_of_items
    except ValueError:
        num_of_items += int(input('Not valid number. Please enter the item you would like to purchase: '))
        print("The total for", num_of_items, item_to_purch, "is:", clothing_dict[item_to_purch] * num_of_items, 'NIS')
        total += clothing_dict[item_to_purch] * num_of_items
    p_confirmation = input("In order to verify your purchase, please enter the product again ")
    n_confirmation = int(input("In order to verify your purchase, please enter the amount again "))
    if p_confirmation == item_to_purch and n_confirmation == num_of_items:
        if item_to_purch not in dic_of_order:
            dic_of_order[item_to_purch]=num_of_items
        else:
            dic_of_order[item_to_purch]+=num_of_items
    else:
        print('The confirmation doesn\'t match the ordered item. This item is canceled')
    finish = input('Have you finished ordering?(y/n) ')
    while finish not in ['y','n']:
        finish = input('Invalid input, enter y/n. ')
print('Your order:')
for item, amount in dic_of_order.items():
    print(amount, item)
print('Total:', total)