class Animal:
    def __init__(self, isalive, isAnimal):
        self.isalive =  isalive
        self.isAnimal = isAnimal

    def dead(self):
        self.isalive = False
        return self.isalive

# cat = Animal(True,True)
# print(cat.dead())

class Cat(Animal):
    def __init__(self, isalive, isAnimal):
        super().__init__(isalive, isAnimal)