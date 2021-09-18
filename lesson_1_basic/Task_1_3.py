# 3. Разработать генератор случайных чисел.
# В функцию передавать начальное и конечное число генерации (нуль необходимо исключить).
# Заполнить этими данными список и словарь.
# Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”.
# Вывести содержимое созданных списка и словаря.
import random


def generator(start, finish):
    list_number = []
    dict_number = {}
    for _ in range(10):
        rnd = int((finish - start) * random.random() + start)
        list_number.append(rnd)
        dict_number.update({f'elem_{rnd}': rnd})

    return (list_number, dict_number)


print(generator(7, 26))
