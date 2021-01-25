# Задача-1: Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
my_list = ['a', '1']
my_int = 2
my_tuple = ('b', '3')
my_float = 3.5
my_str = "hello world"
my_dist = {'name': 'Nikita', 'surname': 'Chelikov'}

big_list = [my_list, my_int, my_tuple, my_float, my_str, my_dist]
for i in big_list:
    print(f'{i} is {type(i)}')