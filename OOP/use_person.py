from person1 import Person
def main():
    person1 = Person("Ploni", "Almoni")
    print(person1.get_first_name())
    print(person1.get_last_name())

    firstname = input("Enter your first name: ")
    person1.set_first_name(firstname)

    lastname = input("Enter your last name: ")
    person1.set_last_name(lastname)

    print(person1.get_first_name())
    print(person1.get_last_name())

    firstname = input("Enter another first name: ")
    lastname = input("Enter another last name: ")
    person2 = Person(firstname, lastname)

    print(person2.get_first_name())
    print(person2.get_last_name())

if __name__ == "__main__":
    main()