# 5. Усовершенствовать первую функцию из предыдущего примера.
# Необходимо во втором списке часть строковых значений заменить на значения типа example345 (строка+число).
# Далее — усовершенствовать вторую функцию из предыдущего примера (функцию извлечения данных).
# Дополнительно реализовать поиск определенных подстрок в файле по следующим условиям:
# вывод первого вхождения, вывод всех вхождений. Реализовать замену всех найденных подстрок
# на новое значение и вывод всех подстрок, состоящих из букв и цифр и имеющих пробелы только
# в начале и конце — например, example345.

import os
import re
import random
import string

LINES_COUNT = STRING_SIZE = 7


def search_substring(content):
    print(f'{"Поиск подстроки":-^35}')
    substr = input('Введите подстроку:\n')
    regex = re.compile(f'.*{substr}.*')
    sub_arr = list(filter(regex.match, content))

    if len(sub_arr) == 0:
        print(f'Подстрока {substr} не найдена')
    else:
        print(f'Первое вхождение подстроки {substr}: {sub_arr[0]}')
    print(f'Все вхождения {substr}: {sub_arr}')

    content = [re.sub(substr, 'TEST', d) for d in content]
    print(f'Обновление файла (замена на {substr} -> TEST)')
    [print(d) for d in content]


def search_alphanums(content):
    print(f'{"Поиск строк состоящих из букв и цифр":-^35}')
    sep = ' '
    regex = re.compile(rf'\d+{sep}\w+\d+')
    alphanums = list(filter(regex.match, content))
    [print(s) for s in alphanums]


def generate_str_array(size):
    for i in range(size):
        item = ''.join(random.choice(string.ascii_letters) for _ in range(STRING_SIZE))
        if i % 3 == 0:
            item += str(random.randint(100, 1000))
        yield item


def create_text_file(name):
    if os.path.isfile(name):
        with open(name, 'r', encoding='utf-8') as d:
            content = d.read().split('\n')
            search_substring(content)
            search_alphanums(content)
    with open(name, 'w', encoding='utf-8') as d:
        numbers = [random.randint(0, 100) for _ in range(LINES_COUNT)]
        strings = generate_str_array(LINES_COUNT)
        d.writelines([f'{number} {text}\n' for number, text in zip(numbers, strings)])
        return d


create_text_file('new_file.txt')
