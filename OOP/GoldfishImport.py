from Goldfish import Goldfish
def main():
    Goldie_the_goldfish = Goldfish(5, 9, "A mixture of specialised goldfish flake and granules") # The arguments are: size in cm, age in months, favorite food, and default color = gold.
    print(Goldie_the_goldfish) # print the str method.
    print(Goldie_the_goldfish.species) #print the species- class argument.
    Goldie_the_goldfish.feed_the_fish('morning', False) #call the feed_the_fish method, with the arguments: time(morning, night...), fish ate- True/False.

main()