class Store:
    def __init__(self):
        fave_store = input("Now it's time to go to the store. Which store would you like to go to? ")
        store_address = input("What's the address of the store? ")
        is_usually_well_stocked = input("Is the store usually well stocked? Enter y or n ")
        pref_transport_method = input("What is your preferred method of transportation? ") #bus, car, walk etc

        print("Here we go to " + fave_store + " via a " + pref_transport_method + " at the location " + store_address + "." )
        if is_usually_well_stocked == 'y':
            print("I'm hoping it'll be well stocked because usually it is " )
        else:
            print("I'm hoping it'll be well stocked because usually it is not" )
