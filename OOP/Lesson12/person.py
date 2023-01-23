class Person:
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
        

    def __str__(self) -> str:
        return '{} {}'.format(self.first_name, self.last_name)



