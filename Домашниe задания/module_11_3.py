import inspect
from pprint import pprint


class Func:
    def __init__(self, name):
        self.it = 4            
        sum = self.it + name
        print(sum)

tr = Func


def introspection_info(y):
    obj = ['Тип объекта', 'Методы и функции объекта', 'Модуль, к которому объект принадлежит',
           'Текст кода объекта с номером строки начала кода', 'Кортеж базовых классов']
    obj_data = [type(y), dir(y), inspect.getmodule(y), inspect.getsourcelines(y), inspect.getmro(y)]
    pprint(dict(zip(obj, obj_data)))

number_info = introspection_info(tr)
