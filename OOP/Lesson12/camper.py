import datetime
from allergy import Allergy
from person import Person

class Camper(Person):
    def __init__(self, first_name, last_name, year_of_birth, month_of_birth, day_of_birth):
        super().__init__(first_name, last_name)
        self.year = year_of_birth
        self.month = month_of_birth
        self.day = day_of_birth
        self.allergies = []

    def add_allergy(self, allergy: str):
        new_allergy = Allergy[allergy.upper()]
        self.allergies.append(new_allergy)

    def get_age(self):
        time_now = datetime.datetime.today()
        birth = datetime.datetime(self.year,self.month,self.day) 
        age = time_now - birth
        print(age) 

    # have to fix the str method, and the date to be years
    def __str__(self) -> str:
        return "Camper :" +str(super())+"\n"+"is "+str(self.year)+"and is allergic to: "+str(self.allergies[0])

c = Camper('sh', 'f', 1998,10,2)
c.get_age()
c.add_allergy('milk')
print(c.allergies)
print(c)


