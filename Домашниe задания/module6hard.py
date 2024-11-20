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


class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.sides = sides

    def get_square(self):

        side = self.sides
        p = int(1/2 * (self.sides * self.sides_count))
        return int((p * (p * side) * (p * side) * (p * side))**1/2)

class Cube(Figure):
    sides_count = 12
    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.sides = sides
        self.__cube_side = []

    def set_sides(self, __new_sides):
        super().set_sides()

        for i in range(self.sides_count):
            self.__cube_side.append(self.sides)

    def get_sides(self):
        return self.__cube_side


    def get_volume(self):
        return self.sides**3


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)
triangle = Triangle((120, 66, 38), 2)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(55) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())


# Проверка периметра (круга), это и есть длина:
print(len(circle1))
print(circle1.get_square())

# Проверка объёма (куба):
print(cube1.get_volume())

