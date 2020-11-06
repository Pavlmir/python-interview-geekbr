# 4. Реализовать возможность переустановки значения цены товара.
# Необходимо, чтобы и родительский, и дочерний классы получили новое значение цены.
# Следует проверить это, вызвав соответствующий метод родительского класса
# и функцию дочернего (функция, отвечающая за отображение информации о товаре в одной строке).


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def set_price(self, price):
        self.__price = price

    def get_parent_data(self):
        print(self.__name, self.__price)


child_obj = ItemDiscountReport('Молоко', 50)
child_obj.get_parent_data()
child_obj.set_price(70)
child_obj.get_parent_data()
