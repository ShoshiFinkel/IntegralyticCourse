class Seamstress:
    #class atributes:
    hand = "hand"
    sewing_machine = "singer"
    def __init__(self, experience, talent, specialty):
        self.experience = experience
        self.talent = talent
        self.specialty = specialty

    def cut_material(self, cutting_tool, fabric):
        print("I'm cutting the fabric called", fabric, "with my", cutting_tool, "in my", self.hand)

    def take_measurements(self, measuring_tool):
        print("Now I'm taking measurements with my", measuring_tool)

    def sew_garment(self, requested_garment_type):
        print("I'm sewing a", requested_garment_type, "with my", self.sewing_machine, "sewing machine")

# create an instance of seamstress
def main():
    rivky = Seamstress("6 years", True, "gowns")
    rivky.take_measurements("measuring stick")
    rivky.cut_material("scissors", "velvet")
    rivky.sew_garment("gown")
    print("This is my experience", rivky.experience)

chava_kurman = Seamstress("10 years ", True, "baby things") 
chava_kurman.take_measurements("measuring stick")

if __name__=="__main__":
    main()