immutable_var = ('нож', 88, 123.98)
print(immutable_var)

immutable_var[1] = 'парк'
print(immutable_var)
#появляеться ошибка, потому что  список для такой переменой находиться в круглых скобках, что означает КОРТЕЖ (неизменяемый список)

mutable_list = [789, 'ночь', 'hi']
mutable_list[1] = 'день'
mutable_list[0] = 888.0
mutable_list[-1] = 777
mutable_list.append('лодка')
print(mutable_list)
