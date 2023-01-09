class Seamstress:
    #class atributes:
    hand = "hand"
    sewing_machine = "singer"
    def __init__(self, experience, talent=True, specialty=None):
        self.experience = experience
        self.talent = talent
        self.specialty = specialty

    def cut_material(self, cutting_tool, fabric):
        print("I'm cutting the fabric called", fabric, "with my", cutting_tool, "in my", self.hand)

    def take_measurements(self, measuring_tool):
        print("Now I'm taking measurements with my", measuring_tool)

    def sew_garment(self, requested_garment_type):
        print("I'm sewing a", requested_garment_type, "with my", self.sewing_machine, "sewing machine")

    def __str__(self):
        description = "HI I'm a seamstress. I have " + self.experience +" experience."
        if self.talent == True:
            description += " I've got talent."
        else :
            description += " I've got no talent."
        description += " My speciality is " + self.specialty
        return description

    def sew(self, tool_to_cut, implement_for_mesauring, garment_type_requested, fabric_type):
        self.take_measurements(implement_for_mesauring)
        self.cut_material(tool_to_cut, fabric_type)
        self.sew_garment(garment_type_requested)

# create an instance of seamstress
def main():
    rivky = Seamstress("6 years", True, "gowns")
    print(rivky)
    rivky.sew("scissors", "measuring stick", "gown", "velvet")

    chava_kurman = Seamstress("10 years ", True, "baby things") 
    print(chava_kurman)
    chava_kurman.sew("scissors", "measuring stick", "baby things", "cotton")

if __name__=="__main__":
    main()

