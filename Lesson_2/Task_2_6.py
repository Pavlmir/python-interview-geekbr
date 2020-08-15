# 6. Проверить на практике возможности полиморфизма.
# Необходимо разделить дочерний класс ItemDiscountReport на два класса.
# Инициализировать классы необязательно. Внутри каждого поместить функцию get_info,
# которая в первом классе будет отвечать за вывод названия товара, а вторая — его цены.
# Далее реализовать выполнение каждой из функции тремя способами.


class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReportOne(ItemDiscount):
    def get_info(self):
        print(self.name)


class ItemDiscountReportTwo(ItemDiscount):
    def get_info(self):
        print(self.price)


print('Первый способ:')
good_one = ItemDiscountReportOne('Молоко', 50)
good_one.get_info()

good_two = ItemDiscountReportTwo('Кефир', 70)
good_two.get_info()

print('---')
print('Второй способ:')
for obj in (good_one, good_two):
    obj.get_info()


def obj_handler(obj):
    obj.get_info()


print('---')
print('Третий способ:')
obj_handler(good_one)
obj_handler(good_two)
