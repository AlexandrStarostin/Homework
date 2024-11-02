class Animal:
    def __init__(self, name, alive = True, fed = False):
        self.name = name
        self.alive = alive
        self.fed = fed

class Plant:
    def __init__(self, name, edible = False):
        self.edible = edible
        self.name = name

class Mammal(Animal):
    def eat(self, food):
        self.flower = food
        self.fruit = food
        if food := True:
            print(f'{self.name} съел {self.food}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {self.food}')
            self.alive = False
        return


class Predator(Animal):
    def eat(self, food):
        self.flower = food
        self.fruit = food
        if food := True:
            print(f'{self.name} съел {self.food}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {self.food}')
            self.alive = False
        return
#
class Flower(Plant):
    def fl(self, edible = True):
        self.edible = edible


class Meat(Plant):
    def fr(self, edible = True):
        self.edible = edible


n1 = Animal(name='волк')
n2 = Animal(name='черепаха')

mt1 = Plant (name='овца')
fl2 = Plant(name='одуванчик')



print(n1.name)
print(fl2.name)

print(Flower.__mro__)




print(n1.alive)
print(n2.fed)

print(Meat.fr)

