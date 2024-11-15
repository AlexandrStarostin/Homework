class Animal:
    def __init__(self, name, alive = True, fed = False):
        self.name = name
        self.alive = alive     # живой
        self.fed = fed      # накормленый
        a = self.alive


class Plant:
    def __init__(self, food):
        self.edible = False   # съедобный
        self.food = food



class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)
    def eat(self, food):
        if isinstance(food, Plant):
            if food == fl2:
                f = self.fed = True
                return (f'{n2.name} съел {fl2.food} '
                        f'\n{f}')
            else:
                f1 = self.alive = False
                return (f'{n2.name} не стала есть {mt1.food}'
                        f'\n{f1}')

class Predator(Animal):
    def __init__(self, name):
        super().__init__(name)
    def eat(self, food):
        if isinstance(food, Plant):
            if food == mt1:
                f3 = self.fed = True
                return (f'{n1.name} съел {mt1.food}'
                        f'\n{f3}')
            else:
                f4 = self.alive = False
                return (f'{n1.name} не стал есть {fl2.food}'
                        f'\n{f4}')


class Flower(Plant):
    def __init__(self, food):
        super().__init__(food)
    def set_fl(self, edible = True):
        self.edible = edible

class Meat(Plant):
    def set_fr(self, edible = True):
        self.edible = edible


n1 = Animal('волк')
n2 = Animal('черепаха')



mt1 = Plant('овца')
fl2 = Plant('одуванчик')


mn = Mammal
pr = Predator


print(n1.name)
print(fl2.food)

print(n2.fed)
print(n1.alive)

print(mn(n2).eat(fl2))
print(pr(n1).eat(fl2))

