class Product:
    def __init__(self, name, weidht, category):
        self.name = str(name)
        self.weight = float(weidht)
        self.category = str(category)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop(Product):
    __file_name = 'products.txt'
    def __init__(self,name, weidht, category):
        super().__init__(name, weidht, category)

    def get_products(self):
        f = open(Shop.__file_name)
        fl = f.read()
        f.close()
        return fl

    def add(self, *products):
        self.products = products
        f = open(Shop.__file_name, 'r')
        for i in Shop.__file_name:
            i == self.name
            if self.name in Shop.__file_name:
                f.close()
                return f'Продукт {self.products} уже есть в магазине'
            else:
                f = open(Shop.__file_name, 'a')
                f.write(f'{self.name}, {self.weight}, {self.category};\n')
                f.close()
                return




p1 = Product('Potato', 50.4, 'Vegetables')
p2 = Product('Spaghetti', 3.8, 'Groceries')
p3 = Product('Carrot', 5.5, 'Vegetables')


p4 = Shop('Pear', 50.4, 'Vegetables')
p5 = Shop('Spaghetti', 3.4, 'Groceries')
p6 = Shop('Appel', 5.5, 'Vegetables')

print(p1)

print(Shop.get_products(p5))

Shop.add(p1, p4, p3, p6)