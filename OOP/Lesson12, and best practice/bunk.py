from camper import Camper
from counselor import Counselor
class Bunk:
    def __init__(self, bunk_name: str, counselor: Counselor):
        self.bunk_name = bunk_name
        self.counselor = counselor
        self.campers = []

    def add_camper(self, camper):
        if camper not in self.campers:
            self.campers.append(camper)

    def __str__(self) -> str:
        s = 'Bunk name: {},\n Counselor: {}'.format(self.bunk_name, self.counselor)
        s += '\n Campers:'
        for camper in self.campers:
            s += '\n'+camper
        return s
        