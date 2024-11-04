class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False
        return

class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name
        return

class Mammal(Animal):
    def eat(self, food):
        self.food = food
        fl2.name = self.food
        if isinstance(Plant.__init__(self.name) == Mammal.eat(self.food)):
            print(f'{Animal(self.name)} съел {Mammal.eat(self.food)}')
            self.fed = True
        else:
            print(f'{Animal(self.name)} не стал есть {Mammal.eat(self.food)}')
            self.alive = False
        return



# class Predator(Animal):
#     def eat(self, food):
#        self.food = food
#         if food := True:
#             print(f'{self.name} съел {self.food}')
#             self.fed = True
#         else:
#             print(f'{self.name} не стал есть {self.food}')
#             self.alive = False
#         return
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
print(Mammal.__mro__)
print(Mammal.eat(n1.name,"овца"))


print(n1.alive)
print(n2.fed)

print(Meat.fr)

