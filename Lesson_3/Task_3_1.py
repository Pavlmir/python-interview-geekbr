# 1. Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него.
# При вызове функции в качестве аргумента должно передаваться имя файла с расширением.
# В функции необходимо реализовать поиск полного пути по имени файла, а затем «выделение»
# из этого пути имени файла (без расширения).


def get_file_name(path):
    sep = '\\'  # Windows
    if path.find('\\') < 0:
        sep = '/'  # Linux
    array_path = path.split(sep)
    full_path = sep.join(array_path[:-1])
    name_file = array_path[-1].split('.')[0]

    return print(f'Полный путь - {full_path}, имя файла - {name_file}')


get_file_name(r'‪C:\Users\pavlm\Pictures\15973.jpg')
