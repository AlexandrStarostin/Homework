calls = 0

def count_calls():
    global calls             #подсчитывает вызовы остальных функций
    calls += 1


def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())


def is_contains (a, b):
    count_calls()
    b =[i.lower() for i in b]
    if a.lower() in b:
        return True
    else:
        return False


print(string_info('Привет'))
print(string_info('Цивилизация'))
print(is_contains('дОм', ['машина', 'дом']))
print(is_contains('good', ['Мотоцикл', 'участок']))
print(calls)