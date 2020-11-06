# 2. Написать программу, которая запрашивает у пользователя ввод числа.
# На введенное число она отвечает сообщением, целое оно или дробное.
# Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.
# Если они совпадают, программа должна возвращать значение True, иначе False.


def compare_numbers(string):
    try:
        number = float(string)
        if int(number) == number:
            print('Целое')
            return None
        else:
            print('Дробное')
            left, right = string.split('.')
            return left == right
    except ValueError:
        print('Не число')


print(compare_numbers(input('Введите число: ')))