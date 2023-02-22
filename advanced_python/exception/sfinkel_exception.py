import logging
import os
CURR_DIR = os.path.dirname(__file__)
LOG_FOLDER = CURR_DIR + '/logs'
logging.basicConfig(filename= LOG_FOLDER +'/my_store_logs.txt',
filemode='a+',
format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
datefmt='%Y-%m-%d %H:%M:%S',
#datefmt='%H:%M:%S',
level=logging.INFO)

customer_name = input("Please enter your name ")
logging.info("name was entered")
print('Hi', customer_name, '\nwelcome to our clothing store')
clothing_dict = {'socks': 12, 'black skirt': 100, 'blue skirt': 130,  'shirt': 80, 'dress': 450, 'sweater': 145}
print('Items for purchase in our store:', [item for item in clothing_dict])
logging.info("Items list was printed")
dic_of_order = {}
finish = 'n'
total = 0
while finish != 'y':
    num_of_items = 0
    item_to_purch = input('Please enter the item you would like to purchase: ')
    try:
        print("The price of", item_to_purch, "is:", clothing_dict[item_to_purch], 'NIS')
        logging.info("Correct item was chosen")
    except KeyError:
        logging.warning(item_to_purch+' not from list.')
        item_to_purch = input("Item not in store. Please enter a item from our items' list: ")
        print("The price of", item_to_purch, "is:", clothing_dict[item_to_purch], 'NIS')
        logging.info("Correct item was chosen")
    try:
        num_of_items += int(input('Please enter the amount of item you would like to purchase: '))
        print("The total for", num_of_items, item_to_purch, "is:", clothing_dict[item_to_purch] * num_of_items, 'NIS')
        total += clothing_dict[item_to_purch] * num_of_items
        logging.info("amount of item was chosen and add to total")
    except ValueError:
        logging.warning('Not valid number')
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
        logging.info('Item was added to order list.')
    else:
        print('The confirmation doesn\'t match the ordered item. This item is canceled')
        logging.info('The confirmation doesn\'t match the ordered item. This item is canceled')
    finish = input('Have you finished ordering?(y/n) ')
    while finish not in ['y','n']:
        logging.warning('Invalid input')
        finish = input('Invalid input, enter y/n. ')
print('Your order:')
for item, amount in dic_of_order.items():
    print(amount, item)
print('Total:', total)

# 1. Use a lambda to take in the customer's name and phone number. Store all
# the customer info and order details in a df.
# 2. Use regexes to validate the customer's credit card information.
# 3. Use a list comprehension to loop through a list of your customers and find
# the one who spent the most money in your store.
# 4. Add logging to your program to keep track of any errors that may come up
# along the way
#name_phone = lambda name, phone_num: print(name, phone_num)