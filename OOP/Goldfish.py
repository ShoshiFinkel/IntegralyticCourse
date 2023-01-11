class Goldfish:
    species = 'fish'
    def __init__(self, size_cm, age_in_months, food, color='gold'):
        self.size = size_cm
        self.color = color
        self.age = age_in_months
        self.food = food

    def __str__(self):
        goldfish_description = "This is my goldfish; it's {} cm, its color is {}, it's {} months old, and it's like to eat {}".format(self.size, self.color, self.age, self.food)
        return goldfish_description
    
    def feed_the_fish(self, time, fish_ate):
        if time == 'morning' and fish_ate == True:
            print('The fish ate already')
        elif time == 'morning' and fish_ate == False:
            print('Feed the fish with', self.food)
        elif time == 'night' and fish_ate == True:
            print('The fish ate already')
        elif time == 'night' and fish_ate == False:
            print('Feed the fish with', self.food)
        else:
            print("It's not feeding time now")

