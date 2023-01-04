def set_settings(temp, spin_speed, cycle):
    print("my temperature is", temp)
    print("my spin speed is", spin_speed)
    print("my cycle type is", cycle)

def soak(door_is_locked):
    if door_is_locked == True:
        print("I'm soaking!")
    else:
        print("close door")

def agitate(detergent):
    print("scrubbing with", detergent)

def rinse():
    print("rinsing")

def wash_laundry(temp, speed, cycle, door_is_locked, detergent):
    set_settings(temp, speed, cycle)
    soak(door_is_locked)
    agitate(detergent)
    rinse()

wash_laundry(30, 700, 'cottons', True, 'Persil')


