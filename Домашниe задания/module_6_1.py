class Animal:

    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False


class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name

class Mammal(Animal):
    def eat(self, food):
        if isinstance(food, Plant):
            if Plant.fl2.name == food.name:
                self.fed = True
            return f'{n2.name} съел {fl2.name}'

        else:
            self.alive = False
            return f'{n2.name} не стала есть {mt1.name}'



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

mn = Mammal

print(n2.name)
print(fl2.name)

print(Flower.__mro__)
print(Mammal.__mro__)

print(n2.name)
print(mn.eat(Plant(fl2.name), "одуванчик"))


print(n1.alive)
print(n2.fed)

