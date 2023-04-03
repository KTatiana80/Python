# Задача №43.
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод:        Вывод:
# 1 2 3 2 3    2

from random import randint

size_arr = randint(5, 9)
print(size_arr)
arr = [randint(1, 5) for _ in range(size_arr)]
print(arr)
counter = 0
for i in range(size_arr-1):
    for j in range(i+1, size_arr):
        if arr[i] == arr[j]:
            counter += 1
print(counter)