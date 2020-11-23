class Plant:
    def __init__(self, number_of_leaves, root_system):
        self.number_of_leaves = number_of_leaves
        self.root_system = root_system

rose = Plant(7,True)
cactus = Plant(0,True)
print(rose.number_of_leaves)
