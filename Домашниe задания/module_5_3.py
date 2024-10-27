class House:
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors


    def __eq__(self, other):                        # __eq__(==)
        if isinstance(other, House):
            return (self.number_of_floors == other.number_of_floors)
        elif isinstance(other, int):
            return (self.number_of_floors == other)


    def __ne__(self, other):                        # __ne__(!=)
        return not (self.__eq__(other))

    def __lt__(self, other):                       # __lt__(<)
        if isinstance(other, House):
            return (self.number_of_floors < other.number_of_floors)
        elif isinstance(other, int):
            return (self.number_of_floors < other)

    def __le__(self, other):                       # __le__(<=)
        return (self.__eq__(other) or self.__lt__(other))

    def __gt__(self, other):                       # __gt__(>)
        return not self.__le__(other)

    def __ge__(self, other):                       # __ge__(>=)
        return not self.__lt__(other)



    def __add__(self, other):
        if isinstance(other, House):
            self.number_of_floors += other.number_of_floors
        elif isinstance(other, int):
            self.number_of_floors += other
        return self



    def __radd__(self, other):
        return (self.__add__(other))


    def __iadd__(self, other):
        return (self.__add__(other))

p1 = House('"ЖК Загородный"',10)
p2 = House('"ЖК Элитный"',20)

new_floor = 3

print(p1.name, p1.number_of_floors)
print(p2.name, p2.number_of_floors)

print(p1==p2) # __eq__

p1 = p1 + 10 #__add__
print(p1.name, p1.number_of_floors)
print(p1 == p2)


p1 += 10     # __iadd__
print(p1.name, p1.number_of_floors)

p2 = 10 + p2 # __radd__
print(p2.name,p2.number_of_floors)

print(p1 > p2)    #__gt__
print(p1 >= p2)   #__de__
print(p1 < p2)    # __lt__
print(p1 <= p2)   # __le__
print(p1 != p2)   #__ne__
