# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит натуральное число N
# – количество элементов в массиве. В последующих  строках записаны N целых
# чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

# от себя добавила авто заполнение массива


import random


def fill_array(length):
    array = []
    i = 0
    while (i < length):
        array.append(random.randint(-length*2, length*2))
        i += 1
    return array


def search_nearest(array, search):
    diff = None
    nearest = None
    for number in array:
        curr_diff = abs(search-number)
        if (diff == None or curr_diff < diff):
            diff = curr_diff
            nearest = number
    return nearest


length = int(input('Ведите количество элементов: '))
array = fill_array(length)
print(array)
search = int(input('Введите искомое число: '))
nearest = search_nearest(array, search)
print(f'Ближайшее к {search} число {nearest}')
