class Plant:
    def __init__(self, number_of_leaves, root_system, growth_in_inches):
        self.number_of_leaves = number_of_leaves
        self.root_system = root_system
        self.growth_in_inches = growth_in_inches
    
    def grow(self, no_inches):
        self.growth_in_inches = no_inches

    def wither(self, how_many_leaves_fall):
        self.number_of_leaves -= how_many_leaves_fall

    def propagate(self, number_of_weeks):
        if (number_of_weeks > 3):
            print(number_of_weeks)
        elif (number_of_weeks == 3):
            print("now is the best time to propagate")    
        else:
            print("this plant is too young")   



        
        

rose = Plant(7, True,10)
cactus = Plant(0, True,20)

rose.wither(5)
rose.grow(15)
cactus.propagate(3)



