print('Работа со словарями')
my_dict = {"Sasha": 2002, 'Misha': 1983, 'Pasha': 1993}
print(my_dict)
print(my_dict.get("Sasha"))
print(my_dict.get("Sash"))

my_dict.update({'Valia': 1956, 'Masha': 1974})
print(my_dict)

t = my_dict.pop('Misha')
print(t)
print(my_dict)

print('Работа с множествами')
my_set = set ([1, 8, 'Sasha', 3, 67, 5, 'Sasha', 3, 67])
print(my_set)

my_set.update({7777, 896})
print(my_set)

my_set.remove(1)
print(my_set)
