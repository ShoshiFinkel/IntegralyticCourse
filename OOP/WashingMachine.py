class WashingMachine:
    def __init__(self, temp, spin_speed, cycle_type, door_is_locked, detergent):
        self.temp = temp
        self.spin = spin_speed
        self.cycle = cycle_type
        self.door_locked = door_is_locked
        self.detergent = detergent

    def soak(self):
        if self.door_locked == True:
            print("I'm soaking")
        else:
            print("close the door")
    
    def set_settings(self):
        print("my temperature is", self.temp)
        print("my spin speed is", self.spin)
        print("my cycle type is", self.cycle)

    def agitate(self):
        print("scrubbing with", self.detergent)

    def rinse(self):
        print("rinsing")

    def wash_laundry(self):
        self.set_settings()
        self.soak()
        self.agitate()
        self.rinse()

my_washing_machine = WashingMachine(30, 700, 'cottons', False, 'Persil')
my_washing_machine.wash_laundry()
