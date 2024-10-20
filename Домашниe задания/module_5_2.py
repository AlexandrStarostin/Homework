class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        print(self.number_of_floors)

    def __str__(self):
        print(F'Название: {self.name}, кол-во этажей: {self.number_of_floors}')

p1 = House('"ЖК Загородный"', 22)
p2 = House('"ЖК Элитный"', 99)

p1.__str__()
p2.__str__()
p1.__len__()
p2.__len__()