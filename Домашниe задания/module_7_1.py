from pprint import pprint

class Product:
    def __init__(self, name, weidht, category):
        self.name = str(name)
        self.weight = float(weidht)
        self.category = str(category)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'
    def __init__(self, *products):
        # super().__init__(name, weidht, category)
        self.products = products
    def get_products(self):
        f = open(Shop.__file_name)
        fl = f.read()
        f.close()
        return fl

    def add(self, *products):
        self.products = products
        gh = self.name
        f = open(Shop.__file_name, 'r')
        for gh in Shop.__file_name:
            if gh in Shop.__file_name:
                f.close()
                return f'Продукт {self.products} уже есть в магазине'
            else:
                f.close()
                f = open(Shop.__file_name, 'a')
                f.write(f'\n{self.name}')
                f.close()



p1 = Product('Potato', 50.4, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s = Shop()

print(p1)
# print(p2)
# print(p3)
print(s.get_products())

# print(s.add(p1, p2, p3))