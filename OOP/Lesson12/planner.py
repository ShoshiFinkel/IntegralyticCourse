from day import Day

class Planner:
    def __init__(self, day_entered: str) -> None:
        self.day = Day[day_entered.upper()]