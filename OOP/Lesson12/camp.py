from bunk import Bunk
from counselor import Counselor
from camper import Camper
class Camp:
    def __init__(self, camp_name: str, max_bunks: int):
        self.camp_name = camp_name
        self.bunks = []
        self.max_bunks = max_bunks
        self.num_bunks = 0
        self.persons = []

    def find_counselor(self, fname, lname):
        for person in self.persons:
            if isinstance(person, Counselor):
                if fname == person.first_name and lname == person.last_name:
                    return person
        return None

    def find_camper(self, fname, lname):
        for person in self.persons:
            if isinstance(person, Camper):
                if fname == person.first_name and lname == person.last_name:
                    return person
        return None

    def add_counselor(self, fname, lname, hire_date, salary):
        c = self.find_counselor(fname, lname)
        if c == None:
            new_counselor = Counselor(fname, lname, hire_date, salary)
            self.persons.append(new_counselor)

    def add_camper(self, fname, lname, dob):
        c = self.find_camper(fname, lname)
        if c == None:
            new_camper = Camper(fname, lname, dob)
            self.persons.append(new_camper)

    def add_bunk(self, bunk_name, counselor_fname, counselor_lname):
        if self.num_bunks < self.max_bunks:
            new_bunk=Bunk(bunk_name, counselor_fname + ' ' + counselor_lname)
            self.bunks.append(new_bunk)
            self.num_bunks += 1
        else:
            raise Exception ('You have reached the maximum number of bunks.')
    
    def find_bunk(self,bunk_name):
        for bunk in self.bunks:
            if bunk_name  == bunk.bunk_name:
                return bunk
        return None
    
    def place_camper(self, fname, lname, bunk_name):
        bunk=self.find_bunk(bunk_name)
        if bunk==None:
            raise Exception("Could not find bunk")
        camper=self.find_camper(fname,lname)
        if camper==None:
            raise Exception("Could can't find camper")
        else:
            bunk.add_camper(camper)
        
    
    def add_allergy(self, fname, lname, allergy):
        my_camper = self.find_camper(fname, lname)
        return my_camper.add_allergy(allergy)
    
    def __str__(self) -> str:
        s = "Welcome to " + str(self.camp_name)
        s += '\nThere are ' + str(self.num_bunks) + ' bunks in the camp.'
        s += '\nThe bunks:'
        # for bunk in self.bunks:
        #     for each in bunk:
        #         s += str(each)
        return s

