class Person:
    def __init__(self, firstname, lastname):
        self.__first_name = firstname #double underscore for private attribute
        self.__last_name = lastname

    def get_first_name(self):
        return self.__first_name.title()

    def set_first_name(self, fname):
        self.__first_name = fname
    
    def get_last_name(self):
        return self.__last_name.title()

    def set_last_name(self, lname):
        self.__last_name = lname