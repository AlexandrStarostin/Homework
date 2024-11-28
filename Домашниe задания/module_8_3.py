class Car:
    def __init__(self, model, vin, numder):
        self.model = model
        if self.__is_valid_vin(vin):
            self.__vin = vin
        if self.__is_valid_numbers(numder):
            self.__number = numder

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):   # Если vin-номер не целочисленный:
            raise IncorrectVinNumber('Некорректный тип vin номер')   #то тогда вызываются(raise) исключения
        elif not (1_000_000 <= vin_number <= 9_999_999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')

        return True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        elif not (len(numbers) == 6):
            raise IncorrectCarNumbers('Неверная длина номера')

        return  True


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

try:
    first = Car('Model1', 5_557_556, 'ytgkju')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создана')