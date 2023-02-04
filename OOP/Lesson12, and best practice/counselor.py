from person import Person
from datetime import datetime

class Counselor(Person):
    def __init__(self, first_name, last_name, hire_date: str, salary: float):
        super().__init__(first_name, last_name)
        self.hire_date = datetime.strptime(hire_date, "%d-%m-%Y")
        self.salary = salary

    def __str__(self) -> str:
        return "Counselor :"+super()+"\n"+" was hired on: "+str(self.hire_date)+"\n"+"gets paid: "+self.salary