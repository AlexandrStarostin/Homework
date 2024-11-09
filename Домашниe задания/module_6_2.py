class Vehicle:
    __COLOR_VARIANTS = ['blue', 'RED', 'green', 'black', 'white']
    def __init__(self,  __MODEL, __ENGINE_POWER, __color, *owner):
        self.__COLOR_VARIANTS = Vehicle.__COLOR_VARIANTS
        self.owner = str(*owner)
        self.__MODEL = str(__MODEL)
        self.__ENGINE_POWER = int(__ENGINE_POWER)
        self.__color = __color

    def det_model(self):
        self.__MODEL = 'Mustang'
        return f"Модель: {self.__MODEL}"

    def get_horsepower(self):
        self.__ENGINE_POWER = 555
        return f'Мощность двигателя: {self.__ENGINE_POWER}'

    def get_color(self):
        return f'Цвет: {self.__COLOR_VARIANTS[3]}'

    def get_owner(self):
        own = self.owner
        return f'Владелец: {own}'

    def print_info(self):
        return (f'{self.det_model()} '
                f'\n{self.get_horsepower()} '
                f'\n{self.get_color()},' 
                f'\n{self.get_owner()}')

    def set_color(self, new_color):
        for _ in self.__COLOR_VARIANTS:
            col = self.__color
            if col.lower() in self.__COLOR_VARIANTS or col.upper() in self.__COLOR_VARIANTS:
                return f'Цвет поменин на: {col}'
            else:
                return f'Нельзя сменить цвет на: {col}'


class  Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5



car = Vehicle("Ford", 255, 'GREE', "Вася")

car1 = Vehicle("Lada", 878,'whtE', "Дима")


print(car.print_info())
print(car.set_color(str))
print()

print(car1.print_info())
print(car1.set_color(''))
print()

car3 = Sedan("uy", 657, "reD", "Саша")

print(car3.print_info())
print(car3.set_color(''))