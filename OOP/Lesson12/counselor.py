from person import Person

class Counselor(Person):
    def __init__(self, first_name, last_name, hire_date, salary) -> None:
        super().__init__(first_name, last_name)
        self.hire_date = hire_date
        self.salary = salary

    def __str__(self) -> str:
        return "Counselor :"+super()+"\n"+" was hired on: "+str(self.hire_date)+"\n"+"gets paid: "+self.salar