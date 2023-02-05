from camp import Camp
import logging
import logging_file as lf
import traceback

logging.basicConfig(filename =  lf.LOG_FILE,
                    filemode = 'a+',
                    format = '%(asctime)s ,%(msecs)d %(name)s  %(levelname)s  %(message)s',
                    datefmt = '%H:%M:%S',
                    level = logging.INFO)


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
                try:
                    our_camp.add_counselor(fname, lname, hire_date, salary)
                    logging.info("Added counselor")
                except ValueError as exc:
                    logging.error(traceback.format_exc())
                    hire_date = input('Hire date was bad format, please re-enter(yyyy-MM-dd: ')
                    our_camp.add_counselor(fname, lname, hire_date, salary)
                    logging.info("Added counselor after change")

            elif menu_choice == 2: #add bunk
                bunk_name = input('Enter bunk name:')
                counselor_fname = input('Enter counselor\'s first name:' )
                counselor_lname = input('Enter last name:')
                our_camp.add_bunk(bunk_name, counselor_fname, counselor_lname)
                logging.info("bunk added successfully")

            elif menu_choice == 3: #add camper
                fname = input('Enter camper first name:')
                lname = input('Enrer last name:')
                dob = input('Enter day of birth (dd-mm-yyyy):')
                try:
                    our_camp.add_camper(fname, lname, dob)
                    logging.info("camper added successfully")
                except ValueError as exc:
                    logging.error(str(exc)+traceback.format_exc())
                    dob=input('Date of birth was bad format,please re-enter (dd/mm/yyyy):')
                    our_camp.add_camper(fname, lname, dob)
                    logging.info("camper added successfully after change")


            elif menu_choice == 4: #add an allergy
                fname = input('Enter camper first name:')
                lname = input('Enter camper last name:')
                allergy = input('Add allergy:')
                our_camp.add_allergy(fname, lname, allergy)
                logging.info("allergy added successfully")

            elif menu_choice == 5: #assign camper to bunk
                fname = input('Enter camper first name:')
                lname = input('Enter camper last name:')
                dob = dob = input('Enter day of birth (dd-mm-yyyy):') 
                bunk_name = input('Enter bunk name:')
                our_camp.place_camper(fname, lname, bunk_name)
                logging.info("camper assigned successfully")
                
            elif menu_choice == 6: #
                print(our_camp)
                logging.info("printed __str__ of our_camp")

            elif menu_choice == 0:
                print('You exited the application')
                logging.info('You exited the application')

        except Exception as ex:
            #traceback.print_exc()
            logging.error(str(ex))
            logging.error(traceback.format_exc())
                    
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