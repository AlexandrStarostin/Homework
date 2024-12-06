def personal_sum(numbers):
    int_num = []
    result = 0
    res = 0
    incorrect_data = 0

    for i in numbers:

        try:
            res += i
            result = res
        except TypeError:
            if not isinstance(i, int):
                incorrect_data += 1

                print(f'В numbers записан некорректный тип данных')
                print()
                print(f'Некорректный тип данных для подсчета суммы - {i}')
        else:
            int_num.append(i)

    print(f'Кол-во некорректных данных: {incorrect_data}')
    print(f'Количество введенных цифр: {len(int_num)}')
    print(f'Сумма чисел: {result}')

    print()

    try:
        s_result = result/len(int_num)
    except ZeroDivisionError:
        if len(int_num) == 0:
            print(f'Правильных введенных значений: 0')
    else:
        print(f'Cреднее арифметическое всех чисел: {s_result}')


def calculate_average(number):
    number = personal_sum(8)
    print()

personal_sum([8, 78,'75', 5])
personal_sum([8, 0.7, 'yuy'])

