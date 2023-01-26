from abc import ABC, abstractmethod
class Employee(ABC):

    def __init__(self, fname, lname) -> None:
        super().__init__()
        self.first_name = fname
        self.last_name = lname
        
    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name
    
    @abstractmethod
    def get_salary(self):
        pass

class HourlyEmployee(Employee):
    def __init__(self, fname, lname, hourly_rate, hours_worked_this_week) -> None:
        super().__init__(fname, lname)
        self.hourly_rate = hourly_rate
        self.hours_worked_this_week = hours_worked_this_week

    def get_salary(self):
        return self.hourly_rate * self.hours_worked_this_week
    
class SalariedEmployee(Employee):
    def __init__(self, fname, lname, weekly_salary) -> None:
        super().__init__(fname, lname)
        self.weekly_salary = weekly_salary

    def get_salary(self):
        return self.weekly_salary

def main():
    Shoshi = HourlyEmployee('Shoshi', 'Finkel', 50, 20)
    Miriam = SalariedEmployee('Miriam', 'Marsh', 1000)
    Leeora = HourlyEmployee('Leeora', 'Gross', 100, 10)
    Chani = SalariedEmployee('Chani', 'Bendheim', 250)
    Efrat = HourlyEmployee('Efrat', 'Finkel', 30, 40)
    employees = [Shoshi, Miriam, Leeora, Chani, Efrat]
    for employee in employees:
        print('Employee fullname: ' + str(employee.full_name) + '\nWeekly Salary: ' + str(employee.get_salary()))
        
if __name__ == '__main__':
    main()


        