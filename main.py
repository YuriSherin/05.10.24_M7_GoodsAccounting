# Задача "Учет товаров"
import os.path as path

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        """Метод считывает всю информацию из файла __file_name, закрывает его
        и возвращает единую строку со всеми товарами из файла __file_name."""
        res = ''  # содержит результат работы метода
        if not path.isfile(self.__file_name):
            # файл не существует. Создадим новый файл и закроем его
            try:
                with open(self.__file_name, 'w', encoding='utf8') as file:
                    file.close()
            except ValueError as e:
                print(f'Ошибка при создании нового файла {self.__file_name}: {e}')
        else:
            # файл существует. Попытаемся открыть его и прочитать данные
            try:
                with open(self.__file_name, 'r', encoding='utf8') as file:
                    res = file.read()
            except ValueError as e:
                print(f'Ошибка при чтении из файла {self.__file_name}: {e}')

        return res

    def add(self, *products):
        """Метод принимает неограниченное количество объектов класса Product.
        Добавляет в файл __file_name каждый продукт из products, если его ещё нет
        в файле (по названию). Если такой продукт уже есть, то не добавляет
        и выводит строку 'Продукт <название> уже есть в магазине'"""
        products_exist = self.get_products()    # прочитать файл
        flag = False if products_exist == '' else True  # флаг показывает, были строки в файле или нет
        try:
            with open(self.__file_name, 'a', encoding='utf8') as file:
                for product in products:
                    pr = f'{product.name}, {product.weight}, {product.category}\n'
                    if products_exist.find(product.name) >= 0:  # поиск по имени продукта
                        print(f'Продукт {product} уже есть в магазине')
                        continue
                    file.write(pr)
                    if not flag:    # если заисей в файле не было, то
                        products_exist = products_exist + pr    # формируем строку добавленных продуктов
        except ValueError as e:
            print(f'Ошибка при записи в файл {self.__file_name}: {e}')

if __name__ == '__main__':
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')
    print(p2)  # __str__
    s1.add(p1, p2, p3)
    print(s1.get_products())
