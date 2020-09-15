# 2. Дополнить следующую функцию недостающим кодом:
# def print_directory_contents(sPath):


def print_directory_contents(sPath):
    """
    Функция принимает имя каталога и распечатывает его содержимое
    в виде «путь и имя файла», а также любые другие
    файлы во вложенных каталогах.
    Эта функция подобна os.walk. Использовать функцию os.walk
    нельзя. Данная задача показывает ваше умение работать с
    вложенными структурами.
    """
    import os
    dirs = []
    for file_or_directory in os.listdir(sPath):
        full_name = os.path.join(sPath, file_or_directory)
        if os.path.isdir(full_name):
            dirs.extend(print_directory_contents(full_name))
        else:
            dirs.append((sPath, file_or_directory))

    return dirs


dirs = print_directory_contents(r'C:\Users\pavlm\Pictures')
for _ in dirs:
    print(_)
