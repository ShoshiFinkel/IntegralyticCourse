from camp import Camp

def main():

    our_camp = Camp("Camp Integralytic", 20)

    menu_choice = None
    while menu_choice != 0:
        menu_choice = get_menu_choice()
        try:
            if menu_choice == 1: #add counselor
                fname = input('Enter counselor\'s first name:' )
                lname = input('Enter last name:')
                hire_date = input('hire date(dd-mm-yyyy):')
                salary = input('salary:')
                our_camp.add_counselor(fname, lname, hire_date, salary)
            elif menu_choice == 2: #add bunk
                bunk_name = input('Enter bunk name:')
                counselor_fname = input('Enter counselor\'s first name:' )
                counselor_lname = input('Enter last name:')
                our_camp.add_bunk(bunk_name, counselor_fname, counselor_lname)
            elif menu_choice == 3: #add camper
                fname = input('Enter camper first name:')
                lname = input('Enrer last name:')
                dob = input('Enter day of birth (dd-mm-yyyy):')
                our_camp.add_camper(fname, lname, dob)
            elif menu_choice == 4: #add an allergy
                fname = input('Enter camper first name:')
                lname = input('Enter camper last name:')
                allergy = input('Add allergy:')
                our_camp.add_allergy(fname, lname, allergy)
            elif menu_choice == 5: #assign camper to bunk
                fname = input('Enter camper first name:')
                lname = input('Enter camper last name:')
                dob = dob = input('Enter day of birth (dd-mm-yyyy):') 
                bunk_name = input('Enter bunk name:')
                our_camp.place_camper(fname, lname, bunk_name)
            elif menu_choice == 6: #
                print(our_camp)
            elif menu_choice == 0:
                print('You exited the application')
        except Exception as ex:
            print('Error!'+str(ex))
                    
def get_menu_choice():
    menu = "\n1. Add A Counselor"
    menu +=	"\n2. Add a Bunk" 
    menu +=	"\n3. Add a Camper" 
    menu +=	"\n4. Add an Allergy"
    menu +=	"\n5. Assign a Camper to a Bunk"
    menu +=	"\n6. Display Camp data"
    menu +=	"\n0. Exit Application"

    choice = input(menu + "\nPlease enter 1-6 (or 0 to exit): ")
    return int(choice)

if __name__ == "__main__":
    main()