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
        f = open(self.__file_name)
        fl = f.read()
        f.close()
        return fl

    def add(self, *products):
        all_inf = str(self.get_products())
        all_info = all_inf.split('\n')
        file = open(self.__file_name, 'a+', encoding='UTF-8')
        for prod in products:
            for i in all_info:
                pr = i.split(',')
                if prod.name in pr:
                    print(f"Продукт {str(prod.name)} уже есть в магазине")
                    break

            else:
                file.write(str(prod) + '\n')
                return
        file.close()

p1 = Product('Potato',50.8,'Vegetables')
p2 = Product('Spaghetti',3.8,'Groceries')
p3 = Product('Carrot',5.5,'Vegetables')

s = Shop()

print(p1, p2, p3)

s.add(p1, p2, p3)

print(s.get_products())

