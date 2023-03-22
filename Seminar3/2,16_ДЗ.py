# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N –
# количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

# от себя добавила авто заполнение массива


import random


def fill_array(length):
    array = []
    i = 0
    while (i < length):
        array.append(random.randint(0, int(length/2)))
        i += 1
    return array


def search_repeat(array, search):
    count = 0
    for number in array:
        count += 1 if search == number else 0
    return count


length = int(input('Ведите количество элементов: '))
array = fill_array(length)
print(array)
search = int(input('Введите искомое число: '))
repeat_count = search_repeat(array, search)
print(f'Число {search} встречается {repeat_count} раз')
