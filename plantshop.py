class Plant:
    def __init__(self, number_of_leaves, root_system):
        self.number_of_leaves = number_of_leaves
        self.root_system = root_system

    def wither(self, how_many_leaves_fall):
        self.number_of_leaves -= how_many_leaves_fall


rose = Plant(7, True)
cactus = Plant(0, True)

rose.wither(5)


print(rose.number_of_leaves)
