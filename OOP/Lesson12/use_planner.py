from planner import Planner
from day import Day

def main():
    my_planner = plan_day()
    print(my_planner.day)
    if my_planner.day == Day.SUNDAY:
        print("catch up on HW")
    elif my_planner.day == Day.THURSDAY:
        print("shop for shabbos")

def plan_day():
    day_entered = input('Enter day: ')
    your_planner= Planner(day_entered)
    return your_planner

if __name__ == "__main__":
    main()
