from math import pi

class Figure:
    sides_count = 0
    def __init__(self, __color, *__sides):
        self.__color = list(__color)       #_Приватный атрибут (внутри файла)
        self.__sides = __sides       # __Скрытые атрибут (внутри класса)
        self.filled = None

    def get_color(self):          # get - (интерфейс) возвращать значение переменной
        #detter
        return  self.__color      # set - (интерфейс) устанавливает значения переменных
                                     # мы можем получить доступ только с помощью этих 2-х (get и set) методов
    def __is_valid_color(self, r, g, b):
        #if isinstance(r, int) and isinstance(r, int) and isinstance(r, int):    #(r, int) - где проверяеться, что "r" принадлежит целому числу
            #if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            #   return True
        if not (isinstance(r, int) and isinstance(r, int) and isinstance(r, int)):
            return False
        elif not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            return False
        return True                  #по умолчанию возвращаеться True

    def set_color(self, r, g, b):
        #setter
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, sides):
        if len(sides) != self.sides_count:
            return False
        for side in sides:
            if not (isinstance(side, int) and side > 0):
                return False
        return True

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        return sum(self.__sides)

class Circle(Figure):
    sides_count = 1                         # прописанно здесь, а не в __init__, чтобы он был виден для всех экземпляров
    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__radius = len(self) / (2 * pi)

    def set_sides(self, new_sides):
        super().set_sides(new_sides)        # извлечено из класса Figure и функции set_sides
        self.__radius = len(self) / (2 * pi)

    def get_square(self):
        return pi * self.__radius**2

########################################################################
class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, sides):
        super().__init__(color, sides)

    def get_square(self):
        return

class Cube(Figure):
    sides_count = 12
    def __init__(self, color, sides):
        super().__init__(color, sides)
    #Сделать список из 12 одинаковых сторон (передается 1 сторона)

    def get_volume(self):
        return #объем куба
########################################################################



circle1 = Circle((200, 200, 100), 10)

circle1.set_sides(15)
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

#print(Figure()._Figure__color)