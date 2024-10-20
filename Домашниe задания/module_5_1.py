class House:
    def __init__(self, name, number_of_floors):         # __init__ - метод для инициализации создавая уникальные характеристики
        self.name = name                                             #self - указатель на переменную
        self.number_of_floors = number_of_floors

    def go_to (self):
        self.floor = new_floor
        if self.floor < 1 or self.floor > self.number_of_floors:
            print('Такого этажа не существует')
        if self.floor > 0 and self.floor <= self.number_of_floors:
            print(self.floor)

p1 = House('"ЖК Загородный"', 22)
p2 = House('"ЖК Элитный"', 99)

new_floor = 23

print(p1.name, p1.number_of_floors)
print(p2.name, p2.number_of_floors)

p1.go_to()
p2.go_to()








