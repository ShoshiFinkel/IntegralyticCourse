from datetime import datetime
from allergy import Allergy
from person import Person

class Camper(Person):
    def __init__(self, first_name, last_name, dob):
        super().__init__(first_name, last_name)
        self.dob = dob
        self.allergies = []

    def add_allergy(self, allergy: str):
        if Allergy[allergy.upper()] not in self.allergies:
            self.allergies.append(Allergy[allergy.upper()])

    def get_age(self):
        time_now = datetime.datetime.now().year
        birth = datetime.strptime(self.dob, "%d-%m-%Y").year
        age = time_now - birth
        return int(age) 

  
    def __str__(self) -> str:
        return "Camper :" +str(super())+"\n"+"is "+str(self.get_age())+"and is allergic to: "+str(self.allergies[0])




