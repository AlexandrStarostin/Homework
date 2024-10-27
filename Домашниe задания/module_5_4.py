class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        #obj = object.__new__(cls)
        #return obj
        return super().__new__(cls)

    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __del__(self):
        print(f'{self.name} снесён, но он останеться в истории.')

p1 = House('"ЖК Загородный"', 22)
print(House.houses_history)
del p1

p2 = House('"ЖК Элитный"', 99)
print(House.houses_history)
del p2

p3 = House('"ЖК Матрешки"', 55)
print(House.houses_history)
del p3
