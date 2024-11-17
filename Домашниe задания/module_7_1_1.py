from itertools import product


class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        f = open(self.__file_name, "r")
        fl = f.read()
        f.close()
        return fl

    def add(self, *products):
        all_info = self.get_products().split("\n")
        file = open(self.__file_name, 'a+')
        prod = self.add(*products).split(",")
        for product in prod:
            for string in all_info:
                if str(product.name) == str(string):
                    print(f"Продукт {product.name} уже есть в магазине")
                    break
            else:
                file.write(str(product) + "\n")

        file.close()

p1 = Product('Potato', 50.1, 'Vegetables')
p2 = Product('Spaghetti', 3.8, 'Groceries')
p3 = Product('Carrot', 5.5, 'Vegetables')

s = Shop()

print(p1)

print(s.get_products())

s.add(p1, p2, p3)

