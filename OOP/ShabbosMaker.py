import datetime
class ShabbosMaker:
    lekoved_shabbos = "LEKOVED SHABBOS KODESH"
    def __init__(self, guests, shabbos_time):
        self.guests = guests
        self.time = shabbos_time

    def buy_ingredients(self, have_list, store, day):
        if have_list == True:
            print("Let's go to", store)
        else:
            print("write a list")
        if day == 'Friday':
            print("It's late, next week you should buy the ingredients on Wed.")
        print(self.lekoved_shabbos)

    def cook_and_bake(self, kitchen_tools, list_of_food_with_cook_time):
        print("Turn on music")
        print("Take out the", kitchen_tools)
        if self.guests > 0:
            print(self.guests, "guests will come for Shabbos,", "make more food for them")
        print("Find the recipes. you can find some recipes in this link: https://krepalach.com/%d7%9e%d7%aa%d7%9b%d7%95%d7%a0%d7%99-%d7%90%d7%95%d7%9b%d7%9c-%d7%99%d7%94%d7%95%d7%93%d7%99/")
        sorted_list = sorted(list_of_food_with_cook_time.items(), key=lambda x: x[1], reverse=True)
        print("Start cooking in the following order:", sorted_list )
        for food in sorted_list:
            print("The", food[0], "is ready")
        print(self.lekoved_shabbos)
        return 'completed'

    def clean_the_house(self, rooms, finish_cook):
        if finish_cook == True:
            print("clean the kitchen")
        print("sweep the rooms")
        print("fold the laundry")
        print("iron shirts")
        print("The", rooms, "are cleaned and the smell in the house is wonderful")

    def set_the_table(self, family):
        print("put the tablecloth")
        print("put dishes for", family + self.guests, "people")
        print("put The kiddush cup and the challah tray")
        print("fold napkins")
        print("put the flowers in a vase")
        print(self.lekoved_shabbos)

    def last_minute_reminders(self):
        print("Don't forget to put oil in the candles")
        print("Move the refrigerator to Shabbos mode")

    def shabbos_time(self):
        print("The time now is", datetime.datetime.now(), "shabbos is at", self.time, "hurry up to finish the preparations for Shabbos")

def main():
    Vayechi = ShabbosMaker(4, '4:15')
    Vayechi.buy_ingredients(True, 'Shaarey Revachah', 'Thursday')
    Vayechi.cook_and_bake(['mixer', 'blender'], {'Challah': 150, 'soup':20, 'cake':25, 'salad':10, 'meat': 180})
    Vayechi.clean_the_house(['kitchen', 'dining room', 'bedroom', 'bedroom', 'bathroom'], True)
    Vayechi.set_the_table(6)
    Vayechi.last_minute_reminders()
    Vayechi.shabbos_time()

if __name__=="__main__":
    main()
