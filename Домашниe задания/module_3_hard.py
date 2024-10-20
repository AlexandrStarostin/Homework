def calculate_structure_sum (data):
    summa = int()
    for elem in data:
        if isinstance(elem,(tuple, list, set)):
            summa += calculate_structure_sum(elem)
        elif isinstance(elem,dict):
            summa += calculate_structure_sum(elem.items())
        elif isinstance(elem, int):
            summa += elem
        elif isinstance(elem, str):
            summa += len(elem)
    return summa

calculate_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

print(calculate_structure_sum(calculate_structure))