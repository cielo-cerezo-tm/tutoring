class Plant:
    def __init__(self, number_of_leaves, root_system, growth_in_inches):
        self.number_of_leaves = number_of_leaves
        self.root_system = root_system
        self.growth_in_inches = growth_in_inches
    
    def grow(self, no_inches):
        self.growth_in_inches = no_inches

    def wither(self, how_many_leaves_fall):
        self.number_of_leaves -= how_many_leaves_fall

        
        

rose = Plant(7, True,10)
cactus = Plant(0, True,20)

rose.wither(5)
rose.grow(15)

print(rose.growth_in_inches)


