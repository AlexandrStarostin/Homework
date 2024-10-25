class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        print(F'Название: {self.name}, кол-во этажей: {self.number_of_floors}')
                                                                             # методы
    def __eq__(self, other):                                        #"__eq__(==), __lt__(<),
        return (self.number_of_floors == other.number_of_floors)     #__le__(<=), __gt__(>),
                                                                     #__ge__(>=), __ne__(!=)".
    def __add__(self, value):                             #реализации перегрузки оператора равенства
        return (self.number_of_floors + value)


    def __iadd__(self, value):
        return (self.number_of_floors + value)

    def __radd__(self, value):
        return (self.number_of_floors + value)



    def __gt__(self, other):
        return (self.number_of_floors > other.number_of_floors)
    def __ge__(self, other):
        return (self.number_of_floors >= other.number_of_floors)
    def __lt__(self, other):
        return (self.number_of_floors < other.number_of_floors)
    def __le__(self, other):
        return (self.number_of_floors <= other.number_of_floors)
    def __ne__(self, other):
        return (self.number_of_floors != other.number_of_floors)

    def isinstance(other, int):
        print(other, int)

    def isinstance(other, House):
        print(other, House)


p1 = House('"ЖК Загородный" P1', 10)
p2 = House('"ЖК Элитный"', 20)

p1.__str__()
p2.__str__()

print(p1 == p2)
print(f'Кол. этажей в р1 после +10-ти:        {p1 + 10}')
p1.__str__()
print(p1 == p2)

print(p1 + 10)
print(p1 + 10)

print(p1 < p2)
print(p1 <= p2)
print(p1 > p2)
print(p1 >= p2)
print(p1 != p2)


print(isinstance(p2.number_of_floors, int))
print(isinstance(p2, House))