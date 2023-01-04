class HomeOrganizer:
    def __init__(self, num_shirts_to_fold, games_on_floor,meal):
        self.fold_shirts = num_shirts_to_fold
        self.games_on_floor = games_on_floor
        self.meal = meal
        
    def sweep(self):
        if self.games_on_floor == False:
            print("Start sweeping")  
        else:
            print("The room is not ready to sweep")
            
    def fold_laundry(self):
        if self.fold_shirts > 25:
            print("It will probably take more than 5 minutes to fold", self.fold_shirts, "shirts")
        else:
            print("It will probably take less than 5 minutes to fold", self.fold_shirts, "shirts")
    
    def wash_dishes(self):
        print("Starting to wash the dishes from", self.meal)

    def organize_home(self):
        self.sweep()
        self.fold_laundry()
        self.wash_dishes()
