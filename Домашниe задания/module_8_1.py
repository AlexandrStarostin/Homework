try:
    def add_everything_up(a, b):
        add = a + b
        print(add)

    # s1 = add_everything_up(88.56, 'строка')
    # s2 = add_everything_up('груша', 5)
    s3 = add_everything_up(4.4, 6)

except TypeError as tr:
    print(f'Найдена ошибка {tr}')

    def add_everything_up(a, b):
        a = str(a)
        b = str(b)
        add1 = a + b
        print(f'С заменой на строковый тип {add1}')

else:
    print('Ок')

# s1 = add_everything_up(88.56, 'строка')
# s2 = add_everything_up('груша', 5)
s3 = add_everything_up(4.4, 6)