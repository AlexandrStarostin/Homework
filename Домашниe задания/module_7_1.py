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
        file_name = self.__file_name
        file_inf = Shop.get_products(self).split('\n')
        # f_inf = self.get_products().split("\n")
        f = open(file_name, 'a+')      # 'a+' - режим открытия файла для дополнения и чтения
        pr = Shop().add
        pp = pr[0]
        for i  in file_inf:
            if pr[0] == i:
                print(f'Продукт {pr[0]} уже есть в магазине')
                break
        else:
            f.write(str(pr) + '\n')
        f.close()


        # for p in products:
        #
        #     for name_p in file_inf:
        #         if str(p) == name_p:
        #             print(f'Продукт {p.name} уже есть в магазине')
        #             break
        #     else:
        #         f.write(str(p)+'\n')
        # f.close()

p1 = Product('Potato', 50.4, 'Vegetables')
p2 = Product('Spaghetti', 3.8, 'Groceries')
p3 = Product('Carrot', 5.5, 'Vegetables')

prod = Product.__init__

print(p1)

Shop().add(p1, p3, p2)
print()
print(p1.__str__())




# pri = Product().split(',')
#
# print(pri(p1))