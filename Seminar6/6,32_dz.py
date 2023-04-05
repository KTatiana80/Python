# Задача 32: 
# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# Диапазон от [5, 11]

# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]

# Вывод: [1, 9, 13, 14, 19]

import random

def fill_array(length):
    array = []
    i = 0
    while(i<length):
        array.append(random.randint(-length, length))
        i+=1
    return array

def search_index_by_border(min, max, array):
    result = []
    count=len(array)
    i=0
    while(i<count):
        if array[i]>=min and array[i]<=max:
            result.append(i)
        i+=1
    return result

min = int(input('Введите минимальное значение: '))
max = int(input('Введите максимальное значение: '))
count = int(input('Введите количество элементов: '))
array = fill_array(count)
index_array = search_index_by_border(min,max,array)
print(f'Исходный массив: {array}')
print(f'Индексы элементов принадлежащие диапазону [{min},{max}]: {index_array}')