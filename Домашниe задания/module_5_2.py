class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        print(self.number_of_floors)

    def __str__(self):
        print(F'Название: {self.name}, кол-во этажей: {self.number_of_floors}')

заг = House('"ЖК Загородный"', 22)
элит = House('"ЖК Элитный"', 99)

заг.__str__()
элит.__str__()
заг.__len__()
элит.__len__()