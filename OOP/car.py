class Car:
    #class attributes
    num_wheels = 4
    has_doors = True

    def __init__(self, brand, number_seats, clr, model, gas_tank_size = 14):
        #instance attributes
        self.brand = brand
        self.num_seats = number_seats
        self.color = clr
        self.model = model
        self.gas_tank_size = gas_tank_size
        self.fuel_level = 0  #every single instance of a car will start out at fuel level 0, it will not remain that way once we start using our cars

    def add_fuel_and_show_message(self, amount, type_fuel = "regular"):
        old_fuel_level = self.fuel_level
        new_fuel_level = self.add_fuel_and_get_fuel_level(amount)
        if new_fuel_level > old_fuel_level:
            return  "Added fuel of type " + type_fuel
        else:
            return "The tank won't hold that much"


    def add_fuel_and_get_fuel_level(self, amount):
        if self.fuel_level + amount <= self.gas_tank_size:
            self.fuel_level += amount
        return self.fuel_level

    def __str__(self):
        return "This is my car:  {} {}. I have {} of fuel".format(self.brand, self.num_wheels, self.fuel_level)

def main():
    myLexus = Car("Lexus", 7, "silver", "Qx60")
    myHonda = Car("Honda", 5, "purple", "L700", 17)


    myLexus.add_fuel_and_show_message(14)
    make_fuel_levels_equal(myLexus, myHonda)
    
    print(myLexus)
    print(myHonda)
    
    #print("Result of my lexus: " + result)
    #result = myHonda.add_fuel_and_show_message(5)
    #print("Result of my honda: " +result)

    #print(myLexus)
    #print(myHonda)

    #print(4)

def make_fuel_levels_equal(car1, car2):
    if car1.fuel_level > car2.fuel_level:
        amt_diff = car1.fuel_level - car2.fuel_level
        car2.add_fuel_and_show_message(amt_diff)
    elif car2.fuel_level > car1.fuel_level:
        amt_diff = car2.fuel_level - car1.fuel_level
        car1.add_fuel_and_show_message(amt_diff)

    return car1.fuel_level == car2.fuel_level
    

        


main()




        


