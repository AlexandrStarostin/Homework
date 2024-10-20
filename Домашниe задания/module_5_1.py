class House:
    def __init__(self, name, number_of_floors):         # __init__ - метод для инициализации создавая уникальные характеристики
        self.name = name                                             #self - указатель на переменную
        self.number_of_floors = number_of_floors

    def go_to (self):
        self.floor = int(input())
        if self.floor < 1 or self.floor > self.number_of_floors:
            print('Такого этажа не существует')
        if self.floor > 0 and self.floor <= self.number_of_floors:
            print(self.floor)

заг = House('"ЖК Загородный"', 22)
элит = House('"ЖК Элитный"', 99)

print(заг.name, заг.number_of_floors)
print(элит.name, элит.number_of_floors)

заг.go_to()
элит.go_to()








