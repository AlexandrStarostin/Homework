from random import choice

# Lambda-функция:
first = 'Мама мыла раму'
second = 'Рамена мало было'

one = map(lambda x, y: x == y, first, second)
print(list(one))


# Замыкание:
def get_advanced_writer(file_name):
    with open(file_name, 'w', encoding='utf-8'):
        def write_everything(*data_set):
            with open(file_name, 'w', encoding='utf-8') as file:
                for i in data_set:
                    for j in i:
                        file.write(str(j) + "\n")
        return write_everything

writ = get_advanced_writer('example.txt')
wr = 'Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке']
print(writ(wr))


# Метод __call__:
class MysticBall:
    def __init__(self, *world):
        self.world = world

    def __call__(self):
        return choice(self.world)


first_ball = MysticBall('Да', 'Нет', 'Наверное')

print(first_ball())
print(first_ball())
print(first_ball())